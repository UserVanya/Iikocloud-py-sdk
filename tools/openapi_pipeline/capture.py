from __future__ import annotations

import json
import math
import os
import re
import tempfile
import unicodedata
import uuid
from collections.abc import Mapping, Set
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any
from urllib.parse import unquote, unquote_to_bytes, urlsplit

from pydantic import BaseModel

from .errors import SafetyError
from .io import canonical_json_bytes, write_json_atomic
from .live.lock import (
    ensure_private_directory,
    validate_private_regular_file,
)

SECRET_KEYS = {
    "authorization",
    "cookie",
    "set-cookie",
    "apikey",
    "api_key",
    "apilogin",
    "api_login",
    "token",
    "accesstoken",
    "access_token",
    "authtoken",
    "auth_token",
    "password",
    "secret",
}
EMAIL_KEYS = {"email", "emailaddress"}
PHONE_KEYS = {"phone", "phone_number", "phonenumber"}
FREE_TEXT_KEYS = {"comment", "description", "name", "address", "message"}

_CAPTURE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_UUID_TEXT = (
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}"
)
_UUID = re.compile(_UUID_TEXT + r"\Z")
_UUID_ANY = re.compile(_UUID_TEXT)
_JWT = re.compile(
    r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\."
    r"[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])"
)
_BEARER = re.compile(r"\bbearer\s+\S+", re.IGNORECASE)
_EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?!\w)")
_PHONE = re.compile(r"(?<!\w)\+?\d(?:[ ().-]*\d){9,14}(?!\w)")
_MEDIA_TYPE = re.compile(
    r"(?:application|text)/[A-Za-z0-9!#$&^_.+*-]+"
    r"(?:\s*;\s*charset=[A-Za-z0-9._-]+)?\Z",
    re.IGNORECASE,
)
_MAX_DEPTH = 64
_ALLOWED_HEADERS = {"accept", "content-type", "x-correlation-id"}
_REQUIRED_METADATA = {"method", "path", "status"}
_OPTIONAL_METADATA = {"duration", "headers"}
_HTTP_METHODS = {
    "delete",
    "get",
    "head",
    "options",
    "patch",
    "post",
    "put",
    "trace",
}
_HEX = frozenset("0123456789abcdefABCDEF")


def _iter_strings(value: Any) -> list[str]:
    if type(value) is str:
        return [value]
    if type(value) is list:
        return [item for child in value for item in _iter_strings(child)]
    if type(value) is dict:
        return [item for key, child in value.items() for item in (key, *_iter_strings(child))]
    return []


def _decode_fragment(value: str) -> str:
    for index, character in enumerate(value):
        if character == "%" and (
            index + 2 >= len(value) or value[index + 1] not in _HEX or value[index + 2] not in _HEX
        ):
            raise SafetyError("Capture schema contains an invalid URI fragment")
    try:
        return unquote_to_bytes(value).decode("utf-8")
    except UnicodeDecodeError as error:
        raise SafetyError("Capture schema URI fragment is not UTF-8") from error


def _decode_pointer_token(value: str) -> str:
    result: list[str] = []
    index = 0
    while index < len(value):
        character = value[index]
        if character != "~":
            result.append(character)
            index += 1
            continue
        if index + 1 >= len(value) or value[index + 1] not in {"0", "1"}:
            raise SafetyError("Capture schema contains an invalid JSON Pointer token")
        result.append("~" if value[index + 1] == "0" else "/")
        index += 2
    return "".join(result)


def _resolve_local_reference(document: dict[str, Any], reference: object) -> Any:
    if type(reference) is not str or not reference.startswith("#"):
        raise SafetyError("Capture schema references must be local")
    pointer = _decode_fragment(reference[1:])
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise SafetyError("Capture schema reference is not a JSON Pointer")
    current: Any = document
    for raw_token in pointer[1:].split("/"):
        token = _decode_pointer_token(raw_token)
        if type(current) is dict:
            if token not in current:
                raise SafetyError("Capture schema contains a broken local reference")
            current = current[token]
        elif type(current) is list:
            if not re.fullmatch(r"0|[1-9][0-9]*", token):
                raise SafetyError("Capture schema reference has an invalid array index")
            index = int(token)
            if index >= len(current):
                raise SafetyError("Capture schema contains a broken local reference")
            current = current[index]
        else:
            raise SafetyError("Capture schema local reference traverses a scalar")
    return current


