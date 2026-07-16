from __future__ import annotations

import copy
import json
import re
from typing import Any

from .io import canonical_json_bytes, sha256_bytes

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


def build_types_overlay(document: dict[str, Any]) -> dict[str, Any]:
    working = copy.deepcopy(document)
    actions: list[dict[str, Any]] = []
    correction_number = 0

    def visit(value: Any, path: tuple[str | int, ...]) -> None:
        nonlocal correction_number

        if isinstance(value, dict):
            raw_type = value.get("type")
            if isinstance(raw_type, str):
                correction = correction_for_type(raw_type)
                if correction is not None:
                    correction_number += 1
                    issue_prefix = f"normalize-pseudo-type-{correction_number}"

                    keys_to_clear = list(_NORMALIZED_KEYS)
                    if "enum" in correction:
                        keys_to_clear.append("enum")
                    for key in keys_to_clear:
                        if key not in value:
                            continue
                        previous = copy.deepcopy(value[key])
                        actions.append(
                            {
                                "target": _jsonpath((*path, key)),
                                "description": (
                                    f"Clear {key!r} before normalizing iiko pseudo type "
                                    f"{raw_type!r}"
                                ),
                                "x-iiko-sdk-guard": _guard(
                                    f"{issue_prefix}-clear-{key}", previous
                                ),
                                "remove": True,
                            }
                        )
                        del value[key]

                    actions.append(
                        {
                            "target": _jsonpath(path),
                            "description": f"Normalize iiko pseudo type {raw_type!r}",
                            "x-iiko-sdk-guard": _guard(
                                f"{issue_prefix}-apply", copy.deepcopy(value)
                            ),
                            "update": copy.deepcopy(correction),
                        }
                    )
                    value.update(copy.deepcopy(correction))

            for key in sorted(value):
                visit(value[key], (*path, key))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, (*path, index))

    visit(working, ())
    return {
        "overlay": "1.1.0",
        "info": {"title": "Normalize iiko pseudo types", "version": "1.0.0"},
        "actions": actions,
    }
