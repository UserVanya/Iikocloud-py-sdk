from __future__ import annotations

import dataclasses
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest
from test_evidence_promotion_reader import _effective_schema, _response_body

import tools.openapi_pipeline.evidence_promotion as promotion_module
from tools.openapi_pipeline.capture import Sanitizer
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence import build_versioned_evidence_redaction_hints
from tools.openapi_pipeline.evidence_analysis import analyze_menu_evidence
from tools.openapi_pipeline.evidence_promotion import EvidencePair
from tools.openapi_pipeline.evidence_validation import MenuEvidenceValidator
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_reviewed_bootstrap_candidate

OPERATION = "get_external_menu_by_id"
ITEM3 = "ExternalMenuItem3"
COMBO = "ExternalMenuComboItem"
EXACT_FIVE = (
    "allergenGroupIds",
    "itemSizes",
    "modifierSchemaId",
    "orderItemType",
    "splittable",
)


def _dish(literal: str = "DISH", **changes: Any) -> dict[str, Any]:
    item: dict[str, Any] = {
        "allergenGroupIds": ["allergen"],
        "id": "10000000-0000-4000-8000-000000000001",
        "itemSizes": ["size"],
        "modifierSchemaId": "modifier",
        "orderItemType": "Product",
        "splittable": False,
        "type": literal,
    }
    item.update(changes)
    return item


def _combo(literal: str = "COMBO", **changes: Any) -> dict[str, Any]:
    item: dict[str, Any] = {
        "id": "20000000-0000-4000-8000-000000000002",
        "sizes": [
            {
                "name": "size",
                "sizeId": "30000000-0000-4000-8000-000000000003",
            }
        ],
        "type": literal,
    }
    item.update(changes)
    return item


def _sanitized_pair(
    schema: dict[str, Any],
    version: int,
    *,
    items: list[dict[str, Any]] | None = None,
    response_change: tuple[str, Any] | None = None,
) -> EvidencePair:
    request_body = {
        "externalMenuId": "40000000-0000-4000-8000-000000000004",
        "organizationIds": ["50000000-0000-4000-8000-000000000005"],
        "version": version,
    }
    response_body = _response_body(version)
    if version == 4 and items is not None:
        response_body["itemGroups"] = [{"items": items}]
    if response_change is not None:
        name, value = response_change
        response_body[name] = value
    return _pair_from_bodies(schema, version, request_body, response_body)


def _pair_from_bodies(
    schema: dict[str, Any],
    version: int,
    request_body: dict[str, Any],
    response_body: dict[str, Any],
) -> EvidencePair:
    hints = build_versioned_evidence_redaction_hints(schema, OPERATION, version)
    sanitizer = Sanitizer.for_fixed_point_validation()
    sanitized_request = sanitizer.sanitize(
        {key: value for key, value in request_body.items()},
        path_values=hints.request_values,
    )
    sanitized_response = sanitizer.sanitize(
        response_body,
        path_values=hints.response_values_for_status(200),
    )
    metadata = {
        "method": "POST",
        "operationId": OPERATION,
        "path": "/api/2/menu/by_id",
        "runId": f"synthetic-v{version}",
        "status": 200,
    }
    request = {"body": sanitized_request, "metadata": dict(metadata)}
    response = {"body": sanitized_response, "metadata": dict(metadata)}
    return EvidencePair(
        version=version,
        request=request,
        response=response,
        request_sha256=sha256_bytes(canonical_json_bytes(request)),
        response_sha256=sha256_bytes(canonical_json_bytes(response)),
    )


def _pairs(
    schema: dict[str, Any],
    items: list[dict[str, Any]],
    *,
    order: tuple[int, int, int] = (2, 3, 4),
) -> Mapping[int, EvidencePair]:
    by_version = {
        version: _sanitized_pair(schema, version, items=items if version == 4 else None)
        for version in (2, 3, 4)
    }
    return {version: by_version[version] for version in order}


def _ambiguous_schema() -> dict[str, Any]:
    schema = _effective_schema()
    item3 = schema["components"]["schemas"][ITEM3]
    item3["properties"]["sizes"] = {
        "type": "array",
        "items": {"$ref": "#/components/schemas/ExternalMenuComboItemSize"},
    }
    return schema


