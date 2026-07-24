"""Reviewed write-lifecycle scenario registry.

A write lifecycle is a reviewed chain of live operations that prepares,
creates, checks, and always compensates an owned entity. The registry is
declarative; execution stays in the generated adapter's validated executors.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

from ..errors import SafetyError
from .contract_io import exact_keys, load_yaml_mapping, safe_identifier, safe_review_reason

_MAX_REGISTRY_BYTES = 256 * 1024
_ROLES = frozenset({"prepare", "create", "check", "cleanup"})
_MARKER_SOURCES = frozenset({"literal", "profile_field"})
_PROFILE_MARKER_FIELDS = frozenset(
    {"organization_id", "terminal_group_id", "write_product_id"}
)
_PROFILE_REQUIREMENTS = frozenset({"terminal_group_id", "write_product_id"})
_ROLE_EFFECTS = {
    "prepare": frozenset({"read"}),
    "check": frozenset({"read"}),
    "create": frozenset({"create", "update"}),
    "cleanup": frozenset({"delete", "update", "action"}),
}
_ROLE_OPERATION_KINDS = {
    "prepare": "read",
    "check": "read",
    "create": "compensating",
    "cleanup": "cleanup",
}


@dataclass(frozen=True)
class OwnershipMarker:
    source: str
    field: str
    value: str | None


@dataclass(frozen=True)
class LifecycleStep:
    role: str
    operation: str
    compensates: str | None


@dataclass(frozen=True)
class WriteLifecycle:
    scenario_id: str
    enabled: bool
    disabled_reason: str | None
    requires_profile_fields: tuple[str, ...]
    ownership_marker: OwnershipMarker
    steps: tuple[LifecycleStep, ...]

    @property
    def operation_ids(self) -> frozenset[str]:
        return frozenset(step.operation for step in self.steps)

    @property
    def write_operation_ids(self) -> frozenset[str]:
        return frozenset(
            step.operation
            for step in self.steps
            if step.role in {"create", "cleanup"}
        )


@dataclass(frozen=True)
class WriteLifecycleRegistry:
    version: int
    scenarios: Mapping[str, WriteLifecycle]

    @classmethod
    def load(cls, path: Path) -> WriteLifecycleRegistry:
        value = load_yaml_mapping(
            path,
            label="write lifecycle registry",
            maximum_bytes=_MAX_REGISTRY_BYTES,
        )
        return cls.from_mapping(value)

    @classmethod
    def from_mapping(cls, value: object) -> WriteLifecycleRegistry:
        if not isinstance(value, Mapping):
            raise SafetyError("Write lifecycle registry root must be an object")
        exact_keys(value, {"version", "scenarios"}, label="Write lifecycle registry root")
        version = value["version"]
        if type(version) is not int or version != 1:
            raise SafetyError("Write lifecycle registry version must be the integer 1")
        raw_scenarios = value["scenarios"]
        if not isinstance(raw_scenarios, Mapping) or not raw_scenarios:
            raise SafetyError("Write lifecycle registry scenarios must be a non-empty object")

        scenarios: dict[str, WriteLifecycle] = {}
        for raw_id in sorted(raw_scenarios, key=str):
            scenario_id = safe_identifier(raw_id, label="scenario ID")
            scenarios[scenario_id] = _parse_scenario(scenario_id, raw_scenarios[raw_id])
        return cls(version=version, scenarios=MappingProxyType(scenarios))

    def enabled_operation_ids(self) -> frozenset[str]:
        result: set[str] = set()
        for scenario in self.scenarios.values():
            if scenario.enabled:
                result.update(scenario.operation_ids)
        return frozenset(result)


def _parse_scenario(scenario_id: str, raw: object) -> WriteLifecycle:
    label = f"Write lifecycle scenario {scenario_id!r}"
    if not isinstance(raw, Mapping):
        raise SafetyError(f"{label} must be an object")
    keys = set(raw)
    required = {"enabled", "ownership_marker", "requires_profile_fields", "steps"}
    if not required.issubset(keys) or not keys.issubset(required | {"disabled_reason"}):
        raise SafetyError(f"{label} has unknown or missing fields")
    enabled = raw["enabled"]
    if type(enabled) is not bool:
        raise SafetyError(f"{label} enabled must be a boolean")
    disabled_reason = raw.get("disabled_reason")
    if enabled:
        if disabled_reason is not None:
            raise SafetyError(f"{label} enabled scenario must not carry a disabled reason")
    else:
        disabled_reason = safe_review_reason(
            disabled_reason, label=f"{label} disabled_reason"
        )

    requires = raw["requires_profile_fields"]
    if not isinstance(requires, list) or any(
        type(field) is not str or field not in _PROFILE_REQUIREMENTS for field in requires
    ):
        raise SafetyError(f"{label} requires_profile_fields names are invalid")
    if len(set(requires)) != len(requires):
        raise SafetyError(f"{label} requires_profile_fields must not contain duplicates")

    marker = _parse_marker(label, raw["ownership_marker"])
    steps = _parse_steps(label, raw["steps"])
    return WriteLifecycle(
        scenario_id=scenario_id,
        enabled=enabled,
        disabled_reason=disabled_reason,
        requires_profile_fields=tuple(requires),
        ownership_marker=marker,
        steps=steps,
    )


def _parse_marker(label: str, raw: object) -> OwnershipMarker:
    if not isinstance(raw, Mapping):
        raise SafetyError(f"{label} ownership_marker must be an object")
    marker_keys = set(raw)
    if not {"field", "source"}.issubset(marker_keys) or not marker_keys.issubset(
        {"field", "source", "value"}
    ):
        raise SafetyError(f"{label} ownership_marker has unknown or missing fields")
    source = raw["source"]
    if type(source) is not str or source not in _MARKER_SOURCES:
        raise SafetyError(f"{label} ownership_marker source is invalid")
    field = safe_identifier(raw["field"], label=f"{label} ownership_marker field")
    value = raw.get("value")
    if source == "literal":
        if not isinstance(value, str) or not value or len(value) > 64:
            raise SafetyError(f"{label} ownership_marker value must be a short string")
        return OwnershipMarker(source=source, field=field, value=value)
    if value is not None:
        raise SafetyError(f"{label} profile-field marker must not carry a literal value")
    if field not in _PROFILE_MARKER_FIELDS:
        raise SafetyError(f"{label} ownership_marker field is not a known profile field")
    return OwnershipMarker(source=source, field=field, value=None)


def _parse_steps(label: str, raw: object) -> tuple[LifecycleStep, ...]:
    if not isinstance(raw, list) or not raw:
        raise SafetyError(f"{label} steps must be a non-empty array")
    steps: list[LifecycleStep] = []
    for index, raw_step in enumerate(raw):
        step_label = f"{label} step {index}"
        if not isinstance(raw_step, Mapping):
            raise SafetyError(f"{step_label} must be an object")
        step_keys = set(raw_step)
        if not {"operation", "role"}.issubset(step_keys) or not step_keys.issubset(
            {"compensates", "operation", "role"}
        ):
            raise SafetyError(f"{step_label} has unknown or missing fields")
        role = raw_step["role"]
        if type(role) is not str or role not in _ROLES:
            raise SafetyError(f"{step_label} role is invalid")
        operation = safe_identifier(raw_step["operation"], label=f"{step_label} operation")
        compensates = raw_step.get("compensates")
        if compensates is not None:
            compensates = safe_identifier(compensates, label=f"{step_label} compensates")
        if role == "cleanup" and compensates is None:
            raise SafetyError(f"{step_label} cleanup must name its compensated operation")
        if role != "cleanup" and compensates is not None:
            raise SafetyError(f"{step_label} only cleanup steps may compensate")
        steps.append(LifecycleStep(role=role, operation=operation, compensates=compensates))

    operations = [step.operation for step in steps]
    if len(set(operations)) != len(operations):
        raise SafetyError(f"{label} steps must not repeat an operation")
    create_ids = {step.operation for step in steps if step.role == "create"}
    if not create_ids:
        raise SafetyError(f"{label} requires at least one create step")
    compensated = {step.compensates for step in steps if step.role == "cleanup"}
    if compensated != create_ids:
        raise SafetyError(f"{label} every create step requires exactly one cleanup step")
    earlier: set[str] = set()
    for step in steps:
        if step.compensates is not None and step.compensates not in earlier:
            raise SafetyError(f"{label} cleanup must compensate an earlier create step")
        earlier.add(step.operation)
    if not any(step.role == "prepare" for step in steps):
        raise SafetyError(f"{label} requires a read prepare step")
    return tuple(steps)


def assert_lifecycle_consistency(
    registry: WriteLifecycleRegistry,
    *,
    operation_ids: frozenset[str],
    safety_effects: Mapping[str, str],
    live_operation_kinds: Mapping[str, str],
    rate_operation_ids: frozenset[str],
) -> None:
    """Cross-check the registry against the reviewed live contracts."""

    if type(registry) is not WriteLifecycleRegistry:
        raise SafetyError("Write lifecycle consistency requires a parsed registry")
    for scenario in registry.scenarios.values():
        for step in scenario.steps:
            operation = step.operation
            if operation not in operation_ids:
                raise SafetyError(
                    f"Write lifecycle operation {operation!r} "
                    "is missing from the operation ID registry"
                )
            effect = safety_effects.get(operation)
            if effect is None:
                raise SafetyError(
                    f"Write lifecycle operation {operation!r} is missing from the safety catalog"
                )
            if effect not in _ROLE_EFFECTS[step.role]:
                raise SafetyError(
                    f"Write lifecycle operation {operation!r} effect {effect!r} "
                    f"does not fit role {step.role!r}"
                )
            kind = live_operation_kinds.get(operation)
            if kind != _ROLE_OPERATION_KINDS[step.role]:
                raise SafetyError(
                    f"Write lifecycle operation {operation!r} must be allowlisted "
                    f"as kind {_ROLE_OPERATION_KINDS[step.role]!r}"
                )
            if not scenario.enabled:
                continue
            if operation not in rate_operation_ids:
                raise SafetyError(
                    f"Write lifecycle operation {operation!r} is missing from the rate catalog"
                )
