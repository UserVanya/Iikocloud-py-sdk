from __future__ import annotations

import copy
import math
import struct
from typing import Any

from .errors import SafetyError
from .evidence_analysis import MenuEvidenceAnalysis
from .io import canonical_json_bytes

_VERSIONS = (2, 3, 4)
_ITEM3 = "ExternalMenuItem3"
_COMBO = "ExternalMenuComboItem"
_CATEGORY3 = "ExternalMenuCategory3"
_COMPONENT_PREFIX = "#/components/schemas/"
_MAX_DEPTH = 128
_SYNTHETIC_STRING = "synthetic-value"
_SYNTHETIC_UUID = "f0000000-0000-4000-8000-000000000001"
_SUPPORTED_KEYS = frozenset(
    {
        "additionalProperties",
        "default",
        "deprecated",
        "description",
        "discriminator",
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


def build_and_validate_synthetic_fixtures(
    document: dict[str, Any],
    analysis: MenuEvidenceAnalysis,
) -> dict[int, dict[str, Any]]:
    """Minimize three synthetic response bodies and prove their patched branch matches."""

    retained = frozenset(
        field
        for field, decision in analysis.combo_fields.items()
        if decision.required_action == "retain-required"
    )
    fixtures: dict[int, dict[str, Any]] = {}
    for version in _VERSIONS:
        root = _synthesize(
            document,
            {"$ref": f"{_COMPONENT_PREFIX}ExternalMenuV{version}"},
        )
        if type(root) is not dict:
            raise SafetyError("Evidence synthetic menu root is not an object")
        if version == 4:
            category = _synthesize(
                document,
                {"$ref": f"{_COMPONENT_PREFIX}{_CATEGORY3}"},
            )
            dish = _synthesize(
                document,
                {"$ref": f"{_COMPONENT_PREFIX}{_ITEM3}"},
            )
            combo = _synthesize(
                document,
                {"$ref": f"{_COMPONENT_PREFIX}{_COMBO}"},
                nonempty_properties=retained,
            )
            if type(category) is not dict or type(dish) is not dict or type(combo) is not dict:
                raise SafetyError("Evidence synthetic V4 branches are not objects")
            category["items"] = [dish, combo]
            root["itemGroups"] = [category]
        fixtures[version] = root
    _validate_fixtures(document, fixtures, analysis)
    return fixtures


def _synthesize(
    document: dict[str, Any],
    schema: dict[str, Any],
    *,
    nonempty: bool = False,
    nonempty_properties: frozenset[str] = frozenset(),
    active_refs: frozenset[str] = frozenset(),
    depth: int = 0,
) -> Any:
    if depth > _MAX_DEPTH or type(schema) is not dict:
        raise SafetyError("Evidence synthesis schema is invalid or excessively deep")
    reference = schema.get("$ref")
    if reference is not None:
        target = _resolve_ref(document, reference)
        if reference in active_refs:
            raise SafetyError("Evidence synthesis does not support cyclic schemas")
        return _synthesize(
            document,
            target,
            nonempty=nonempty,
            nonempty_properties=nonempty_properties,
            active_refs=active_refs | {reference},
            depth=depth + 1,
        )
    if set(schema) - _SUPPORTED_KEYS:
        raise SafetyError("Evidence synthesis encountered an unsupported schema keyword")
    enum = schema.get("enum")
    if enum is not None:
        if type(enum) is not list or not enum:
            raise SafetyError("Evidence synthesis enum is invalid")
        return min(copy.deepcopy(enum), key=canonical_json_bytes)
    one_of = schema.get("oneOf")
    if one_of is not None:
        return _synthesize_one_of(
            document,
            one_of,
            nonempty=nonempty,
            active_refs=active_refs,
            depth=depth,
        )
    if schema.get("nullable") is True and not nonempty:
        return None

    schema_type = schema.get("type")
    if schema_type == "object":
        return _synthesize_object(
            document,
            schema,
            nonempty=nonempty,
            nonempty_properties=nonempty_properties,
            active_refs=active_refs,
            depth=depth,
        )
    if schema_type == "array":
        items = schema.get("items")
        if type(items) is not dict:
            raise SafetyError("Evidence synthesis array schema is invalid")
        if not nonempty:
            return []
        return [
            _synthesize(
                document,
                items,
                active_refs=active_refs,
                depth=depth + 1,
            )
        ]
    return _synthesize_scalar(schema)


def _synthesize_one_of(
    document: dict[str, Any],
    one_of: Any,
    *,
    nonempty: bool,
    active_refs: frozenset[str],
    depth: int,
) -> Any:
    if type(one_of) is not list or not one_of:
        raise SafetyError("Evidence synthesis oneOf is invalid")
    candidates: dict[bytes, Any] = {}
    for branch in one_of:
        if type(branch) is not dict:
            raise SafetyError("Evidence synthesis oneOf branch is invalid")
        candidate = _synthesize(
            document,
            branch,
            nonempty=nonempty,
            active_refs=active_refs,
            depth=depth + 1,
        )
        if _match_count(document, candidate, one_of) == 1:
            candidates[canonical_json_bytes(candidate)] = candidate
    if not candidates:
        raise SafetyError("Evidence synthesis cannot make oneOf unambiguous")
    return candidates[min(candidates)]


def _synthesize_object(
    document: dict[str, Any],
    schema: dict[str, Any],
    *,
    nonempty: bool,
    nonempty_properties: frozenset[str],
    active_refs: frozenset[str],
    depth: int,
) -> dict[str, Any]:
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    if type(properties) is not dict or type(required) is not list:
        raise SafetyError("Evidence synthesis object schema is invalid")
    result: dict[str, Any] = {}
    for name in required:
        if type(name) is not str or type(properties.get(name)) is not dict:
            raise SafetyError("Evidence synthesis required property is undefined")
        result[name] = _synthesize(
            document,
            properties[name],
            nonempty=name in nonempty_properties,
            active_refs=active_refs,
            depth=depth + 1,
        )
    if nonempty and not result:
        candidates = sorted(
            name for name, child in properties.items() if type(name) is str and type(child) is dict
        )
        if not candidates:
            raise SafetyError("Evidence synthesis cannot make an object non-empty")
        name = candidates[0]
        result[name] = _synthesize(
            document,
            properties[name],
            active_refs=active_refs,
            depth=depth + 1,
        )
    return result


def _synthesize_scalar(schema: dict[str, Any]) -> Any:
    schema_type = schema.get("type")
    schema_format = schema.get("format")
    if schema_format == "uuid":
        return _SYNTHETIC_UUID
    if schema_format not in {None, "enum", "float", "int32", "int64"}:
        raise SafetyError("Evidence synthesis encountered an unsupported format")
    if schema_type == "string" or schema_type is None:
        minimum = schema.get("minLength", 0)
        maximum = schema.get("maxLength")
        if (
            type(minimum) is not int
            or minimum < 0
            or (maximum is not None and (type(maximum) is not int or maximum < minimum))
        ):
            raise SafetyError("Evidence synthesis string bounds are invalid")
        value = _SYNTHETIC_STRING if len(_SYNTHETIC_STRING) >= minimum else "x" * minimum
        if type(maximum) is int and len(value) > maximum:
            return "" if maximum == 0 else "x" * maximum
        return value
    if schema_type == "boolean":
        return False
    if schema_type == "integer":
        return 0
    if schema_type == "number":
        return 0.0
    raise SafetyError("Evidence synthesis encountered an unsupported schema type")


class _Mismatch(Exception):
    pass


def _validate_fixtures(
    document: dict[str, Any],
    fixtures: dict[int, dict[str, Any]],
    analysis: MenuEvidenceAnalysis,
) -> None:
    response = _at(
        document,
        (
            "paths",
            "/api/2/menu/by_id",
            "post",
            "responses",
            "200",
            "content",
            "application/json",
            "schema",
        ),
    )
    if type(response) is not dict or type(response.get("oneOf")) is not list:
        raise SafetyError("Evidence candidate response oneOf has drifted")
    for version in _VERSIONS:
        fixture = fixtures[version]
        _require_match(
            document,
            fixture,
            {"$ref": f"{_COMPONENT_PREFIX}ExternalMenuV{version}"},
        )
        if _match_count(document, fixture, response["oneOf"]) != 1:
            raise SafetyError("Evidence synthetic response does not match exactly one version")
    _validate_v4_items(document, fixtures[4], analysis)


def _validate_v4_items(
    document: dict[str, Any],
    fixture: dict[str, Any],
    analysis: MenuEvidenceAnalysis,
) -> None:
    v4_items = fixture["itemGroups"][0]["items"]
    union = _at(
        document,
        (
            "components",
            "schemas",
            _CATEGORY3,
            "properties",
            "items",
            "items",
        ),
    )
    if type(union) is not dict or type(union.get("oneOf")) is not list:
        raise SafetyError("Evidence candidate V4 item union has drifted")
    discriminator = union.get("discriminator")
    mapping = discriminator.get("mapping") if type(discriminator) is dict else None
    if type(mapping) is not dict:
        raise SafetyError("Evidence candidate V4 discriminator is missing")
    matched_branches: set[str] = set()
    for item in v4_items:
        matches = _matching_refs(document, item, union["oneOf"])
        if len(matches) != 1:
            raise SafetyError("Evidence synthetic V4 item is not structurally unambiguous")
        literal = item.get("type") if type(item) is dict else None
        if type(literal) is not str or mapping.get(literal) != matches[0]:
            raise SafetyError("Evidence synthetic V4 item conflicts with discriminator mapping")
        matched_branches.add(matches[0])
    expected = {f"{_COMPONENT_PREFIX}{branch}" for branch in analysis.branch_to_literal}
    if matched_branches != expected:
        raise SafetyError("Evidence synthetic V4 fixture must contain both item branches")


def _matching_refs(document: dict[str, Any], value: Any, branches: list[Any]) -> tuple[str, ...]:
    result: list[str] = []
    for branch in branches:
        if type(branch) is not dict or set(branch) != {"$ref"} or type(branch["$ref"]) is not str:
            raise SafetyError("Evidence candidate V4 union branch is unsupported")
        try:
            _validate_instance(document, value, branch, active_refs=frozenset(), depth=0)
        except _Mismatch:
            continue
        result.append(branch["$ref"])
    return tuple(result)


def _match_count(document: dict[str, Any], value: Any, branches: list[Any]) -> int:
    count = 0
    for branch in branches:
        if type(branch) is not dict:
            raise SafetyError("Evidence candidate oneOf branch is invalid")
        try:
            _validate_instance(document, value, branch, active_refs=frozenset(), depth=0)
        except _Mismatch:
            continue
        count += 1
    return count


def _require_match(document: dict[str, Any], value: Any, schema: dict[str, Any]) -> None:
    try:
        _validate_instance(document, value, schema, active_refs=frozenset(), depth=0)
    except _Mismatch as error:
        raise SafetyError(
            "Evidence synthetic fixture does not match its patched schema"
        ) from error


def _validate_instance(
    document: dict[str, Any],
    value: Any,
    schema: dict[str, Any],
    *,
    active_refs: frozenset[str],
    depth: int,
) -> None:
    if depth > _MAX_DEPTH or type(schema) is not dict:
        raise SafetyError("Evidence candidate validation schema is invalid or too deep")
    reference = schema.get("$ref")
    if reference is not None:
        if type(reference) is not str or reference in active_refs:
            raise SafetyError("Evidence candidate validation reference is cyclic or invalid")
        _validate_instance(
            document,
            value,
            _resolve_ref(document, reference),
            active_refs=active_refs | {reference},
            depth=depth + 1,
        )
        return
    if value is None and schema.get("nullable") is True:
        return
    one_of = schema.get("oneOf")
    if one_of is not None:
        if type(one_of) is not list or _match_count(document, value, one_of) != 1:
            raise _Mismatch
        return
    schema_type = schema.get("type")
    if schema_type is not None and not _matches_type(value, schema_type):
        raise _Mismatch
    enum = schema.get("enum")
    if enum is not None and not any(_strict_equal(value, candidate) for candidate in enum):
        raise _Mismatch
    _validate_format(value, schema.get("format"))
    if type(value) is str:
        minimum = schema.get("minLength")
        maximum = schema.get("maxLength")
        if type(minimum) is int and len(value) < minimum:
            raise _Mismatch
        if type(maximum) is int and len(value) > maximum:
            raise _Mismatch
    if type(value) is dict:
        _validate_object(document, value, schema, active_refs=active_refs, depth=depth)
    if type(value) is list:
        _validate_array(document, value, schema, active_refs=active_refs, depth=depth)


def _validate_object(
    document: dict[str, Any],
    value: dict[str, Any],
    schema: dict[str, Any],
    *,
    active_refs: frozenset[str],
    depth: int,
) -> None:
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    if type(properties) is not dict or type(required) is not list:
        raise SafetyError("Evidence candidate validation object schema is invalid")
    if not set(required).issubset(value):
        raise _Mismatch
    if schema.get("additionalProperties") is False and set(value) - set(properties):
        raise _Mismatch
    for name, child in value.items():
        child_schema = properties.get(name)
        if child_schema is not None:
            if type(child_schema) is not dict:
                raise SafetyError("Evidence candidate property schema is invalid")
            _validate_instance(
                document,
                child,
                child_schema,
                active_refs=active_refs,
                depth=depth + 1,
            )


def _validate_array(
    document: dict[str, Any],
    value: list[Any],
    schema: dict[str, Any],
    *,
    active_refs: frozenset[str],
    depth: int,
) -> None:
    items = schema.get("items")
    if items is None:
        return
    if type(items) is not dict:
        raise SafetyError("Evidence candidate array item schema is invalid")
    for child in value:
        _validate_instance(
            document,
            child,
            items,
            active_refs=active_refs,
            depth=depth + 1,
        )


def _validate_format(value: Any, schema_format: Any) -> None:
    if schema_format in {None, "enum"}:
        return
    if schema_format == "uuid":
        if type(value) is not str or value != _SYNTHETIC_UUID:
            raise _Mismatch
        return
    if schema_format == "float":
        try:
            converted = struct.unpack("!f", struct.pack("!f", value))[0]
        except (OverflowError, struct.error, TypeError):
            raise _Mismatch from None
        if not math.isfinite(converted):
            raise _Mismatch
        return
    if schema_format == "int32":
        if type(value) is not int or not -(2**31) <= value < 2**31:
            raise _Mismatch
        return
    if schema_format == "int64":
        if type(value) is not int or not -(2**63) <= value < 2**63:
            raise _Mismatch
        return
    raise SafetyError("Evidence candidate validation encountered an unsupported format")


def _component(document: dict[str, Any], name: str) -> dict[str, Any]:
    components = document.get("components")
    schemas = components.get("schemas") if type(components) is dict else None
    component = schemas.get(name) if type(schemas) is dict else None
    if type(component) is not dict:
        raise SafetyError(f"Evidence candidate component {name!r} is missing")
    return component


def _resolve_ref(document: dict[str, Any], reference: Any) -> dict[str, Any]:
    if (
        type(reference) is not str
        or not reference.startswith(_COMPONENT_PREFIX)
        or not reference[len(_COMPONENT_PREFIX) :]
        or "/" in reference[len(_COMPONENT_PREFIX) :]
    ):
        raise SafetyError("Evidence candidate supports only local component references")
    return _component(document, reference[len(_COMPONENT_PREFIX) :])


def _at(document: dict[str, Any], parts: tuple[str, ...]) -> Any:
    value: Any = document
    try:
        for part in parts:
            if type(value) is not dict:
                raise KeyError(part)
            value = value[part]
    except (KeyError, TypeError):
        raise SafetyError("Evidence candidate reviewed schema path has drifted") from None
    return value


def _matches_type(value: Any, schema_type: Any) -> bool:
    return {
        "array": type(value) is list,
        "boolean": type(value) is bool,
        "integer": type(value) is int,
        "number": type(value) in {int, float},
        "object": type(value) is dict,
        "string": type(value) is str,
    }.get(schema_type, False)


def _strict_equal(left: Any, right: Any) -> bool:
    try:
        return canonical_json_bytes(left) == canonical_json_bytes(right)
    except (TypeError, ValueError):
        return False
