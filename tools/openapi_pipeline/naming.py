from __future__ import annotations

import copy
import keyword
import re
from collections import defaultdict
from typing import Any
from urllib.parse import unquote

from .errors import ValidationError
from .inventory import HTTP_METHODS

_PYTHON_IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_GENERATOR_SCHEMA_NAME = re.compile(r"[a-zA-Z0-9.\-_]+")
_COMPONENT_SCHEMA_REF_PREFIX = "#/components/schemas/"


def _is_python_identifier(value: Any) -> bool:
    return (
        isinstance(value, str)
        and _PYTHON_IDENTIFIER.fullmatch(value) is not None
        and not keyword.iskeyword(value)
    )


def _pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _decode_pointer_token(value: str) -> str | None:
    result: list[str] = []
    index = 0
    while index < len(value):
        character = value[index]
        if character != "~":
            result.append(character)
            index += 1
            continue
        if index + 1 >= len(value) or value[index + 1] not in {"0", "1"}:
            return None
        result.append("~" if value[index + 1] == "0" else "/")
        index += 2
    return "".join(result)


def _component_schema_ref(name: str) -> str:
    return f"{_COMPONENT_SCHEMA_REF_PREFIX}{_pointer_token(name)}"


def _local_component_schema_name(ref: str) -> str | None:
    decoded = unquote(ref)
    if not decoded.startswith(_COMPONENT_SCHEMA_REF_PREFIX):
        return None
    token = decoded.removeprefix(_COMPONENT_SCHEMA_REF_PREFIX)
    if "/" in token:
        return None
    return _decode_pointer_token(token)