def _dereference_object(
    document: dict[str, Any], value: object, *, visited: frozenset[str] = frozenset()
) -> dict[str, Any]:
    if type(value) is not dict:
        raise SafetyError("Capture OpenAPI object must be an object")
    reference = value.get("$ref")
    if reference is None:
        return value
    if type(reference) is not str or reference in visited:
        raise SafetyError("Capture OpenAPI object contains a broken reference cycle")
    target = _resolve_local_reference(document, reference)
    resolved = _dereference_object(document, target, visited=visited | {reference})
    siblings = {key: item for key, item in value.items() if key != "$ref"}
    return {**resolved, **siblings}


@dataclass(frozen=True)
class RedactionHints:
    """Immutable schema-declared string values safe to preserve for one operation."""

    operation_id: str
    enum_values: Mapping[str, frozenset[str]]

    def __post_init__(self) -> None:
        if type(self.operation_id) is not str or _CAPTURE_ID.fullmatch(self.operation_id) is None:
            raise SafetyError("Capture redaction hints operation ID is invalid")
        if not isinstance(self.enum_values, Mapping):
            raise SafetyError("Capture redaction hints values must be a mapping")
        copied: dict[str, frozenset[str]] = {}
        for key, values in self.enum_values.items():
            if (
                type(key) is not str
                or not isinstance(values, Set)
                or any(type(value) is not str for value in values)
            ):
                raise SafetyError("Capture redaction hints values are invalid")
            copied[key] = frozenset(values)
        object.__setattr__(self, "enum_values", MappingProxyType(dict(sorted(copied.items()))))

    @property
    def enum_keys(self) -> frozenset[str]:
        return frozenset(self.enum_values)

    @classmethod
    def for_operation(cls, effective_schema: dict[str, Any], operation_id: str) -> RedactionHints:
        if type(effective_schema) is not dict or type(operation_id) is not str:
            raise SafetyError("Capture schema and operation ID are invalid")
        operation = cls._find_operation(effective_schema, operation_id)
        collected: dict[str, set[str]] = {}

        request_body = operation.get("requestBody")
        if request_body is not None:
            request = _dereference_object(effective_schema, request_body)
            request_schema = cls._json_content_schema(request, label="request")
            cls._walk_schema(effective_schema, request_schema, collected)

        responses = operation.get("responses")
        if type(responses) is not dict:
            raise SafetyError("Capture operation responses must be an object")
        success_responses: list[dict[str, Any]] = []
        for status, response in responses.items():
            if type(status) is not str:
                raise SafetyError("Capture response status keys must be strings")
            if re.fullmatch(r"2[0-9]{2}", status):
                success_responses.append(_dereference_object(effective_schema, response))
        if not success_responses:
            raise SafetyError("Capture operation has no 2xx response")
        for response in success_responses:
            response_schema = cls._json_content_schema(response, label="response")
            cls._walk_schema(effective_schema, response_schema, collected)

        frozen = {
            key: frozenset(sorted(values)) for key, values in sorted(collected.items()) if values
        }
        return cls(operation_id, MappingProxyType(frozen))

    @staticmethod
    def _find_operation(document: dict[str, Any], operation_id: str) -> dict[str, Any]:
        paths = document.get("paths")
        if type(paths) is not dict:
            raise SafetyError("Capture schema paths must be an object")
        matches: list[dict[str, Any]] = []
        for route, path_item in paths.items():
            if type(route) is not str or type(path_item) is not dict:
                raise SafetyError("Capture schema path item is invalid")
            for method, operation in path_item.items():
                if method not in _HTTP_METHODS:
                    continue
                if type(operation) is not dict:
                    raise SafetyError("Capture schema operation is invalid")
                candidate = operation.get("operationId")
                if candidate is not None and type(candidate) is not str:
                    raise SafetyError("Capture schema operationId is invalid")
                if candidate == operation_id:
                    matches.append(operation)
        if not matches:
            raise SafetyError(f"Unknown capture operation {operation_id!r}")
        if len(matches) != 1:
            raise SafetyError(f"Capture operation {operation_id!r} appears multiple times")
        return matches[0]

    @staticmethod
    def _json_content_schema(value: dict[str, Any], *, label: str) -> dict[str, Any]:
        content = value.get("content")
        if type(content) is not dict:
            raise SafetyError(f"Capture {label} content must be an object")
        media = content.get("application/json")
        if type(media) is not dict or type(media.get("schema")) is not dict:
            raise SafetyError(f"Capture {label} must declare application/json schema")
        return media["schema"]

    @staticmethod
    def _walk_schema(
        document: dict[str, Any],
        root: dict[str, Any],
        collected: dict[str, set[str]],
    ) -> None:
        visited_refs: set[str] = set()
        visited_objects: set[int] = set()

        def add(property_name: str | None, values: object) -> None:
            if property_name is None:
                return
            if type(values) is not list:
                raise SafetyError("Capture schema enum must be an array")
            strings = {item for item in values if type(item) is str}
            if strings:
                collected.setdefault(property_name, set()).update(strings)

        def walk(schema: object, property_name: str | None = None) -> None:
            if type(schema) is not dict:
                raise SafetyError("Capture schema traversal reached a non-object")
            identity = id(schema)
            if identity in visited_objects:
                return
            visited_objects.add(identity)

            if "$ref" in schema:
                reference = schema["$ref"]
                if type(reference) is not str:
                    raise SafetyError("Capture schema $ref must be a string")
                target = _resolve_local_reference(document, reference)
                if type(target) is not dict:
                    raise SafetyError("Capture schema $ref target must be an object")
                if reference not in visited_refs:
                    visited_refs.add(reference)
                    walk(target, property_name)

            if "enum" in schema:
                add(property_name, schema["enum"])
            if "const" in schema and property_name is not None:
                constant = schema["const"]
                if type(constant) is str:
                    collected.setdefault(property_name, set()).add(constant)

            properties = schema.get("properties")
            if properties is not None:
                if type(properties) is not dict:
                    raise SafetyError("Capture schema properties must be an object")
                for name, child in properties.items():
                    if type(name) is not str or type(child) is not dict:
                        raise SafetyError("Capture schema property is invalid")
                    walk(child, name)

            for keyword in ("allOf", "anyOf", "oneOf"):
                if keyword not in schema:
                    continue
                branches = schema[keyword]
                if type(branches) is not list:
                    raise SafetyError(f"Capture schema {keyword} must be an array")
                for branch in branches:
                    if type(branch) is not dict:
                        raise SafetyError(f"Capture schema {keyword} branch is invalid")
                    walk(branch, property_name)

            if "items" in schema:
                items = schema["items"]
                if type(items) is not dict:
                    raise SafetyError("Capture schema items must be an object")
                walk(items, property_name)

            if "additionalProperties" in schema:
                additional = schema["additionalProperties"]
                if type(additional) is dict:
                    walk(additional)
                elif type(additional) is not bool:
                    raise SafetyError(
                        "Capture schema additionalProperties must be a boolean or object"
                    )

            if "discriminator" in schema:
                discriminator = schema["discriminator"]
                if type(discriminator) is not dict:
                    raise SafetyError("Capture schema discriminator must be an object")
                discriminator_name = discriminator.get("propertyName")
                if type(discriminator_name) is not str or not discriminator_name:
                    raise SafetyError("Capture schema discriminator propertyName is invalid")
                mapping = discriminator.get("mapping", {})
                if type(mapping) is not dict:
                    raise SafetyError("Capture schema discriminator mapping is invalid")
                for discriminator_value, reference in mapping.items():
                    if type(discriminator_value) is not str or type(reference) is not str:
                        raise SafetyError("Capture schema discriminator entry is invalid")
                    target = _resolve_local_reference(document, reference)
                    if type(target) is not dict:
                        raise SafetyError("Capture schema discriminator target must be an object")
                    collected.setdefault(discriminator_name, set()).add(discriminator_value)
                    if reference not in visited_refs:
                        visited_refs.add(reference)
                        walk(target)

        walk(root)


