from __future__ import annotations

from collections.abc import Iterator
from typing import Any

SchemaPath = tuple[str | int, ...]
SchemaLocation = tuple[SchemaPath, dict[str, Any]]

_DATA_FIELDS = {"default", "enum", "example", "examples", "value"}
_SCHEMA_ARRAY_FIELDS = ("allOf", "anyOf", "oneOf")
_SCHEMA_OBJECT_FIELDS = ("additionalProperties", "items", "not")


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
