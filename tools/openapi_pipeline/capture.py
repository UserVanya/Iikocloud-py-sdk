from __future__ import annotations

import ctypes
import errno
import json
import math
import os
import re
import secrets
import stat
import unicodedata
import uuid
from collections.abc import Mapping, Set
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum, auto
from itertools import combinations
from pathlib import Path
from types import MappingProxyType
from typing import Any
from urllib.parse import unquote, unquote_to_bytes, urlsplit

from pydantic import BaseModel

from .errors import SafetyError
from .io import canonical_json_bytes

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


class _HintWildcard(Enum):
    ARRAY_ITEM = auto()
    OBJECT_VALUE = auto()


ARRAY_ITEM = _HintWildcard.ARRAY_ITEM
OBJECT_VALUE = _HintWildcard.OBJECT_VALUE
HintPath = tuple[str | _HintWildcard, ...]
PathValues = Mapping[HintPath, frozenset[str]]
ResponseSelector = int | str
ResponsePathValues = Mapping[ResponseSelector, PathValues]
_Constraint = frozenset[str] | None
_ConstraintMap = dict[HintPath, _Constraint]
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
_FILE_FLAGS = os.O_WRONLY | os.O_CLOEXEC | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
_RENAME_NOREPLACE = 1


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
    request_values: PathValues
    response_values_by_status: ResponsePathValues

    def __post_init__(self) -> None:
        if type(self.operation_id) is not str or _CAPTURE_ID.fullmatch(self.operation_id) is None:
            raise SafetyError("Capture redaction hints operation ID is invalid")
        object.__setattr__(self, "request_values", self._freeze_values(self.request_values))
        object.__setattr__(
            self,
            "response_values_by_status",
            self._freeze_response_values(self.response_values_by_status),
        )

    @staticmethod
    def _freeze_values(values_by_path: PathValues) -> PathValues:
        if not isinstance(values_by_path, Mapping):
            raise SafetyError("Capture redaction hints values must be a mapping")
        copied: dict[HintPath, frozenset[str]] = {}
        for path, values in values_by_path.items():
            if (
                type(path) is not tuple
                or any(
                    type(token) is not str and token not in {ARRAY_ITEM, OBJECT_VALUE}
                    for token in path
                )
                or not isinstance(values, Set)
                or any(type(value) is not str for value in values)
            ):
                raise SafetyError("Capture redaction hints values are invalid")
            copied[path] = frozenset(values)
        return MappingProxyType(copied)

    @classmethod
    def _freeze_response_values(cls, values_by_status: ResponsePathValues) -> ResponsePathValues:
        if not isinstance(values_by_status, Mapping):
            raise SafetyError("Capture response redaction hints must be a mapping")
        copied: dict[ResponseSelector, PathValues] = {}
        for selector, values in values_by_status.items():
            if (
                not (
                    (type(selector) is int and 200 <= selector <= 299)
                    or (type(selector) is str and selector in {"2XX", "default"})
                )
                or selector in copied
            ):
                raise SafetyError("Capture response redaction hint selector is invalid")
            copied[selector] = cls._freeze_values(values)
        return MappingProxyType(copied)

    def response_values_for_status(self, status: object) -> PathValues:
        if type(status) is not int or not 200 <= status <= 299:
            raise SafetyError("Capture response status must be an integer from 200 to 299")
        for selector in (status, "2XX", "default"):
            values = self.response_values_by_status.get(selector)
            if values is not None:
                return values
        raise SafetyError("Capture schema has no response hints for status")

    @classmethod
    def for_operation(cls, effective_schema: dict[str, Any], operation_id: str) -> RedactionHints:
        if type(effective_schema) is not dict or type(operation_id) is not str:
            raise SafetyError("Capture schema and operation ID are invalid")
        operation = cls._find_operation(effective_schema, operation_id)
        request_values: dict[HintPath, set[str]] = {}
        response_values_by_status: dict[ResponseSelector, PathValues] = {}

        request_body = operation.get("requestBody")
        if request_body is not None:
            request = _dereference_object(effective_schema, request_body)
            request_schema = cls._json_content_schema(request, label="request")
            cls._walk_schema(effective_schema, request_schema, request_values)

        responses = operation.get("responses")
        if type(responses) is not dict:
            raise SafetyError("Capture operation responses must be an object")
        success_responses: list[tuple[ResponseSelector, dict[str, Any]]] = []
        for status, response in responses.items():
            if type(status) is not str:
                raise SafetyError("Capture response status keys must be strings")
            selector: ResponseSelector | None = None
            if re.fullmatch(r"2[0-9]{2}", status):
                selector = int(status)
            elif status.casefold() == "2xx":
                selector = "2XX"
            elif status == "default":
                selector = status
            if selector is not None:
                if any(existing == selector for existing, _response in success_responses):
                    raise SafetyError("Capture operation has duplicate response selectors")
                success_responses.append(
                    (selector, _dereference_object(effective_schema, response))
                )
        if not success_responses:
            raise SafetyError("Capture operation has no 2xx response")
        for selector, response in success_responses:
            response_schema = cls._json_content_schema(response, label="response")
            response_values: dict[HintPath, set[str]] = {}
            cls._walk_schema(effective_schema, response_schema, response_values)
            response_values_by_status[selector] = {
                path: frozenset(values) for path, values in response_values.items()
            }

        return cls(
            operation_id,
            {path: frozenset(values) for path, values in request_values.items()},
            response_values_by_status,
        )

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
        collected: dict[HintPath, set[str]],
    ) -> None:
        active_refs: set[str] = set()
        active_objects: set[int] = set()

        def enum_values(values: object) -> frozenset[str]:
            if type(values) is not list:
                raise SafetyError("Capture schema enum must be an array")
            return frozenset(item for item in values if type(item) is str)

        def intersect(parts: list[_ConstraintMap]) -> _ConstraintMap:
            result: _ConstraintMap = {}
            for path in set().union(*(part.keys() for part in parts)):
                explicit = [value for part in parts if (value := part.get(path)) is not None]
                if not explicit:
                    result[path] = None
                    continue
                allowed = explicit[0]
                for values in explicit[1:]:
                    allowed = allowed.intersection(values)
                result[path] = allowed
            return result

        def alternatives(parts: list[_ConstraintMap], path: HintPath) -> _ConstraintMap:
            if not parts:
                return {path: None}
            result: _ConstraintMap = {}
            for candidate in set().union(*(part.keys() for part in parts)):
                values = [part.get(candidate) for part in parts]
                if any(value is None for value in values):
                    result[candidate] = None
                else:
                    result[candidate] = frozenset().union(*values)  # type: ignore[arg-type]
            return result

        def walk(schema: object, path: HintPath = ()) -> _ConstraintMap:
            if type(schema) is not dict:
                raise SafetyError("Capture schema traversal reached a non-object")
            identity = id(schema)
            if identity in active_objects:
                return {path: None}
            active_objects.add(identity)
            try:
                parts: list[_ConstraintMap] = [{path: None}]
                if "$ref" in schema:
                    reference = schema["$ref"]
                    if type(reference) is not str:
                        raise SafetyError("Capture schema $ref must be a string")
                    target = _resolve_local_reference(document, reference)
                    if type(target) is not dict:
                        raise SafetyError("Capture schema $ref target must be an object")
                    if reference in active_refs:
                        parts.append({path: None})
                    else:
                        active_refs.add(reference)
                        try:
                            parts.append(walk(target, path))
                        finally:
                            active_refs.remove(reference)

                if "enum" in schema:
                    parts.append({path: enum_values(schema["enum"])})
                if "const" in schema:
                    constant = schema["const"]
                    parts.append(
                        {path: frozenset({constant}) if type(constant) is str else frozenset()}
                    )

                properties = schema.get("properties")
                if properties is not None:
                    if type(properties) is not dict:
                        raise SafetyError("Capture schema properties must be an object")
                    for name, child in properties.items():
                        if type(name) is not str or type(child) is not dict:
                            raise SafetyError("Capture schema property is invalid")
                        parts.append(walk(child, (*path, name)))

                for keyword in ("allOf", "anyOf", "oneOf"):
                    if keyword not in schema:
                        continue
                    branches = schema[keyword]
                    if type(branches) is not list:
                        raise SafetyError(f"Capture schema {keyword} must be an array")
                    branch_maps: list[_ConstraintMap] = []
                    for branch in branches:
                        if type(branch) is not dict:
                            raise SafetyError(f"Capture schema {keyword} branch is invalid")
                        branch_maps.append(walk(branch, path))
                    parts.append(
                        intersect(branch_maps)
                        if keyword == "allOf"
                        else alternatives(branch_maps, path)
                    )

                if "items" in schema:
                    items = schema["items"]
                    if type(items) is not dict:
                        raise SafetyError("Capture schema items must be an object")
                    parts.append(walk(items, (*path, ARRAY_ITEM)))

                if "additionalProperties" in schema:
                    additional = schema["additionalProperties"]
                    if type(additional) is dict:
                        parts.append(walk(additional, (*path, OBJECT_VALUE)))
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
                    discriminator_path = (*path, discriminator_name)
                    mapping = discriminator.get("mapping", {})
                    if type(mapping) is not dict:
                        raise SafetyError("Capture schema discriminator mapping is invalid")
                    discriminator_values: set[str] = set()
                    target_maps: list[_ConstraintMap] = []
                    for discriminator_value, reference in mapping.items():
                        if type(discriminator_value) is not str or type(reference) is not str:
                            raise SafetyError("Capture schema discriminator entry is invalid")
                        target = _resolve_local_reference(document, reference)
                        if type(target) is not dict:
                            raise SafetyError(
                                "Capture schema discriminator target must be an object"
                            )
                        discriminator_values.add(discriminator_value)
                        if reference in active_refs:
                            target_maps.append({path: None})
                        else:
                            active_refs.add(reference)
                            try:
                                target_maps.append(walk(target, path))
                            finally:
                                active_refs.remove(reference)
                    parts.append({discriminator_path: frozenset(discriminator_values)})
                    if target_maps:
                        parts.append(alternatives(target_maps, path))
                return intersect(parts)
            finally:
                active_objects.remove(identity)

        for path, values in walk(root).items():
            destination = collected.setdefault(path, set())
            if values is not None:
                destination.update(values)


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
        response_path_values = self.hints.response_values_for_status(metadata.get("status"))
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
            request_path_values=self.hints.request_values,
            response_path_values=response_path_values,
            approved_path=operation.path,
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
        path_values: PathValues | None = None,
    ) -> Any:
        if any(type(key) is not str for key in enum_keys):
            raise SafetyError("Capture enum keys must be strings")
        safe_path_values = (
            RedactionHints._freeze_values(path_values) if path_values is not None else None
        )
        copied = _strict_json_copy(value)
        return self._sanitize(
            copied,
            key=None,
            enum_keys=frozenset(enum_keys),
            path_values=safe_path_values,
            path=(),
        )

    def _sanitize(
        self,
        value: Any,
        *,
        key: str | None,
        enum_keys: frozenset[str],
        path_values: PathValues | None,
        path: HintPath,
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
                    path_values=path_values,
                    path=(*path, child_key),
                )
                for child_key, child_value in value.items()
            }
        if type(value) is list:
            return [
                self._sanitize(
                    item,
                    key=key,
                    enum_keys=enum_keys,
                    path_values=path_values,
                    path=(*path, ARRAY_ITEM),
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
        allowed_values = self._allowed_values(path, path_values)
        if (key is not None and key in enum_keys) or value in allowed_values:
            return value
        return "<redacted:string>"

    @staticmethod
    def _allowed_values(path: HintPath, values_by_path: PathValues | None) -> frozenset[str]:
        if values_by_path is None:
            return frozenset()
        if path in values_by_path:
            return values_by_path[path]
        string_positions = [index for index, token in enumerate(path) if type(token) is str]
        for replacement_count in range(1, len(string_positions) + 1):
            matches: list[frozenset[str]] = []
            for positions in combinations(string_positions, replacement_count):
                candidate = list(path)
                for index in positions:
                    candidate[index] = OBJECT_VALUE
                candidate_path = tuple(candidate)
                if candidate_path in values_by_path:
                    matches.append(values_by_path[candidate_path])
            if matches:
                return frozenset().union(*matches)
        return frozenset()


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


def _approved_static_path(value: object, *, metadata_path: object) -> str:
    if (
        type(value) is not str
        or "%" in value
        or any(ord(character) <= 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Capture approved path must be an exact static relative path")
    safe_path = _safe_path(value)
    if safe_path != value or "{" in safe_path or "}" in safe_path:
        raise SafetyError("Capture approved path must be an exact static relative path")
    if value != metadata_path:
        raise SafetyError("Capture approved path does not match metadata path")
    return safe_path


def _validate_directory_fd(fd: int, *, private: bool) -> None:
    metadata = os.fstat(fd)
    if not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError("Capture path component is not a directory")
    if private and (stat.S_IMODE(metadata.st_mode) != 0o700 or metadata.st_uid != os.getuid()):
        raise SafetyError(
            "Private capture directory must be owned by the current user with mode 0700"
        )


def _close_fd_best_effort(fd: int | None) -> None:
    if fd is not None:
        with suppress(OSError):
            os.close(fd)


def _open_absolute_private_root(root: Path, *, create_missing: bool = True) -> int:
    if getattr(os, "O_NOFOLLOW", 0) == 0 or not root.is_absolute():
        raise SafetyError("Secure capture directory traversal is unavailable")
    components = root.parts[1:]
    if not components or any(component in {"", ".", ".."} for component in components):
        raise SafetyError("Capture root path is invalid")
    try:
        current_fd = os.open("/", _DIRECTORY_FLAGS)
    except OSError as error:
        raise SafetyError("Cannot open capture filesystem root safely") from error
    try:
        for index, component in enumerate(components):
            created = False
            try:
                next_fd = os.open(component, _DIRECTORY_FLAGS, dir_fd=current_fd)
            except FileNotFoundError as error:
                if not create_missing:
                    raise SafetyError("Capture published path ancestry is missing") from error
                try:
                    os.mkdir(component, 0o700, dir_fd=current_fd)
                    created = True
                except FileExistsError:
                    pass
                except OSError as error:
                    raise SafetyError("Cannot create private capture directory") from error
                try:
                    next_fd = os.open(component, _DIRECTORY_FLAGS, dir_fd=current_fd)
                except OSError as error:
                    raise SafetyError("Capture path component is not a safe directory") from error
            except OSError as error:
                raise SafetyError("Capture path component is not a safe directory") from error
            try:
                _validate_directory_fd(
                    next_fd,
                    private=index >= len(components) - 2,
                )
                if created:
                    os.fsync(current_fd)
            except BaseException:
                _close_fd_best_effort(next_fd)
                raise
            _close_fd_best_effort(current_fd)
            current_fd = next_fd
        return current_fd
    except BaseException:
        _close_fd_best_effort(current_fd)
        raise


def _open_existing_private_child(parent_fd: int, name: str) -> int:
    try:
        child_fd = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent_fd)
    except OSError as error:
        raise SafetyError("Capture child path is not a safe directory or is a symlink") from error
    try:
        _validate_directory_fd(child_fd, private=True)
    except BaseException:
        _close_fd_best_effort(child_fd)
        raise
    return child_fd


def _open_or_create_private_child(parent_fd: int, name: str) -> int:
    try:
        os.mkdir(name, 0o700, dir_fd=parent_fd)
    except FileExistsError:
        pass
    except OSError as error:
        raise SafetyError("Cannot create private capture child directory") from error
    else:
        os.fsync(parent_fd)
    return _open_existing_private_child(parent_fd, name)


def _entry_exists(parent_fd: int, name: str) -> bool:
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return False
    except OSError as error:
        raise SafetyError("Cannot inspect capture operation path safely") from error
    return True


def _create_staging_directory(parent_fd: int, operation_id: str) -> tuple[str, int]:
    for _attempt in range(32):
        name = f".{operation_id}.tmp-{secrets.token_hex(12)}"
        try:
            os.mkdir(name, 0o700, dir_fd=parent_fd)
        except FileExistsError:
            continue
        except OSError as error:
            raise SafetyError("Cannot create capture staging directory") from error
        try:
            os.fsync(parent_fd)
            try:
                staging_fd = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent_fd)
            except OSError as error:
                raise SafetyError("Cannot open capture staging directory safely") from error
            try:
                _validate_directory_fd(staging_fd, private=True)
            except BaseException:
                _close_fd_best_effort(staging_fd)
                raise
            return name, staging_fd
        except BaseException:
            with suppress(OSError):
                os.rmdir(name, dir_fd=parent_fd)
            with suppress(OSError):
                os.fsync(parent_fd)
            raise
    raise SafetyError("Cannot allocate a unique capture staging directory")


def _validate_private_file_fd(fd: int) -> None:
    metadata = os.fstat(fd)
    if (
        not stat.S_ISREG(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != 0o600
        or metadata.st_uid != os.getuid()
        or metadata.st_nlink != 1
    ):
        raise SafetyError("Capture file is not a private regular 0600 file")


def _write_file_at(directory_fd: int, name: str, body: bytes) -> None:
    try:
        fd = os.open(name, _FILE_FLAGS, 0o600, dir_fd=directory_fd)
    except OSError as error:
        raise SafetyError("Cannot create private capture file safely") from error
    try:
        os.fchmod(fd, 0o600)
        offset = 0
        while offset < len(body):
            written = os.write(fd, body[offset:])
            if written <= 0:
                raise OSError("short capture write")
            offset += written
        os.fsync(fd)
        _validate_private_file_fd(fd)
    finally:
        os.close(fd)


def _validate_file_at(directory_fd: int, name: str) -> None:
    flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(name, flags, dir_fd=directory_fd)
    except OSError as error:
        raise SafetyError("Cannot validate published capture file safely") from error
    try:
        _validate_private_file_fd(fd)
    finally:
        os.close(fd)


def _rename_directory_noreplace(
    parent_fd: int,
    source: str,
    destination: str,
) -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        raise SafetyError("Atomic no-replace capture publication is unavailable")
    renameat2.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    result = renameat2(
        parent_fd,
        os.fsencode(source),
        parent_fd,
        os.fsencode(destination),
        _RENAME_NOREPLACE,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in {errno.EEXIST, errno.ENOTEMPTY}:
        raise SafetyError("Capture refuses to overwrite an operation directory")
    raise SafetyError("Atomic no-replace capture publication failed") from OSError(
        error_number, os.strerror(error_number)
    )


def _cleanup_staging_at(parent_fd: int, staging_fd: int, staging_name: str) -> None:
    for name in ("request.json", "response.json"):
        with suppress(OSError):
            os.unlink(name, dir_fd=staging_fd)
    with suppress(OSError):
        os.rmdir(staging_name, dir_fd=parent_fd)


def _same_directory(left_fd: int, right_fd: int) -> bool:
    left = os.fstat(left_fd)
    right = os.fstat(right_fd)
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _revalidate_published_capture(
    root: Path,
    run_id: str,
    operation_id: str,
    *,
    root_fd: int,
    run_fd: int,
    operation_fd: int,
) -> None:
    reopened_root_fd: int | None = None
    reopened_run_fd: int | None = None
    reopened_operation_fd: int | None = None
    try:
        reopened_root_fd = _open_absolute_private_root(root, create_missing=False)
        if not _same_directory(reopened_root_fd, root_fd):
            raise SafetyError("Capture published path ancestry changed during publication")
        reopened_run_fd = _open_existing_private_child(reopened_root_fd, run_id)
        if not _same_directory(reopened_run_fd, run_fd):
            raise SafetyError("Capture published run directory changed during publication")
        reopened_operation_fd = _open_existing_private_child(reopened_run_fd, operation_id)
        if not _same_directory(reopened_operation_fd, operation_fd):
            raise SafetyError("Capture published operation directory changed during publication")
        _validate_file_at(reopened_operation_fd, "request.json")
        _validate_file_at(reopened_operation_fd, "response.json")
    finally:
        _close_fd_best_effort(reopened_operation_fd)
        _close_fd_best_effort(reopened_run_fd)
        _close_fd_best_effort(reopened_root_fd)


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
        request_path_values: PathValues | None = None,
        response_path_values: PathValues | None = None,
        approved_path: str | None = None,
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
        raw_path = metadata["path"]
        safe_path = _safe_path(raw_path)
        path = (
            self._sanitize_path(safe_path)
            if approved_path is None
            else _approved_static_path(approved_path, metadata_path=raw_path)
        )

        request_body = self._sanitizer.sanitize(
            request_json,
            enum_keys=enum_keys,
            path_values=request_path_values,
        )
        response_body = self._sanitizer.sanitize(
            response_json,
            enum_keys=enum_keys,
            path_values=response_path_values,
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

        root_fd: int | None = None
        run_fd: int | None = None
        staging_fd: int | None = None
        staging_name: str | None = None
        published_name: str | None = None
        complete = False
        try:
            root_fd = _open_absolute_private_root(self.root)
            run_fd = _open_or_create_private_child(root_fd, run_id)
            if _entry_exists(run_fd, operation_id):
                raise SafetyError("Capture refuses to overwrite an operation directory")
            staging_name, staging_fd = _create_staging_directory(run_fd, operation_id)
            _write_file_at(staging_fd, "request.json", request_bytes)
            _write_file_at(staging_fd, "response.json", response_bytes)
            os.fsync(staging_fd)
            _validate_directory_fd(staging_fd, private=True)
            _validate_file_at(staging_fd, "request.json")
            _validate_file_at(staging_fd, "response.json")
            _rename_directory_noreplace(run_fd, staging_name, operation_id)
            published_name = operation_id
            os.fsync(run_fd)
            _revalidate_published_capture(
                self.root,
                run_id,
                operation_id,
                root_fd=root_fd,
                run_fd=run_fd,
                operation_fd=staging_fd,
            )
            complete = True
        finally:
            try:
                if staging_fd is not None and not complete:
                    assert run_fd is not None
                    cleanup_name = published_name or staging_name
                    assert cleanup_name is not None
                    _cleanup_staging_at(run_fd, staging_fd, cleanup_name)
            finally:
                _close_fd_best_effort(staging_fd)
                _close_fd_best_effort(run_fd)
                _close_fd_best_effort(root_fd)
        operation_path = self.root / run_id / operation_id
        request_path = operation_path / "request.json"
        response_path = operation_path / "response.json"
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
                    enum_keys={normalized},
                )[normalized]
            else:
                safe_value = self._sanitizer.sanitize({normalized: header_value})[normalized]
            result[normalized] = safe_value
        return result

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
