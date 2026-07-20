from __future__ import annotations

import copy
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any

import yaml

from .capture import EMAIL_KEYS, PHONE_KEYS, SECRET_KEYS
from .errors import SafetyError, ValidationError
from .evidence_analysis import (
    ComboFieldDecision,
    EvidenceProvenance,
    MenuEvidenceAnalysis,
    analyze_menu_evidence,
)
from .evidence_candidate_store import _candidate_manifest_document
from .evidence_candidate_synthesis import build_and_validate_synthetic_fixtures
from .evidence_promotion import EvidencePair, FrozenJson
from .io import canonical_json_bytes, sha256_bytes
from .overlay import apply_overlay
from .validate import ensure_valid_effective_schema

EVIDENCE_OPERATION_ID = "get_external_menu_by_id"
OPERATIONS_OVERLAY_PATH = "openapi/overlays/operations.overlay.yaml"
POLYMORPHISM_OVERLAY_PATH = "openapi/overlays/polymorphism.overlay.yaml"
_FIXTURE_PATHS = {
    version: f"tests/fixtures/contracts/external-menu-v{version}.json" for version in (2, 3, 4)
}
_VERSIONS = (2, 3, 4)
EVIDENCE_CANDIDATE_PAYLOAD_PATHS = (
    OPERATIONS_OVERLAY_PATH,
    POLYMORPHISM_OVERLAY_PATH,
    *(_FIXTURE_PATHS[version] for version in _VERSIONS),
)
_ITEM3 = "ExternalMenuItem3"
_COMBO = "ExternalMenuComboItem"
_CATEGORY3 = "ExternalMenuCategory3"
_EXACT_FIVE = (
    "allergenGroupIds",
    "itemSizes",
    "modifierSchemaId",
    "orderItemType",
    "splittable",
)
_COMPONENT_PREFIX = "#/components/schemas/"
_MAX_DEPTH = 128
_REDACTION = re.compile(r"<redacted:[^>]*>", re.IGNORECASE)
_JWT = re.compile(
    r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\."
    r"[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])"
)
_BEARER = re.compile(r"\bbearer\s+\S+", re.IGNORECASE)
_EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?!\w)")
_PHONE = re.compile(r"(?<!\w)\+?\d(?:[ ().-]*\d){9,14}(?!\w)")
_UUID_ANY = re.compile(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}"
)


@dataclass(frozen=True)
class EvidenceCandidateBundle:
    """A deeply immutable, deterministic set of five in-memory promotion candidates."""

    operation_id: str
    effective_schema_sha256: str
    evidence_analysis_sha256: str
    evidence_provenance: Mapping[int, EvidenceProvenance]
    integrity_sha256: str
    operations_overlay: Mapping[str, Any]
    polymorphism_overlay: Mapping[str, Any]
    fixtures: Mapping[int, Mapping[str, Any]]
    canonical_bytes: Mapping[str, bytes]
    sha256: Mapping[str, str]


