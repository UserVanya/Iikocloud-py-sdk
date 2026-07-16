from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

import jsonpath_rfc9535 as jsonpath
import yaml

from .errors import StaleOverlayError, ValidationError
from .io import canonical_json_bytes, sha256_bytes

_SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")
_PRIMITIVE_TYPES = (str, int, float, bool, type(None))


def _merge(target: Any, update: Any) -> Any:
    if isinstance(target, dict) and isinstance(update, dict):
        merged = copy.deepcopy(target)
        for key, value in update.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    if isinstance(target, list) and isinstance(update, list):
        return copy.deepcopy(target) + copy.deepcopy(update)
    if isinstance(target, _PRIMITIVE_TYPES) and isinstance(update, _PRIMITIVE_TYPES):
        return copy.deepcopy(update)
    raise ValidationError(
        "Overlay update types are incompatible: "
        f"{type(target).__name__} and {type(update).__name__}"
    )


def _guard(action: dict[str, Any], values: list[Any]) -> None:
    guard = action.get("x-iiko-sdk-guard")
    if not isinstance(guard, dict):
        raise ValidationError("Every overlay action requires x-iiko-sdk-guard")

    issue = guard.get("issue", "unnamed-overlay-action")
    if not isinstance(issue, str) or not issue.strip():
        raise ValidationError("Overlay guard.issue must be a non-empty string")

    expected_matches = guard.get("expected-matches")
    if (
        not isinstance(expected_matches, int)
        or isinstance(expected_matches, bool)
        or expected_matches < 1
    ):
        raise ValidationError("Overlay guard.expected-matches must be a positive integer")

    expected_hash = guard.get("expected-sha256")
    if expected_hash is not None and (
        not isinstance(expected_hash, str) or _SHA256_PATTERN.fullmatch(expected_hash) is None
    ):
        raise ValidationError(
            "Overlay guard.expected-sha256 must be a lowercase SHA-256 digest"
        )

    if expected_matches != len(values):
        raise StaleOverlayError(
            f"{issue}: expected {expected_matches} matches, found {len(values)}"
        )

    actual_value = values[0] if len(values) == 1 else values
    actual_hash = sha256_bytes(canonical_json_bytes(actual_value))
    if expected_hash is not None and expected_hash != actual_hash:
        raise StaleOverlayError(f"{issue}: upstream fragment hash changed")


def _find_nodes(expression: str, document: dict[str, Any], field: str) -> list[Any]:
    try:
        return list(jsonpath.find(expression, document))
    except jsonpath.JSONPathError as error:
        raise ValidationError(f"Invalid overlay {field} JSONPath: {expression}") from error


def _remove_node(node: Any) -> None:
    if node.parent is None or not node.location:
        raise ValidationError("Overlay cannot remove the document root")
    key = node.location[-1]
    parent = node.parent.value
    if isinstance(parent, list) and isinstance(key, int):
        parent.pop(key)
    elif isinstance(parent, dict) and isinstance(key, str):
        del parent[key]
    else:
        raise ValidationError("Overlay remove target has an unsupported parent")


def _remove_sort_key(node: Any) -> tuple[int, tuple[tuple[int, int | str], ...]]:
    comparable_location = tuple(
        (0, key) if isinstance(key, int) else (1, key) for key in node.location
    )
    return len(node.location), comparable_location


def _validate_overlay(overlay: Any) -> list[dict[str, Any]]:
    if not isinstance(overlay, dict):
        raise ValidationError("Overlay must be an object")
    if overlay.get("overlay") != "1.1.0":
        raise ValidationError("Only Overlay 1.1.0 is supported")

    info = overlay.get("info")
    if not isinstance(info, dict) or any(
        not isinstance(info.get(key), str) or not info[key].strip()
        for key in ("title", "version")
    ):
        raise ValidationError("Overlay info.title and info.version must be non-empty strings")

    actions = overlay.get("actions")
    if not isinstance(actions, list) or not actions:
        raise ValidationError("Overlay actions must be a non-empty list")
    if not all(isinstance(action, dict) for action in actions):
        raise ValidationError("Overlay action must be an object")
    return actions


def _validate_action_operation(action: dict[str, Any]) -> str:
    operations = [name for name in ("update", "copy", "remove") if name in action]
    if len(operations) != 1:
        raise ValidationError("Overlay action requires exactly one of update, copy, or remove")

    operation = operations[0]
    if operation == "remove" and action[operation] is not True:
        raise ValidationError("Overlay action.remove must be true")
    if operation == "copy" and (
        not isinstance(action[operation], str) or not action[operation]
    ):
        raise ValidationError("Overlay action.copy must be a JSONPath string")
    return operation


def apply_overlay(source: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(source, dict):
        raise ValidationError("OpenAPI target document must be an object")

    actions = _validate_overlay(overlay)
    result = copy.deepcopy(source)

    for action in actions:
        target = action.get("target")
        if not isinstance(target, str) or not target:
            raise ValidationError("Overlay action.target must be a JSONPath string")

        nodes = _find_nodes(target, result, "target")
        _guard(action, [node.value for node in nodes])
        operation = _validate_action_operation(action)

        if operation == "remove":
            for node in sorted(nodes, key=_remove_sort_key, reverse=True):
                _remove_node(node)
            continue

        if operation == "copy":
            copy_expression = action[operation]
            sources = _find_nodes(copy_expression, result, "copy")
            if len(sources) != 1:
                raise ValidationError("Overlay copy must select exactly one source node")
            update = sources[0].value
        else:
            update = action[operation]

        for node in nodes:
            merged = _merge(node.value, update)
            if node.parent is None:
                if not isinstance(merged, dict):
                    raise ValidationError(
                        "Overlay cannot replace the document root with a non-object"
                    )
                result = merged
            else:
                node.value = merged

    return result


def apply_overlay_files(source: dict[str, Any], paths: list[Path]) -> dict[str, Any]:
    result = copy.deepcopy(source)
    for path in paths:
        try:
            overlay = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError) as error:
            raise ValidationError(f"Cannot load overlay: {path}") from error
        if not isinstance(overlay, dict):
            raise ValidationError(f"Overlay is not an object: {path}")
        result = apply_overlay(result, overlay)
    return result