def _minimal_schema_value(
    document: dict[str, Any],
    schema: dict[str, Any],
    *,
    active: frozenset[str] = frozenset(),
) -> Any:
    reference = schema.get("$ref")
    if reference is not None:
        assert isinstance(reference, str) and reference.startswith("#/components/schemas/")
        name = reference.removeprefix("#/components/schemas/")
        assert name not in active
        return _minimal_schema_value(
            document,
            document["components"]["schemas"][name],
            active=active | {name},
        )
    if schema.get("nullable") is True:
        return None
    one_of = schema.get("oneOf")
    if isinstance(one_of, list):
        return _minimal_schema_value(document, one_of[0], active=active)
    enum = schema.get("enum")
    if isinstance(enum, list) and enum:
        return enum[0]
    schema_type = schema.get("type")
    if schema_type == "object":
        properties = schema.get("properties", {})
        return {
            name: _minimal_schema_value(document, properties[name], active=active)
            for name in schema.get("required", [])
            if name in properties
        }
    if schema_type == "array":
        return []
    if schema_type == "boolean":
        return False
    if schema_type == "integer":
        return 0
    if schema_type == "number":
        return 0.0
    if schema.get("format") == "uuid":
        return "00000000-0000-4000-8000-000000000000"
    return "<redacted:string>"


def _field_values(field: str) -> tuple[Any, Any]:
    return {
        "allergenGroupIds": (["first"], ["second"]),
        "itemSizes": (["first"], ["second"]),
        "modifierSchemaId": ("first", "second"),
        "orderItemType": ("Product", "Compound"),
        "splittable": (False, True),
    }[field]


def _semantic_result(result: Any) -> tuple[Any, ...]:
    return (
        dict(result.branch_to_literal),
        dict(result.literal_to_branch),
        dict(result.unambiguous_counts),
        result.ambiguous_count,
        result.total_item_count,
        result.combo_observation_count,
        dict(result.combo_fields),
    )


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _plain(child) for key, child in value.items()}
    if type(value) is tuple:
        return [_plain(child) for child in value]
    return value


def _replace_pair(
    pair: EvidencePair,
    *,
    request: dict[str, Any] | None = None,
    response: dict[str, Any] | None = None,
) -> EvidencePair:
    request_value = request if request is not None else _plain(pair.request)
    response_value = response if response is not None else _plain(pair.response)
    return EvidencePair(
        version=pair.version,
        request=request_value,
        response=response_value,
        request_sha256=sha256_bytes(canonical_json_bytes(request_value)),
        response_sha256=sha256_bytes(canonical_json_bytes(response_value)),
    )


def test_analyzer_derives_normal_mapping_counts_and_sorted_provenance() -> None:
    schema = _effective_schema()
    pairs = _pairs(schema, [_dish(), _combo()], order=(4, 2, 3))

    result = analyze_menu_evidence(pairs, schema)

    assert tuple(result.provenance) == (2, 3, 4)
    assert result.provenance[4].request_sha256 == pairs[4].request_sha256
    assert result.provenance[4].response_sha256 == pairs[4].response_sha256
    assert dict(result.branch_to_literal) == {COMBO: "COMBO", ITEM3: "DISH"}
    assert dict(result.literal_to_branch) == {
        "COMBO": COMBO,
        "DISH": ITEM3,
        "SERVICE": ITEM3,
    }
    assert dict(result.unambiguous_counts) == {COMBO: 1, ITEM3: 1}
    assert result.ambiguous_count == 0
    assert result.total_item_count == 2
    assert result.combo_observation_count == 1
    assert tuple(result.combo_fields) == EXACT_FIVE


def test_analyzer_rejects_observations_conflicting_with_reviewed_mapping() -> None:
    schema = _effective_schema()

    with pytest.raises(SafetyError, match="reviewed.*mapping|literal.*branch"):
        analyze_menu_evidence(_pairs(schema, [_dish("COMBO"), _combo("DISH")]), schema)


