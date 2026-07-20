from __future__ import annotations

import copy
import os
from pathlib import Path
from typing import Any

import pytest
import yaml

import tools.openapi_pipeline.pipeline as pipeline_module
from tools.openapi_pipeline.capture import RedactionHints
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.normalization import build_types_overlay
from tools.openapi_pipeline.overlay import apply_overlay
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_reviewed_bootstrap_candidate


def _guarded_root_update(document: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
    return {
        "overlay": "1.1.0",
        "info": {"title": "synthetic", "version": "1"},
        "actions": [
            {
                "target": "$",
                "update": update,
                "x-iiko-sdk-guard": {
                    "issue": "synthetic-stage",
                    "expected-matches": 1,
                    "expected-sha256": sha256_bytes(canonical_json_bytes(document)),
                },
            }
        ],
    }


def _raw_document() -> dict[str, Any]:
    return {
        "openapi": "3.0.3",
        "info": {"title": "synthetic", "version": "1"},
        "paths": {
            "/api/2/menu/by_id": {
                "post": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Raw.Bool"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {"schemas": {"Raw.Bool": {"type": "bool"}}},
    }


def _write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=True), encoding="utf-8")


def _reviewed_repo(root: Path, *, raw_document: dict[str, Any] | None = None) -> RepoPaths:
    (root / "pyproject.toml").write_text("[project]\nname='synthetic'\n", encoding="utf-8")
    raw = copy.deepcopy(raw_document) if raw_document is not None else _raw_document()
    candidate = root / "build/upstream/candidate.json"
    candidate.parent.mkdir(parents=True)
    candidate.write_bytes(canonical_json_bytes(raw))

    contracts = _guarded_root_update(raw, {"x-stage-contracts": True})
    after_contracts = apply_overlay(raw, contracts)
    types = build_types_overlay(raw)
    after_types = apply_overlay(after_contracts, types)
    semantic = _guarded_root_update(after_types, {"x-stage-semantic": True})
    _write_yaml(root / "openapi/overlays/contracts.overlay.yaml", contracts)
    _write_yaml(root / "openapi/overlays/operations.overlay.yaml", semantic)
    _write_yaml(root / "build/bootstrap/types.overlay.yaml", types)
    _write_yaml(
        root / "build/bootstrap/operation-ids.yaml",
        {"operations": {"POST /api/2/menu/by_id": "menu_by_id"}},
    )
    _write_yaml(root / "build/bootstrap/model-collisions.yaml", {"collisions": {}})
    _write_yaml(root / "openapi/model-name-overrides.yaml", {"models": {}})
    return RepoPaths(root)


def _reviewed_repo_with_all_semantic_overlays(root: Path) -> RepoPaths:
    paths = _reviewed_repo(root)
    raw = _raw_document()
    contracts = yaml.safe_load(
        (root / "openapi/overlays/contracts.overlay.yaml").read_text(encoding="utf-8")
    )
    after_contracts = apply_overlay(raw, contracts)
    types = yaml.safe_load(
        (root / "build/bootstrap/types.overlay.yaml").read_text(encoding="utf-8")
    )
    after_types = apply_overlay(after_contracts, types)
    extra = {
        "overlay": "1.1.0",
        "info": {"title": "synthetic", "version": "1"},
        "actions": [
            {
                "target": "$.info",
                "update": {"x-other-reviewed": True},
                "x-iiko-sdk-guard": {
                    "issue": "synthetic-other-overlay",
                    "expected-matches": 1,
                    "expected-sha256": sha256_bytes(canonical_json_bytes(after_types["info"])),
                },
            }
        ],
    }
    after_extra = apply_overlay(after_types, extra)
    operations = _guarded_root_update(
        after_extra,
        {"x-evidence-operations": True},
    )
    after_operations = apply_overlay(after_extra, operations)
    polymorphism = _guarded_root_update(
        after_operations,
        {"x-evidence-polymorphism": True},
    )
    _write_yaml(root / "openapi/overlays/operations-extra.overlay.yaml", extra)
    _write_yaml(root / "openapi/overlays/operations.overlay.yaml", operations)
    _write_yaml(root / "openapi/overlays/polymorphism.overlay.yaml", polymorphism)
    return paths


def test_reviewed_evidence_base_excludes_exactly_two_evidence_owned_overlays(
    tmp_path: Path,
) -> None:
    paths = _reviewed_repo_with_all_semantic_overlays(tmp_path)
    composer = getattr(pipeline_module, "compose_reviewed_evidence_base_candidate", None)
    assert callable(composer)

    effective, mappings = composer(paths)
    bootstrap, bootstrap_mappings = compose_reviewed_bootstrap_candidate(paths)

    assert effective["x-stage-contracts"] is True
    assert effective["info"]["x-other-reviewed"] is True
    assert "x-evidence-operations" not in effective
    assert "x-evidence-polymorphism" not in effective
    assert effective["components"]["schemas"]["Raw.Bool"]["type"] == "boolean"
    assert effective["paths"]["/api/2/menu/by_id"]["post"]["operationId"] == "menu_by_id"
    assert mappings == {"Raw.Bool": "Bool"}
    assert bootstrap["x-evidence-operations"] is True
    assert bootstrap["x-evidence-polymorphism"] is True
    assert bootstrap["info"]["x-other-reviewed"] is True
    assert bootstrap_mappings == mappings


def test_reviewed_evidence_base_is_identical_before_and_after_evidence_accept(
    tmp_path: Path,
) -> None:
    paths = _reviewed_repo_with_all_semantic_overlays(tmp_path)
    overlay_root = paths.root / "openapi/overlays"
    candidate_root = paths.build / "evidence-candidates/openapi/overlays"
    candidate_root.mkdir(parents=True)
    evidence_names = ("operations.overlay.yaml", "polymorphism.overlay.yaml")
    for name in evidence_names:
        (overlay_root / name).replace(candidate_root / name)

    before_accept, before_mappings = pipeline_module.compose_reviewed_evidence_base_candidate(
        paths
    )
    bootstrap_before, _ = compose_reviewed_bootstrap_candidate(paths)
    assert "x-evidence-operations" not in bootstrap_before
    assert "x-evidence-polymorphism" not in bootstrap_before

    for name in evidence_names:
        (candidate_root / name).replace(overlay_root / name)
    after_accept, after_mappings = pipeline_module.compose_reviewed_evidence_base_candidate(paths)
    bootstrap_after, _ = compose_reviewed_bootstrap_candidate(paths)

    assert after_accept == before_accept
    assert after_mappings == before_mappings
    assert bootstrap_after["x-evidence-operations"] is True
    assert bootstrap_after["x-evidence-polymorphism"] is True


def test_reviewed_evidence_base_ignores_effective_cache_and_exposes_raw_drift(
    tmp_path: Path,
) -> None:
    paths = _reviewed_repo_with_all_semantic_overlays(tmp_path)
    effective_cache = paths.effective
    effective_cache.parent.mkdir(parents=True, exist_ok=True)
    effective_cache.write_bytes(canonical_json_bytes({"x-untrusted-effective-cache": True}))

    effective, _mappings = pipeline_module.compose_reviewed_evidence_base_candidate(paths)

    assert "x-untrusted-effective-cache" not in effective
    raw = _raw_document()
    raw["components"]["schemas"]["Raw.Bool"]["type"] = "string"
    paths.candidate.write_bytes(canonical_json_bytes(raw))
    with pytest.raises(PipelineError, match="type.*candidate.*raw|raw.*type"):
        pipeline_module.compose_reviewed_evidence_base_candidate(paths)


def test_reviewed_candidate_applies_stages_without_accepting_or_writing(tmp_path: Path) -> None:
    paths = _reviewed_repo(tmp_path)
    before = {
        path.relative_to(tmp_path): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }

    effective, mappings = compose_reviewed_bootstrap_candidate(paths)

    operation = effective["paths"]["/api/2/menu/by_id"]["post"]
    assert effective["x-stage-contracts"] is True
    assert effective["x-stage-semantic"] is True
    assert effective["components"]["schemas"]["Raw.Bool"]["type"] == "boolean"
    assert operation["operationId"] == "menu_by_id"
    assert mappings == {"Raw.Bool": "Bool"}
    after = {
        path.relative_to(tmp_path): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    assert after == before


def test_reviewed_candidate_normalizes_generator_invalid_schema_names(
    tmp_path: Path,
) -> None:
    raw = _raw_document()
    invalid = "Namespace.Wrapper`1[[Namespace.Item, Assembly]]"
    old_ref = f"#/components/schemas/{invalid}"
    raw["components"]["schemas"] = {
        invalid: raw["components"]["schemas"]["Raw.Bool"],
        "Holder": {"properties": {"value": {"$ref": old_ref}}},
    }
    raw["paths"]["/api/2/menu/by_id"]["post"]["responses"]["200"]["content"]["application/json"][
        "schema"
    ] = {"$ref": old_ref}
    paths = _reviewed_repo(tmp_path, raw_document=raw)
    _write_yaml(
        tmp_path / "build/bootstrap/model-name-overrides.yaml",
        {"models": {invalid: "ReviewedResponse"}},
    )

    effective, mappings = compose_reviewed_bootstrap_candidate(paths)

    schemas = effective["components"]["schemas"]
    assert invalid not in schemas
    assert schemas["Holder"]["properties"]["value"]["$ref"] == (
        "#/components/schemas/ReviewedResponse"
    )
    assert (
        effective["paths"]["/api/2/menu/by_id"]["post"]["responses"]["200"]["content"][
            "application/json"
        ]["schema"]["$ref"]
        == "#/components/schemas/ReviewedResponse"
    )
    assert mappings == {
        "Holder": "Holder",
        "ReviewedResponse": "ReviewedResponse",
    }


def test_reviewed_candidate_rejects_candidate_not_derived_from_raw(tmp_path: Path) -> None:
    paths = _reviewed_repo(tmp_path)
    operation_ids = tmp_path / "build/bootstrap/operation-ids.yaml"
    _write_yaml(operation_ids, {"operations": {"POST /api/2/menu/wrong": "tampered"}})

    with pytest.raises(PipelineError, match="Missing operationId|Stale operationId"):
        compose_reviewed_bootstrap_candidate(paths)


@pytest.mark.parametrize("kind", ["missing", "symlink", "hardlink", "fifo", "directory"])
def test_reviewed_candidate_rejects_unsafe_required_input(tmp_path: Path, kind: str) -> None:
    paths = _reviewed_repo(tmp_path)
    target = tmp_path / "build/bootstrap/types.overlay.yaml"
    original = target.read_bytes()
    target.unlink()
    if kind == "symlink":
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(original)
        target.symlink_to(outside)
    elif kind == "hardlink":
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(original)
        target.hardlink_to(outside)
    elif kind == "fifo":
        os.mkfifo(target)
    elif kind == "directory":
        target.mkdir()

    with pytest.raises(PipelineError, match="[Rr]eviewed|regular|missing|symlink|hard links"):
        compose_reviewed_bootstrap_candidate(paths)


def test_reviewed_candidate_rejects_symlink_parent_and_duplicate_yaml(
    tmp_path: Path,
) -> None:
    paths = _reviewed_repo(tmp_path)
    bootstrap = tmp_path / "build/bootstrap"
    moved = tmp_path / "build/bootstrap-real"
    bootstrap.rename(moved)
    bootstrap.symlink_to(moved, target_is_directory=True)
    with pytest.raises(PipelineError, match="parent.*non-symlink|symlink"):
        compose_reviewed_bootstrap_candidate(paths)

    bootstrap.unlink()
    moved.rename(bootstrap)
    (bootstrap / "operation-ids.yaml").write_text(
        "operations: {}\noperations: {}\n",
        encoding="utf-8",
    )
    with pytest.raises(PipelineError, match="strict.*YAML"):
        compose_reviewed_bootstrap_candidate(paths)


def test_reviewed_candidate_rejects_tampered_type_and_collision_candidates(
    tmp_path: Path,
) -> None:
    paths = _reviewed_repo(tmp_path)
    types_path = tmp_path / "build/bootstrap/types.overlay.yaml"
    original_types = types_path.read_bytes()
    value = yaml.safe_load(original_types)
    update_action = next(action for action in value["actions"] if "update" in action)
    update_action["update"]["type"] = "string"
    _write_yaml(types_path, value)
    with pytest.raises(PipelineError, match="type.*candidate.*raw|raw.*type"):
        compose_reviewed_bootstrap_candidate(paths)

    types_path.write_bytes(original_types)
    _write_yaml(
        tmp_path / "build/bootstrap/model-collisions.yaml",
        {"collisions": {"Invented": ["Raw.Bool", "Other"]}},
    )
    with pytest.raises(PipelineError, match="collision.*candidate.*raw|raw.*collision"):
        compose_reviewed_bootstrap_candidate(paths)


def test_reviewed_candidate_does_not_mutate_input_object_helpers(tmp_path: Path) -> None:
    paths = _reviewed_repo(tmp_path)
    raw = _raw_document()
    pristine = copy.deepcopy(raw)

    compose_reviewed_bootstrap_candidate(paths)

    assert raw == pristine


@pytest.mark.skipif(
    not Path("build/upstream/candidate.json").is_file(),
    reason="ignored reviewed bootstrap candidate is absent in a clean checkout",
)
def test_current_reviewed_candidate_composes_locally_without_mutating_raw() -> None:
    paths = RepoPaths.discover()
    raw_before = paths.candidate.read_bytes()

    effective, mappings = compose_reviewed_bootstrap_candidate(paths)

    menu = effective["paths"]["/api/2/menu/by_id"]["post"]
    assert menu["operationId"] == "get_external_menu_by_id"
    assert (
        RedactionHints.for_operation(effective, "get_external_menu_by_id").operation_id
        == "get_external_menu_by_id"
    )
    assert len(mappings) == len(effective["components"]["schemas"])
    assert paths.candidate.read_bytes() == raw_before
