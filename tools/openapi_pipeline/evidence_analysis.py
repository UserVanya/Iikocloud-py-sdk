from __future__ import annotations

import inspect
import math
from collections.abc import Callable, Mapping
from contextlib import suppress
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Literal, cast

from .errors import SafetyError
from .evidence_promotion import (
    EvidencePair,
    FrozenJson,
    revalidate_evidence_pair_contract,
)
from .evidence_validation import MenuEvidenceValidator
from .io import canonical_json_bytes, sha256_bytes

_VERSIONS = (2, 3, 4)
_BRANCHES = ("ExternalMenuItem3", "ExternalMenuComboItem")
_ITEM3 = "ExternalMenuItem3"
_COMBO = "ExternalMenuComboItem"
_LITERALS = frozenset({"DISH", "COMBO"})
_EXACT_FIVE = (
    "allergenGroupIds",
    "itemSizes",
    "modifierSchemaId",
    "orderItemType",
    "splittable",
)
_CONSTRAINT_KEYS = frozenset({"$ref", "enum", "format"})

RequiredAction = Literal["retain-required", "remove-required"]
ReasonCode = Literal[
    "complete-valid-evidence",
    "missing-observation",
    "null-observation",
    "empty-observation",
    "inconsistent-shape",
    "insufficient-constrained-observations",
]


@dataclass(frozen=True)
class EvidenceProvenance:
    request_sha256: str
    response_sha256: str


@dataclass(frozen=True)
class ComboFieldDecision:
    field_name: str
    required_action: RequiredAction
    reason_code: ReasonCode
    observation_count: int
    property_schema: Mapping[str, FrozenJson] | None


@dataclass(frozen=True)
class MenuEvidenceAnalysis:
    provenance: Mapping[int, EvidenceProvenance]
    branch_to_literal: Mapping[str, str]
    literal_to_branch: Mapping[str, str]
    unambiguous_counts: Mapping[str, int]
    ambiguous_count: int
    total_item_count: int
    combo_observation_count: int
    combo_fields: Mapping[str, ComboFieldDecision]


@dataclass(frozen=True)
class _ItemObservation:
    item: Mapping[str, FrozenJson]
    literal: str
    branches: tuple[str, ...]


def analyze_menu_evidence(
    pairs: Mapping[int, EvidencePair],
    effective_schema: dict[str, Any],
) -> MenuEvidenceAnalysis:
    """Analyze three reviewed capture pairs without producing promotion artifacts."""

    validator = MenuEvidenceValidator(effective_schema)
    ordered_pairs, provenance = _validate_pairs(pairs, validator)
    observations = _inspect_v4_items(ordered_pairs[4], validator)
    branch_to_literal, literal_to_branch, counts = _derive_discriminator_mapping(observations)

    combo_items: list[Mapping[str, FrozenJson]] = []
    ambiguous_count = 0
    for observation in observations:
        if len(observation.branches) == 1:
            resolved = observation.branches[0]
        else:
            ambiguous_count += 1
            resolved = literal_to_branch.get(observation.literal, "")
            if resolved not in observation.branches:
                raise SafetyError(
                    "Ambiguous Evidence V4 item is inconsistent with the derived mapping"
                )
        if resolved == _COMBO:
            combo_items.append(observation.item)

    decisions = {
        field: _analyze_combo_field(field, combo_items, validator) for field in _EXACT_FIVE
    }
    return MenuEvidenceAnalysis(
        provenance=MappingProxyType(provenance),
        branch_to_literal=MappingProxyType(dict(sorted(branch_to_literal.items()))),
        literal_to_branch=MappingProxyType(dict(sorted(literal_to_branch.items()))),
        unambiguous_counts=MappingProxyType(dict(sorted(counts.items()))),
        ambiguous_count=ambiguous_count,
        total_item_count=len(observations),
        combo_observation_count=len(combo_items),
        combo_fields=MappingProxyType(decisions),
    )