def test_analyzer_routes_reviewed_service_to_item3_without_changing_primary_mapping() -> None:
    schema = _effective_schema()
    items = [
        _dish(),
        _combo(),
        _dish("SERVICE"),
    ]

    result = analyze_menu_evidence(_pairs(schema, items), schema)

    assert dict(result.branch_to_literal) == {COMBO: "COMBO", ITEM3: "DISH"}
    assert dict(result.literal_to_branch) == {
        "COMBO": COMBO,
        "DISH": ITEM3,
        "SERVICE": ITEM3,
    }
    assert result.total_item_count == 3
    assert result.combo_observation_count == 1


def test_analyzer_uses_exact_reviewed_mapping_without_combo_observation() -> None:
    schema = _effective_schema()

    result = analyze_menu_evidence(_pairs(schema, [_dish(), _dish("SERVICE")]), schema)

    assert dict(result.branch_to_literal) == {COMBO: "COMBO", ITEM3: "DISH"}
    assert dict(result.literal_to_branch) == {
        "COMBO": COMBO,
        "DISH": ITEM3,
        "SERVICE": ITEM3,
    }
    assert dict(result.unambiguous_counts) == {COMBO: 0, ITEM3: 2}
    assert result.combo_observation_count == 0
    assert {decision.reason_code for decision in result.combo_fields.values()} == {
        "missing-observation"
    }


@pytest.mark.parametrize("mutation", ["branch", "enum"])
def test_analyzer_rejects_reviewed_discriminator_fragment_drift(mutation: str) -> None:
    schema = _effective_schema()
    if mutation == "branch":
        union = schema["components"]["schemas"]["ExternalMenuCategory3"]["properties"]["items"][
            "items"
        ]
        union["oneOf"].reverse()
    else:
        schema["components"]["schemas"][ITEM3]["properties"]["type"]["enum"] = [
            "DISH",
            "COMBO",
            "UNKNOWN",
        ]

    with pytest.raises(SafetyError, match="drift|fragment|repair"):
        analyze_menu_evidence(_pairs(_effective_schema(), [_dish()]), schema)


def test_validator_rejects_unknown_v4_literal_without_echoing_it() -> None:
    validator = MenuEvidenceValidator(_effective_schema())
    marker = "unknown-sensitive-literal"

    with pytest.raises(SafetyError, match="reviewed public literal") as caught:
        validator.reviewed_v4_item_literal(_dish(marker))

    assert marker not in str(caught.value)


def test_analyzer_rejects_conflicting_literals_for_one_branch() -> None:
    schema = _effective_schema()
    items = [_dish("DISH"), _dish("COMBO"), _combo("COMBO")]

    with pytest.raises(SafetyError, match="consistent|literal|mapping"):
        analyze_menu_evidence(_pairs(schema, items), schema)


def test_analyzer_rejects_the_same_literal_for_both_branches() -> None:
    schema = _effective_schema()

    with pytest.raises(SafetyError, match="distinct|literal|mapping"):
        analyze_menu_evidence(_pairs(schema, [_dish("DISH"), _combo("DISH")]), schema)


def test_analyzer_resolves_ambiguous_only_evidence_with_reviewed_mapping() -> None:
    schema = _ambiguous_schema()
    ambiguous = _combo(
        "COMBO",
        allergenGroupIds=["allergen"],
        itemSizes=["size"],
        modifierSchemaId="modifier",
        orderItemType="Product",
        splittable=False,
    )

    result = analyze_menu_evidence(_pairs(schema, [ambiguous]), schema)

    assert result.ambiguous_count == 1
    assert result.combo_observation_count == 1
    assert dict(result.unambiguous_counts) == {COMBO: 0, ITEM3: 0}


