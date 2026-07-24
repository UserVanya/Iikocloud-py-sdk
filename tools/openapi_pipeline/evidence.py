from __future__ import annotations

import copy
import secrets
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

from .capture import ARRAY_ITEM, OBJECT_VALUE, CaptureWriter, LiveCapture, RedactionHints
from .errors import SafetyError
from .evidence_schema_repairs import (
    build_reviewed_external_menu_hint_schema,
    is_reviewed_dynamic_map_schema,
)
from .live.lock import LiveProcessLock
from .live.profile import ResolvedLiveProfile
from .live.pytest_support import resolve_locked_live_profile
from .live.rates import LiveRateGuard, RateCatalog
from .live.session import LiveOperation, SafeLiveSession, load_operation_contract
from .live.state import LiveStateStore
from .paths import RepoPaths
from .pipeline import compose_reviewed_bootstrap_candidate

if TYPE_CHECKING:
    from .evidence_candidate_writer import EvidenceCandidateWriteResult

_EVIDENCE_OPERATION = "get_external_menu_by_id"
_EVIDENCE_VERSIONS = frozenset({2, 3, 4})
_EVIDENCE_PATH = "/api/2/menu/by_id"
_ITEM_TYPE_HINT_PATH = (
    "itemGroups",
    ARRAY_ITEM,
    "items",
    ARRAY_ITEM,
    "type",
)
_ITEM_ORDER_TYPE_HINT_PATH = (*_ITEM_TYPE_HINT_PATH[:-1], "orderItemType")
_ITEM_PRICE_STRATEGY_HINT_PATH = (*_ITEM_TYPE_HINT_PATH[:-1], "priceStrategy")
_OVERRIDE_TAX_CATEGORIES_HINT_PATH = ("overrideTaxCategories", OBJECT_VALUE)
_REDACTED_STRING_SENTINEL = "<redacted:string>"


def _evidence_component(document: dict[str, Any], name: str) -> dict[str, Any]:
    components = document.get("components")
    schemas = components.get("schemas") if type(components) is dict else None
    schema = schemas.get(name) if type(schemas) is dict else None
    if type(schema) is not dict:
        raise SafetyError(f"Evidence schema component {name!r} is missing or invalid")
    return schema


def _evidence_string_enum(
    component: dict[str, Any],
    property_name: str,
    *,
    expected_keys: frozenset[str],
    expected_format: str | None = None,
) -> frozenset[str]:
    properties = component.get("properties")
    property_schema = properties.get(property_name) if type(properties) is dict else None
    if type(property_schema) is not dict or set(property_schema) != expected_keys:
        raise SafetyError(f"Evidence {property_name} enum shape has drifted")
    enum = property_schema.get("enum")
    if (
        property_schema.get("type") != "string"
        or type(enum) is not list
        or not enum
        or any(
            type(value) is not str or not value.strip() or value == _REDACTED_STRING_SENTINEL
            for value in enum
        )
        or len(set(enum)) != len(enum)
        or (expected_format is not None and property_schema.get("format") != expected_format)
        or (
            "description" in expected_keys
            and (
                type(property_schema.get("description")) is not str
                or not property_schema["description"].strip()
            )
        )
        or ("default" in expected_keys and property_schema.get("default") not in enum)
    ):
        raise SafetyError(f"Evidence {property_name} enum is invalid")
    return frozenset(enum)


def _assert_reviewed_override_tax_array_shape(
    document: dict[str, Any],
    menu_version: int,
) -> None:
    component_name, item_component = {
        3: ("ExternalMenuV3", "OverrideTaxesDto"),
        4: ("ExternalMenuV4", "OverrideTaxesDto2"),
    }[menu_version]
    component = _evidence_component(document, component_name)
    properties = component.get("properties")
    override_tax_categories = (
        properties.get("overrideTaxCategories") if type(properties) is dict else None
    )
    if override_tax_categories != {
        "description": "Tax benefits",
        "items": {"$ref": f"#/components/schemas/{item_component}"},
        "type": "array",
    } and not is_reviewed_dynamic_map_schema(
        schema_path=(f"components.schemas.{component_name}.properties.overrideTaxCategories"),
        schema=override_tax_categories,
    ):
        raise SafetyError("Evidence overrideTaxCategories broken array shape has drifted")


