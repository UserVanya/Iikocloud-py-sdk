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

import tools.openapi_pipeline.evidence_candidates as candidate_module
import tools.openapi_pipeline.evidence_promotion as promotion_module
from tools.openapi_pipeline.errors import SafetyError, StaleOverlayError
from tools.openapi_pipeline.evidence_analysis import MenuEvidenceAnalysis, analyze_menu_evidence
from tools.openapi_pipeline.evidence_candidates import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    EVIDENCE_OPERATION_ID,
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
SENSITIVE_MARKER = "synthetic-sensitive-marker"


class _RaisingMapping(Mapping[Any, Any]):
    def __iter__(self) -> Iterator[Any]:
        raise RuntimeError(SENSITIVE_MARKER)

    def __getitem__(self, key: Any) -> Any:
        raise RuntimeError(SENSITIVE_MARKER)

    def __len__(self) -> int:
        raise RuntimeError(SENSITIVE_MARKER)


class _RaisingDict(dict[str, Any]):
    def __iter__(self) -> Iterator[str]:
        raise RuntimeError(SENSITIVE_MARKER)

    def items(self) -> Any:
        raise RuntimeError(SENSITIVE_MARKER)


def _assert_sanitized_error(error: SafetyError, message: str) -> None:
    assert str(error) == message
    assert SENSITIVE_MARKER not in str(error)
    assert SENSITIVE_MARKER not in repr(error)
    assert error.__cause__ is None
    assert error.__context__ is None


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


def test_bundle_binds_payloads_to_schema_analysis_and_exact_provenance() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    analysis = analyze_menu_evidence(pairs, schema)

    bundle = build_evidence_candidate_bundle(
        analysis=analysis,
        pairs=pairs,
        effective_schema=schema,
    )

    assert bundle.operation_id == EVIDENCE_OPERATION_ID == "get_external_menu_by_id"
    assert bundle.effective_schema_sha256 == sha256_bytes(canonical_json_bytes(schema))
    assert bundle.evidence_analysis_sha256 == sha256_bytes(
        candidate_module._analysis_bytes(analysis)
    )
    assert tuple(bundle.evidence_provenance) == (2, 3, 4)
    assert {
        version: (
            provenance.request_sha256,
            provenance.response_sha256,
        )
        for version, provenance in bundle.evidence_provenance.items()
    } == {
        version: (pair.request_sha256, pair.response_sha256)
        for version, pair in sorted(pairs.items())
    }
    assert bundle.evidence_provenance is not analysis.provenance
    assert EVIDENCE_CANDIDATE_PAYLOAD_PATHS == (
        "openapi/overlays/operations.overlay.yaml",
        "openapi/overlays/polymorphism.overlay.yaml",
        "tests/fixtures/contracts/external-menu-v2.json",
        "tests/fixtures/contracts/external-menu-v3.json",
        "tests/fixtures/contracts/external-menu-v4.json",
    )
    assert tuple(bundle.canonical_bytes) == EVIDENCE_CANDIDATE_PAYLOAD_PATHS


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
    with pytest.raises(TypeError):
        bundle.evidence_provenance[2] = bundle.evidence_provenance[3]  # type: ignore[index]
    with pytest.raises(dataclasses.FrozenInstanceError):
        bundle.operation_id = "changed"  # type: ignore[misc]
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


@pytest.mark.parametrize("field", ["provenance", "branch_to_literal"])
def test_builder_sanitizes_nested_analysis_mapping_failures_without_mutation(
    field: str,
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    poisoned = (
        dataclasses.replace(analysis, provenance=_RaisingMapping())
        if field == "provenance"
        else dataclasses.replace(analysis, branch_to_literal=_RaisingMapping())
    )
    before_schema = canonical_json_bytes(schema)

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=poisoned,
            pairs=pairs,
            effective_schema=schema,
        )

    _assert_sanitized_error(
        caught.value,
        "Evidence candidate analysis cannot be canonicalized",
    )
    assert canonical_json_bytes(schema) == before_schema
    assert list(tmp_path.iterdir()) == []