def test_analyzer_resolves_ambiguous_items_after_mapping_regardless_of_item_order() -> None:
    schema = _ambiguous_schema()
    ambiguous_combo = _combo(
        "COMBO",
        allergenGroupIds=["allergen"],
        itemSizes=["size"],
        modifierSchemaId="modifier",
        orderItemType="Product",
        splittable=False,
    )
    ambiguous_dish = {**ambiguous_combo, "type": "DISH"}
    items = [ambiguous_combo, _combo(), ambiguous_dish, _dish()]

    forward = analyze_menu_evidence(_pairs(schema, items), schema)
    reverse = analyze_menu_evidence(_pairs(schema, list(reversed(items))), schema)

    assert _semantic_result(forward) == _semantic_result(reverse)
    assert forward.ambiguous_count == 2
    assert forward.combo_observation_count == 2


def test_analyzer_result_is_independent_of_pair_and_item_order() -> None:
    schema = _effective_schema()
    items = [_combo(), _dish(), _combo()]
    same_pairs = _pairs(schema, items, order=(4, 3, 2))

    first = analyze_menu_evidence(same_pairs, schema)
    mapping_reordered = analyze_menu_evidence(
        {version: same_pairs[version] for version in (2, 4, 3)}, schema
    )
    items_reordered = analyze_menu_evidence(
        _pairs(schema, list(reversed(items)), order=(2, 4, 3)), schema
    )

    assert first == mapping_reordered
    assert _semantic_result(first) == _semantic_result(items_reordered)


@pytest.mark.parametrize("field", EXACT_FIVE)
@pytest.mark.parametrize(
    ("presence", "expected_action", "expected_reason"),
    [
        ("absent", "remove-required", "missing-observation"),
        ("some", "remove-required", "missing-observation"),
        ("all", "retain-required", "complete-valid-evidence"),
    ],
)
def test_analyzer_limits_combo_inference_to_exact_five_and_tracks_presence(
    field: str,
    presence: str,
    expected_action: str,
    expected_reason: str,
) -> None:
    schema = _effective_schema()
    first_value, second_value = _field_values(field)
    first = _combo()
    second = _combo()
    if presence in {"some", "all"}:
        first[field] = first_value
    if presence == "all":
        second[field] = second_value

    result = analyze_menu_evidence(_pairs(schema, [_dish(), first, second]), schema)
    decision = result.combo_fields[field]

    assert decision.required_action == expected_action
    assert decision.reason_code == expected_reason
    assert decision.observation_count == (
        2 if presence == "all" else 1 if presence == "some" else 0
    )
    sibling = schema["components"]["schemas"][ITEM3]["properties"][field]
    if expected_action == "retain-required":
        assert _plain(decision.property_schema) == sibling
    else:
        assert decision.property_schema is None


@pytest.mark.parametrize(
    ("values", "reason"),
    [
        ((None, "value"), "null-observation"),
        (([], ["value"]), "empty-observation"),
        ((["value"], [1]), "inconsistent-shape"),
    ],
)
def test_analyzer_conservatively_blocks_null_empty_or_mixed_values(
    values: tuple[Any, Any],
    reason: str,
) -> None:
    schema = _effective_schema()
    first = _combo(itemSizes=values[0])
    second = _combo(itemSizes=values[1])

    decision = analyze_menu_evidence(
        _pairs(schema, [_dish(), first, second]), schema
    ).combo_fields["itemSizes"]

    assert decision.required_action == "remove-required"
    assert decision.reason_code == reason
    assert decision.property_schema is None


def test_analyzer_requires_two_observations_for_a_constrained_sibling_schema() -> None:
    schema = _effective_schema()
    combo = _combo(orderItemType="Product")

    decision = analyze_menu_evidence(_pairs(schema, [_dish(), combo]), schema).combo_fields[
        "orderItemType"
    ]

    assert decision.required_action == "remove-required"
    assert decision.reason_code == "insufficient-constrained-observations"
    assert decision.property_schema is None


def test_analyzer_copies_the_exact_constrained_sibling_schema_after_two_observations() -> None:
    schema = _effective_schema()
    items = [_dish(), _combo(orderItemType="Product"), _combo(orderItemType="Compound")]

    decision = analyze_menu_evidence(_pairs(schema, items), schema).combo_fields["orderItemType"]

    assert decision.required_action == "retain-required"
    assert decision.reason_code == "complete-valid-evidence"
    assert _plain(decision.property_schema) == {
        "description": "Product or compound",
        "enum": ["Product", "Compound"],
        "format": "enum",
        "type": "string",
    }
    assert decision.property_schema is not None
    assert isinstance(decision.property_schema["enum"], tuple)


