from __future__ import annotations

import copy
import keyword
import re
from collections import defaultdict
from typing import Any

from .errors import ValidationError
from .inventory import HTTP_METHODS

_PYTHON_IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def _is_python_identifier(value: Any) -> bool:
    return (
        isinstance(value, str)
        and _PYTHON_IDENTIFIER.fullmatch(value) is not None
        and not keyword.iskeyword(value)
    )


def inject_operation_ids(
    source: dict[str, Any], registry: dict[str, str]
) -> dict[str, Any]:
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
    return name


def build_model_mappings(
    schemas: dict[str, Any], overrides: dict[str, str]
) -> dict[str, str]:
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
    collisions = {
        name: raws for name, raws in sorted(reverse.items()) if len(raws) > 1
    }
    if collisions:
        details = "; ".join(f"{name}: {', '.join(raws)}" for name, raws in collisions.items())
        raise ValidationError(f"Normalized model name collisions: {details}")
    return result
