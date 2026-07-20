from __future__ import annotations

import dataclasses
import json
from collections.abc import Iterator, Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest
import yaml
from test_evidence_analysis import (
    _combo,
    _dish,
    _minimal_schema_value,
    _pair_from_bodies,
    _pairs,
    _plain,
    _sanitized_pair,
)
from test_evidence_promotion_reader import _effective_schema

from tools.openapi_pipeline.errors import SafetyError, StaleOverlayError
from tools.openapi_pipeline.evidence_analysis import MenuEvidenceAnalysis, analyze_menu_evidence
from tools.openapi_pipeline.evidence_candidates import (
    OPERATIONS_OVERLAY_PATH,
    POLYMORPHISM_OVERLAY_PATH,
    EvidenceCandidateBundle,
    build_evidence_candidate_bundle,
)
from tools.openapi_pipeline.evidence_promotion import EvidencePair
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.overlay import apply_overlay
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_reviewed_bootstrap_candidate

ITEM3 = "ExternalMenuItem3"
COMBO = "ExternalMenuComboItem"
EXACT_FIVE = (
    "allergenGroupIds",
    "itemSizes",
    "modifierSchemaId",
    "orderItemType",
    "splittable",
)


def _reviewed_schema() -> dict[str, Any]:
    schema = _effective_schema()
    schema["servers"] = [{"url": "https://api-ru.iiko.services"}]
    schema["components"]["securitySchemes"] = {"BearerAuth": {"type": "http", "scheme": "bearer"}}
    schema["paths"]["/api/2/menu/by_id"]["post"]["security"] = [{"BearerAuth": []}]
    return schema


def _retained_items() -> list[dict[str, Any]]:
    first = _combo(
        allergenGroupIds=["allergen-a"],
        itemSizes=["size-a"],
        modifierSchemaId="modifier-a",
        orderItemType="Product",
        splittable=False,
    )
    second = _combo(
        allergenGroupIds=["allergen-b"],
        itemSizes=["size-b"],
        modifierSchemaId="modifier-b",
        orderItemType="Compound",
        splittable=True,
    )
    return [_dish(), first, second]


def _mutable(value: Any) -> Any:
    return _plain(value)


def test_builder_returns_in_memory_guarded_overlays_and_minimal_fixtures() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    analysis = analyze_menu_evidence(pairs, schema)

    bundle = build_evidence_candidate_bundle(
        analysis=analysis,
        pairs=pairs,
        effective_schema=schema,
    )

    assert isinstance(bundle, EvidenceCandidateBundle)
    assert bundle.operations_overlay["overlay"] == "1.1.0"
    assert bundle.polymorphism_overlay["overlay"] == "1.1.0"
    for overlay in (bundle.operations_overlay, bundle.polymorphism_overlay):
        assert overlay["info"]["title"]
        assert overlay["info"]["version"]
        assert all(
            action["x-iiko-sdk-guard"]["expected-matches"] == 1 for action in overlay["actions"]
        )

    with_operations = apply_overlay(schema, _mutable(bundle.operations_overlay))
    patched = apply_overlay(with_operations, _mutable(bundle.polymorphism_overlay))
    response_schema = patched["paths"]["/api/2/menu/by_id"]["post"]["responses"]["200"]["content"][
        "application/json"
    ]["schema"]
    assert response_schema["title"] == "ExternalMenuResponse"

    components = patched["components"]["schemas"]
    for version in (2, 3, 4):
        component = components[f"ExternalMenuV{version}"]
        assert component["properties"]["formatVersion"]["enum"] == [version]
        assert component["properties"]["formatVersion"]["default"] == version
        assert component["required"].count("formatVersion") == 1

    union = components["ExternalMenuCategory3"]["properties"]["items"]["items"]
    assert union["discriminator"] == {
        "propertyName": "type",
        "mapping": {
            "COMBO": "#/components/schemas/ExternalMenuComboItem",
            "DISH": "#/components/schemas/ExternalMenuItem3",
        },
    }
    assert components[ITEM3]["properties"]["type"]["enum"] == ["DISH"]
    assert components[ITEM3]["properties"]["type"]["default"] == "DISH"
    assert components[ITEM3]["required"].count("type") == 1
    assert components[COMBO]["properties"]["type"]["enum"] == ["COMBO"]
    assert components[COMBO]["properties"]["type"]["default"] == "COMBO"

    combo = components[COMBO]
    assert combo["required"] == [
        "sizes",
        "itemSizes",
        "modifierSchemaId",
        "type",
        "orderItemType",
        "allergenGroupIds",
        "id",
        "splittable",
    ]
    for field in EXACT_FIVE:
        assert combo["properties"][field] == components[ITEM3]["properties"][field]

    assert tuple(bundle.fixtures) == (2, 3, 4)
    assert bundle.fixtures[2]["formatVersion"] == 2
    assert bundle.fixtures[3]["formatVersion"] == 3
    v4_items = bundle.fixtures[4]["itemGroups"][0]["items"]
    assert [item["type"] for item in v4_items] == ["DISH", "COMBO"]
    retained_combo = v4_items[1]
    assert all(retained_combo[field] not in ([], {}) for field in EXACT_FIVE)

    expected_paths = {
        OPERATIONS_OVERLAY_PATH,
        POLYMORPHISM_OVERLAY_PATH,
        "tests/fixtures/contracts/external-menu-v2.json",
        "tests/fixtures/contracts/external-menu-v3.json",
        "tests/fixtures/contracts/external-menu-v4.json",
    }
    assert set(bundle.canonical_bytes) == expected_paths
    assert set(bundle.sha256) == expected_paths
    assert all(type(body) is bytes and body for body in bundle.canonical_bytes.values())
    assert all(len(digest) == 64 for digest in bundle.sha256.values())