def test_analyzer_rejects_a_value_invalid_for_the_sibling_schema_without_echoing_it() -> None:
    schema = _effective_schema()
    marker = "must-not-appear-in-errors"

    with pytest.raises(SafetyError, match="sibling schema") as caught:
        analyze_menu_evidence(_pairs(schema, [_dish(), _combo(splittable=marker)]), schema)

    assert marker not in str(caught.value)


def test_analyzer_revalidation_rejects_a_sixth_unknown_combo_property() -> None:
    schema = _effective_schema()

    with pytest.raises(SafetyError, match="undefined property|reviewed schema branch"):
        analyze_menu_evidence(_pairs(schema, [_dish(), _combo(sixthUnknown="value")]), schema)


def test_analyzer_outputs_are_deeply_immutable() -> None:
    schema = _effective_schema()
    result = analyze_menu_evidence(
        _pairs(
            schema,
            [_dish(), _combo(orderItemType="Product"), _combo(orderItemType="Compound")],
        ),
        schema,
    )

    assert isinstance(result.provenance, MappingProxyType)
    assert isinstance(result.branch_to_literal, MappingProxyType)
    assert isinstance(result.literal_to_branch, MappingProxyType)
    assert isinstance(result.unambiguous_counts, MappingProxyType)
    assert isinstance(result.combo_fields, MappingProxyType)
    assert isinstance(result.combo_fields["orderItemType"].property_schema, MappingProxyType)
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.ambiguous_count = 99  # type: ignore[misc]
    with pytest.raises(TypeError):
        result.branch_to_literal[ITEM3] = "COMBO"  # type: ignore[index]
    with pytest.raises(TypeError):
        result.combo_fields["orderItemType"].property_schema["type"] = "number"  # type: ignore[index]


def test_public_reader_contract_revalidator_accepts_a_valid_frozen_pair() -> None:
    schema = _effective_schema()
    pair = _pairs(schema, [_dish(), _combo()])[4]

    version = promotion_module.revalidate_evidence_pair_contract(
        pair.request,
        pair.response,
    )

    assert version == 4
    assert isinstance(pair.request, MappingProxyType)
    assert isinstance(pair.request["metadata"], MappingProxyType)


def test_analyzer_rejects_request_version_mismatch_with_fresh_valid_hashes() -> None:
    schema = _effective_schema()
    pairs = dict(_pairs(schema, [_dish(), _combo()]))
    request = _plain(pairs[2].request)
    request["body"]["version"] = 3
    pairs[2] = _replace_pair(pairs[2], request=request)

    with pytest.raises(SafetyError, match="version|contract"):
        analyze_menu_evidence(pairs, schema)


def test_concrete_validator_binds_request_version_to_selected_version() -> None:
    schema = _effective_schema()
    pair = _pairs(schema, [_dish(), _combo()])[2]
    request = _plain(pair.request)
    response = _plain(pair.response)
    request["body"]["version"] = 3

    with pytest.raises(SafetyError, match="request.*version|selected.*version"):
        MenuEvidenceValidator(schema).validate(2, request, response)


def test_analyzer_rejects_extra_envelope_field_with_fresh_valid_hash() -> None:
    schema = _effective_schema()
    pairs = dict(_pairs(schema, [_dish(), _combo()]))
    response = _plain(pairs[3].response)
    response["extra"] = "<redacted:string>"
    pairs[3] = _replace_pair(pairs[3], response=response)

    with pytest.raises(SafetyError, match="envelope|contract|metadata"):
        analyze_menu_evidence(pairs, schema)