def build_evidence_candidate_bundle(
    *,
    analysis: MenuEvidenceAnalysis,
    pairs: Mapping[int, EvidencePair],
    effective_schema: dict[str, Any],
) -> EvidenceCandidateBundle:
    """Build reviewed menu correction candidates without performing filesystem I/O."""

    schema = _strict_document_copy(effective_schema)
    stable_pairs = _snapshot_pairs(pairs)
    fresh_analysis = analyze_menu_evidence(stable_pairs, schema)
    supplied_analysis_body = _analysis_bytes(analysis)
    fresh_analysis_body = _analysis_bytes(fresh_analysis)
    if supplied_analysis_body != fresh_analysis_body:
        raise SafetyError("Evidence candidate analysis is forged, stale, or mismatched")

    operations, after_operations = _build_operations_overlay(schema)
    polymorphism, patched = _build_polymorphism_overlay(
        after_operations,
        fresh_analysis,
    )
    try:
        ensure_valid_effective_schema(patched, require_iikocloud_contracts=True)
    except ValidationError as error:
        raise SafetyError("Evidence candidate patched schema failed strict lint") from error

    fixtures = build_and_validate_synthetic_fixtures(patched, fresh_analysis)
    _reject_candidate_leaks(operations, polymorphism, fixtures, stable_pairs, patched)

    operations_body = _yaml_bytes(operations)
    polymorphism_body = _yaml_bytes(polymorphism)
    bodies = {
        OPERATIONS_OVERLAY_PATH: operations_body,
        POLYMORPHISM_OVERLAY_PATH: polymorphism_body,
        **{
            _FIXTURE_PATHS[version]: canonical_json_bytes(fixtures[version])
            for version in _VERSIONS
        },
    }
    _scan_bytes(bodies.values())
    frozen_operations = _freeze_mapping(operations)
    frozen_polymorphism = _freeze_mapping(polymorphism)
    frozen_fixtures = MappingProxyType(
        {version: _freeze_mapping(fixtures[version]) for version in _VERSIONS}
    )
    frozen_bodies = MappingProxyType(dict(sorted(bodies.items())))
    frozen_hashes = MappingProxyType(
        {path: sha256_bytes(body) for path, body in sorted(bodies.items())}
    )
    frozen_provenance = MappingProxyType(
        {
            version: EvidenceProvenance(
                fresh_analysis.provenance[version].request_sha256,
                fresh_analysis.provenance[version].response_sha256,
            )
            for version in _VERSIONS
        }
    )
    effective_schema_sha256 = sha256_bytes(canonical_json_bytes(schema))
    evidence_analysis_sha256 = sha256_bytes(fresh_analysis_body)
    integrity_value = _candidate_manifest_document(
        operation_id=EVIDENCE_OPERATION_ID,
        effective_schema_sha256=effective_schema_sha256,
        evidence_analysis_sha256=evidence_analysis_sha256,
        provenance=frozen_provenance,
        files=frozen_hashes,
        payload_paths=EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    )
    return EvidenceCandidateBundle(
        operation_id=EVIDENCE_OPERATION_ID,
        effective_schema_sha256=effective_schema_sha256,
        evidence_analysis_sha256=evidence_analysis_sha256,
        evidence_provenance=frozen_provenance,
        integrity_sha256=sha256_bytes(canonical_json_bytes(integrity_value)),
        operations_overlay=frozen_operations,
        polymorphism_overlay=frozen_polymorphism,
        fixtures=frozen_fixtures,
        canonical_bytes=frozen_bodies,
        sha256=frozen_hashes,
    )


def _snapshot_pairs(pairs: Mapping[int, EvidencePair]) -> Mapping[int, EvidencePair]:
    entries = _caller_mapping_entries(
        pairs,
        key_type=int,
        message="Evidence candidate pair mapping is invalid",
    )
    if len(entries) != len(_VERSIONS) or {version for version, _pair in entries} != set(_VERSIONS):
        raise SafetyError("Evidence candidate requires exactly versions 2, 3, and 4")
    pairs_by_version = dict(entries)
    copied: dict[int, EvidencePair] = {}
    for version in _VERSIONS:
        pair = pairs_by_version[version]
        if type(pair) is not EvidencePair:
            raise SafetyError("Evidence candidate pair version is inconsistent")
        pair_version = pair.version
        if type(pair_version) is not int or pair_version != version:
            raise SafetyError("Evidence candidate pair version is inconsistent")
        request = _materialize_caller_json(
            pair.request,
            message="Evidence candidate pair cannot be safely snapshotted",
        )
        response = _materialize_caller_json(
            pair.response,
            message="Evidence candidate pair cannot be safely snapshotted",
        )
        if type(request) is not dict or type(response) is not dict:
            raise SafetyError("Evidence candidate pair cannot be safely snapshotted")
        copied[version] = EvidencePair(
            version=pair_version,
            request=request,
            response=response,
            request_sha256=pair.request_sha256,
            response_sha256=pair.response_sha256,
        )
    return MappingProxyType(copied)