def build_evidence_redaction_hints(
    effective_schema: dict[str, Any], operation_id: str
) -> RedactionHints:
    """Build the one reviewed exception needed by external-menu evidence captures."""

    if operation_id != _EVIDENCE_OPERATION:
        raise SafetyError("Evidence redaction hints operation is not approved")
    hints = RedactionHints.for_operation(effective_schema, operation_id)
    if set(hints.response_values_by_status) != {200}:
        raise SafetyError("Evidence redaction hints require exactly the 200 success response")

    paths = effective_schema.get("paths")
    path_item = paths.get(_EVIDENCE_PATH) if type(paths) is dict else None
    operation = path_item.get("post") if type(path_item) is dict else None
    if type(operation) is not dict or operation.get("operationId") != operation_id:
        raise SafetyError("Evidence redaction hints endpoint contract has drifted")
    responses = operation.get("responses")
    response = responses.get("200") if type(responses) is dict else None
    content = response.get("content") if type(response) is dict else None
    media = content.get("application/json") if type(content) is dict else None
    response_schema = media.get("schema") if type(media) is dict else None
    expected_response_schema = {
        "oneOf": [
            {"$ref": "#/components/schemas/ExternalMenuV2"},
            {"$ref": "#/components/schemas/ExternalMenuV3"},
            {"$ref": "#/components/schemas/ExternalMenuV4"},
        ]
    }
    if response_schema != expected_response_schema:
        raise SafetyError("Evidence external-menu V4 response reference chain has drifted")

    menu_v4 = _evidence_component(effective_schema, "ExternalMenuV4")
    menu_v4_properties = menu_v4.get("properties")
    item_groups = (
        menu_v4_properties.get("itemGroups") if type(menu_v4_properties) is dict else None
    )
    if item_groups != {
        "type": "array",
        "items": {"$ref": "#/components/schemas/ExternalMenuCategory3"},
    }:
        raise SafetyError("Evidence external-menu V4 category reference has drifted")

    category = _evidence_component(effective_schema, "ExternalMenuCategory3")
    category_properties = category.get("properties")
    category_items = (
        category_properties.get("items") if type(category_properties) is dict else None
    )
    if category_items != {
        "type": "array",
        "items": {
            "oneOf": [
                {"$ref": "#/components/schemas/ExternalMenuItem3"},
                {"$ref": "#/components/schemas/ExternalMenuComboItem"},
            ]
        },
    }:
        raise SafetyError("Evidence external-menu item oneOf reference chain has drifted")

    combo = _evidence_component(effective_schema, "ExternalMenuComboItem")
    combo_required = combo.get("required")
    combo_properties = combo.get("properties")
    combo_type = combo_properties.get("type") if type(combo_properties) is dict else None
    if (
        type(combo_required) is not list
        or combo_required.count("type") != 1
        or combo_type != {"type": "string"}
    ):
        raise SafetyError("Evidence external-menu combo type shape has drifted")

    item = _evidence_component(effective_schema, "ExternalMenuItem3")
    item_properties = item.get("properties")
    item_type = item_properties.get("type") if type(item_properties) is dict else None
    if type(item_type) is not dict or set(item_type) != {
        "enum",
        "type",
        "description",
        "default",
    }:
        raise SafetyError("Evidence external-menu item type shape has drifted")
    enum = item_type.get("enum")
    if (
        item_type.get("type") != "string"
        or type(enum) is not list
        or not enum
        or any(type(value) is not str or not value for value in enum)
        or len(set(enum)) != len(enum)
    ):
        raise SafetyError("Evidence external-menu item type enum is invalid")

    response_values = {
        selector: dict(values) for selector, values in hints.response_values_by_status.items()
    }
    if response_values[200].get(_ITEM_TYPE_HINT_PATH, frozenset()):
        raise SafetyError("Evidence item type path is already constrained unexpectedly")
    response_values[200][_ITEM_TYPE_HINT_PATH] = frozenset(enum)
    return RedactionHints(hints.operation_id, hints.request_values, response_values)