@pytest.mark.parametrize(
    "mutation",
    ["wrong-path", "different-run-id", "duration-type-mismatch"],
)
def test_analyzer_rejects_wrong_or_type_different_metadata_with_fresh_hashes(
    mutation: str,
) -> None:
    schema = _effective_schema()
    pairs = dict(_pairs(schema, [_dish(), _combo()]))
    request = _plain(pairs[3].request)
    response = _plain(pairs[3].response)
    if mutation == "wrong-path":
        request["metadata"]["path"] = "/api/2/menu/other"
        response["metadata"]["path"] = "/api/2/menu/other"
    elif mutation == "different-run-id":
        response["metadata"]["runId"] = "synthetic-other"
    else:
        request["metadata"]["duration"] = 1
        response["metadata"]["duration"] = 1.0
    pairs[3] = _replace_pair(pairs[3], request=request, response=response)

    with pytest.raises(SafetyError, match="metadata|runId|contract"):
        analyze_menu_evidence(pairs, schema)


def test_analyzer_generic_scan_rejects_unsafe_metadata_without_echoing_it() -> None:
    schema = _effective_schema()
    pairs = dict(_pairs(schema, [_dish(), _combo()]))
    request = _plain(pairs[4].request)
    response = _plain(pairs[4].response)
    marker = "Bearer synthetic-sensitive-marker"
    request["metadata"]["headers"] = {"x-correlation-id": marker}
    response["metadata"]["headers"] = {"x-correlation-id": marker}
    pairs[4] = _replace_pair(pairs[4], request=request, response=response)

    with pytest.raises(SafetyError, match="secret/PII|contract") as caught:
        analyze_menu_evidence(pairs, schema)

    assert marker not in str(caught.value)


def test_analyzer_rejects_tampered_pair_provenance() -> None:
    schema = _effective_schema()
    pairs = dict(_pairs(schema, [_dish(), _combo()]))
    original = pairs[3]
    pairs[3] = EvidencePair(
        version=3,
        request=original.request,
        response=original.response,
        request_sha256="0" * 64,
        response_sha256=original.response_sha256,
    )

    with pytest.raises(SafetyError, match="provenance|hash"):
        analyze_menu_evidence(pairs, schema)


def test_analyzer_rejects_reviewed_schema_fragment_drift() -> None:
    schema = _effective_schema()
    pairs = _pairs(schema, [_dish(), _combo()])
    schema["components"]["schemas"][COMBO]["properties"]["description"]["default"] = None

    with pytest.raises(SafetyError, match="drift|fragment"):
        analyze_menu_evidence(pairs, schema)


@pytest.mark.skipif(
    not Path("build/upstream/candidate.json").is_file(),
    reason="ignored reviewed bootstrap candidate is absent in a clean checkout",
)
def test_analyzer_smoke_uses_the_locally_composed_reviewed_schema_without_fetch() -> None:
    schema, _mappings = compose_reviewed_bootstrap_candidate(RepoPaths.discover())
    components = schema["components"]["schemas"]
    request_schema = components["iikoTransport.PublicApi.Contracts.Nomenclature.MenuRequest"]
    pairs: dict[int, EvidencePair] = {}
    for version in (2, 3, 4):
        request_body = _minimal_schema_value(schema, request_schema)
        response_body = _minimal_schema_value(schema, components[f"ExternalMenuV{version}"])
        assert isinstance(request_body, dict)
        assert isinstance(response_body, dict)
        request_body["externalMenuId"] = "40000000-0000-4000-8000-000000000004"
        request_body["organizationIds"] = ["50000000-0000-4000-8000-000000000005"]
        request_body["version"] = version
        response_body["formatVersion"] = version
        if version == 4:
            category = _minimal_schema_value(schema, components["ExternalMenuCategory3"])
            dish = _minimal_schema_value(schema, components[ITEM3])
            combo = _minimal_schema_value(schema, components[COMBO])
            assert isinstance(category, dict)
            assert isinstance(dish, dict)
            assert isinstance(combo, dict)
            dish["type"] = "DISH"
            combo["type"] = "COMBO"
            category["items"] = [dish, combo]
            response_body["itemGroups"] = [category]
        pairs[version] = _pair_from_bodies(
            schema,
            version,
            request_body,
            response_body,
        )

    result = analyze_menu_evidence(pairs, schema)

    assert dict(result.branch_to_literal) == {COMBO: "COMBO", ITEM3: "DISH"}
    assert result.total_item_count == 2