def _validate_pairs(
    pairs: Mapping[int, EvidencePair],
    validator: MenuEvidenceValidator,
) -> tuple[dict[int, EvidencePair], dict[int, EvidenceProvenance]]:
    if not isinstance(pairs, Mapping):
        raise SafetyError("Evidence analysis requires a mapping of capture pairs")
    try:
        keys = tuple(pairs)
    except Exception:
        raise SafetyError("Evidence analysis capture pair mapping is invalid") from None
    if (
        len(keys) != len(_VERSIONS)
        or any(type(version) is not int for version in keys)
        or set(keys) != set(_VERSIONS)
    ):
        raise SafetyError("Evidence analysis requires exactly versions 2, 3, and 4")

    ordered: dict[int, EvidencePair] = {}
    provenance: dict[int, EvidenceProvenance] = {}
    for version in _VERSIONS:
        try:
            pair = pairs[version]
        except Exception:
            raise SafetyError(
                "Evidence analysis capture pair mapping changed during read"
            ) from None
        if type(pair) is not EvidencePair or pair.version != version:
            raise SafetyError("Evidence analysis capture pair version is inconsistent")
        request_hash = _canonical_mapping_hash(pair.request)
        response_hash = _canonical_mapping_hash(pair.response)
        if request_hash != pair.request_sha256 or response_hash != pair.response_sha256:
            raise SafetyError("Evidence analysis capture pair provenance hash is invalid")
        try:
            contract_version = revalidate_evidence_pair_contract(pair.request, pair.response)
        except SafetyError:
            raise
        except Exception:
            raise SafetyError("Evidence analysis reader contract validation failed") from None
        if contract_version != version:
            raise SafetyError("Evidence analysis reader contract version is inconsistent")
        try:
            validate = cast(
                Callable[[int, Mapping[str, Any], Mapping[str, Any]], object],
                validator.validate,
            )
            result = validate(version, pair.request, pair.response)
        except SafetyError:
            raise
        except Exception:
            raise SafetyError("Evidence analysis schema validation failed") from None
        _require_synchronous_none(result)
        ordered[version] = pair
        provenance[version] = EvidenceProvenance(request_hash, response_hash)
    return ordered, provenance


def _inspect_v4_items(
    pair: EvidencePair,
    validator: MenuEvidenceValidator,
) -> tuple[_ItemObservation, ...]:
    body = pair.response.get("body")
    groups = body.get("itemGroups") if isinstance(body, Mapping) else None
    if type(groups) is not tuple:
        raise SafetyError("Evidence V4 itemGroups shape is invalid")
    collected: list[_ItemObservation] = []
    for group in groups:
        items = group.get("items") if isinstance(group, Mapping) else None
        if type(items) is not tuple:
            raise SafetyError("Evidence V4 items shape is invalid")
        for item in items:
            if not isinstance(item, Mapping):
                raise SafetyError("Evidence V4 item shape is invalid")
            literal = item.get("type")
            if type(literal) is not str or literal not in _LITERALS:
                raise SafetyError("Evidence V4 item discriminator literal is unsafe")
            try:
                branches = validator.match_v4_item_branches(cast(Mapping[str, Any], item))
            except SafetyError:
                raise
            except Exception:
                raise SafetyError("Evidence V4 structural branch matching failed") from None
            if (
                not branches
                or set(branches) - set(_BRANCHES)
                or len(set(branches)) != len(branches)
            ):
                raise SafetyError("Evidence V4 structural branch result is unsafe")
            collected.append(_ItemObservation(item, literal, branches))
    return tuple(collected)


def _derive_discriminator_mapping(
    observations: tuple[_ItemObservation, ...],
) -> tuple[dict[str, str], dict[str, str], dict[str, int]]:
    literals_by_branch: dict[str, set[str]] = {branch: set() for branch in _BRANCHES}
    counts = {branch: 0 for branch in _BRANCHES}
    for observation in observations:
        if len(observation.branches) != 1:
            continue
        branch = observation.branches[0]
        if branch not in literals_by_branch:
            raise SafetyError("Evidence V4 structural branch result is unsafe")
        literals_by_branch[branch].add(observation.literal)
        counts[branch] += 1
    if any(counts[branch] < 1 for branch in _BRANCHES):
        raise SafetyError("Evidence requires unambiguous observations of both V4 item branches")
    if any(len(literals_by_branch[branch]) != 1 for branch in _BRANCHES):
        raise SafetyError("Evidence V4 branch literals do not form a consistent mapping")
    branch_to_literal = {branch: next(iter(literals_by_branch[branch])) for branch in _BRANCHES}
    if set(branch_to_literal.values()) != _LITERALS:
        raise SafetyError("Evidence V4 branch literals must form a distinct complete mapping")
    literal_to_branch = {literal: branch for branch, literal in branch_to_literal.items()}
    if len(literal_to_branch) != len(_BRANCHES):
        raise SafetyError("Evidence V4 branch literals must be distinct")
    for observation in observations:
        if len(observation.branches) == 1 and (
            literal_to_branch.get(observation.literal) != observation.branches[0]
        ):
            raise SafetyError("Evidence V4 item literal conflicts with its structural branch")
        if len(observation.branches) > 1 and observation.literal not in literal_to_branch:
            raise SafetyError("Ambiguous Evidence V4 item literal cannot be resolved safely")
    return branch_to_literal, literal_to_branch, counts


