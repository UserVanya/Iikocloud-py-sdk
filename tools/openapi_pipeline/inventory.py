from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

HTTP_METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}


@dataclass(frozen=True)
class Inventory:
    openapi: str
    paths: tuple[str, ...]
    operations: tuple[str, ...]
    schemas: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class InventoryDiff:
    added_paths: tuple[str, ...]
    removed_paths: tuple[str, ...]
    added_operations: tuple[str, ...]
    removed_operations: tuple[str, ...]
    added_schemas: tuple[str, ...]
    removed_schemas: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def collect_inventory(document: dict[str, Any]) -> Inventory:
    paths = document.get("paths", {})
    operations = tuple(
        sorted(
            f"{method.upper()} {path}"
            for path, path_item in paths.items()
            for method in path_item
            if method.lower() in HTTP_METHODS
        )
    )
    schemas = document.get("components", {}).get("schemas", {})
    return Inventory(
        openapi=str(document.get("openapi", "")),
        paths=tuple(sorted(paths)),
        operations=operations,
        schemas=tuple(sorted(schemas)),
    )


def diff_inventory(before: Inventory, after: Inventory) -> InventoryDiff:
    def delta(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(sorted(set(right) - set(left)))

    return InventoryDiff(
        added_paths=delta(before.paths, after.paths),
        removed_paths=delta(after.paths, before.paths),
        added_operations=delta(before.operations, after.operations),
        removed_operations=delta(after.operations, before.operations),
        added_schemas=delta(before.schemas, after.schemas),
        removed_schemas=delta(after.schemas, before.schemas),
    )
