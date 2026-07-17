from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .io import canonical_json_bytes, sha256_bytes

HTTP_METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}


def _resolve_local_reference(document: dict[str, Any], reference: str) -> Any:
    if not reference.startswith("#/"):
        return None
    current: Any = document
    for encoded in reference[2:].split("/"):
        part = encoded.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _operation_contract(
    document: dict[str, Any], path_item: dict[str, Any], operation: Any
) -> dict[str, Any]:
    path_context = {
        key: value for key, value in path_item.items() if key.lower() not in HTTP_METHODS
    }
    root_context = {key: document[key] for key in ("servers", "security") if key in document}
    effective_security = (
        operation.get("security", document.get("security", []))
        if isinstance(operation, dict)
        else document.get("security", [])
    )
    selected_security_names = sorted(
        {
            name
            for requirement in effective_security
            if isinstance(requirement, dict)
            for name in requirement
            if isinstance(name, str)
        }
        if isinstance(effective_security, list)
        else set()
    )
    all_security_schemes = document.get("components", {}).get("securitySchemes", {})
    if not isinstance(all_security_schemes, dict):
        all_security_schemes = {}
    selected_security = {
        name: all_security_schemes.get(name, {"$unresolved": True})
        for name in selected_security_names
    }

    references: dict[str, Any] = {}

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            reference = value.get("$ref")
            if (
                isinstance(reference, str)
                and reference.startswith("#/")
                and reference not in references
            ):
                resolved = _resolve_local_reference(document, reference)
                references[reference] = {"$unresolved": True} if resolved is None else resolved
                if resolved is not None:
                    collect(resolved)
            for key in sorted(value):
                collect(value[key])
        elif isinstance(value, list):
            for item in value:
                collect(item)

    for root in (operation, path_context, root_context, selected_security):
        collect(root)
    return {
        "operation": operation,
        "path": path_context,
        "root": root_context,
        "securitySchemes": selected_security,
        "references": dict(sorted(references.items())),
    }


@dataclass(frozen=True)
class Inventory:
    openapi: str
    paths: tuple[str, ...]
    operations: tuple[str, ...]
    schemas: tuple[str, ...]
    operation_hashes: tuple[tuple[str, str], ...]
    schema_hashes: tuple[tuple[str, str], ...]

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["operation_hashes"] = dict(self.operation_hashes)
        value["schema_hashes"] = dict(self.schema_hashes)
        return value


@dataclass(frozen=True)
class InventoryDiff:
    added_paths: tuple[str, ...]
    removed_paths: tuple[str, ...]
    added_operations: tuple[str, ...]
    removed_operations: tuple[str, ...]
    changed_operations: tuple[str, ...]
    added_schemas: tuple[str, ...]
    removed_schemas: tuple[str, ...]
    changed_schemas: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def collect_inventory(document: dict[str, Any]) -> Inventory:
    paths = document.get("paths", {})
    operation_bodies = {
        f"{method.upper()} {path}": _operation_contract(document, path_item, body)
        for path, path_item in paths.items()
        for method, body in path_item.items()
        if method.lower() in HTTP_METHODS
    }
    operations = tuple(sorted(operation_bodies))
    schemas = document.get("components", {}).get("schemas", {})
    return Inventory(
        openapi=str(document.get("openapi", "")),
        paths=tuple(sorted(paths)),
        operations=operations,
        schemas=tuple(sorted(schemas)),
        operation_hashes=tuple(
            (name, sha256_bytes(canonical_json_bytes(operation_bodies[name])))
            for name in operations
        ),
        schema_hashes=tuple(
            (name, sha256_bytes(canonical_json_bytes(schemas[name]))) for name in sorted(schemas)
        ),
    )


def diff_inventory(before: Inventory, after: Inventory) -> InventoryDiff:
    def delta(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(sorted(set(right) - set(left)))

    def changed(
        left: tuple[tuple[str, str], ...], right: tuple[tuple[str, str], ...]
    ) -> tuple[str, ...]:
        before_hashes = dict(left)
        after_hashes = dict(right)
        return tuple(
            name
            for name in sorted(before_hashes.keys() & after_hashes.keys())
            if before_hashes[name] != after_hashes[name]
        )

    return InventoryDiff(
        added_paths=delta(before.paths, after.paths),
        removed_paths=delta(after.paths, before.paths),
        added_operations=delta(before.operations, after.operations),
        removed_operations=delta(after.operations, before.operations),
        changed_operations=changed(before.operation_hashes, after.operation_hashes),
        added_schemas=delta(before.schemas, after.schemas),
        removed_schemas=delta(after.schemas, before.schemas),
        changed_schemas=changed(before.schema_hashes, after.schema_hashes),
    )