def _caller_mapping_entries(
    value: object,
    *,
    key_type: type,
    message: str,
) -> tuple[tuple[Any, Any], ...]:
    if not isinstance(value, Mapping):
        raise SafetyError(message)
    traversal_failed = False
    try:
        keys = tuple(value)
    except (SafetyError, MemoryError):
        raise
    except Exception:
        traversal_failed = True
        keys = ()
    if traversal_failed:
        raise SafetyError(message) from None
    if any(type(key) is not key_type for key in keys) or len(set(keys)) != len(keys):
        raise SafetyError(message)

    entries: list[tuple[Any, Any]] = []
    for key in keys:
        lookup_failed = False
        try:
            child = value[key]
        except (SafetyError, MemoryError):
            raise
        except Exception:
            lookup_failed = True
            child = None
        if lookup_failed:
            raise SafetyError(message) from None
        entries.append((key, child))
    return tuple(entries)


def _caller_sequence_values(
    value: list[Any] | tuple[Any, ...], *, message: str
) -> tuple[Any, ...]:
    traversal_failed = False
    try:
        children: tuple[Any, ...] = tuple(value)
    except (SafetyError, MemoryError):
        raise
    except Exception:
        traversal_failed = True
        children = ()
    if traversal_failed:
        raise SafetyError(message) from None
    return children


def _materialize_caller_json(
    value: object,
    *,
    message: str,
    depth: int = 0,
    active: set[int] | None = None,
) -> Any:
    if depth > _MAX_DEPTH:
        raise SafetyError(message)
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError(message)
        return value
    if not isinstance(value, (Mapping, list, tuple)):
        raise SafetyError(message)

    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError(message)
    seen.add(identity)
    try:
        if isinstance(value, Mapping):
            entries = _caller_mapping_entries(value, key_type=str, message=message)
            return {
                key: _materialize_caller_json(
                    child,
                    message=message,
                    depth=depth + 1,
                    active=seen,
                )
                for key, child in entries
            }
        return [
            _materialize_caller_json(
                child,
                message=message,
                depth=depth + 1,
                active=seen,
            )
            for child in _caller_sequence_values(value, message=message)
        ]
    finally:
        seen.remove(identity)


