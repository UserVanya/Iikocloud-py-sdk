from __future__ import annotations

import json
import math
import re
import struct
from collections.abc import Mapping
from typing import Any, cast

from .capture import RedactionHints, Sanitizer
from .errors import SafetyError
from .evidence import build_versioned_evidence_redaction_hints
from .io import canonical_json_bytes, sha256_bytes

_OPERATION = "get_external_menu_by_id"
_VERSIONS = frozenset({2, 3, 4})
_VERSION_COMPONENTS = {
    2: "ExternalMenuV2",
    3: "ExternalMenuV3",
    4: "ExternalMenuV4",
}
_MENU_REQUEST_COMPONENT = "iikoTransport.PublicApi.Contracts.Nomenclature.MenuRequest"
_COMPONENT_PREFIX = "#/components/schemas/"
_SUPPORTED_SCHEMA_KEYS = frozenset(
    {
        "$ref",
        "additionalProperties",
        "default",
        "deprecated",
        "description",
        "enum",
        "example",
        "format",
        "items",
        "maxLength",
        "minLength",
        "nullable",
        "oneOf",
        "properties",
        "required",
        "title",
        "type",
    }
)
_SUPPORTED_TYPES = frozenset({"array", "boolean", "integer", "number", "object", "string"})
_SUPPORTED_FORMATS = frozenset({"enum", "float", "int32", "int64", "uuid"})
_FORMAT_TYPES = {
    "enum": "string",
    "float": "number",
    "int32": "integer",
    "int64": "integer",
    "uuid": "string",
}
_UUID_FORMAT = re.compile(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\Z"
)
_BROKEN_COMBO_COMPONENT = "ExternalMenuComboItem"
_ITEM3_COMPONENT = "ExternalMenuItem3"
_V4_ITEM_BRANCHES = (_ITEM3_COMPONENT, _BROKEN_COMBO_COMPONENT)
_RAW_ITEM_TYPES = frozenset({"DISH", "COMBO"})
_BROKEN_COMBO_UNDEFINED_REQUIRED = frozenset(
    {
        "allergenGroupIds",
        "itemSizes",
        "modifierSchemaId",
        "orderItemType",
        "splittable",
    }
)
_MAX_SCHEMA_DEPTH = 256
_REVIEWED_COMBO_SHA256 = "dcc5f6184a905905df5a1ba2818157da41603a9b488dc178bc8ae4401635d6b2"
_REVIEWED_ITEM_UNION_SHA256 = "a4bcd95a4d376a2e0d0cb7e7f19e2b97a48379cfea7219c79f5287eba3d32af0"