def test_builder_supports_inverse_mapping_and_all_remove_decisions() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, [_dish("COMBO"), _combo("DISH")])

    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )

    patched = apply_overlay(schema, _mutable(bundle.operations_overlay))
    patched = apply_overlay(patched, _mutable(bundle.polymorphism_overlay))
    components = patched["components"]["schemas"]
    mapping = components["ExternalMenuCategory3"]["properties"]["items"]["items"]["discriminator"][
        "mapping"
    ]
    assert mapping == {
        "COMBO": "#/components/schemas/ExternalMenuItem3",
        "DISH": "#/components/schemas/ExternalMenuComboItem",
    }
    assert [item["type"] for item in bundle.fixtures[4]["itemGroups"][0]["items"]] == [
        "COMBO",
        "DISH",
    ]
    combo = components[COMBO]
    assert combo["required"] == ["sizes", "type", "id"]
    assert set(combo["properties"]).isdisjoint(EXACT_FIVE)
    assert set(bundle.fixtures[4]["itemGroups"][0]["items"][1]).isdisjoint(EXACT_FIVE)


def test_builder_replaces_existing_lists_without_duplicates() -> None:
    schema = _reviewed_schema()
    for version in (2, 3, 4):
        component = schema["components"]["schemas"][f"ExternalMenuV{version}"]
        component["properties"]["formatVersion"]["enum"] = [version]
        component["required"].append("formatVersion")
    pairs = _pairs(schema, _retained_items())

    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )

    patched = apply_overlay(schema, _mutable(bundle.operations_overlay))
    patched = apply_overlay(patched, _mutable(bundle.polymorphism_overlay))
    for version in (2, 3, 4):
        component = patched["components"]["schemas"][f"ExternalMenuV{version}"]
        assert component["properties"]["formatVersion"]["enum"] == [version]
        assert component["required"].count("formatVersion") == 1
    assert len(patched["components"]["schemas"][ITEM3]["required"]) == len(
        set(patched["components"]["schemas"][ITEM3]["required"])
    )
    assert len(patched["components"]["schemas"][COMBO]["required"]) == len(
        set(patched["components"]["schemas"][COMBO]["required"])
    )


