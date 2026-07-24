from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..errors import SafetyError
from ..inventory import HTTP_METHODS
from ..io import canonical_json_bytes, sha256_bytes
from .contract_io import exact_keys, load_yaml_mapping, safe_identifier, safe_review_reason
from .receipt import AUTH_OPERATION_IDS

_MAX_CATALOG_BYTES = 1024 * 1024
_EFFECTS = frozenset(
    {"auth", "read", "create", "update", "delete", "action", "irreversible", "unknown"}
)
_LIVE_POLICIES = frozenset({"automatic", "lifecycle_only", "manual_only", "blocked"})
_ALLOWED_POLICIES = {
    "auth": frozenset({"automatic", "blocked"}),
    "read": frozenset({"automatic", "blocked"}),
    "create": frozenset({"lifecycle_only", "manual_only", "blocked"}),
    "update": frozenset({"lifecycle_only", "manual_only", "blocked"}),
    "delete": frozenset({"lifecycle_only", "manual_only", "blocked"}),
    "action": frozenset({"lifecycle_only", "manual_only", "blocked"}),
    "irreversible": frozenset({"manual_only", "blocked"}),
    "unknown": frozenset({"blocked"}),
}


@dataclass(frozen=True)
class OperationSafety:
    effect: str
    live_policy: str
    reason: str


@dataclass(frozen=True)
class OperationSafetyCatalog:
    version: int
    operations: Mapping[str, OperationSafety]
    sha256: str

    @classmethod
    def load(cls, path: Path) -> OperationSafetyCatalog:
        value = load_yaml_mapping(
            path,
            label="operation safety catalog",
            maximum_bytes=_MAX_CATALOG_BYTES,
        )
        return cls.from_mapping(value)

    @classmethod
    def from_mapping(cls, value: object) -> OperationSafetyCatalog:
        if not isinstance(value, Mapping):
            raise SafetyError("Operation safety catalog root must be an object")
        exact_keys(
            value,
            {"version", "operations"},
            label="Operation safety catalog root",
        )
        version = value["version"]
        if type(version) is not int or version != 1:
            raise SafetyError("Operation safety catalog version must be the integer 1")
        raw_operations = value["operations"]
        if not isinstance(raw_operations, Mapping):
            raise SafetyError("Operation safety catalog operations must be an object")

        parsed: dict[str, OperationSafety] = {}
        for raw_operation_id, raw_entry in sorted(
            raw_operations.items(), key=lambda item: str(item[0])
        ):
            operation_id = safe_identifier(raw_operation_id, label="operation ID")
            if not isinstance(raw_entry, Mapping):
                raise SafetyError(f"Operation safety entry for {operation_id!r} must be an object")
            exact_keys(
                raw_entry,
                {"effect", "live_policy", "reason"},
                label=f"Operation safety entry for {operation_id!r}",
            )
            effect = raw_entry["effect"]
            if not isinstance(effect, str) or effect not in _EFFECTS:
                raise SafetyError(f"effect for {operation_id!r} is invalid")
            live_policy = raw_entry["live_policy"]
            if not isinstance(live_policy, str) or live_policy not in _LIVE_POLICIES:
                raise SafetyError(f"live_policy for {operation_id!r} is invalid")
            reason = safe_review_reason(
                raw_entry["reason"],
                label=f"reason for {operation_id!r}",
            )

            if effect == "unknown" and live_policy != "blocked":
                raise SafetyError(
                    f"Operation {operation_id!r} with unknown effect must be blocked"
                )
            if live_policy == "automatic" and effect not in {"auth", "read"}:
                raise SafetyError(
                    "automatic live policy is permitted only for reads and authenticate"
                )
            if (
                effect == "auth"
                and live_policy == "automatic"
                and operation_id not in AUTH_OPERATION_IDS
            ):
                raise SafetyError(
                    "Only reviewed authentication operations may use automatic auth policy"
                )
            if live_policy not in _ALLOWED_POLICIES[effect]:
                raise SafetyError(
                    f"live_policy {live_policy!r} is not allowed for effect {effect!r}"
                )
            parsed[operation_id] = OperationSafety(effect, live_policy, reason)

        operations = MappingProxyType(dict(sorted(parsed.items())))
        canonical = {
            "version": version,
            "operations": {
                operation_id: {
                    "effect": entry.effect,
                    "live_policy": entry.live_policy,
                    "reason": entry.reason,
                }
                for operation_id, entry in operations.items()
            },
        }
        return cls(
            version=version,
            operations=operations,
            sha256=sha256_bytes(canonical_json_bytes(canonical)),
        )

    @property
    def automatic_read_ids(self) -> frozenset[str]:
        return frozenset(
            operation_id
            for operation_id, entry in self.operations.items()
            if entry.effect == "read" and entry.live_policy == "automatic"
        )

    def assert_matches_openapi(self, document: dict[str, Any]) -> None:
        paths = document.get("paths")
        if not isinstance(paths, Mapping):
            raise SafetyError("OpenAPI paths must be an object for operation safety review")

        operation_locations: dict[str, str] = {}
        for raw_path, raw_path_item in sorted(paths.items(), key=lambda item: str(item[0])):
            if not isinstance(raw_path, str) or not isinstance(raw_path_item, Mapping):
                raise SafetyError("OpenAPI path items must be string-keyed objects")
            if "$ref" in raw_path_item:
                raise SafetyError(
                    f"OpenAPI path item {raw_path!r} contains $ref and cannot be classified"
                )
            for raw_method, raw_operation in raw_path_item.items():
                if not isinstance(raw_method, str) or raw_method.lower() not in HTTP_METHODS:
                    continue
                location = f"{raw_method.upper()} {raw_path}"
                if not isinstance(raw_operation, Mapping):
                    raise SafetyError(f"OpenAPI operation {location} is not an object")
                raw_operation_id = raw_operation.get("operationId")
                if raw_operation_id is None:
                    raise SafetyError(f"OpenAPI operation {location} is missing operationId")
                operation_id = safe_identifier(raw_operation_id, label="OpenAPI operation ID")
                previous = operation_locations.get(operation_id)
                if previous is not None:
                    raise SafetyError(
                        f"OpenAPI contains duplicate operation ID {operation_id!r}: "
                        f"{previous} and {location}"
                    )
                operation_locations[operation_id] = location

        catalog_ids = set(self.operations)
        openapi_ids = set(operation_locations)
        if catalog_ids != openapi_ids:
            missing = ", ".join(sorted(catalog_ids - openapi_ids)) or "<none>"
            extra = ", ".join(sorted(openapi_ids - catalog_ids)) or "<none>"
            raise SafetyError(
                "OpenAPI operation IDs do not match the operation safety catalog; "
                f"missing from OpenAPI: {missing}; extra in OpenAPI: {extra}"
            )