def _build_operations_overlay(
    schema: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    working = copy.deepcopy(schema)
    target = _jsonpath(
        "paths",
        "/api/2/menu/by_id",
        "post",
        "responses",
        "200",
        "content",
        "application/json",
        "schema",
    )
    response_schema = _at(
        working,
        (
            "paths",
            "/api/2/menu/by_id",
            "post",
            "responses",
            "200",
            "content",
            "application/json",
            "schema",
        ),
    )
    if type(response_schema) is not dict:
        raise SafetyError("Evidence candidate menu response schema has drifted")
    working = _append_action(
        actions,
        working,
        target=target,
        value=response_schema,
        issue="external-menu-response-title",
        update={"title": "ExternalMenuResponse"},
    )
    overlay = _overlay(
        "iiko Cloud external menu response model contract",
        actions,
    )
    if apply_overlay(schema, copy.deepcopy(overlay)) != working:
        raise SafetyError("Evidence operations overlay is not sequentially reproducible")
    return overlay, working


def _build_polymorphism_overlay(
    schema: dict[str, Any],
    analysis: MenuEvidenceAnalysis,
) -> tuple[dict[str, Any], dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    working = copy.deepcopy(schema)
    for version in _VERSIONS:
        component_name = f"ExternalMenuV{version}"
        working = _replace_enum_default(
            actions,
            working,
            component_name=component_name,
            property_name="formatVersion",
            literal=version,
            issue=f"external-menu-v{version}-format-version",
        )
        working = _replace_required(
            actions,
            working,
            component_name,
            _required_with(
                _component(working, component_name).get("required"),
                ("formatVersion",),
            ),
            issue=f"external-menu-v{version}-required",
        )

    union_parts = (
        "components",
        "schemas",
        _CATEGORY3,
        "properties",
        "items",
        "items",
    )
    union = _at(working, union_parts)
    if type(union) is not dict:
        raise SafetyError("Evidence candidate V4 item union has drifted")
    if "discriminator" in union:
        discriminator = union["discriminator"]
        working = _append_action(
            actions,
            working,
            target=_jsonpath(*union_parts, "discriminator"),
            value=discriminator,
            issue="external-menu-v4-discriminator-remove",
            remove=True,
        )
        union = _at(working, union_parts)
        assert type(union) is dict
    mapping = {
        literal: f"{_COMPONENT_PREFIX}{branch}"
        for literal, branch in sorted(analysis.literal_to_branch.items())
    }
    working = _append_action(
        actions,
        working,
        target=_jsonpath(*union_parts),
        value=union,
        issue="external-menu-v4-discriminator",
        update={"discriminator": {"propertyName": "type", "mapping": mapping}},
    )

    for component_name in (_ITEM3, _COMBO):
        literal = analysis.branch_to_literal[component_name]
        working = _replace_enum_default(
            actions,
            working,
            component_name=component_name,
            property_name="type",
            literal=literal,
            issue=f"{_kebab(component_name)}-type",
        )

    item_required = _required_with(_component(working, _ITEM3).get("required"), ("type",))
    working = _replace_required(
        actions,
        working,
        _ITEM3,
        item_required,
        issue="external-menu-item3-required",
    )

    combo = _component(working, _COMBO)
    combo_properties = combo.get("properties")
    combo_required = combo.get("required")
    if type(combo_properties) is not dict or type(combo_required) is not list:
        raise SafetyError("Evidence candidate combo schema has drifted")
    additions: dict[str, Any] = {}
    retained = {
        field
        for field, decision in analysis.combo_fields.items()
        if decision.required_action == "retain-required"
    }
    for field in _EXACT_FIVE:
        decision = analysis.combo_fields[field]
        if decision.required_action == "retain-required":
            if decision.property_schema is None:
                raise SafetyError("Evidence retained combo field lacks a reviewed schema")
            copied = _thaw_json(decision.property_schema)
            existing = combo_properties.get(field)
            if existing is not None and canonical_json_bytes(existing) != canonical_json_bytes(
                copied
            ):
                raise SafetyError("Evidence retained combo property conflicts with upstream")
            if existing is None:
                additions[field] = copied
        elif decision.required_action != "remove-required":
            raise SafetyError("Evidence combo decision action is unsupported")
    if additions:
        working = _append_action(
            actions,
            working,
            target=_jsonpath("components", "schemas", _COMBO),
            value=combo,
            issue="external-menu-combo-retained-properties",
            update={"properties": dict(sorted(additions.items()))},
        )
        combo = _component(working, _COMBO)
        combo_properties = combo["properties"]

    replacement_required = [
        field
        for field in combo_required
        if field in combo_properties and (field not in _EXACT_FIVE or field in retained)
    ]
    for field in _EXACT_FIVE:
        if field in retained and field not in replacement_required:
            replacement_required.append(field)
    working = _replace_required(
        actions,
        working,
        _COMBO,
        replacement_required,
        issue="external-menu-combo-required",
    )

    overlay = _overlay("iiko Cloud external menu polymorphism contract", actions)
    if apply_overlay(schema, copy.deepcopy(overlay)) != working:
        raise SafetyError("Evidence polymorphism overlay is not sequentially reproducible")
    return overlay, working


def _replace_enum_default(
    actions: list[dict[str, Any]],
    working: dict[str, Any],
    *,
    component_name: str,
    property_name: str,
    literal: str | int,
    issue: str,
) -> dict[str, Any]:
    parts = ("components", "schemas", component_name, "properties", property_name)
    property_schema = _at(working, parts)
    if type(property_schema) is not dict:
        raise SafetyError("Evidence candidate discriminator/version property has drifted")
    if "enum" in property_schema:
        working = _append_action(
            actions,
            working,
            target=_jsonpath(*parts, "enum"),
            value=property_schema["enum"],
            issue=f"{issue}-enum-remove",
            remove=True,
        )
        property_schema = _at(working, parts)
        assert type(property_schema) is dict
    return _append_action(
        actions,
        working,
        target=_jsonpath(*parts),
        value=property_schema,
        issue=issue,
        update={"default": literal, "enum": [literal]},
    )


def _replace_required(
    actions: list[dict[str, Any]],
    working: dict[str, Any],
    component_name: str,
    required: list[str],
    *,
    issue: str,
) -> dict[str, Any]:
    if len(set(required)) != len(required):
        raise SafetyError("Evidence candidate required replacement contains duplicates")
    component_parts = ("components", "schemas", component_name)
    component = _at(working, component_parts)
    if type(component) is not dict or type(component.get("required")) is not list:
        raise SafetyError("Evidence candidate required schema has drifted")
    working = _append_action(
        actions,
        working,
        target=_jsonpath(*component_parts, "required"),
        value=component["required"],
        issue=f"{issue}-remove",
        remove=True,
    )
    component = _at(working, component_parts)
    assert type(component) is dict
    return _append_action(
        actions,
        working,
        target=_jsonpath(*component_parts),
        value=component,
        issue=issue,
        update={"required": required},
    )


def _append_action(
    actions: list[dict[str, Any]],
    working: dict[str, Any],
    *,
    target: str,
    value: Any,
    issue: str,
    update: Any | None = None,
    remove: bool = False,
) -> dict[str, Any]:
    action: dict[str, Any] = {
        "target": target,
        "x-iiko-sdk-guard": {
            "issue": issue,
            "expected-matches": 1,
            "expected-sha256": sha256_bytes(canonical_json_bytes(value)),
        },
    }
    if remove:
        action["remove"] = True
    else:
        action["update"] = update
    next_document = apply_overlay(working, _overlay("candidate action", [action]))
    actions.append(action)
    return next_document


def _reject_candidate_leaks(
    operations: dict[str, Any],
    polymorphism: dict[str, Any],
    fixtures: dict[int, dict[str, Any]],
    pairs: Mapping[int, EvidencePair],
    schema: dict[str, Any],
) -> None:
    _scan_json_strings((operations, polymorphism, fixtures))
    captured = {
        text
        for version in _VERSIONS
        for envelope in (pairs[version].request, pairs[version].response)
        for text in _leaf_strings(envelope)
    }
    allowed = _schema_enum_strings(schema)
    for fixture in fixtures.values():
        for value in _leaf_strings(fixture):
            if value in captured and value not in allowed:
                raise SafetyError("Evidence candidate fixture contains a captured string value")


def _scan_json_strings(values: Any) -> None:
    sensitive_keys = SECRET_KEYS | EMAIL_KEYS | PHONE_KEYS
    if any(key.casefold() in sensitive_keys for key in _all_mapping_keys(values)):
        raise SafetyError("Evidence candidate failed the secret/PII key scan")
    for value in _all_strings(values):
        without_uuids = _UUID_ANY.sub("", value)
        if (
            _REDACTION.search(value)
            or _JWT.search(value)
            or _BEARER.search(value)
            or _EMAIL.search(value)
            or _PHONE.search(without_uuids)
        ):
            raise SafetyError("Evidence candidate failed the secret/PII/redaction scan")


def _all_mapping_keys(value: Any) -> tuple[str, ...]:
    if isinstance(value, Mapping):
        return tuple(
            key
            for candidate, child in value.items()
            for key in (
                *((candidate,) if type(candidate) is str else ()),
                *_all_mapping_keys(child),
            )
        )
    if isinstance(value, (list, tuple)):
        return tuple(key for child in value for key in _all_mapping_keys(child))
    return ()


def _scan_bytes(bodies: Any) -> None:
    for body in bodies:
        try:
            text = body.decode("utf-8")
        except (AttributeError, UnicodeError) as error:
            raise SafetyError("Evidence candidate bytes are not UTF-8") from error
        _scan_json_strings(text)


def _all_strings(value: Any) -> tuple[str, ...]:
    if type(value) is str:
        return (value,)
    if isinstance(value, Mapping):
        return tuple(
            text
            for key, child in value.items()
            for text in ((*((key,) if type(key) is str else ()), *_all_strings(child)))
        )
    if isinstance(value, (list, tuple)):
        return tuple(text for child in value for text in _all_strings(child))
    return ()


def _leaf_strings(value: Any) -> tuple[str, ...]:
    if type(value) is str:
        return (value,)
    if isinstance(value, Mapping):
        return tuple(text for child in value.values() for text in _leaf_strings(child))
    if isinstance(value, (list, tuple)):
        return tuple(text for child in value for text in _leaf_strings(child))
    return ()


def _schema_enum_strings(value: Any) -> frozenset[str]:
    result: set[str] = set()
    if isinstance(value, Mapping):
        enum = value.get("enum")
        if isinstance(enum, (list, tuple)):
            result.update(item for item in enum if type(item) is str)
        for child in value.values():
            result.update(_schema_enum_strings(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            result.update(_schema_enum_strings(child))
    return frozenset(result)


def _analysis_bytes(value: MenuEvidenceAnalysis) -> bytes:
    if type(value) is not MenuEvidenceAnalysis:
        raise SafetyError("Evidence candidate requires an exact analysis result")
    message = "Evidence candidate analysis cannot be canonicalized"
    provenance_entries = _caller_mapping_entries(
        value.provenance,
        key_type=int,
        message=message,
    )
    if len(provenance_entries) != len(_VERSIONS) or {
        version for version, _item in provenance_entries
    } != set(_VERSIONS):
        raise SafetyError("Evidence candidate analysis provenance is incomplete")
    provenance: dict[str, Any] = {}
    for version, provenance_item in provenance_entries:
        if type(provenance_item) is not EvidenceProvenance or (
            type(provenance_item.request_sha256) is not str
            or type(provenance_item.response_sha256) is not str
        ):
            raise SafetyError("Evidence candidate analysis provenance is invalid")
        provenance[str(version)] = {
            "request": provenance_item.request_sha256,
            "response": provenance_item.response_sha256,
        }

    field_entries = _caller_mapping_entries(
        value.combo_fields,
        key_type=str,
        message=message,
    )
    if len(field_entries) != len(_EXACT_FIVE) or {
        name for name, _decision in field_entries
    } != set(_EXACT_FIVE):
        raise SafetyError("Evidence candidate analysis field scope is invalid")
    decisions = dict(field_entries)
    fields: dict[str, Any] = {}
    for name in _EXACT_FIVE:
        decision = decisions[name]
        if (
            type(decision) is not ComboFieldDecision
            or type(decision.field_name) is not str
            or decision.field_name != name
            or type(decision.required_action) is not str
            or type(decision.observation_count) is not int
            or type(decision.reason_code) is not str
        ):
            raise SafetyError("Evidence candidate combo decision is invalid")
        property_schema: Any = None
        if decision.property_schema is not None:
            materialized_schema = _materialize_caller_json(
                decision.property_schema,
                message=message,
            )
            if type(materialized_schema) is not dict:
                raise SafetyError("Evidence candidate combo decision is invalid")
            property_schema = _thaw_json(materialized_schema)
        fields[name] = {
            "action": decision.required_action,
            "count": decision.observation_count,
            "reason": decision.reason_code,
            "schema": property_schema,
        }

    if any(
        type(count) is not int
        for count in (
            value.ambiguous_count,
            value.combo_observation_count,
            value.total_item_count,
        )
    ):
        raise SafetyError(message)
    semantic = {
        "ambiguousCount": value.ambiguous_count,
        "branchToLiteral": _analysis_primitive_mapping(
            value.branch_to_literal,
            value_type=str,
            message=message,
        ),
        "comboFields": fields,
        "comboObservationCount": value.combo_observation_count,
        "literalToBranch": _analysis_primitive_mapping(
            value.literal_to_branch,
            value_type=str,
            message=message,
        ),
        "provenance": provenance,
        "totalItemCount": value.total_item_count,
        "unambiguousCounts": _analysis_primitive_mapping(
            value.unambiguous_counts,
            value_type=int,
            message=message,
        ),
    }
    return canonical_json_bytes(semantic)


def _analysis_primitive_mapping(
    value: object,
    *,
    value_type: type,
    message: str,
) -> dict[str, Any]:
    entries = _caller_mapping_entries(
        value,
        key_type=str,
        message=message,
    )
    if any(type(child) is not value_type for _key, child in entries):
        raise SafetyError(message)
    return dict(entries)


def _required_with(value: Any, additions: tuple[str, ...]) -> list[str]:
    if type(value) is not list or any(type(item) is not str or not item for item in value):
        raise SafetyError("Evidence candidate required list has drifted")
    result = list(value)
    for addition in additions:
        if addition not in result:
            result.append(addition)
    return result


def _component(document: dict[str, Any], name: str) -> dict[str, Any]:
    components = document.get("components")
    schemas = components.get("schemas") if type(components) is dict else None
    component = schemas.get(name) if type(schemas) is dict else None
    if type(component) is not dict:
        raise SafetyError(f"Evidence candidate component {name!r} is missing")
    return component


def _at(document: dict[str, Any], parts: tuple[str, ...]) -> Any:
    value: Any = document
    try:
        for part in parts:
            if type(value) is not dict:
                raise KeyError(part)
            value = value[part]
    except (KeyError, TypeError):
        raise SafetyError("Evidence candidate reviewed schema path has drifted") from None
    return value


def _jsonpath(*parts: str) -> str:
    return "$" + "".join(f"[{json.dumps(part)}]" for part in parts)


def _overlay(title: str, actions: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "overlay": "1.1.0",
        "info": {"title": title, "version": "1.0.0"},
        "actions": copy.deepcopy(actions),
    }


def _kebab(value: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "-", value).lower()


def _yaml_bytes(value: Any) -> bytes:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    ).encode("utf-8")


def _strict_document_copy(value: Any) -> dict[str, Any]:
    message = "Evidence candidate schema is not strict canonical JSON"
    materialized = _materialize_caller_json(value, message=message)
    body = canonical_json_bytes(materialized)
    copied = json.loads(body)
    if type(copied) is not dict:
        raise SafetyError("Evidence candidate schema must be an object")
    return copied


def _thaw_json(value: Any, *, depth: int = 0) -> Any:
    if depth > _MAX_DEPTH:
        raise SafetyError("Evidence candidate immutable JSON is too deep")
    if isinstance(value, Mapping):
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence candidate immutable JSON key is invalid")
        return {key: _thaw_json(child, depth=depth + 1) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_thaw_json(child, depth=depth + 1) for child in value]
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence candidate immutable JSON is invalid")


def _freeze_json(value: Any, *, depth: int = 0) -> FrozenJson:
    if depth > _MAX_DEPTH:
        raise SafetyError("Evidence candidate JSON is too deep")
    if type(value) is dict:
        return MappingProxyType(
            {key: _freeze_json(child, depth=depth + 1) for key, child in value.items()}
        )
    if type(value) is list:
        return tuple(_freeze_json(child, depth=depth + 1) for child in value)
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence candidate JSON is not strict")


def _freeze_mapping(value: Mapping[str, Any]) -> Mapping[str, FrozenJson]:
    frozen = _freeze_json(dict(value))
    if not isinstance(frozen, Mapping):
        raise SafetyError("Evidence candidate JSON root is not an object")
    return frozen
