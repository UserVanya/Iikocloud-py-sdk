from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import Mock

import pytest
import yaml

from tools.openapi_pipeline import pipeline as pipeline_module
from tools.openapi_pipeline.errors import PipelineError, StaleOverlayError
from tools.openapi_pipeline.fetch import FetchResult
from tools.openapi_pipeline.generator import Toolchain
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes, write_json_atomic
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import (
    UPSTREAM_SCHEMA_URL,
    PipelineDependencies,
    _apply_committed_corrections,
    bootstrap,
    default_dependencies,
    sync,
    upstream_check,
    verify,
)
from tools.openapi_pipeline.promotion import build_generated_manifest


@pytest.fixture
def fake_dependencies(tmp_path: Path) -> PipelineDependencies:
    paths = RepoPaths(tmp_path)
    paths.candidate.parent.mkdir(parents=True)
    paths.candidate.write_bytes(b'{"openapi":"3.0.1","info":{},"paths":{}}\n')
    generated = tmp_path / "build/generated/iikocloud_client"
    generated.mkdir(parents=True)
    (generated / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "generator").mkdir()
    (tmp_path / "generator/manual-files.txt").write_text("", encoding="utf-8")
    (tmp_path / "generator/toolchain.lock").write_text(
        '{"image":"openapitools/openapi-generator-cli",'
        '"version":"v7.22.0","digest":"sha256:' + "a" * 64 + '"}\n',
        encoding="utf-8",
    )
    dependencies = PipelineDependencies(
        paths=paths,
        fetch=Mock(return_value=FetchResult("a" * 64, paths.candidate, True)),
        apply_corrections=Mock(return_value=({}, {})),
        validate=Mock(),
        generate=Mock(return_value=generated),
        verify_package=Mock(),
        verify_contracts=Mock(),
        promote=Mock(),
    )
    return dependencies


