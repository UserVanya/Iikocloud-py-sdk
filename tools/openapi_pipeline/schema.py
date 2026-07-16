from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any

SchemaPath = tuple[str | int, ...]
SchemaLocation = tuple[SchemaPath, dict[str, Any]]
ReferenceLocation = tuple[SchemaPath, Any]
ReferenceWalker = Callable[
    [Any, SchemaPath, frozenset[int]], Iterator[ReferenceLocation]
]

_DATA_FIELDS = {"default", "enum", "example", "examples", "value"}
_SCHEMA_ARRAY_FIELDS = ("allOf", "anyOf", "oneOf")
_SCHEMA_OBJECT_FIELDS = ("additionalProperties", "items", "not")
_COMPONENT_OBJECT_MAP_FIELDS = {
    "callbacks",
    "headers",
    "parameters",
    "pathItems",
    "requestBodies",
    "responses",
    "securitySchemes",
}
_OPENAPI_OBJECT_MAP_FIELDS = {
    "callbacks",
    "content",
    "encoding",
    "headers",
    "paths",
    "responses",
    "webhooks",
}


def _sort_key(value: Any) -> tuple[str, str]:
    return type(value).__name__, repr(value)


def iter_schema_objects(document: dict[str, Any]) -> Iterator[SchemaLocation]:
    """Yield only OpenAPI Schema Objects, in deterministic document order."""

    def walk_schema(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[SchemaLocation]:
        if not isinstance(value, dict):
            return
        identity = id(value)
        if identity in ancestors:
            return
        child_ancestors = ancestors | {identity}

        yield path, value

        properties = value.get("properties")
        if isinstance(properties, dict):
            for name in sorted(properties, key=_sort_key):
                yield from walk_schema(
                    properties[name], (*path, "properties", name), child_ancestors
                )

        for field in _SCHEMA_OBJECT_FIELDS:
            child = value.get(field)
            if isinstance(child, dict):
                yield from walk_schema(child, (*path, field), child_ancestors)

        for field in _SCHEMA_ARRAY_FIELDS:
            branches = value.get(field)
            if not isinstance(branches, list):
                continue
            for index, branch in enumerate(branches):
                if isinstance(branch, dict):
                    yield from walk_schema(
                        branch, (*path, field, index), child_ancestors
                    )

    def walk_openapi(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[SchemaLocation]:
        if isinstance(value, dict):
            identity = id(value)
            if identity in ancestors:
                return
            child_ancestors = ancestors | {identity}

            for key in sorted(value, key=_sort_key):
                child = value[key]
                child_path = (*path, key)
                if path == ("components",) and key == "schemas":
                    if isinstance(child, dict):
                        for name in sorted(child, key=_sort_key):
                            yield from walk_schema(
                                child[name], (*child_path, name), child_ancestors
                            )
                    continue
                if key == "schema":
                    yield from walk_schema(child, child_path, child_ancestors)
                    continue
                if isinstance(key, str) and (
                    key in _DATA_FIELDS or key.startswith("x-")
                ):
                    continue
                yield from walk_openapi(child, child_path, child_ancestors)
        elif isinstance(value, list):
            identity = id(value)
            if identity in ancestors:
                return
            child_ancestors = ancestors | {identity}
            for index, child in enumerate(value):
                yield from walk_openapi(child, (*path, index), child_ancestors)

    yield from walk_openapi(document, (), frozenset())


def iter_structural_references(
    document: dict[str, Any],
) -> Iterator[ReferenceLocation]:
    """Yield `$ref` values only where OpenAPI permits structural references."""

    def own_reference(value: dict[Any, Any], path: SchemaPath) -> Iterator[ReferenceLocation]:
        if "$ref" in value:
            yield path, value["$ref"]

    def walk_schema(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[ReferenceLocation]:
        if not isinstance(value, dict):
            return
        identity = id(value)
        if identity in ancestors:
            return
        child_ancestors = ancestors | {identity}

        yield from own_reference(value, path)

        properties = value.get("properties")
        if isinstance(properties, dict):
            for name in sorted(properties, key=_sort_key):
                yield from walk_schema(
                    properties[name], (*path, "properties", name), child_ancestors
                )

        for field in _SCHEMA_OBJECT_FIELDS:
            child = value.get(field)
            if isinstance(child, dict):
                yield from walk_schema(child, (*path, field), child_ancestors)

        for field in _SCHEMA_ARRAY_FIELDS:
            branches = value.get(field)
            if not isinstance(branches, list):
                continue
            for index, branch in enumerate(branches):
                if isinstance(branch, dict):
                    yield from walk_schema(
                        branch, (*path, field, index), child_ancestors
                    )

    def walk_example(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[ReferenceLocation]:
        if not isinstance(value, dict) or id(value) in ancestors:
            return
        yield from own_reference(value, path)

    def walk_link(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[ReferenceLocation]:
        if not isinstance(value, dict) or id(value) in ancestors:
            return
        yield from own_reference(value, path)

    def walk_map(
        value: Any,
        path: SchemaPath,
        ancestors: frozenset[int],
        walker: ReferenceWalker,
    ) -> Iterator[ReferenceLocation]:
        if not isinstance(value, dict):
            return
        for name in sorted(value, key=_sort_key):
            yield from walker(value[name], (*path, name), ancestors)

    def walk_openapi(
        value: Any, path: SchemaPath, ancestors: frozenset[int]
    ) -> Iterator[ReferenceLocation]:
        if isinstance(value, dict):
            identity = id(value)
            if identity in ancestors:
                return
            child_ancestors = ancestors | {identity}
            yield from own_reference(value, path)

            for key in sorted(value, key=_sort_key):
                if key == "$ref":
                    continue
                child = value[key]
                child_path = (*path, key)
                if path == ("components",) and key == "schemas":
                    yield from walk_map(child, child_path, child_ancestors, walk_schema)
                    continue
                if path == ("components",) and key in _COMPONENT_OBJECT_MAP_FIELDS:
                    yield from walk_map(
                        child, child_path, child_ancestors, walk_openapi
                    )
                    continue
                if key == "schema":
                    yield from walk_schema(child, child_path, child_ancestors)
                    continue
                if key == "examples":
                    yield from walk_map(child, child_path, child_ancestors, walk_example)
                    continue
                if key == "links":
                    yield from walk_map(child, child_path, child_ancestors, walk_link)
                    continue
                if key in _OPENAPI_OBJECT_MAP_FIELDS:
                    yield from walk_map(
                        child, child_path, child_ancestors, walk_openapi
                    )
                    continue
                if isinstance(key, str) and (
                    key in {"default", "enum", "example", "scopes", "security", "value"}
                    or key.startswith("x-")
                ):
                    continue
                yield from walk_openapi(child, child_path, child_ancestors)
        elif isinstance(value, list):
            identity = id(value)
            if identity in ancestors:
                return
            child_ancestors = ancestors | {identity}
            for index, child in enumerate(value):
                yield from walk_openapi(child, (*path, index), child_ancestors)

    yield from walk_openapi(document, (), frozenset())