def build_versioned_evidence_redaction_hints(
    effective_schema: dict[str, Any],
    operation_id: str,
    menu_version: int,
) -> RedactionHints:
    """Build fail-closed response hints for one explicitly selected menu version."""

    if type(menu_version) is not int or menu_version not in _EVIDENCE_VERSIONS:
        raise SafetyError("Evidence redaction hint version must be exactly 2, 3, or 4")
    effective_schema = build_reviewed_external_menu_hint_schema(effective_schema)
    if menu_version in {3, 4}:
        _assert_reviewed_override_tax_array_shape(effective_schema, menu_version)
    reviewed = build_evidence_redaction_hints(effective_schema, operation_id)
    item = _evidence_component(effective_schema, "ExternalMenuItem3")
    combo = _evidence_component(effective_schema, "ExternalMenuComboItem")
    item_properties = item.get("properties")
    combo_properties = combo.get("properties")
    if (
        type(item_properties) is not dict
        or "priceStrategy" in item_properties
        or type(combo_properties) is not dict
        or "orderItemType" in combo_properties
    ):
        raise SafetyError("Evidence orderItemType/priceStrategy oneOf exception has drifted")
    item_order_types = _evidence_string_enum(
        item,
        "orderItemType",
        expected_keys=frozenset({"description", "enum", "format", "type"}),
        expected_format="enum",
    )
    combo_price_strategies = _evidence_string_enum(
        combo,
        "priceStrategy",
        expected_keys=frozenset({"default", "description", "enum", "type"}),
    )
    selected_schema = copy.deepcopy(effective_schema)
    paths = selected_schema.get("paths")
    path_item = paths.get(_EVIDENCE_PATH) if type(paths) is dict else None
    operation = path_item.get("post") if type(path_item) is dict else None
    responses = operation.get("responses") if type(operation) is dict else None
    response = responses.get("200") if type(responses) is dict else None
    content = response.get("content") if type(response) is dict else None
    media = content.get("application/json") if type(content) is dict else None
    if type(media) is not dict:
        raise SafetyError("Evidence versioned response contract has drifted")
    component = {2: "ExternalMenuV2", 3: "ExternalMenuV3", 4: "ExternalMenuV4"}[menu_version]
    media["schema"] = {"$ref": f"#/components/schemas/{component}"}
    selected = RedactionHints.for_operation(selected_schema, operation_id)
    if selected.request_values != reviewed.request_values:
        raise SafetyError("Evidence versioned request redaction hints have drifted")
    if set(selected.response_values_by_status) != {200}:
        raise SafetyError("Evidence versioned hints require exactly the 200 response")

    response_values = dict(selected.response_values_by_status[200])
    if menu_version in {3, 4}:
        existing_override_values = response_values.get(_OVERRIDE_TAX_CATEGORIES_HINT_PATH)
        if existing_override_values not in {None, frozenset()}:
            raise SafetyError("Evidence overrideTaxCategories map redaction values have drifted")
        response_values[_OVERRIDE_TAX_CATEGORIES_HINT_PATH] = frozenset()
    if menu_version == 4:
        reviewed_item_types = reviewed.response_values_by_status[200].get(_ITEM_TYPE_HINT_PATH)
        selected_item_types = response_values.get(_ITEM_TYPE_HINT_PATH, frozenset())
        if reviewed_item_types is None or (
            selected_item_types and selected_item_types != reviewed_item_types
        ):
            raise SafetyError("Evidence V4 item type redaction hints have drifted")
        response_values[_ITEM_TYPE_HINT_PATH] = reviewed_item_types
        for path, expected_values in (
            (_ITEM_ORDER_TYPE_HINT_PATH, item_order_types),
            (_ITEM_PRICE_STRATEGY_HINT_PATH, combo_price_strategies),
        ):
            selected_values = response_values.get(path, frozenset())
            if selected_values and selected_values != expected_values:
                raise SafetyError("Evidence V4 item enum redaction hints have drifted")
            response_values[path] = expected_values
    return RedactionHints(operation_id, selected.request_values, {200: response_values})


@dataclass(frozen=True)
class CaptureEvidenceDependencies:
    paths: RepoPaths
    rate_catalog_loader: Callable[[Path], RateCatalog]
    candidate_composer: Callable[[RepoPaths], tuple[dict[str, Any], dict[str, str]]]
    operation_contract_loader: Callable[[Path], Mapping[str, LiveOperation]]
    hints_builder: Callable[[dict[str, Any], str, int], RedactionHints]
    lock_factory: Callable[[Path], LiveProcessLock]
    profile_resolver: Callable[..., ResolvedLiveProfile]
    state_factory: Callable[..., LiveStateStore]
    guard_factory: Callable[..., LiveRateGuard]
    writer_factory: Callable[[Path], CaptureWriter]
    capture_factory: Callable[..., LiveCapture]
    session_factory: Callable[..., SafeLiveSession]
    run_id_factory: Callable[[], str]


def _new_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}-{secrets.token_hex(4)}"


def default_capture_evidence_dependencies(
    paths: RepoPaths | None = None,
) -> CaptureEvidenceDependencies:
    return CaptureEvidenceDependencies(
        paths=paths or RepoPaths.discover(),
        rate_catalog_loader=RateCatalog.load,
        candidate_composer=compose_reviewed_bootstrap_candidate,
        operation_contract_loader=load_operation_contract,
        hints_builder=build_versioned_evidence_redaction_hints,
        lock_factory=LiveProcessLock,
        profile_resolver=resolve_locked_live_profile,
        state_factory=LiveStateStore,
        guard_factory=LiveRateGuard,
        writer_factory=CaptureWriter,
        capture_factory=LiveCapture,
        session_factory=SafeLiveSession,
        run_id_factory=_new_run_id,
    )