def test_sync_does_not_mutate_committed_outputs_when_overlay_is_stale(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    committed = tmp_path / "openapi/upstream/iikocloud.openapi.json"
    committed.parent.mkdir(parents=True)
    old_snapshot = b'{"openapi":"3.0.1","info":{},"paths":{}}\n'
    committed.write_bytes(old_snapshot)
    generated = tmp_path / "src/iikocloud_client"
    generated.mkdir(parents=True)
    (generated / "old.py").write_text("old", encoding="utf-8")
    fake_dependencies.apply_corrections.side_effect = StaleOverlayError("stale")

    with pytest.raises(StaleOverlayError, match="stale"):
        sync(fake_dependencies)

    assert committed.read_bytes() == old_snapshot
    assert (generated / "old.py").read_text(encoding="utf-8") == "old"
    fake_dependencies.promote.assert_not_called()


def test_sync_checks_staged_package_before_single_promotion(
    fake_dependencies: PipelineDependencies,
) -> None:
    events: list[str] = []
    fake_dependencies.fetch.side_effect = lambda: (
        events.append("fetch") or FetchResult("a" * 64, fake_dependencies.paths.candidate, True)
    )
    fake_dependencies.apply_corrections.side_effect = lambda document: (
        events.append("correct") or (document, {})
    )
    fake_dependencies.validate.side_effect = lambda document: events.append("validate")
    generated = fake_dependencies.paths.build / "generated/iikocloud_client"
    fake_dependencies.generate.side_effect = lambda mappings: (
        events.append("generate") or generated
    )
    fake_dependencies.verify_package.side_effect = lambda package: events.append("package")
    fake_dependencies.verify_contracts.side_effect = lambda package: events.append("contracts")
    fake_dependencies.promote.side_effect = lambda items: events.append("promote")

    sync(fake_dependencies)

    assert events == [
        "fetch",
        "correct",
        "validate",
        "generate",
        "package",
        "contracts",
        "promote",
    ]
    promoted = fake_dependencies.promote.call_args.args[0]
    assert [item.target for item in promoted] == [
        fake_dependencies.paths.upstream,
        fake_dependencies.paths.root / "src/iikocloud_client",
        fake_dependencies.paths.root / "generator/generated-manifest.json",
    ]


def test_sync_preserves_exact_snapshot_and_excludes_manual_files_from_manifest(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    candidate = b'{ "openapi": "3.0.1", "info": {}, "paths": {} }\n'
    fake_dependencies.paths.candidate.write_bytes(candidate)
    manual_list = tmp_path / "generator/manual-files.txt"
    manual_list.write_text("iikocloud_client/_contracts/manual.yaml\n", encoding="utf-8")
    manual_source = tmp_path / "src/iikocloud_client/_contracts/manual.yaml"
    manual_source.parent.mkdir(parents=True)
    manual_source.write_bytes(b"manual\n")

    sync(fake_dependencies)

    items = fake_dependencies.promote.call_args.args[0]
    assert items[0].staged.read_bytes() == candidate
    manifest = yaml.safe_load(items[2].staged.read_text(encoding="utf-8"))
    assert "iikocloud_client/__init__.py" in manifest["files"]
    assert "iikocloud_client/_contracts/manual.yaml" not in manifest["files"]
    assert (items[1].staged / "_contracts/manual.yaml").read_bytes() == b"manual\n"


def test_sync_package_failure_leaves_committed_outputs_and_staging_for_diagnosis(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    upstream = fake_dependencies.paths.upstream
    upstream.parent.mkdir(parents=True)
    old_snapshot = b'{ "openapi": "3.0.1", "info": {}, "paths": {} }\n'
    upstream.write_bytes(old_snapshot)
    committed = tmp_path / "src/iikocloud_client/old.py"
    committed.parent.mkdir(parents=True)
    committed.write_text("old", encoding="utf-8")
    fake_dependencies.verify_package.side_effect = PipelineError("broken package")

    with pytest.raises(PipelineError, match="broken package"):
        sync(fake_dependencies)

    assert upstream.read_bytes() == old_snapshot
    assert committed.read_text(encoding="utf-8") == "old"
    assert (tmp_path / "build/promotion/iikocloud.openapi.json").exists()
    fake_dependencies.promote.assert_not_called()


def test_sync_contract_failure_leaves_committed_outputs_untouched(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    upstream = fake_dependencies.paths.upstream
    upstream.parent.mkdir(parents=True)
    old_snapshot = b'{"openapi":"3.0.1","info":{},"paths":{}}\n'
    upstream.write_bytes(old_snapshot)
    committed = tmp_path / "src/iikocloud_client/old.py"
    committed.parent.mkdir(parents=True)
    committed.write_text("old", encoding="utf-8")
    fake_dependencies.verify_contracts.side_effect = PipelineError("contract failed")

    with pytest.raises(PipelineError, match="contract failed"):
        sync(fake_dependencies)

    assert upstream.read_bytes() == old_snapshot
    assert committed.read_text(encoding="utf-8") == "old"
    fake_dependencies.verify_package.assert_called_once()
    fake_dependencies.promote.assert_not_called()


def test_sync_contract_gate_receives_disposable_copy_and_cannot_mutate_staging(
    fake_dependencies: PipelineDependencies,
) -> None:
    checked_packages: list[Path] = []

    def mutate_checked_copy(package: Path) -> None:
        checked_packages.append(package)
        (package / "__init__.py").write_text("mutated\n", encoding="utf-8")
        cache = package / "__pycache__"
        cache.mkdir()
        (cache / "leak.pyc").write_bytes(b"cache")

    fake_dependencies.verify_contracts.side_effect = mutate_checked_copy

    sync(fake_dependencies)

    promoted = fake_dependencies.promote.call_args.args[0]
    staged_package = promoted[1].staged
    assert checked_packages == [
        fake_dependencies.paths.build / "contract-check/src/iikocloud_client"
    ]
    assert checked_packages[0] != staged_package
    assert (staged_package / "__init__.py").read_text(encoding="utf-8") == ""
    assert not (staged_package / "__pycache__").exists()


def test_sync_rejects_raw_generated_symlink_before_copying_external_bytes(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    sentinel = tmp_path / "outside-sentinel.txt"
    sentinel.write_bytes(b"must-never-enter-staging")
    generated = fake_dependencies.paths.build / "generated/iikocloud_client"
    (generated / "escaped.py").symlink_to(sentinel)

    with pytest.raises(PipelineError, match="symlink"):
        sync(fake_dependencies)

    promotion = fake_dependencies.paths.build / "promotion"
    regular_files = [
        path for path in promotion.rglob("*") if path.is_file() and not path.is_symlink()
    ]
    assert all(path.read_bytes() != sentinel.read_bytes() for path in regular_files)
    fake_dependencies.verify_package.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def test_sync_rejects_raw_generated_special_file_as_pipeline_error_before_copy(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    generated = fake_dependencies.paths.build / "generated/iikocloud_client"
    os.mkfifo(generated / "generator-output.fifo")

    with pytest.raises(PipelineError, match=r"non-regular.*generator-output\.fifo"):
        sync(fake_dependencies)

    assert not (fake_dependencies.paths.build / "promotion/iikocloud_client").exists()
    fake_dependencies.verify_package.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def test_sync_rejects_unsafe_manual_allowlist_before_package_check(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    (tmp_path / "generator/manual-files.txt").write_text(
        "iikocloud_client/../../outside.txt\n", encoding="utf-8"
    )

    with pytest.raises(PipelineError, match="Unsafe manual"):
        sync(fake_dependencies)

    fake_dependencies.verify_package.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def test_sync_rejects_symlinked_manual_parent_before_external_bytes_reach_staging(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    (tmp_path / "generator/manual-files.txt").write_text(
        "iikocloud_client/_contracts/manual.yaml\n", encoding="utf-8"
    )
    package_root = tmp_path / "src/iikocloud_client"
    package_root.mkdir(parents=True)
    outside = tmp_path / "outside-contracts"
    outside.mkdir()
    (outside / "manual.yaml").write_bytes(b"external-sentinel")
    (package_root / "_contracts").symlink_to(outside, target_is_directory=True)

    with pytest.raises(PipelineError, match="Manual.*symlink|symlink.*Manual"):
        sync(fake_dependencies)

    staged = tmp_path / "build/promotion/iikocloud_client/_contracts/manual.yaml"
    assert not staged.exists()
    assert (outside / "manual.yaml").read_bytes() == b"external-sentinel"
    fake_dependencies.verify_package.assert_not_called()
    fake_dependencies.verify_contracts.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def _prepare_verify_fixture(tmp_path: Path) -> PipelineDependencies:
    dependencies = fake_dependencies.__wrapped__(tmp_path)  # type: ignore[attr-defined]
    document = {"openapi": "3.0.1", "info": {}, "paths": {}}
    dependencies.paths.upstream.parent.mkdir(parents=True)
    dependencies.paths.upstream.write_bytes(canonical_json_bytes(document))
    generated = dependencies.paths.build / "generated/iikocloud_client"
    committed = tmp_path / "src/iikocloud_client"
    committed.mkdir(parents=True)
    (committed / "__init__.py").write_text("", encoding="utf-8")
    toolchain = Toolchain.load(tmp_path / "generator/toolchain.lock")
    manifest = build_generated_manifest(
        generated,
        effective_schema_sha256=sha256_bytes(canonical_json_bytes(document)),
        toolchain=toolchain,
    )
    write_json_atomic(tmp_path / "generator/generated-manifest.json", manifest)
    dependencies.apply_corrections = Mock(return_value=(document, {}))
    dependencies.verify_root_package = Mock()
    return dependencies


def test_verify_regenerates_without_fetch_and_checks_both_wheels(tmp_path: Path) -> None:
    dependencies = _prepare_verify_fixture(tmp_path)

    verify(dependencies)

    dependencies.fetch.assert_not_called()
    dependencies.verify_package.assert_called_once()
    dependencies.verify_contracts.assert_called_once()
    dependencies.verify_root_package.assert_called_once_with(tmp_path)
    dependencies.promote.assert_not_called()


def test_verify_detects_committed_generated_drift(tmp_path: Path) -> None:
    dependencies = _prepare_verify_fixture(tmp_path)
    (tmp_path / "src/iikocloud_client/__init__.py").write_text("changed", encoding="utf-8")

    with pytest.raises(PipelineError, match="generated files differ"):
        verify(dependencies)


def test_verify_contract_failure_stops_before_root_wheel_check(tmp_path: Path) -> None:
    dependencies = _prepare_verify_fixture(tmp_path)
    dependencies.verify_contracts.side_effect = PipelineError("contract failed")

    with pytest.raises(PipelineError, match="contract failed"):
        verify(dependencies)

    dependencies.verify_package.assert_called_once()
    dependencies.verify_root_package.assert_not_called()


def test_verify_contract_gate_mutation_does_not_change_generated_candidate(
    tmp_path: Path,
) -> None:
    dependencies = _prepare_verify_fixture(tmp_path)
    generated = dependencies.paths.build / "generated/iikocloud_client"

    def mutate_checked_copy(package: Path) -> None:
        (package / "__init__.py").write_text("mutated\n", encoding="utf-8")

    dependencies.verify_contracts.side_effect = mutate_checked_copy

    verify(dependencies)

    assert (generated / "__init__.py").read_text(encoding="utf-8") == ""
    checked = dependencies.verify_contracts.call_args.args[0]
    assert checked == tmp_path / "build/contract-check/src/iikocloud_client"


def test_upstream_check_only_fetches_and_writes_ignored_reports(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    old = {"openapi": "3.0.1", "info": {}, "paths": {}}
    fake_dependencies.paths.upstream.parent.mkdir(parents=True)
    write_json_atomic(fake_dependencies.paths.upstream, old)
    new = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {"/api/1/new": {"post": {}}},
    }
    write_json_atomic(fake_dependencies.paths.candidate, new)

    upstream_check(fake_dependencies)

    assert (tmp_path / "build/reports/upstream-diff.json").is_file()
    markdown = (tmp_path / "build/reports/upstream-diff.md").read_text(encoding="utf-8")
    assert "POST /api/1/new" in markdown
    fake_dependencies.apply_corrections.assert_not_called()
    fake_dependencies.generate.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def test_bootstrap_preview_writes_deterministic_candidates_without_promotion(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {
            "/api/1/organizations": {
                "post": {
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": (
                                        "#/components/schemas/OrganizationsGetOrganizationsRequest"
                                    )
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {"schemas": {"OrganizationsGetOrganizationsRequest": {"type": "object"}}},
    }
    write_json_atomic(fake_dependencies.paths.candidate, document)

    bootstrap(fake_dependencies, accept_current_upstream=False)
    first = {
        path.name: path.read_bytes() for path in sorted((tmp_path / "build/bootstrap").iterdir())
    }
    bootstrap(fake_dependencies, accept_current_upstream=False)
    second = {
        path.name: path.read_bytes() for path in sorted((tmp_path / "build/bootstrap").iterdir())
    }

    registry = yaml.safe_load(first["operation-ids.yaml"])
    assert registry == {"operations": {"POST /api/1/organizations": "get_organizations"}}
    assert first == second
    assert yaml.safe_load(first["model-collisions.yaml"]) == {"collisions": {}}
    fake_dependencies.promote.assert_not_called()


def test_bootstrap_preview_falls_back_to_paths_for_duplicate_request_phrases(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    request_schema = {
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/CustomerChangeUserBalanceRequest"}
                }
            }
        }
    }
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {
            "/api/1/loyalty/iiko/customer/wallet/chargeoff": {
                "post": request_schema,
            },
            "/api/1/loyalty/iiko/customer/wallet/topup": {
                "post": request_schema,
            },
        },
        "components": {"schemas": {"CustomerChangeUserBalanceRequest": {"type": "object"}}},
    }
    write_json_atomic(fake_dependencies.paths.candidate, document)

    bootstrap(fake_dependencies, accept_current_upstream=False)

    registry = yaml.safe_load(
        (tmp_path / "build/bootstrap/operation-ids.yaml").read_text(encoding="utf-8")
    )
    assert registry == {
        "operations": {
            "POST /api/1/loyalty/iiko/customer/wallet/chargeoff": (
                "loyalty_iiko_customer_wallet_chargeoff"
            ),
            "POST /api/1/loyalty/iiko/customer/wallet/topup": (
                "loyalty_iiko_customer_wallet_topup"
            ),
        }
    }


def test_bootstrap_preview_stops_on_model_collisions_but_preserves_candidates(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {
            "schemas": {"One.Item": {}, "Two.Item": {}},
        },
    }
    write_json_atomic(fake_dependencies.paths.candidate, document)

    with pytest.raises(PipelineError, match="model collision"):
        bootstrap(fake_dependencies, accept_current_upstream=False)

    collisions = tmp_path / "build/bootstrap/model-collisions.yaml"
    assert yaml.safe_load(collisions.read_text(encoding="utf-8")) == {
        "collisions": {"Item": ["One.Item", "Two.Item"]}
    }
    fake_dependencies.promote.assert_not_called()


def test_bootstrap_accept_refuses_nonempty_registry_without_fetch_or_mutation(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    registry = tmp_path / "openapi/operation-ids.yaml"
    registry.parent.mkdir(parents=True)
    registry.write_text("operations:\n  POST /api/1/existing: existing\n", encoding="utf-8")

    with pytest.raises(PipelineError, match="non-empty"):
        bootstrap(fake_dependencies, accept_current_upstream=True)

    assert "existing" in registry.read_text(encoding="utf-8")
    fake_dependencies.fetch.assert_not_called()
    fake_dependencies.generate.assert_not_called()
    fake_dependencies.promote.assert_not_called()


def _write_valid_empty_registries(root: Path) -> None:
    openapi = root / "openapi"
    openapi.mkdir(parents=True, exist_ok=True)
    (openapi / "operation-ids.yaml").write_text("operations: {}\n", encoding="utf-8")
    (openapi / "model-name-overrides.yaml").write_text("models: {}\n", encoding="utf-8")


def test_committed_mechanical_overlay_applies_to_original_upstream_once(tmp_path: Path) -> None:
    _write_valid_empty_registries(tmp_path)
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": {"BooleanValue": {"type": "bool"}}},
    }
    overlay = pipeline_module.build_types_overlay(document)
    overlay_path = tmp_path / "openapi/overlays/types.overlay.yaml"
    overlay_path.parent.mkdir()
    overlay_path.write_text(yaml.safe_dump(overlay, sort_keys=True), encoding="utf-8")

    effective, mappings = _apply_committed_corrections(RepoPaths(tmp_path), document)

    assert effective["components"]["schemas"]["BooleanValue"]["type"] == "boolean"
    assert mappings == {"BooleanValue": "BooleanValue"}
    assert document["components"]["schemas"]["BooleanValue"]["type"] == "bool"


def test_valid_empty_committed_mechanical_overlay_is_noop(tmp_path: Path) -> None:
    _write_valid_empty_registries(tmp_path)
    document = {"openapi": "3.0.1", "info": {}, "paths": {}}
    overlay_path = tmp_path / "openapi/overlays/types.overlay.yaml"
    overlay_path.parent.mkdir()
    overlay_path.write_text(
        yaml.safe_dump(pipeline_module.build_types_overlay(document), sort_keys=True),
        encoding="utf-8",
    )

    effective, mappings = _apply_committed_corrections(RepoPaths(tmp_path), document)

    assert effective == document
    assert effective is not document
    assert mappings == {}


def test_malformed_empty_mechanical_overlay_does_not_bypass_validation(tmp_path: Path) -> None:
    _write_valid_empty_registries(tmp_path)
    overlay_path = tmp_path / "openapi/overlays/types.overlay.yaml"
    overlay_path.parent.mkdir()
    overlay_path.write_text("actions: []\n", encoding="utf-8")

    with pytest.raises(PipelineError, match="Overlay 1.1.0|mechanical overlay"):
        _apply_committed_corrections(
            RepoPaths(tmp_path), {"openapi": "3.0.1", "info": {}, "paths": {}}
        )


def _write_bootstrap_candidates(
    dependencies: PipelineDependencies,
    document: dict[str, object],
    *,
    collisions: dict[str, list[str]] | None = None,
) -> None:
    write_json_atomic(dependencies.paths.candidate, document)
    bootstrap_root = dependencies.paths.build / "bootstrap"
    bootstrap_root.mkdir(parents=True)
    (bootstrap_root / "types.overlay.yaml").write_text(
        yaml.safe_dump(pipeline_module.build_types_overlay(document), sort_keys=True),
        encoding="utf-8",
    )
    (bootstrap_root / "operation-ids.yaml").write_text("operations: {}\n", encoding="utf-8")
    (bootstrap_root / "model-collisions.yaml").write_text(
        yaml.safe_dump({"collisions": collisions or {}}, sort_keys=True),
        encoding="utf-8",
    )
    _write_valid_empty_registries(dependencies.paths.root)


def test_bootstrap_accept_checks_then_promotes_all_outputs_once(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document: dict[str, object] = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": {}},
    }
    _write_bootstrap_candidates(fake_dependencies, document)

    bootstrap(fake_dependencies, accept_current_upstream=True)

    fake_dependencies.fetch.assert_not_called()
    fake_dependencies.validate.assert_called_once()
    fake_dependencies.verify_package.assert_called_once()
    fake_dependencies.verify_contracts.assert_called_once()
    fake_dependencies.promote.assert_called_once()
    targets = [item.target for item in fake_dependencies.promote.call_args.args[0]]
    assert targets == [
        fake_dependencies.paths.upstream,
        tmp_path / "openapi/overlays/types.overlay.yaml",
        tmp_path / "openapi/operation-ids.yaml",
        tmp_path / "src/iikocloud_client",
        tmp_path / "generator/generated-manifest.json",
    ]


def test_bootstrap_accept_uses_reviewed_model_override_to_resolve_collision(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document: dict[str, object] = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": {"One.Item": {}, "Two.Item": {}}},
    }
    collisions = {"Item": ["One.Item", "Two.Item"]}
    _write_bootstrap_candidates(fake_dependencies, document, collisions=collisions)
    override = tmp_path / "build/bootstrap/model-name-overrides.yaml"
    override.write_text("models:\n  Two.Item: SecondItem\n", encoding="utf-8")

    bootstrap(fake_dependencies, accept_current_upstream=True)

    fake_dependencies.generate.assert_called_once_with(
        {"One.Item": "Item", "Two.Item": "SecondItem"}
    )
    targets = [item.target for item in fake_dependencies.promote.call_args.args[0]]
    assert tmp_path / "openapi/model-name-overrides.yaml" in targets


def test_bootstrap_accept_package_failure_preserves_reviewed_candidates(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document: dict[str, object] = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": {}},
    }
    _write_bootstrap_candidates(fake_dependencies, document)
    before = {path.name: path.read_bytes() for path in (tmp_path / "build/bootstrap").iterdir()}
    fake_dependencies.verify_package.side_effect = PipelineError("package failed")

    with pytest.raises(PipelineError, match="package failed"):
        bootstrap(fake_dependencies, accept_current_upstream=True)

    after = {path.name: path.read_bytes() for path in (tmp_path / "build/bootstrap").iterdir()}
    assert after == before
    fake_dependencies.promote.assert_not_called()


def test_bootstrap_accept_contract_failure_preserves_candidates_and_destinations(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    document: dict[str, object] = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": {}},
    }
    _write_bootstrap_candidates(fake_dependencies, document)
    types_target = tmp_path / "openapi/overlays/types.overlay.yaml"
    types_target.parent.mkdir(parents=True, exist_ok=True)
    types_target.write_text("old overlay\n", encoding="utf-8")
    registry_target = tmp_path / "openapi/operation-ids.yaml"
    registry_before = registry_target.read_bytes()
    candidates_before = {
        path.name: path.read_bytes() for path in (tmp_path / "build/bootstrap").iterdir()
    }
    fake_dependencies.verify_contracts.side_effect = PipelineError("contract failed")

    with pytest.raises(PipelineError, match="contract failed"):
        bootstrap(fake_dependencies, accept_current_upstream=True)

    assert types_target.read_text(encoding="utf-8") == "old overlay\n"
    assert registry_target.read_bytes() == registry_before
    assert {
        path.name: path.read_bytes() for path in (tmp_path / "build/bootstrap").iterdir()
    } == candidates_before
    fake_dependencies.verify_package.assert_called_once()
    fake_dependencies.promote.assert_not_called()


def test_default_online_fetch_uses_only_exact_production_schema_url(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "fixture"\nversion = "1.0.0"\n', encoding="utf-8"
    )
    generator = tmp_path / "generator"
    generator.mkdir()
    (generator / "toolchain.lock").write_text(
        '{"image":"openapitools/openapi-generator-cli",'
        '"version":"v7.22.0","digest":"sha256:' + "a" * 64 + '"}\n',
        encoding="utf-8",
    )
    captured: list[tuple[str, Path]] = []

    def fake_fetch(url: str, destination: Path) -> FetchResult:
        captured.append((url, destination))
        return FetchResult("b" * 64, destination, True)

    monkeypatch.setattr(pipeline_module, "fetch_candidate", fake_fetch)
    dependencies = default_dependencies(offline=False, paths=RepoPaths(tmp_path))

    dependencies.fetch()

    assert UPSTREAM_SCHEMA_URL == "https://api-ru.iiko.services/api-docs/docs"
    assert captured == [(UPSTREAM_SCHEMA_URL, tmp_path / "build/upstream/candidate.json")]
    assert "api-ru.iiko.services/docs" not in UPSTREAM_SCHEMA_URL