@dataclass(frozen=True)
class LiveCapture:
    """Bind one private writer to one reviewed operation and effective schema."""

    writer: CaptureWriter
    run_id: str
    selected_operation: str
    operation_catalog: Mapping[str, Any]
    hints: RedactionHints

    def __post_init__(self) -> None:
        if not isinstance(self.writer, CaptureWriter):
            raise SafetyError("Live capture writer is invalid")
        if type(self.run_id) is not str or _CAPTURE_ID.fullmatch(self.run_id) is None:
            raise SafetyError("Live capture run ID is invalid")
        if (
            type(self.selected_operation) is not str
            or _CAPTURE_ID.fullmatch(self.selected_operation) is None
        ):
            raise SafetyError("Live capture selected operation is invalid")
        if not isinstance(self.operation_catalog, Mapping):
            raise SafetyError("Live capture operation catalog is invalid")
        copied: dict[str, Any] = {}
        for operation_id, operation in self.operation_catalog.items():
            if (
                type(operation_id) is not str
                or _CAPTURE_ID.fullmatch(operation_id) is None
                or not self._valid_operation(operation)
            ):
                raise SafetyError("Live capture operation catalog is invalid")
            copied[operation_id] = operation
        selected = copied.get(self.selected_operation)
        if selected is None:
            raise SafetyError("Live capture selected operation is absent from catalog")
        if selected.kind == "auth" or self.selected_operation == "authenticate":
            raise SafetyError("Live capture refuses auth operations")
        if not isinstance(self.hints, RedactionHints):
            raise SafetyError("Live capture redaction hints are invalid")
        if self.hints.operation_id != self.selected_operation:
            raise SafetyError("Live capture redaction hints do not match selected operation")
        object.__setattr__(
            self,
            "operation_catalog",
            MappingProxyType(copied),
        )

    @staticmethod
    def _valid_operation(operation: object) -> bool:
        kind = getattr(operation, "kind", None)
        method = getattr(operation, "method", None)
        path = getattr(operation, "path", None)
        cleanup = getattr(operation, "cleanup", None)
        if type(path) is not str:
            return False
        try:
            safe_path = _safe_path(path)
        except SafetyError:
            return False
        return (
            kind in {"auth", "read", "compensating", "cleanup"}
            and method in {"GET", "POST"}
            and safe_path == path
            and (
                cleanup is None
                or (type(cleanup) is str and _CAPTURE_ID.fullmatch(cleanup) is not None)
            )
        )

    def add_known_secret(self, secret: str) -> None:
        self.writer.add_known_secret(secret)

    def assert_selected(
        self,
        operation_id: str,
        *,
        method: str | None = None,
        path: str | None = None,
    ) -> None:
        if operation_id != self.selected_operation:
            raise SafetyError("Live capture operation was not explicitly selected")
        operation = self.operation_catalog[operation_id]
        if operation.kind == "auth" or operation_id == "authenticate":
            raise SafetyError("Live capture refuses auth operations")
        if method is not None and method != operation.method:
            raise SafetyError("Live capture method does not match operation catalog")
        if path is not None and path != operation.path:
            raise SafetyError("Live capture path does not match operation catalog")

    def write_model_pair(
        self,
        operation_id: str,
        request_model: object,
        response_model: object,
        metadata: Mapping[str, Any],
    ) -> tuple[Path, Path]:
        self.assert_selected(operation_id)
        if type(metadata) is not dict:
            raise SafetyError("Live capture metadata must be a strict object")
        supplied_method = metadata.get("method")
        supplied_path = metadata.get("path")
        operation = self.operation_catalog[operation_id]
        if supplied_method is not None and supplied_method != operation.method:
            raise SafetyError("Live capture method does not match operation catalog")
        if supplied_path is not None and supplied_path != operation.path:
            raise SafetyError("Live capture path does not match operation catalog")
        full_metadata = dict(metadata)
        full_metadata["method"] = operation.method
        full_metadata["path"] = operation.path
        request_json = self._json_value(request_model)
        response_json = self._json_value(response_model)
        return self.writer.write(
            run_id=self.run_id,
            operation_id=operation_id,
            kind=operation.kind,
            request_json=request_json,
            response_json=response_json,
            metadata=full_metadata,
            enum_values=self.hints.enum_values,
        )

    @staticmethod
    def _json_value(value: object) -> Any:
        if isinstance(value, BaseModel):
            try:
                return value.model_dump(mode="json", by_alias=True)
            except Exception:
                raise SafetyError("Cannot dump Pydantic capture model safely") from None
        if value is None or type(value) in {bool, int, float, str, list, dict}:
            return value
        raise SafetyError("Capture models must be Pydantic or strict JSON values")