def test_bundle_bytes_hashes_and_semantics_are_deterministic_across_orders() -> None:
    schema = _reviewed_schema()
    forward_pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    reverse_pairs = _pairs(schema, list(reversed(_retained_items())), order=(3, 4, 2))
    forward_analysis = analyze_menu_evidence(forward_pairs, schema)
    reverse_analysis = analyze_menu_evidence(reverse_pairs, schema)
    reordered_analysis = MenuEvidenceAnalysis(
        provenance=MappingProxyType(dict(reversed(tuple(forward_analysis.provenance.items())))),
        branch_to_literal=MappingProxyType(
            dict(reversed(tuple(forward_analysis.branch_to_literal.items())))
        ),
        literal_to_branch=MappingProxyType(
            dict(reversed(tuple(forward_analysis.literal_to_branch.items())))
        ),
        unambiguous_counts=MappingProxyType(
            dict(reversed(tuple(forward_analysis.unambiguous_counts.items())))
        ),
        ambiguous_count=forward_analysis.ambiguous_count,
        total_item_count=forward_analysis.total_item_count,
        combo_observation_count=forward_analysis.combo_observation_count,
        combo_fields=MappingProxyType(
            dict(reversed(tuple(forward_analysis.combo_fields.items())))
        ),
    )

    forward = build_evidence_candidate_bundle(
        analysis=forward_analysis,
        pairs=forward_pairs,
        effective_schema=schema,
    )
    reordered = build_evidence_candidate_bundle(
        analysis=reordered_analysis,
        pairs=forward_pairs,
        effective_schema=schema,
    )
    reversed_items = build_evidence_candidate_bundle(
        analysis=reverse_analysis,
        pairs=reverse_pairs,
        effective_schema=schema,
    )

    assert dict(forward.canonical_bytes) == dict(reordered.canonical_bytes)
    assert dict(forward.canonical_bytes) == dict(reversed_items.canonical_bytes)
    assert dict(forward.sha256) == dict(reordered.sha256) == dict(reversed_items.sha256)
    for path, body in forward.canonical_bytes.items():
        assert forward.sha256[path] == sha256_bytes(body)
        if path.endswith(".json"):
            version = int(path.removesuffix(".json").rsplit("v", 1)[1])
            assert json.loads(body) == _mutable(forward.fixtures[version])
            assert body == canonical_json_bytes(json.loads(body))
        else:
            parsed = yaml.safe_load(body)
            expected = (
                forward.operations_overlay
                if path == OPERATIONS_OVERLAY_PATH
                else forward.polymorphism_overlay
            )
            assert parsed == _mutable(expected)


def test_bundle_is_deeply_immutable() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )

    with pytest.raises(TypeError):
        bundle.operations_overlay["overlay"] = "changed"  # type: ignore[index]
    with pytest.raises(TypeError):
        bundle.operations_overlay["actions"][0]["target"] = "changed"
    with pytest.raises(TypeError):
        bundle.fixtures[4]["formatVersion"] = 9  # type: ignore[index]
    with pytest.raises(TypeError):
        bundle.canonical_bytes[OPERATIONS_OVERLAY_PATH] = b"changed"  # type: ignore[index]
    with pytest.raises(dataclasses.FrozenInstanceError):
        bundle.sha256 = MappingProxyType({})  # type: ignore[misc]


def test_generated_overlay_guards_fail_on_drift_and_reapplication() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )
    operations = _mutable(bundle.operations_overlay)
    polymorphism = _mutable(bundle.polymorphism_overlay)
    drifted = _mutable(schema)
    drifted["paths"]["/api/2/menu/by_id"]["post"]["responses"]["200"]["content"][
        "application/json"
    ]["schema"]["description"] = "drift"

    with pytest.raises(StaleOverlayError, match="external-menu-response-title"):
        apply_overlay(drifted, operations)
    with_operations = apply_overlay(schema, operations)
    with pytest.raises(StaleOverlayError):
        apply_overlay(with_operations, operations)
    patched = apply_overlay(with_operations, polymorphism)
    with pytest.raises(StaleOverlayError):
        apply_overlay(patched, polymorphism)


def test_builder_rejects_forged_analysis() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    forged = dataclasses.replace(analysis, total_item_count=analysis.total_item_count + 1)

    with pytest.raises(SafetyError, match="forged|stale|mismatched"):
        build_evidence_candidate_bundle(
            analysis=forged,
            pairs=pairs,
            effective_schema=schema,
        )


