from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import unquote

from .errors import ValidationError
from .inventory import HTTP_METHODS
from .schema import iter_schema_objects, iter_structural_references

VALID_TYPES = {"array", "boolean", "integer", "number", "object", "string"}
_ARRAY_INDEX = re.compile(r"(?:0|[1-9][0-9]*)")


@dataclass(frozen=True, order=True)
class LintIssue:
    code: str
    path: str
    message: str


def _decode_pointer_token(token: str) -> str:
    result: list[str] = []
    index = 0
    while index < len(token):
        character = token[index]
        if character != "~":
            result.append(character)
            index += 1
            continue
        if index + 1 >= len(token) or token[index + 1] not in {"0", "1"}:
            raise KeyError(token)
        result.append("~" if token[index + 1] == "0" else "/")
        index += 2
    return "".join(result)


def _resolve_ref(document: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        raise KeyError(ref)
    pointer = unquote(ref[1:])
    value: Any = document
    for raw_token in pointer[1:].split("/"):
        token = _decode_pointer_token(raw_token)
        if isinstance(value, dict):
            value = value[token]
        elif isinstance(value, list):
            if _ARRAY_INDEX.fullmatch(token) is None:
                raise KeyError(ref)
            value = value[int(token)]
        else:
            raise KeyError(ref)
    return value


def _properties(
    document: dict[str, Any], schema: dict[str, Any], seen: set[str]
) -> set[str]:
    raw_properties = schema.get("properties")
    result = set(raw_properties) if isinstance(raw_properties, dict) else set()
    all_of = schema.get("allOf")
    if not isinstance(all_of, list):
        return result

    for branch in all_of:
        if not isinstance(branch, dict):
            continue
        ref = branch.get("$ref")
        if isinstance(ref, str):
            if ref in seen:
                continue
            seen.add(ref)
            try:
                resolved = _resolve_ref(document, ref)
            except (IndexError, KeyError, TypeError, ValueError):
                continue
            if isinstance(resolved, dict):
                result |= _properties(document, resolved, seen)
            continue
        result |= _properties(document, branch, seen)
    return result


def _pointer(path: str, part: Any) -> str:
    token = (
        part.replace("~", "~0").replace("/", "~1")
        if isinstance(part, str)
        else repr(part)
    )
    return f"{path}/{token}"


def _sort_key(value: Any) -> tuple[str, str]:
    return type(value).__name__, repr(value)


def _path_from_parts(parts: tuple[str | int, ...]) -> str:
    path = "#"
    for part in parts:
        path = _pointer(path, part)
    return path


def lint_effective_schema(document: dict[str, Any]) -> list[LintIssue]:
    if not isinstance(document, dict):
        return [LintIssue("invalid-document", "#", "document must be an object")]

    issues: list[LintIssue] = []

    def add(code: str, path: str, message: str) -> None:
        issues.append(LintIssue(code, path, message))

    def visit(value: Any, path: str, ancestors: frozenset[int]) -> None:
        if isinstance(value, dict):
            identity = id(value)
            if identity in ancestors:
                add("cyclic-object", path, "document contains an in-memory object cycle")
                return
            child_ancestors = ancestors | {identity}

            for key in value:
                if not isinstance(key, str):
                    add("invalid-object-key", path, f"object key must be a string: {key!r}")

            for key in sorted(value, key=_sort_key):
                visit(value[key], _pointer(path, key), child_ancestors)
        elif isinstance(value, list):
            identity = id(value)
            if identity in ancestors:
                add("cyclic-object", path, "document contains an in-memory object cycle")
                return
            child_ancestors = ancestors | {identity}
            for index, child in enumerate(value):
                visit(child, _pointer(path, index), child_ancestors)

    visit(document, "#", frozenset())

    for parts, ref in iter_structural_references(document):
        path = _path_from_parts(parts)
        if not isinstance(ref, str):
            add("invalid-ref", path, "$ref must be a string")
            continue
        try:
            _resolve_ref(document, ref)
        except (IndexError, KeyError, TypeError, ValueError):
            add("broken-ref", path, ref)

    for parts, schema in iter_schema_objects(document):
        path = _path_from_parts(parts)
        if "type" in schema:
            raw_type = schema["type"]
            if not isinstance(raw_type, str) or raw_type not in VALID_TYPES:
                add("invalid-type", path, repr(raw_type))
        else:
            raw_type = None

        if "properties" in schema and not isinstance(schema["properties"], dict):
            add("invalid-properties", path, "properties must be an object")

        all_of = schema.get("allOf")
        if "allOf" in schema and not isinstance(all_of, list):
            add("invalid-allof", path, "allOf must be an array")
        elif isinstance(all_of, list):
            for index, branch in enumerate(all_of):
                if not isinstance(branch, dict):
                    add(
                        "invalid-allof-branch",
                        _pointer(_pointer(path, "allOf"), index),
                        "allOf branch must be an object",
                    )

        if "required" in schema:
            required = schema["required"]
            if not isinstance(required, list) or not all(
                isinstance(name, str) and bool(name) for name in required
            ):
                add(
                    "invalid-required",
                    path,
                    "schema required must be an array of non-empty strings",
                )
            if isinstance(required, list):
                names = {name for name in required if isinstance(name, str) and name}
                missing = sorted(names - _properties(document, schema, set()))
                if missing:
                    add("required-not-defined", path, ", ".join(missing))

        if raw_type == "array":
            if "items" not in schema:
                add("array-without-items", path, "items is required")
            elif not isinstance(schema["items"], dict):
                add("invalid-items", path, "array items must be an object")

    paths = document.get("paths")
    if not isinstance(paths, dict):
        add("invalid-paths", "#/paths", "paths must be an object")
    else:
        operation_ids: dict[str, str] = {}
        for route in sorted(paths, key=_sort_key):
            path_item = paths[route]
            route_path = _pointer("#/paths", route)
            if not isinstance(route, str):
                add("invalid-path-key", "#/paths", f"path key must be a string: {route!r}")
            if not isinstance(path_item, dict):
                add("invalid-path-item", route_path, "path item must be an object")
                continue
            for method in sorted(path_item, key=_sort_key):
                if not isinstance(method, str):
                    add(
                        "invalid-path-item-key",
                        route_path,
                        f"path item key must be a string: {method!r}",
                    )
                    continue
                if method.lower() not in HTTP_METHODS:
                    continue
                operation = path_item[method]
                location = f"{method.upper()} {route}"
                if not isinstance(operation, dict):
                    add("invalid-operation", location, "operation must be an object")
                    continue
                operation_id = operation.get("operationId")
                if not isinstance(operation_id, str) or not operation_id.strip():
                    add("missing-operation-id", location, "operationId is required")
                elif operation_id in operation_ids:
                    add(
                        "duplicate-operation-id",
                        location,
                        f"already used by {operation_ids[operation_id]}",
                    )
                else:
                    operation_ids[operation_id] = location

    servers = document.get("servers")
    if servers is None or servers == []:
        add("missing-servers", "#", "at least one server is required")
    elif not isinstance(servers, list):
        add("invalid-servers", "#/servers", "servers must be an array")
    else:
        for index, server in enumerate(servers):
            path = _pointer("#/servers", index)
            if not isinstance(server, dict):
                add("invalid-server", path, "server must be an object")
                continue
            url = server.get("url")
            if not isinstance(url, str) or not url.strip():
                add("invalid-server", path, "server url must be a non-empty string")

    return sorted(set(issues))


def ensure_valid_effective_schema(document: dict[str, Any]) -> None:
    issues = lint_effective_schema(document)
    if issues:
        summary = "; ".join(f"{issue.code}@{issue.path}: {issue.message}" for issue in issues)
        raise ValidationError(summary)