def _strict_json_copy(value: Any, *, depth: int = 0, active: set[int] | None = None) -> Any:
    if depth > _MAX_DEPTH:
        raise SafetyError("Capture JSON exceeds the maximum nesting depth")
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError("Capture JSON contains a non-finite number")
        return value
    if type(value) not in {dict, list}:
        raise SafetyError("Capture accepts only strict JSON-like values")

    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError("Capture JSON contains a cycle")
    seen.add(identity)
    try:
        if type(value) is list:
            return [_strict_json_copy(item, depth=depth + 1, active=seen) for item in value]
        result: dict[str, Any] = {}
        for key, item in value.items():
            if type(key) is not str:
                raise SafetyError("Capture JSON object keys must be strings")
            result[key] = _strict_json_copy(item, depth=depth + 1, active=seen)
        return result
    finally:
        seen.remove(identity)


class Sanitizer:
    """Recursively redact a strict JSON-like value without mutating its input."""

    def __init__(self, *, known_secrets: tuple[str, ...] = ()) -> None:
        if any(type(secret) is not str or not secret for secret in known_secrets):
            raise SafetyError("Known capture secrets must be non-empty strings")
        self._known_secrets = set(known_secrets)
        self._normalized_secrets = {
            unicodedata.normalize("NFKC", secret) for secret in known_secrets
        }
        self._uuid_aliases: dict[str, str] = {}

    def add_known_secret(self, secret: str) -> None:
        if type(secret) is not str or not secret:
            raise SafetyError("Known capture secrets must be non-empty strings")
        self._known_secrets.add(secret)
        self._normalized_secrets.add(unicodedata.normalize("NFKC", secret))

    def _contains_known_secret(self, value: str) -> bool:
        normalized_value = unicodedata.normalize("NFKC", value)
        return any(secret in normalized_value for secret in self._normalized_secrets)

    def sanitize(
        self,
        value: Any,
        *,
        enum_keys: Set[str] = frozenset(),
        enum_values: Mapping[str, Set[str]] | None = None,
    ) -> Any:
        if any(type(key) is not str for key in enum_keys):
            raise SafetyError("Capture enum keys must be strings")
        safe_enum_values: dict[str, frozenset[str]] | None = None
        if enum_values is not None:
            if not isinstance(enum_values, Mapping):
                raise SafetyError("Capture enum values must be a mapping")
            safe_enum_values = {}
            for enum_key, values in enum_values.items():
                if (
                    type(enum_key) is not str
                    or not isinstance(values, Set)
                    or any(type(item) is not str for item in values)
                ):
                    raise SafetyError("Capture enum values must contain only strings")
                safe_enum_values[enum_key] = frozenset(values)
        copied = _strict_json_copy(value)
        return self._sanitize(
            copied,
            key=None,
            enum_keys=frozenset(enum_keys),
            enum_values=safe_enum_values,
        )

    def _sanitize(
        self,
        value: Any,
        *,
        key: str | None,
        enum_keys: frozenset[str],
        enum_values: dict[str, frozenset[str]] | None,
    ) -> Any:
        normalized_key = key.casefold() if key is not None else None
        if normalized_key in SECRET_KEYS:
            return "<redacted:secret>"
        if normalized_key in EMAIL_KEYS:
            return "<redacted:email>"
        if normalized_key in PHONE_KEYS:
            return "<redacted:phone>"
        if type(value) is dict:
            return {
                child_key: self._sanitize(
                    child_value,
                    key=child_key,
                    enum_keys=enum_keys,
                    enum_values=enum_values,
                )
                for child_key, child_value in value.items()
            }
        if type(value) is list:
            return [
                self._sanitize(
                    item,
                    key=key,
                    enum_keys=enum_keys,
                    enum_values=enum_values,
                )
                for item in value
            ]
        if type(value) is not str:
            return value
        if self._contains_known_secret(value):
            return "<redacted:secret>"
        if _UUID.fullmatch(value):
            canonical = str(uuid.UUID(value))
            alias = self._uuid_aliases.get(canonical)
            if alias is None:
                alias = f"00000000-0000-4000-8000-{len(self._uuid_aliases) + 1:012d}"
                self._uuid_aliases[canonical] = alias
            return alias
        if _JWT.search(value) or _BEARER.search(value):
            return "<redacted:secret>"
        if _EMAIL.search(value):
            return "<redacted:email>"
        if _PHONE.search(value):
            return "<redacted:phone>"
        if key is not None and (
            (enum_values is None and key in enum_keys)
            or (enum_values is not None and value in enum_values.get(key, ()))
        ):
            return value
        return "<redacted:string>"


