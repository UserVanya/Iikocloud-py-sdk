"""Deterministic dependency planning for guarded live reads."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass, field
from types import MappingProxyType

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.live.read_case import READ_SEED_KEYS, ReadCase


@dataclass(frozen=True, slots=True)
class ReadPlan:
    cases: tuple[ReadCase, ...]
    ordered_operation_ids: tuple[str, ...]
    registry_sha256: str
    _case_lookup: Mapping[str, ReadCase] = field(
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        lookup = {case.operation_id: case for case in self.cases}
        object.__setattr__(self, "_case_lookup", MappingProxyType(lookup))

    @classmethod
    def build(cls, cases: Iterable[ReadCase]) -> ReadPlan:
        try:
            supplied_cases = tuple(cases)
        except TypeError:
            raise SafetyError("read cases must be iterable") from None
        if any(type(case) is not ReadCase for case in supplied_cases):
            raise SafetyError("read plan contains an invalid case")

        case_lookup: dict[str, ReadCase] = {}
        for case in supplied_cases:
            if case.operation_id in case_lookup:
                raise SafetyError("duplicate read operation id")
            case_lookup[case.operation_id] = case

        _validate_declared_dependencies(case_lookup)
        ordered_operation_ids = _layered_topological_order(case_lookup)
        _validate_context_providers(case_lookup, ordered_operation_ids)
        ordered_cases = tuple(
            case_lookup[operation_id] for operation_id in ordered_operation_ids
        )
        return cls._from_ordered_cases(ordered_cases)

    @classmethod
    def _from_ordered_cases(cls, cases: tuple[ReadCase, ...]) -> ReadPlan:
        ordered_operation_ids = tuple(case.operation_id for case in cases)
        return cls(
            cases=cases,
            ordered_operation_ids=ordered_operation_ids,
            registry_sha256=_registry_sha256(cases),
        )

    def case_for(self, operation_id: str) -> ReadCase:
        if type(operation_id) is not str:
            raise SafetyError("read operation is unknown")
        try:
            return self._case_lookup[operation_id]
        except KeyError:
            raise SafetyError("read operation is unknown") from None

    def dependency_closure(self, operation_id: str) -> ReadPlan:
        selected = self.case_for(operation_id)
        required_operation_ids = {selected.operation_id}
        pending = list(selected.depends_on)
        while pending:
            dependency_id = pending.pop()
            if dependency_id in required_operation_ids:
                continue
            dependency = self.case_for(dependency_id)
            required_operation_ids.add(dependency_id)
            pending.extend(dependency.depends_on)

        subset = tuple(
            case
            for case in self.cases
            if case.operation_id in required_operation_ids
        )
        return self._from_ordered_cases(subset)


def _validate_declared_dependencies(case_lookup: Mapping[str, ReadCase]) -> None:
    for case in case_lookup.values():
        for dependency_id in case.depends_on:
            if dependency_id == case.operation_id:
                raise SafetyError("read operation has a self dependency")
            if dependency_id not in case_lookup:
                raise SafetyError("read dependency is missing")


def _layered_topological_order(
    case_lookup: Mapping[str, ReadCase],
) -> tuple[str, ...]:
    remaining_dependencies = {
        operation_id: len(case.depends_on)
        for operation_id, case in case_lookup.items()
    }
    dependents: dict[str, list[str]] = {
        operation_id: [] for operation_id in case_lookup
    }
    for case in case_lookup.values():
        for dependency_id in case.depends_on:
            dependents[dependency_id].append(case.operation_id)

    ready = sorted(
        operation_id
        for operation_id, count in remaining_dependencies.items()
        if count == 0
    )
    ordered: list[str] = []
    while ready:
        ordered.extend(ready)
        next_ready: list[str] = []
        for operation_id in ready:
            for dependent_id in dependents[operation_id]:
                remaining_dependencies[dependent_id] -= 1
                if remaining_dependencies[dependent_id] == 0:
                    next_ready.append(dependent_id)
        ready = sorted(next_ready)

    if len(ordered) != len(case_lookup):
        raise SafetyError("read dependency cycle detected")
    return tuple(ordered)


def _validate_context_providers(
    case_lookup: Mapping[str, ReadCase],
    ordered_operation_ids: tuple[str, ...],
) -> None:
    provider_by_key: dict[str, str] = {}
    for case in case_lookup.values():
        for key in case.provides:
            if key in provider_by_key:
                raise SafetyError("duplicate context provider")
            provider_by_key[key] = case.operation_id

    transitive_dependencies: dict[str, frozenset[str]] = {}
    for operation_id in ordered_operation_ids:
        case = case_lookup[operation_id]
        dependencies: set[str] = set()
        for dependency_id in case.depends_on:
            dependencies.add(dependency_id)
            dependencies.update(transitive_dependencies[dependency_id])
        frozen_dependencies = frozenset(dependencies)
        transitive_dependencies[operation_id] = frozen_dependencies

        for required_key in case.requires:
            if required_key in READ_SEED_KEYS:
                continue
            provider_id = provider_by_key.get(required_key)
            if provider_id is None or provider_id not in frozen_dependencies:
                raise SafetyError("required context key has no dependency provider")


def _registry_sha256(cases: tuple[ReadCase, ...]) -> str:
    descriptors: list[dict[str, object]] = []
    for case in sorted(cases, key=lambda item: item.operation_id):
        descriptors.append(
            {
                "operation_id": case.operation_id,
                "revision": case.revision,
                "depends_on": list(case.depends_on),
                "requires": list(case.requires),
                "provides": list(case.provides),
                "allowed_no_target_codes": sorted(
                    code.value for code in case.allowed_no_target_codes
                ),
                "binding": asdict(case.binding),
            }
        )
    descriptor: dict[str, object] = {
        "version": 1,
        "cases": descriptors,
    }
    return sha256_bytes(canonical_json_bytes(descriptor))


__all__ = ["ReadPlan"]