def _rewrite_schema_refs(value: Any, replacements: dict[str, str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                raw_name = _local_component_schema_name(child)
                if raw_name in replacements:
                    value[key] = _component_schema_ref(replacements[raw_name])
            else:
                _rewrite_schema_refs(child, replacements)
    elif isinstance(value, list):
        for child in value:
            _rewrite_schema_refs(child, replacements)


def _remaining_schema_refs(value: Any, old_names: frozenset[str]) -> list[str]:
    remaining: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                raw_name = _local_component_schema_name(child)
                if raw_name in old_names:
                    remaining.append(child)
            else:
                remaining.extend(_remaining_schema_refs(child, old_names))
    elif isinstance(value, list):
        for child in value:
            remaining.extend(_remaining_schema_refs(child, old_names))
    return remaining


def inject_operation_ids(source: dict[str, Any], registry: dict[str, str]) -> dict[str, Any]:
    result = copy.deepcopy(source)
    seen: dict[str, str] = {}
    actual_keys: set[str] = set()
    for path, path_item in sorted(result.get("paths", {}).items()):
        for method, operation in sorted(path_item.items()):
            if method.lower() not in HTTP_METHODS:
                continue
            key = f"{method.upper()} {path}"
            actual_keys.add(key)
            if key not in registry:
                raise ValidationError(f"Missing operationId registry entry: {key}")
            operation_id = registry[key]
            if not _is_python_identifier(operation_id):
                raise ValidationError(f"Invalid operationId for {key}: {operation_id!r}")
            if operation_id in seen:
                raise ValidationError(
                    f"Duplicate operationId {operation_id}: {seen[operation_id]} and {key}"
                )
            seen[operation_id] = key
            operation["operationId"] = operation_id
    stale = sorted(set(registry) - actual_keys)
    if stale:
        raise ValidationError(f"Stale operationId registry entries: {', '.join(stale)}")
    return result


def normalize_model_name(raw: str) -> str:
    leaf = raw.rsplit(".", 1)[-1]
    leaf = re.sub(r"`\d+", "", leaf)
    words = re.findall(r"[A-Za-z0-9]+", leaf)
    if not words:
        raise ValidationError(f"Cannot normalize model name: {raw!r}")
    name = "".join(word[:1].upper() + word[1:] for word in words)
    if name[0].isdigit():
        name = f"Model{name}"
    if not _is_python_identifier(name):
        raise ValidationError(
            f"Invalid auto-normalized model name for {raw}: {name!r}; add an explicit override"
        )
    return name


def build_model_mappings(schemas: dict[str, Any], overrides: dict[str, str]) -> dict[str, str]:
    unknown = sorted(set(overrides) - set(schemas))
    if unknown:
        raise ValidationError(f"Stale model name overrides: {', '.join(unknown)}")

    for raw in sorted(overrides):
        model_name = overrides[raw]
        if not _is_python_identifier(model_name):
            raise ValidationError(f"Invalid model name override for {raw}: {model_name!r}")

    result = {
        raw: overrides[raw] if raw in overrides else normalize_model_name(raw)
        for raw in sorted(schemas)
    }
    reverse: dict[str, list[str]] = defaultdict(list)
    for raw, normalized in result.items():
        reverse[normalized].append(raw)
    collisions = {name: raws for name, raws in sorted(reverse.items()) if len(raws) > 1}
    if collisions:
        details = "; ".join(f"{name}: {', '.join(raws)}" for name, raws in collisions.items())
        raise ValidationError(f"Normalized model name collisions: {details}")
    return result


def normalize_generator_schema_names(
    source: dict[str, Any], overrides: dict[str, str]
) -> tuple[dict[str, Any], dict[str, str]]:
    components = source.get("components")
    schemas_value = components.get("schemas") if isinstance(components, dict) else None
    if schemas_value is None:
        schemas: dict[str, Any] = {}
    elif not isinstance(schemas_value, dict):
        raise ValidationError("OpenAPI components.schemas must be an object")
    else:
        schemas = schemas_value
    if not all(isinstance(name, str) for name in schemas):
        raise ValidationError("OpenAPI component schema names must be strings")

    invalid_names = tuple(
        sorted(name for name in schemas if _GENERATOR_SCHEMA_NAME.fullmatch(name) is None)
    )
    missing = tuple(name for name in invalid_names if name not in overrides)
    if missing:
        raise ValidationError(
            "Generator-invalid schema keys require an explicit reviewed model-name "
            f"override: {', '.join(missing)}"
        )

    replacements: dict[str, str] = {}
    targets: dict[str, list[str]] = defaultdict(list)
    for raw_name in invalid_names:
        target = overrides[raw_name]
        if not _is_python_identifier(target) or _GENERATOR_SCHEMA_NAME.fullmatch(target) is None:
            raise ValidationError(f"Invalid physical schema target for {raw_name}: {target!r}")
        replacements[raw_name] = target
        targets[target].append(raw_name)

    duplicate_targets = {
        target: raw_names for target, raw_names in sorted(targets.items()) if len(raw_names) > 1
    }
    if duplicate_targets:
        details = "; ".join(
            f"{target}: {', '.join(sorted(raw_names))}"
            for target, raw_names in duplicate_targets.items()
        )
        raise ValidationError(f"duplicate physical schema target: {details}")

    untouched_names = set(schemas) - set(invalid_names)
    collisions = sorted(set(replacements.values()) & untouched_names)
    if collisions:
        raise ValidationError(
            "physical schema target collision with untouched component: " + ", ".join(collisions)
        )

    raw_mappings = build_model_mappings(schemas, overrides)
    corrected = copy.deepcopy(source)
    corrected_components = corrected.get("components")
    corrected_schemas = (
        corrected_components.get("schemas") if isinstance(corrected_components, dict) else None
    )
    if not isinstance(corrected_schemas, dict):
        if schemas:
            raise ValidationError("OpenAPI components.schemas must be an object")
    elif isinstance(corrected_components, dict):
        renamed_schemas = {
            replacements.get(raw_name, raw_name): schema
            for raw_name, schema in corrected_schemas.items()
        }
        corrected_components["schemas"] = dict(sorted(renamed_schemas.items()))

    _rewrite_schema_refs(corrected, replacements)

    final_components = corrected.get("components")
    final_schemas = final_components.get("schemas") if isinstance(final_components, dict) else {}
    if not isinstance(final_schemas, dict) or any(
        not isinstance(name, str) or _GENERATOR_SCHEMA_NAME.fullmatch(name) is None
        for name in final_schemas
    ):
        raise ValidationError("Generator-invalid component schema key remains")
    if _remaining_schema_refs(corrected, frozenset(replacements)):
        raise ValidationError("Generator-invalid component schema reference remains")

    corrected_mappings = {
        replacements.get(raw_name, raw_name): target for raw_name, target in raw_mappings.items()
    }
    return corrected, dict(sorted(corrected_mappings.items()))