def _analyze_combo_field(
    field: str,
    combo_items: list[Mapping[str, FrozenJson]],
    validator: MenuEvidenceValidator,
) -> ComboFieldDecision:
    values = [item[field] for item in combo_items if field in item]
    count = len(values)
    if count != len(combo_items):
        return _remove_decision(field, "missing-observation", count)
    if any(value is None for value in values):
        return _remove_decision(field, "null-observation", count)
    if any(_is_empty(value) for value in values):
        return _remove_decision(field, "empty-observation", count)

    schemas: list[dict[str, Any]] = []
    for value in values:
        try:
            schemas.append(validator.validate_v4_item3_property(field, value))
        except SafetyError:
            raise SafetyError(
                "Evidence combo property does not match its reviewed sibling schema"
            ) from None
        except Exception:
            raise SafetyError("Evidence combo sibling schema validation failed") from None
    if not schemas:
        return _remove_decision(field, "missing-observation", count)
    encoded_schemas = {canonical_json_bytes(schema) for schema in schemas}
    if len(encoded_schemas) != 1:
        raise SafetyError("Evidence combo sibling property schema changed during analysis")
    signatures = {_shape_signature(value) for value in values}
    if len(signatures) != 1:
        return _remove_decision(field, "inconsistent-shape", count)
    schema = schemas[0]
    if count < 2 and _has_inference_constraint(schema):
        return _remove_decision(field, "insufficient-constrained-observations", count)
    return ComboFieldDecision(
        field_name=field,
        required_action="retain-required",
        reason_code="complete-valid-evidence",
        observation_count=count,
        property_schema=_freeze_mapping(schema),
    )


def _remove_decision(
    field: str,
    reason: ReasonCode,
    count: int,
) -> ComboFieldDecision:
    return ComboFieldDecision(
        field_name=field,
        required_action="remove-required",
        reason_code=reason,
        observation_count=count,
        property_schema=None,
    )


def _is_empty(value: object) -> bool:
    return (type(value) is str and not value) or (
        isinstance(value, (tuple, Mapping)) and len(value) == 0
    )


def _shape_signature(value: FrozenJson) -> tuple[Any, ...]:
    if isinstance(value, Mapping):
        return (
            "object",
            tuple((key, _shape_signature(child)) for key, child in sorted(value.items())),
        )
    if type(value) is tuple:
        return (
            "array",
            tuple(sorted({_shape_signature(child) for child in value}, key=repr)),
        )
    if value is None:
        return ("null",)
    return (type(value).__name__,)


def _has_inference_constraint(schema: object) -> bool:
    if isinstance(schema, Mapping):
        if set(schema).intersection(_CONSTRAINT_KEYS):
            return True
        return any(_has_inference_constraint(value) for value in schema.values())
    if isinstance(schema, (list, tuple)):
        return any(_has_inference_constraint(value) for value in schema)
    return False


def _canonical_mapping_hash(value: Mapping[str, FrozenJson]) -> str:
    try:
        return sha256_bytes(canonical_json_bytes(_thaw_json(value)))
    except (TypeError, ValueError, RecursionError):
        raise SafetyError("Evidence analysis cannot recompute capture provenance") from None


def _thaw_json(value: object, *, depth: int = 0) -> Any:
    if depth > 256:
        raise SafetyError("Evidence analysis JSON exceeds its safe depth")
    if isinstance(value, Mapping):
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence analysis JSON object key is invalid")
        return {key: _thaw_json(child, depth=depth + 1) for key, child in value.items()}
    if type(value) is tuple:
        return [_thaw_json(child, depth=depth + 1) for child in value]
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence analysis value is not strict immutable JSON")


def _freeze_json(value: object) -> FrozenJson:
    if isinstance(value, Mapping):
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence analysis schema key is invalid")
        return MappingProxyType({key: _freeze_json(child) for key, child in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze_json(child) for child in value)
    if value is None:
        return value
    if type(value) is bool:
        return value
    if type(value) is int:
        return value
    if type(value) is str:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence analysis schema is not strict JSON")


def _freeze_mapping(value: Mapping[str, Any]) -> Mapping[str, FrozenJson]:
    frozen = _freeze_json(value)
    if not isinstance(frozen, Mapping):
        raise SafetyError("Evidence analysis schema is not an object")
    return frozen


def _require_synchronous_none(result: object) -> None:
    if inspect.isawaitable(result):
        close = getattr(result, "close", None)
        if callable(close):
            with suppress(Exception):
                close()
        raise SafetyError("Evidence analysis validator must be synchronous")
    if result is not None:
        raise SafetyError("Evidence analysis validator must return exactly None")