def _safe_path(value: object) -> str:
    if (
        type(value) is not str
        or not value.startswith("/")
        or value.startswith("//")
        or len(value) > 2048
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Capture path must be a query-free relative path")
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or parsed.path != value:
        raise SafetyError("Capture path must be a query-free relative path")
    decoded = unquote(value)
    if any(character in decoded for character in ("?", "#", "\\")) or any(
        segment in {"", ".", ".."} for segment in decoded.split("/")[1:]
    ):
        raise SafetyError("Capture path contains unsafe segments")
    return decoded


class CaptureWriter:
    """Persist sanitized request/response pairs under a private capture root."""

    def __init__(self, root: Path, *, known_secrets: tuple[str, ...] = ()) -> None:
        if not isinstance(root, Path):
            raise SafetyError("Capture root must be a filesystem path")
        self.root = root.absolute()
        self._sanitizer = Sanitizer(known_secrets=known_secrets)

    def add_known_secret(self, secret: str) -> None:
        """Add one process-memory-only secret to both sanitizer safety layers."""
        self._sanitizer.add_known_secret(secret)

    def write(
        self,
        *,
        run_id: str,
        operation_id: str,
        kind: str,
        request_json: Any,
        response_json: Any,
        metadata: Mapping[str, Any],
        enum_keys: Set[str] = frozenset(),
        enum_values: Mapping[str, Set[str]] | None = None,
    ) -> tuple[Path, Path]:
        if kind == "auth":
            raise SafetyError("Capture refuses an auth body")
        if not isinstance(run_id, str) or _CAPTURE_ID.fullmatch(run_id) is None:
            raise SafetyError("Capture run ID is unsafe")
        if not isinstance(operation_id, str) or _CAPTURE_ID.fullmatch(operation_id) is None:
            raise SafetyError("Capture operation ID is unsafe")
        if kind not in {"read", "compensating", "cleanup"}:
            raise SafetyError("Capture operation kind is invalid")
        if type(metadata) is not dict or any(type(key) is not str for key in metadata):
            raise SafetyError("Capture metadata fields are invalid")
        fields = set(metadata)
        if not _REQUIRED_METADATA.issubset(fields) or not fields.issubset(
            _REQUIRED_METADATA | _OPTIONAL_METADATA
        ):
            raise SafetyError("Capture metadata fields are invalid")
        method = metadata["method"]
        status = metadata["status"]
        if type(method) is not str or method not in {"GET", "POST"}:
            raise SafetyError("Capture method is invalid")
        if type(status) is not int or not 100 <= status <= 599:
            raise SafetyError("Capture status is invalid")
        path = self._sanitize_path(_safe_path(metadata["path"]))

        request_body = self._sanitizer.sanitize(
            request_json,
            enum_keys=enum_keys,
            enum_values=enum_values,
        )
        response_body = self._sanitizer.sanitize(
            response_json,
            enum_keys=enum_keys,
            enum_values=enum_values,
        )
        safe_metadata = {
            "method": method,
            "operationId": operation_id,
            "path": path,
            "runId": run_id,
            "status": status,
        }
        if "duration" in metadata:
            duration = metadata["duration"]
            if type(duration) not in {int, float} or not math.isfinite(duration) or duration < 0:
                raise SafetyError("Capture duration is invalid")
            safe_metadata["duration"] = duration
        if "headers" in metadata:
            safe_metadata["headers"] = self._sanitize_headers(metadata["headers"])
        request_value = {"body": request_body, "metadata": safe_metadata}
        response_value = {"body": response_body, "metadata": safe_metadata}
        request_bytes = canonical_json_bytes(request_value)
        response_bytes = canonical_json_bytes(response_value)
        self._scan(request_bytes)
        self._scan(response_bytes)

        run_path, operation_path = self._prepare_parent(run_id, operation_id)
        staging_path = Path(tempfile.mkdtemp(prefix=f".{operation_id}.tmp-", dir=run_path))
        os.chmod(staging_path, 0o700, follow_symlinks=False)
        ensure_private_directory(staging_path)
        try:
            staged_request = staging_path / "request.json"
            staged_response = staging_path / "response.json"
            write_json_atomic(staged_request, request_value, mode=0o600)
            write_json_atomic(staged_response, response_value, mode=0o600)
            validate_private_regular_file(staged_request, label="Capture request")
            validate_private_regular_file(staged_response, label="Capture response")
            if self._lexists(operation_path):
                raise SafetyError("Capture refuses to overwrite an operation directory")
            try:
                os.rename(staging_path, operation_path)
            except FileExistsError as error:
                raise SafetyError("Capture refuses to overwrite an operation directory") from error
        finally:
            self._cleanup_staging(staging_path)
        ensure_private_directory(operation_path)
        request_path = operation_path / "request.json"
        response_path = operation_path / "response.json"
        validate_private_regular_file(request_path, label="Capture request")
        validate_private_regular_file(response_path, label="Capture response")
        return request_path, response_path

    def _sanitize_path(self, path: str) -> str:
        sanitized: list[str] = []
        for segment in path.split("/")[1:]:
            value = self._sanitizer.sanitize({"segment": segment})["segment"]
            sanitized.append(value)
        return "/" + "/".join(sanitized)

    def _sanitize_headers(self, value: object) -> dict[str, str]:
        if type(value) is not dict or len(value) > 128:
            raise SafetyError("Capture headers must be a strict object")
        result: dict[str, str] = {}
        seen: set[str] = set()
        for name, header_value in value.items():
            if (
                type(name) is not str
                or type(header_value) is not str
                or not name
                or len(name) > 128
                or len(header_value) > 8192
                or any(
                    ord(character) < 32 or ord(character) == 127
                    for character in name + header_value
                )
            ):
                raise SafetyError("Capture headers contain an invalid name or value")
            normalized = name.casefold()
            if normalized in seen:
                raise SafetyError("Capture headers contain a duplicate name")
            seen.add(normalized)
            if normalized not in _ALLOWED_HEADERS:
                continue
            if normalized in {"accept", "content-type"} and _MEDIA_TYPE.fullmatch(header_value):
                safe_value = self._sanitizer.sanitize(
                    {normalized: header_value},
                    enum_values={normalized: frozenset({header_value})},
                )[normalized]
            else:
                safe_value = self._sanitizer.sanitize({normalized: header_value})[normalized]
            result[normalized] = safe_value
        return result

    def _prepare_parent(self, run_id: str, operation_id: str) -> tuple[Path, Path]:
        self._ensure_private_root()
        run_path = self.root / run_id
        ensure_private_directory(run_path)
        operation_path = run_path / operation_id
        if self._lexists(operation_path):
            raise SafetyError("Capture refuses to overwrite an operation directory")
        return run_path, operation_path

    def _ensure_private_root(self) -> None:
        missing: list[Path] = []
        current = self.root
        while not self._lexists(current):
            missing.append(current)
            parent = current.parent
            if parent == current:
                raise SafetyError("Capture root has no existing private parent")
            current = parent
        if not missing:
            ensure_private_directory(self.root)
            return
        ensure_private_directory(current)
        for directory in reversed(missing):
            try:
                directory.mkdir(mode=0o700)
            except FileExistsError:
                pass
            else:
                os.chmod(directory, 0o700, follow_symlinks=False)
            ensure_private_directory(directory)

    @staticmethod
    def _lexists(path: Path) -> bool:
        try:
            path.lstat()
        except FileNotFoundError:
            return False
        return True

    @staticmethod
    def _cleanup_staging(path: Path) -> None:
        try:
            children = list(path.iterdir())
        except FileNotFoundError:
            return
        for child in children:
            with suppress(FileNotFoundError):
                child.unlink()
        with suppress(FileNotFoundError):
            path.rmdir()

    def _scan(self, body: bytes) -> None:
        text = body.decode("utf-8")
        try:
            value = _strict_json_copy(json.loads(text))
        except (UnicodeError, ValueError) as error:  # pragma: no cover - canonical bytes
            raise SafetyError("Sanitized capture is not strict JSON") from error
        for candidate in _iter_strings(value):
            normalized = unicodedata.normalize("NFKC", candidate)
            without_uuids = _UUID_ANY.sub("", normalized)
            if (
                self._sanitizer._contains_known_secret(candidate)
                or _JWT.search(normalized)
                or _BEARER.search(normalized)
                or _EMAIL.search(normalized)
                or _PHONE.search(without_uuids)
            ):
                raise SafetyError("Sanitized capture failed the final secret/PII scan")