def _validate_selection(operation: object, menu_version: object) -> tuple[str, int]:
    if operation != _EVIDENCE_OPERATION:
        raise SafetyError("Evidence operation is not explicitly approved")
    if type(menu_version) is not int or menu_version not in _EVIDENCE_VERSIONS:
        raise SafetyError("Evidence menu version must be exactly 2, 3, or 4")
    return _EVIDENCE_OPERATION, menu_version


def build_evidence_candidate(
    paths: RepoPaths,
    *,
    operation: str,
) -> EvidenceCandidateWriteResult:
    """Build one detached candidate from reviewed local evidence without accepting it."""

    if type(paths) is not RepoPaths:
        raise SafetyError("Evidence candidate build requires exact repository paths")
    if type(operation) is not str or operation != _EVIDENCE_OPERATION:
        raise SafetyError("Evidence operation is not explicitly approved")

    from .evidence_analysis import analyze_menu_evidence
    from .evidence_candidate_store import build_evidence_candidate_manifest
    from .evidence_candidate_writer import write_evidence_candidate_tree
    from .evidence_candidates import build_evidence_candidate_bundle
    from .evidence_promotion import CaptureEvidenceReader
    from .pipeline import compose_reviewed_evidence_base_candidate

    effective_schema, _model_mappings = compose_reviewed_evidence_base_candidate(paths)
    with LiveProcessLock(paths.state / "live.lock") as process_lock:
        pairs = CaptureEvidenceReader(
            paths.root,
            effective_schema,
            operation,
            process_lock=process_lock,
        ).read_menu_pairs()

    analysis = analyze_menu_evidence(pairs, effective_schema)
    bundle = build_evidence_candidate_bundle(
        analysis=analysis,
        pairs=pairs,
        effective_schema=effective_schema,
    )
    manifest = build_evidence_candidate_manifest(bundle)
    return write_evidence_candidate_tree(manifest, paths)


async def capture_evidence(
    *,
    live_profile: str,
    env_file: str,
    operation: str,
    menu_version: int,
    dependencies: CaptureEvidenceDependencies | None = None,
) -> None:
    selected_operation, selected_version = _validate_selection(operation, menu_version)
    selected = dependencies or default_capture_evidence_dependencies()
    paths = selected.paths

    # Both public rate contracts must be verified before schema composition, lock/state
    # creation, profile parsing, environment access, or HTTP client construction.
    catalog = selected.rate_catalog_loader(paths.root / "contracts/rate-limits.yaml")
    catalog.operation_budget("authenticate")
    catalog.operation_budget(selected_operation)

    effective_schema, _model_mappings = selected.candidate_composer(paths)
    operation_catalog = selected.operation_contract_loader(
        paths.root / "contracts/live-operations.yaml"
    )
    authentication = operation_catalog.get("authenticate")
    if (
        authentication is None
        or authentication.kind != "auth"
        or authentication.cleanup is not None
        or authentication.method != "POST"
        or authentication.path != "/api/1/access_token"
    ):
        raise SafetyError("Evidence authentication contract is not the approved endpoint")
    contract = operation_catalog.get(selected_operation)
    if (
        contract is None
        or contract.kind != "read"
        or contract.cleanup is not None
        or contract.method != "POST"
        or contract.path != "/api/2/menu/by_id"
    ):
        raise SafetyError("Evidence operation contract is not the approved read endpoint")
    hints = selected.hints_builder(effective_schema, selected_operation, selected_version)

    process_lock = selected.lock_factory(paths.root / ".state/live.lock")
    with process_lock:
        profile = selected.profile_resolver(
            paths.root,
            process_lock=process_lock,
            profile_name=live_profile,
            env_file_option=env_file,
        )
        state = selected.state_factory(
            paths.root / ".state/live-rate-limits.json",
            process_lock=process_lock,
        )
        guard = selected.guard_factory(
            profile_fingerprint=profile.fingerprint,
            catalog=catalog,
            state=state,
            process_lock=process_lock,
        )
        writer = selected.writer_factory(paths.root / "private/captures")
        capture = selected.capture_factory(
            writer=writer,
            run_id=selected.run_id_factory(),
            selected_operation=selected_operation,
            operation_catalog=operation_catalog,
            hints=hints,
        )
        session = selected.session_factory(
            profile=profile,
            guard=guard,
            state=state,
            operation_contract=operation_catalog,
            capture=capture,
        )
        if profile.external_menu_id is None:
            raise SafetyError("Evidence capture requires an external menu in the live profile")
        try:
            await session.authenticate()
            await session.request_json(
                selected_operation,
                contract.method,
                contract.path,
                {
                    "externalMenuId": profile.external_menu_id,
                    "organizationIds": [profile.organization_id],
                    "version": selected_version,
                },
            )
        finally:
            await session.close()
