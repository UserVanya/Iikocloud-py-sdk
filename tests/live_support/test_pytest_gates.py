from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from tools.openapi_pipeline import pipeline as pipeline_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.generator import Toolchain
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes, write_json_atomic
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.pytest_support import (
    assert_serial_live_invocation,
    explicit_env_path,
    finalize_live_receipt,
    initialize_receipt,
    prepare_live_preflight,
    profile_path_for_name,
    resolve_locked_live_profile,
)
from tools.openapi_pipeline.live.receipt import (
    LiveArtifactHashes,
    LiveReceipt,
    verify_live_artifacts,
)
from tools.openapi_pipeline.promotion import build_generated_manifest


def _synthetic_artifacts(
    root: Path, monkeypatch: pytest.MonkeyPatch
) -> tuple[dict[str, object], Path]:
    effective: dict[str, object] = {
        "openapi": "3.0.3",
        "info": {"title": "synthetic", "version": "1"},
        "paths": {},
        "servers": [{"url": "https://api.example.invalid"}],
    }
    upstream = root / "openapi/upstream/iikocloud.openapi.json"
    upstream.parent.mkdir(parents=True)
    upstream.write_bytes(canonical_json_bytes(effective))
    build_effective = root / "build/openapi/effective.json"
    build_effective.parent.mkdir(parents=True)
    build_effective.write_bytes(canonical_json_bytes(effective))
    package = root / "src/iikocloud_client"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("# generated\n", encoding="utf-8")
    generator = root / "generator"
    generator.mkdir()
    (generator / "manual-files.txt").write_text("", encoding="utf-8")
    manifest = build_generated_manifest(
        package,
        effective_schema_sha256=sha256_bytes(canonical_json_bytes(effective)),
        toolchain=Toolchain(
            image="openapitools/openapi-generator-cli",
            version="v7.22.0",
            digest="sha256:" + "a" * 64,
        ),
    )
    write_json_atomic(generator / "generated-manifest.json", manifest)
    monkeypatch.setattr(
        pipeline_module,
        "_load_document",
        lambda path, *, label: effective,
    )
    monkeypatch.setattr(
        pipeline_module,
        "_apply_committed_corrections",
        lambda paths, document: (effective, {}),
    )
    return effective, package