def test_builder_snapshots_pair_mapping_before_revalidation_and_scanning() -> None:
    schema = _reviewed_schema()
    pairs = dict(_pairs(schema, _retained_items()))
    analysis = analyze_menu_evidence(pairs, schema)

    class SingleReadPairs(Mapping[int, EvidencePair]):
        def __init__(self, values: dict[int, EvidencePair]) -> None:
            self._values = values
            self._read: set[int] = set()

        def __getitem__(self, key: int) -> EvidencePair:
            if key in self._read:
                raise RuntimeError("pair mapping was read more than once")
            self._read.add(key)
            return self._values[key]

        def __iter__(self) -> Iterator[int]:
            return iter(self._values)

        def __len__(self) -> int:
            return len(self._values)

    bundle = build_evidence_candidate_bundle(
        analysis=analysis,
        pairs=SingleReadPairs(pairs),
        effective_schema=schema,
    )

    assert len(bundle.canonical_bytes) == 5


def test_builder_rejects_a_secret_named_required_fixture_field() -> None:
    schema = _reviewed_schema()
    v2 = schema["components"]["schemas"]["ExternalMenuV2"]
    v2["properties"]["password"] = {"type": "string"}
    v2["required"].append("password")
    pairs = {
        2: _sanitized_pair(schema, 2, response_change=("password", "private-value")),
        3: _sanitized_pair(schema, 3),
        4: _sanitized_pair(schema, 4, items=[_dish(), _combo()]),
    }
    analysis = analyze_menu_evidence(pairs, schema)

    with pytest.raises(SafetyError, match="secret|PII|scan"):
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=schema,
        )


def test_builder_rejects_unsupported_and_cyclic_synthesis_contracts() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    unsupported = _mutable(schema)
    unsupported["components"]["schemas"]["ExternalMenuV2"]["properties"]["extra"] = {
        "pattern": ".*",
        "type": "string",
    }
    cyclic = _mutable(schema)
    cyclic["components"]["schemas"]["ExternalMenuV2"]["properties"]["cycle"] = {
        "$ref": "#/components/schemas/ExternalMenuV2"
    }

    with pytest.raises(SafetyError, match="unsupported"):
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=unsupported,
        )
    with pytest.raises(SafetyError, match="cycle|cyclic"):
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=cyclic,
        )


def test_fixtures_never_copy_capture_redactions_ids_or_schema_example_defaults() -> None:
    schema = _reviewed_schema()
    root = schema["components"]["schemas"]["ExternalMenuV2"]
    root["properties"]["name"]["default"] = "private-default-value"
    root["properties"]["name"]["example"] = "private-example-value"
    root["required"].append("name")
    pairs = {
        2: _sanitized_pair(schema, 2, response_change=("name", "private-observation")),
        3: _sanitized_pair(schema, 3),
        4: _sanitized_pair(schema, 4, items=_retained_items()),
    }

    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )

    joined = b"\n".join(bundle.canonical_bytes.values())
    assert b"<redacted:" not in joined
    assert b"00000000-0000-4000-8000-" not in joined
    assert b"private-default-value" not in joined
    assert b"private-example-value" not in joined
    assert b"private-observation" not in joined
    assert bundle.fixtures[2]["name"] == "synthetic-value"


@pytest.mark.skipif(
    not Path("build/upstream/candidate.json").is_file(),
    reason="ignored reviewed bootstrap candidate is absent in a clean checkout",
)
def test_builder_smoke_uses_public_locally_composed_candidate_without_fetch() -> None:
    schema, _mappings = compose_reviewed_bootstrap_candidate(RepoPaths.discover())
    components = schema["components"]["schemas"]
    request_schema = components["iikoTransport.PublicApi.Contracts.Nomenclature.MenuRequest"]
    pairs = {}
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
    analysis = analyze_menu_evidence(pairs, schema)

    bundle = build_evidence_candidate_bundle(
        analysis=analysis,
        pairs=pairs,
        effective_schema=schema,
    )

    assert len(bundle.canonical_bytes) == 5
    assert bundle.fixtures[4]["formatVersion"] == 4
