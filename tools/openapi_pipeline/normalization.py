from __future__ import annotations

import copy
import json
import re
from typing import Any

from .io import canonical_json_bytes, sha256_bytes
from .schema import iter_schema_objects

DIRECT_TYPES: dict[str, dict[str, Any]] = {
    "bool": {"type": "boolean"},
    "int": {"type": "integer"},
    "float": {"type": "number", "format": "float"},
    "uuid": {"type": "string", "format": "uuid"},
    "enum": {"type": "string"},
    "strings": {"type": "string"},
    "string <uuid>": {"type": "string", "format": "uuid"},
    "integer <int32>": {"type": "integer", "format": "int32"},
    "integer <int64>": {"type": "integer", "format": "int64"},
    "Array of strings <uuid>": {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    },
}

_NORMALIZED_KEYS = ("type", "format", "items")
_SCALAR_TYPES = frozenset({"boolean", "integer", "number", "string"})


def correction_for_type(value: str) -> dict[str, Any] | None:
    direct = DIRECT_TYPES.get(value)
    if direct is not None:
        return copy.deepcopy(direct)
    constant = re.fullmatch(r"constant string '([^']+)'", value)
    if constant:
        literal = constant.group(1)
        return {"type": "string", "enum": [literal]}
    return None


def _jsonpath(parts: tuple[str | int, ...]) -> str:
    result = "$"
    for part in parts:
        if isinstance(part, int):
            result += f"[{part}]"
        else:
            result += f"[{json.dumps(part, ensure_ascii=False)}]"
    return result


def _guard(issue: str, value: Any) -> dict[str, Any]:
    return {
        "issue": issue,
        "expected-matches": 1,
        "expected-sha256": sha256_bytes(canonical_json_bytes(value)),
    }


def _normalizes_to_scalar(raw_type: str) -> bool:
    if raw_type in _SCALAR_TYPES:
        return True
    correction = correction_for_type(raw_type)
    return correction is not None and correction.get("type") in _SCALAR_TYPES


def build_types_overlay(document: dict[str, Any]) -> dict[str, Any]:
    working = copy.deepcopy(document)
    actions: list[dict[str, Any]] = []
    correction_number = 0
    scalar_required_number = 0

    for path, schema in iter_schema_objects(working):
        raw_type = schema.get("type")
        if not isinstance(raw_type, str):
            continue

        if schema.get("required") == ["true"] and _normalizes_to_scalar(raw_type):
            scalar_required_number += 1
            previous_required = copy.deepcopy(schema["required"])
            actions.append(
                {
                    "target": _jsonpath((*path, "required")),
                    "description": (
                        "Remove malformed iiko scalar-schema required marker"
                    ),
                    "x-iiko-sdk-guard": _guard(
                        f"remove-malformed-scalar-required-{scalar_required_number}",
                        previous_required,
                    ),
                    "remove": True,
                }
            )
            del schema["required"]

        correction = correction_for_type(raw_type)
        if correction is None:
            continue

        correction_number += 1
        issue_prefix = f"normalize-pseudo-type-{correction_number}"

        keys_to_clear = list(_NORMALIZED_KEYS)
        if "enum" in correction:
            keys_to_clear.append("enum")
        for key in keys_to_clear:
            if key not in schema:
                continue
            previous = copy.deepcopy(schema[key])
            actions.append(
                {
                    "target": _jsonpath((*path, key)),
                    "description": (
                        f"Clear {key!r} before normalizing iiko pseudo type {raw_type!r}"
                    ),
                    "x-iiko-sdk-guard": _guard(
                        f"{issue_prefix}-clear-{key}", previous
                    ),
                    "remove": True,
                }
            )
            del schema[key]

        actions.append(
            {
                "target": _jsonpath(path),
                "description": f"Normalize iiko pseudo type {raw_type!r}",
                "x-iiko-sdk-guard": _guard(
                    f"{issue_prefix}-apply", copy.deepcopy(schema)
                ),
                "update": copy.deepcopy(correction),
            }
        )
        schema.update(copy.deepcopy(correction))
    return {
        "overlay": "1.1.0",
        "info": {"title": "Normalize iiko pseudo types", "version": "1.0.0"},
        "actions": actions,
    }