def test_live_artifact_hashes_recompute_effective_and_verify_exact_tree(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    effective, _package = _synthetic_artifacts(tmp_path, monkeypatch)
    manifest = tmp_path / "generator/generated-manifest.json"

    hashes = verify_live_artifacts(tmp_path)

    assert hashes.effective_schema_sha256 == sha256_bytes(canonical_json_bytes(effective))
    assert hashes.generated_tree_sha256 == sha256_bytes(manifest.read_bytes())


@pytest.mark.parametrize("target", ["effective", "tree", "manifest"])
def test_live_artifacts_fail_closed_when_missing_or_stale_before_http(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    _effective, package = _synthetic_artifacts(tmp_path, monkeypatch)
    if target == "effective":
        (tmp_path / "build/openapi/effective.json").write_text("{}\n", encoding="utf-8")
    elif target == "tree":
        (package / "__init__.py").write_text("changed\n", encoding="utf-8")
    else:
        (tmp_path / "generator/generated-manifest.json").unlink()

    with pytest.raises(SafetyError, match="artifact|verification"):
        verify_live_artifacts(tmp_path)


@pytest.mark.parametrize(
    "arguments",
    [(), ("-n1",), ("-n", "2"), ("--numprocesses=auto",)],
)
def test_live_invocation_requires_explicit_n0(arguments: tuple[str, ...]) -> None:
    with pytest.raises(SafetyError, match="single-process|parallel"):
        assert_serial_live_invocation(arguments)


@pytest.mark.parametrize(
    "arguments",
    [("-n0",), ("-n", "0"), ("--numprocesses=0",)],
)
def test_live_invocation_accepts_only_explicit_zero_workers(arguments: tuple[str, ...]) -> None:
    assert_serial_live_invocation(arguments)


def test_profile_and_env_paths_are_exact_private_locations(tmp_path: Path) -> None:
    private = tmp_path / "private"
    profiles = private / "profiles"
    profiles.mkdir(parents=True, mode=0o700)
    private.chmod(0o700)
    profiles.chmod(0o700)
    assert profile_path_for_name(tmp_path, "test-server") == (profiles / "test-server.toml")
    assert explicit_env_path(tmp_path, ".env", cwd=tmp_path) == tmp_path / ".env"

    for unsafe in ("../test", "test/server", ".hidden", "UPPER"):
        with pytest.raises(SafetyError, match="safe lowercase"):
            profile_path_for_name(tmp_path, unsafe)
    with pytest.raises(SafetyError, match="repository root"):
        explicit_env_path(tmp_path, "private/.env", cwd=tmp_path)


def test_unverified_auth_catalog_fails_before_profile_or_artifact_access(tmp_path: Path) -> None:
    contracts = tmp_path / "contracts"
    contracts.mkdir()
    (contracts / "rate-limits.yaml").write_text(
        "version: 1\n"
        "defaults:\n"
        "  utilization: 0.20\n"
        "  global_min_interval_seconds: 15\n"
        "  max_calls_per_operation_per_run: 1\n"
        "operations:\n"
        "  authenticate:\n"
        "    server_limit: {calls: 1, per_seconds: 5}\n"
        "    source: synthetic\n"
        "    verified: false\n",
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="not verified"):
        prepare_live_preflight(
            tmp_path,
            invocation_args=("-n0",),
        )
    assert not (tmp_path / "private").exists()
    assert not (tmp_path / "build").exists()


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test",
        base_url="https://api.example.invalid",
        api_login="login",
        organization_id="org",
        external_menu_id="menu",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=(),
        fingerprint="a" * 64,
    )


def test_receipt_completion_requires_every_teardown_gate(tmp_path: Path) -> None:
    state_root = tmp_path / ".state"
    lock = LiveProcessLock(state_root / "live.lock")
    with lock:
        receipt, path = initialize_receipt(
            state_root,
            process_lock=lock,
            run_id="20260716T180000Z-a1b2c3d4",
            profile=_profile(),
            artifacts=LiveArtifactHashes("b" * 64, "c" * 64),
        )
    receipt = receipt.with_operation("authenticate")
    receipt.write(path)
    gate_names = (
        "live_reports_passed",
        "circuit_closed",
        "clients_closed",
        "mutation_journals_clean",
    )
    for failed_gate in gate_names:
        gates = {name: True for name in gate_names}
        gates[failed_gate] = False
        assert not finalize_live_receipt(receipt, path, **gates)
        assert not LiveReceipt.load(path).completed

    assert finalize_live_receipt(
        receipt,
        path,
        live_reports_passed=True,
        circuit_closed=True,
        clients_closed=True,
        mutation_journals_clean=True,
    )
    assert LiveReceipt.load(path).completed


def test_profile_env_and_receipt_require_held_canonical_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    private = tmp_path / "private"
    profiles = private / "profiles"
    profiles.mkdir(parents=True, mode=0o700)
    private.chmod(0o700)
    profiles.chmod(0o700)
    profile_path = profiles / "test.toml"
    profile_path.write_text(
        'name="test"\nbase_url="https://api.example.invalid"\n'
        'api_login_env="IIKO_API_KEY"\norganization_id_env="IIKO_ORG"\n'
        'external_menu_id_env="IIKO_MENU"\nallow_write=false\n'
        "allowed_organization_ids=[]\n",
        encoding="utf-8",
    )
    profile_path.chmod(0o600)
    monkeypatch.setenv("IIKO_API_KEY", "synthetic-login")
    monkeypatch.setenv("IIKO_ORG", "synthetic-org")
    monkeypatch.setenv("IIKO_MENU", "synthetic-menu")
    lock = LiveProcessLock(tmp_path / ".state/live.lock")

    with pytest.raises(SafetyError, match="must be held"):
        resolve_locked_live_profile(
            tmp_path,
            process_lock=lock,
            profile_name="test",
            env_file_option=None,
        )

    with lock:
        profile = resolve_locked_live_profile(
            tmp_path,
            process_lock=lock,
            profile_name="test",
            env_file_option=None,
        )
        receipt, path = initialize_receipt(
            tmp_path / ".state",
            process_lock=lock,
            run_id="20260716T180000Z-a1b2c3d4",
            profile=profile,
            artifacts=LiveArtifactHashes("b" * 64, "c" * 64),
        )
    assert receipt.profile_fingerprint == profile.fingerprint
    assert path.exists()


def test_pytest_options_and_offline_collection_do_not_need_private_files() -> None:
    environment = os.environ.copy()
    for name in (
        "IIKO_API_KEY",
        "IIKO_API_KEY_2",
        "IIKO_TEST_ORGANIZATION_ID",
        "IIKO_TEST_EXTERNAL_MENU_ID",
    ):
        environment.pop(name, None)
    help_result = subprocess.run(
        [sys.executable, "-m", "pytest", "--help"],
        cwd=Path.cwd(),
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    assert help_result.returncode == 0
    assert "--live-profile" in help_result.stdout
    assert "--env-file" in help_result.stdout

    collection = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-n0",
            "--collect-only",
            "tests/pipeline/test_io.py",
            "-q",
        ],
        cwd=Path.cwd(),
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    assert collection.returncode == 0, collection.stderr
    assert "test_canonical_json_bytes_sorts_keys_and_emits_utf8_newline" in collection.stdout