class MenuEvidenceValidator:
    """Concrete, immutable validation contract derived from one reviewed effective schema."""

    def __init__(self, effective_schema: dict[str, Any]) -> None:
        self._schema = _strict_document_copy(effective_schema)
        self._components = _schema_components(self._schema)
        self._request_schema = _reviewed_request_schema(self._schema)
        self._root_schemas = {
            version: self._component(name) for version, name in _VERSION_COMPONENTS.items()
        }
        self._hints = {
            version: build_versioned_evidence_redaction_hints(
                self._schema,
                _OPERATION,
                version,
            )
            for version in sorted(_VERSIONS)
        }
        self._broken_combo_schema = self._component(_BROKEN_COMBO_COMPONENT)
        category = self._component("ExternalMenuCategory3")
        properties = category.get("properties")
        items = properties.get("items") if type(properties) is dict else None
        known_item_union = items.get("items") if type(items) is dict else None
        if type(known_item_union) is not dict:
            raise SafetyError("Evidence V4 item union is missing after reviewed hint validation")
        self._known_item_union = cast(dict[str, Any], known_item_union)
        if sha256_bytes(canonical_json_bytes(self._broken_combo_schema)) != (
            _REVIEWED_COMBO_SHA256
        ):
            raise SafetyError("Reviewed ExternalMenuComboItem defect fragment has drifted")
        if sha256_bytes(canonical_json_bytes(self._known_item_union)) != (
            _REVIEWED_ITEM_UNION_SHA256
        ):
            raise SafetyError("Reviewed ExternalMenuCategory3 item union has drifted")
        self._preflight_contract()

    def validate(
        self,
        version: int,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> None:
        if type(version) is not int or version not in _VERSIONS:
            raise SafetyError("Evidence validator version must be exactly 2, 3, or 4")
        request_value = _mutable_json_copy(request)
        response_value = _mutable_json_copy(response)
        if type(request_value) is not dict or type(response_value) is not dict:
            raise SafetyError("Evidence validator envelopes must be strict JSON objects")
        request_body = request_value.get("body")
        response_body = response_value.get("body")
        if type(request_body) is not dict or type(response_body) is not dict:
            raise SafetyError("Evidence validator bodies must be strict JSON objects")

        self._validate_instance(request_body, self._request_schema, path="request")
        self._validate_instance(
            response_body,
            self._root_schemas[version],
            path=f"response-v{version}",
            component_name=_VERSION_COMPONENTS[version],
        )
        if (
            type(response_body.get("formatVersion")) is not int
            or response_body.get("formatVersion") != version
        ):
            raise SafetyError("Evidence response root does not match the selected menu version")
        self._require_sanitizer_fixed_point(
            request_body,
            response_body,
            hints=self._hints[version],
        )
        return None

    def match_v4_item_branches(self, item: Mapping[str, Any]) -> tuple[str, ...]:
        """Return the reviewed structural V4 branches accepting one raw item."""

        value = _mutable_json_copy(item)
        if type(value) is not dict:
            raise SafetyError("Evidence V4 item branch matching requires an object")
        discriminator = value.get("type")
        if type(discriminator) is not str or discriminator not in _RAW_ITEM_TYPES:
            raise SafetyError("Evidence V4 item discriminator must be a raw DISH or COMBO literal")
        branches = self._known_item_union.get("oneOf")
        if type(branches) is not list or len(branches) != len(_V4_ITEM_BRANCHES):
            raise SafetyError("Reviewed Evidence V4 item branches have drifted")
        matches: list[str] = []
        for index, branch in enumerate(branches):
            if type(branch) is not dict or set(branch) != {"$ref"}:
                raise SafetyError("Reviewed Evidence V4 item branch has drifted")
            branch_name, target = self._resolve_reference(branch["$ref"])
            if branch_name != _V4_ITEM_BRANCHES[index]:
                raise SafetyError("Reviewed Evidence V4 item branch order has drifted")
            try:
                self._validate_instance(
                    value,
                    target,
                    path="response-v4.item",
                    component_name=branch_name,
                )
            except SafetyError:
                continue
            matches.append(branch_name)
        if not matches:
            raise SafetyError("Evidence V4 item does not match a reviewed schema branch")
        return tuple(matches)

    def validate_v4_item3_property(
        self,
        property_name: str,
        value: object,
    ) -> dict[str, Any]:
        """Validate one exact-five value and return its reviewed sibling schema copy."""

        if property_name not in _BROKEN_COMBO_UNDEFINED_REQUIRED:
            raise SafetyError("Evidence combo inference property is outside the exact-five scope")
        item = self._component(_ITEM3_COMPONENT)
        properties = item.get("properties")
        schema = properties.get(property_name) if type(properties) is dict else None
        if type(schema) is not dict:
            raise SafetyError("Evidence combo sibling property schema is missing or invalid")
        copied_value = _mutable_json_copy(value)
        self._validate_instance(
            copied_value,
            schema,
            path=f"response-v4.item.{property_name}",
            component_name=_ITEM3_COMPONENT,
        )
        return _mutable_json_copy(schema)

    def _component(self, name: str) -> dict[str, Any]:
        value = self._components.get(name)
        if type(value) is not dict:
            raise SafetyError(f"Evidence schema component {name!r} is missing or invalid")
        return value

    def _preflight_contract(self) -> None:
        visited: set[str] = set()
        active: set[str] = set()
        self._preflight_schema(
            self._request_schema,
            path="request",
            component_name=None,
            visited=visited,
            active=active,
            depth=0,
        )
        for version, component_name in _VERSION_COMPONENTS.items():
            self._preflight_schema(
                self._root_schemas[version],
                path=f"components.schemas.{component_name}",
                component_name=component_name,
                visited=visited,
                active=active,
                depth=0,
            )

    def _preflight_schema(
        self,
        schema: object,
        *,
        path: str,
        component_name: str | None,
        visited: set[str],
        active: set[str],
        depth: int,
    ) -> None:
        if depth > _MAX_SCHEMA_DEPTH or type(schema) is not dict:
            raise SafetyError("Evidence schema contains an invalid or excessively deep node")
        unknown = set(schema) - _SUPPORTED_SCHEMA_KEYS
        if unknown:
            raise SafetyError("Evidence schema uses an unsupported validation keyword")
        schema_type = schema.get("type")
        if schema_type is not None and (
            type(schema_type) is not str or schema_type not in _SUPPORTED_TYPES
        ):
            raise SafetyError("Evidence schema uses an unsupported type contract")
        nullable = schema.get("nullable")
        if nullable is not None and type(nullable) is not bool:
            raise SafetyError("Evidence schema nullable flag is invalid")
        if (
            any(
                keyword in schema for keyword in ("properties", "required", "additionalProperties")
            )
            and schema_type != "object"
        ):
            raise SafetyError("Evidence schema object keywords require type object")
        if "items" in schema and schema_type != "array":
            raise SafetyError("Evidence schema items keyword requires type array")
        if schema_type == "array" and "items" not in schema:
            raise SafetyError("Evidence schema array contract requires items")
        if "items" in schema and type(schema["items"]) is not dict:
            raise SafetyError("Evidence schema items contract must be an object")
        if any(keyword in schema for keyword in ("minLength", "maxLength")) and (
            schema_type != "string"
        ):
            raise SafetyError("Evidence schema length keywords require type string")
        if nullable is not None and schema_type is None and "oneOf" not in schema:
            raise SafetyError("Evidence schema nullable placement has drifted")
        if "oneOf" in schema and set(schema).intersection(
            {
                "additionalProperties",
                "enum",
                "format",
                "items",
                "maxLength",
                "minLength",
                "properties",
                "required",
                "type",
            }
        ):
            raise SafetyError("Evidence schema oneOf placement has drifted")
        for annotation in ("description", "format", "title"):
            if annotation in schema and type(schema[annotation]) is not str:
                raise SafetyError("Evidence schema annotation shape has drifted")
        if "deprecated" in schema and type(schema["deprecated"]) is not bool:
            raise SafetyError("Evidence schema deprecated flag is invalid")
        schema_format = schema.get("format")
        if schema_format is not None and schema_format not in _SUPPORTED_FORMATS:
            raise SafetyError("Evidence schema format is unsupported")
        if schema_format is not None and _FORMAT_TYPES[schema_format] != schema_type:
            raise SafetyError("Evidence schema format/type contract has drifted")
        if schema_format == "enum" and "enum" not in schema:
            raise SafetyError("Evidence schema enum format lacks its enum contract")

        properties = schema.get("properties", {})
        if type(properties) is not dict or any(
            type(name) is not str or type(value) is not dict for name, value in properties.items()
        ):
            raise SafetyError("Evidence schema properties contract is invalid")
        required = schema.get("required", [])
        if (
            type(required) is not list
            or any(type(name) is not str or not name for name in required)
            or len(set(required)) != len(required)
        ):
            raise SafetyError("Evidence schema required contract is invalid")
        undefined_required = set(required) - set(properties)
        if component_name == _BROKEN_COMBO_COMPONENT and path == (
            f"components.schemas.{_BROKEN_COMBO_COMPONENT}"
        ):
            if undefined_required != _BROKEN_COMBO_UNDEFINED_REQUIRED:
                raise SafetyError("Known ExternalMenuComboItem defect has drifted")
        elif undefined_required:
            raise SafetyError("Evidence schema contains an unsupported undefined required field")

        if "additionalProperties" in schema and schema["additionalProperties"] is not False:
            raise SafetyError("Evidence schema additionalProperties contract is unsupported")
        for keyword in ("minLength", "maxLength"):
            value = schema.get(keyword)
            if value is not None and (type(value) is not int or value < 0):
                raise SafetyError("Evidence schema string length contract is invalid")
        if (
            type(schema.get("minLength")) is int
            and type(schema.get("maxLength")) is int
            and schema["minLength"] > schema["maxLength"]
        ):
            raise SafetyError("Evidence schema string length bounds are inverted")
        enum = schema.get("enum")
        if enum is not None:
            if schema_type is None:
                raise SafetyError("Evidence schema enum requires an explicit type")
            if type(enum) is not list or not enum:
                raise SafetyError("Evidence schema enum contract is invalid")
            encoded = [canonical_json_bytes(value) for value in enum]
            if len(set(encoded)) != len(encoded):
                raise SafetyError("Evidence schema enum values must be type-strict and unique")
            if schema_type is not None and any(
                not _matches_type(value, schema_type) for value in enum
            ):
                raise SafetyError("Evidence schema enum value types have drifted")

        reference = schema.get("$ref")
        if reference is not None:
            if set(schema) != {"$ref"}:
                raise SafetyError("Evidence schema reference siblings are unsupported")
            target_name, target = self._resolve_reference(reference)
            if target_name in active:
                raise SafetyError("Evidence schema reference cycles are unsupported")
            if target_name not in visited:
                active.add(target_name)
                self._preflight_schema(
                    target,
                    path=f"components.schemas.{target_name}",
                    component_name=target_name,
                    visited=visited,
                    active=active,
                    depth=depth + 1,
                )
                active.remove(target_name)
                visited.add(target_name)

        for name, child in properties.items():
            self._preflight_schema(
                child,
                path=f"{path}.properties.{name}",
                component_name=component_name,
                visited=visited,
                active=active,
                depth=depth + 1,
            )
        items = schema.get("items")
        if items is not None:
            self._preflight_schema(
                items,
                path=f"{path}.items",
                component_name=component_name,
                visited=visited,
                active=active,
                depth=depth + 1,
            )
        one_of = schema.get("oneOf")
        if one_of is not None:
            if (
                type(one_of) is not list
                or not one_of
                or any(type(branch) is not dict for branch in one_of)
            ):
                raise SafetyError("Evidence schema oneOf contract is invalid")
            for index, branch in enumerate(one_of):
                self._preflight_schema(
                    branch,
                    path=f"{path}.oneOf.{index}",
                    component_name=component_name,
                    visited=visited,
                    active=active,
                    depth=depth + 1,
                )

    def _resolve_reference(self, reference: object) -> tuple[str, dict[str, Any]]:
        if (
            type(reference) is not str
            or not reference.startswith(_COMPONENT_PREFIX)
            or "/" in reference[len(_COMPONENT_PREFIX) :]
            or not reference[len(_COMPONENT_PREFIX) :]
        ):
            raise SafetyError("Evidence schema reference is not an approved component reference")
        name = reference[len(_COMPONENT_PREFIX) :]
        return name, self._component(name)

    def _validate_instance(
        self,
        value: Any,
        schema: dict[str, Any],
        *,
        path: str,
        component_name: str | None = None,
    ) -> None:
        if value is None and schema.get("nullable") is True:
            return
        reference = schema.get("$ref")
        if reference is not None:
            target_name, target = self._resolve_reference(reference)
            self._validate_instance(
                value,
                target,
                path=path,
                component_name=target_name,
            )
            return
        one_of = schema.get("oneOf")
        if one_of is not None:
            self._validate_one_of(value, schema, path=path, component_name=component_name)
            return

        schema_type = schema.get("type")
        if schema_type is not None and not _matches_type(value, schema_type):
            raise SafetyError("Evidence value does not match its reviewed schema type")
        if schema_type is None and type(value) in {dict, list}:
            raise SafetyError("Evidence untyped schema cannot accept a container value")
        _validate_format(value, schema.get("format"))
        enum = schema.get("enum")
        if enum is not None and not any(_type_strict_equal(value, item) for item in enum):
            raise SafetyError("Evidence value does not match its reviewed schema enum")
        if type(value) is str:
            minimum = schema.get("minLength")
            maximum = schema.get("maxLength")
            if type(minimum) is int and len(value) < minimum:
                raise SafetyError("Evidence string is shorter than its reviewed schema minimum")
            if type(maximum) is int and len(value) > maximum:
                raise SafetyError("Evidence string is longer than its reviewed schema maximum")
        if type(value) is dict:
            properties = schema.get("properties", {})
            required = set(schema.get("required", []))
            is_broken_combo = schema is self._broken_combo_schema
            if is_broken_combo:
                required -= _BROKEN_COMBO_UNDEFINED_REQUIRED
            if not required.issubset(value):
                raise SafetyError("Evidence object is missing a reviewed required property")
            unknown = set(value) - set(properties)
            if is_broken_combo:
                if not unknown.issubset(_BROKEN_COMBO_UNDEFINED_REQUIRED):
                    raise SafetyError(
                        "ExternalMenuComboItem contains an unreviewed undefined property"
                    )
            elif unknown:
                raise SafetyError("Evidence object contains an undeclared property")
            for name, child in value.items():
                property_schema = properties.get(name)
                if property_schema is not None:
                    self._validate_instance(
                        child,
                        property_schema,
                        path=f"{path}.{name}",
                        component_name=component_name,
                    )
        if type(value) is list and "items" in schema:
            for index, item in enumerate(value):
                self._validate_instance(
                    item,
                    schema["items"],
                    path=f"{path}[{index}]",
                    component_name=component_name,
                )

    def _validate_one_of(
        self,
        value: Any,
        schema: dict[str, Any],
        *,
        path: str,
        component_name: str | None,
    ) -> None:
        branches = schema["oneOf"]
        if schema is self._known_item_union:
            self.match_v4_item_branches(value)
            return
        matches = 0
        for branch in branches:
            try:
                self._validate_instance(
                    value,
                    branch,
                    path=path,
                    component_name=component_name,
                )
            except SafetyError:
                continue
            matches += 1
        if matches != 1:
            raise SafetyError("Evidence value does not match exactly one reviewed schema branch")

    @staticmethod
    def _require_sanitizer_fixed_point(
        request_body: dict[str, Any],
        response_body: dict[str, Any],
        *,
        hints: RedactionHints,
    ) -> None:
        sanitizer = Sanitizer.for_fixed_point_validation()
        sanitized_request = sanitizer.sanitize(
            request_body,
            path_values=hints.request_values,
        )
        sanitized_response = sanitizer.sanitize(
            response_body,
            path_values=hints.response_values_for_status(200),
        )
        if not _type_strict_equal(sanitized_request, request_body) or not _type_strict_equal(
            sanitized_response,
            response_body,
        ):
            raise SafetyError("Evidence bodies are not a schema-aware sanitizer fixed point")


def _schema_components(document: dict[str, Any]) -> dict[str, Any]:
    components = document.get("components")
    schemas = components.get("schemas") if type(components) is dict else None
    if type(schemas) is not dict or any(type(name) is not str for name in schemas):
        raise SafetyError("Evidence effective schema components are missing or invalid")
    return schemas


def _reviewed_request_schema(document: dict[str, Any]) -> dict[str, Any]:
    paths = document.get("paths")
    path_item = paths.get("/api/2/menu/by_id") if type(paths) is dict else None
    operation = path_item.get("post") if type(path_item) is dict else None
    request_body = operation.get("requestBody") if type(operation) is dict else None
    content = request_body.get("content") if type(request_body) is dict else None
    media = content.get("application/json") if type(content) is dict else None
    schema = media.get("schema") if type(media) is dict else None
    expected = {"$ref": f"{_COMPONENT_PREFIX}{_MENU_REQUEST_COMPONENT}"}
    if schema != expected:
        raise SafetyError("Evidence menu request schema reference has drifted")
    return schema


def _strict_document_copy(value: object) -> dict[str, Any]:
    copied = _mutable_json_copy(value)
    if type(copied) is not dict:
        raise SafetyError("Evidence effective schema must be a strict JSON object")
    try:
        return json.loads(canonical_json_bytes(copied))
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise SafetyError("Evidence effective schema is not strict canonical JSON data") from error


def _mutable_json_copy(
    value: object,
    *,
    depth: int = 0,
    active: set[int] | None = None,
) -> Any:
    if depth > _MAX_SCHEMA_DEPTH:
        raise SafetyError("Evidence JSON value exceeds the maximum supported depth")
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError("Evidence JSON value contains a non-finite number")
        return value
    if not isinstance(value, (Mapping, tuple, list)):
        raise SafetyError("Evidence value is not strict JSON data")
    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError("Evidence JSON value contains a cycle")
    seen.add(identity)
    try:
        if isinstance(value, Mapping):
            if any(type(key) is not str for key in value):
                raise SafetyError("Evidence JSON object keys must be strings")
            return {
                key: _mutable_json_copy(item, depth=depth + 1, active=seen)
                for key, item in value.items()
            }
        return [_mutable_json_copy(item, depth=depth + 1, active=seen) for item in value]
    finally:
        seen.remove(identity)


def _matches_type(value: object, schema_type: object) -> bool:
    if type(schema_type) is not str:
        return False
    return {
        "array": type(value) is list,
        "boolean": type(value) is bool,
        "integer": type(value) is int,
        "number": type(value) in {int, float},
        "object": type(value) is dict,
        "string": type(value) is str,
    }.get(schema_type, False)


def _validate_format(value: object, schema_format: object) -> None:
    if schema_format is None:
        return
    if type(schema_format) is not str:
        raise SafetyError("Evidence value uses an invalid runtime format")
    if schema_format == "enum":
        return
    if schema_format == "float":
        try:
            converted = struct.unpack("!f", struct.pack("!f", value))[0]
        except (OverflowError, struct.error, TypeError):
            raise SafetyError("Evidence number is outside its reviewed float range") from None
        if not math.isfinite(converted) or (value != 0 and converted == 0.0):
            raise SafetyError("Evidence number is outside its reviewed float range")
        return
    if schema_format == "uuid":
        if type(value) is not str or _UUID_FORMAT.fullmatch(value) is None:
            raise SafetyError("Evidence string does not match its reviewed uuid format")
        return
    if schema_format == "int32":
        if type(value) is not int or not -(2**31) <= value < 2**31:
            raise SafetyError("Evidence integer is outside its reviewed int32 range")
        return
    if schema_format == "int64":
        if type(value) is not int or not -(2**63) <= value < 2**63:
            raise SafetyError("Evidence integer is outside its reviewed int64 range")
        return
    raise SafetyError("Evidence value uses an unsupported runtime format")


def _type_strict_equal(left: object, right: object) -> bool:
    try:
        return canonical_json_bytes(left) == canonical_json_bytes(right)
    except (TypeError, ValueError) as error:
        raise SafetyError("Evidence value cannot be compared as strict canonical JSON") from error