def test_builder_sanitizes_top_level_pair_mapping_failure_without_mutation(
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    before_schema = canonical_json_bytes(schema)

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=_RaisingMapping(),
            effective_schema=schema,
        )

    _assert_sanitized_error(caught.value, "Evidence candidate pair mapping is invalid")
    assert canonical_json_bytes(schema) == before_schema
    assert list(tmp_path.iterdir()) == []


def test_builder_sanitizes_nested_exact_pair_failure_without_mutation(
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = dict(_pairs(schema, _retained_items()))
    analysis = analyze_menu_evidence(pairs, schema)
    poisoned = pairs[2]
    object.__setattr__(poisoned, "request", _RaisingMapping())
    before_schema = canonical_json_bytes(schema)

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=schema,
        )

    _assert_sanitized_error(
        caught.value,
        "Evidence candidate pair cannot be safely snapshotted",
    )
    assert canonical_json_bytes(schema) == before_schema
    assert list(tmp_path.iterdir()) == []


def test_builder_sanitizes_effective_schema_traversal_failure_without_mutation(
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    poisoned = dict(schema)
    poisoned["components"] = _RaisingDict(schema["components"])
    before_hashes = tuple((pair.request_sha256, pair.response_sha256) for pair in pairs.values())

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=poisoned,
        )

    _assert_sanitized_error(
        caught.value,
        "Evidence candidate schema is not strict canonical JSON",
    )
    assert (
        tuple((pair.request_sha256, pair.response_sha256) for pair in pairs.values())
        == before_hashes
    )
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("exception_type", [KeyboardInterrupt, SystemExit])
def test_builder_does_not_swallow_pair_mapping_base_exceptions(
    exception_type: type[BaseException],
) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)

    class RaisingBaseMapping(_RaisingMapping):
        def __iter__(self) -> Iterator[Any]:
            raise exception_type(SENSITIVE_MARKER)

    with pytest.raises(exception_type):
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=RaisingBaseMapping(),
            effective_schema=schema,
        )


def test_builder_preserves_intentional_safety_error_identity() -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    intentional = SafetyError("intentional caller safety failure")

    class RaisingSafetyMapping(_RaisingMapping):
        def __iter__(self) -> Iterator[Any]:
            raise intentional

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=RaisingSafetyMapping(),
            effective_schema=schema,
        )

    assert caught.value is intentional


def test_builder_sanitizes_poisoned_exact_pair_version_without_comparing_it(
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = dict(_pairs(schema, _retained_items()))
    analysis = analyze_menu_evidence(pairs, schema)

    class PoisonedVersion:
        def __ne__(self, other: Any) -> bool:
            raise RuntimeError(SENSITIVE_MARKER)

    object.__setattr__(pairs[2], "version", PoisonedVersion())

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=schema,
        )

    _assert_sanitized_error(
        caught.value,
        "Evidence candidate pair version is inconsistent",
    )
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize(
    "trusted_boundary",
    ["canonical-json", "json-loads", "analysis-thaw", "pair-freeze"],
)
def test_builder_propagates_trusted_internal_runtime_errors_unchanged(
    trusted_boundary: str,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items())
    analysis = analyze_menu_evidence(pairs, schema)
    sentinel = RuntimeError(f"{SENSITIVE_MARKER}-{trusted_boundary}")

    def fail(*args: Any, **kwargs: Any) -> Any:
        raise sentinel

    if trusted_boundary == "canonical-json":
        monkeypatch.setattr(candidate_module, "canonical_json_bytes", fail)
    elif trusted_boundary == "json-loads":
        monkeypatch.setattr(candidate_module.json, "loads", fail)
    elif trusted_boundary == "analysis-thaw":
        monkeypatch.setattr(candidate_module, "_thaw_json", fail)
    else:
        monkeypatch.setattr(promotion_module, "_freeze_mapping", fail)

    with pytest.raises(RuntimeError) as caught:
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=schema,
        )

    assert caught.value is sentinel
    assert SENSITIVE_MARKER in str(caught.value)
    assert list(tmp_path.iterdir()) == []


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
