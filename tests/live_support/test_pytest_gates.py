from __future__ import annotations

import json
import os
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

import pytest

from tests.integration.read.cases import FULL_READ_PLAN
from tools.openapi_pipeline import pipeline as pipeline_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.generator import Toolchain
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes, write_json_atomic
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.pytest_support import (
    assert_exact_live_read_invocation,
    assert_serial_live_invocation,
    explicit_env_path,
    finalize_live_receipt,
    initialize_receipt,
    prepare_live_preflight,
    profile_path_for_name,
    resolve_locked_live_profile,
    validate_live_read_plan,
)
from tools.openapi_pipeline.live.rates import RateCatalog
from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    GeneratedReadBinding,
    ReadCase,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan
from tools.openapi_pipeline.live.receipt import (
    LiveArtifactHashes,
    LiveReceipt,
    verify_live_artifacts,
)
from tools.openapi_pipeline.live.safety import OperationSafetyCatalog
from tools.openapi_pipeline.live.session import LiveOperation, load_operation_contract
from tools.openapi_pipeline.promotion import build_generated_manifest, load_generated_manifest


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
    (generator / "manual-files.txt").write_text(
        "iikocloud_client/_contracts/rate-limits.yaml\n",
        encoding="utf-8",
    )
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
    manual = package / "_contracts/rate-limits.yaml"
    manual.parent.mkdir()
    manual.write_text("manual-v1\n", encoding="utf-8")
    contracts = root / "contracts"
    contracts.mkdir()
    (contracts / "operation-safety.yaml").write_text(
        "version: 1\n"
        "operations:\n"
        "  authenticate:\n"
        "    effect: auth\n"
        "    live_policy: automatic\n"
        "    reason: reviewed synthetic authentication\n",
        encoding="utf-8",
    )
    (contracts / "live-operations.yaml").write_text(
        "version: 1\n"
        "operations:\n"
        "  authenticate:\n"
        "    kind: auth\n"
        "    cleanup: null\n"
        "    method: POST\n"
        "    path: /api/1/access_token\n",
        encoding="utf-8",
    )
    rate_contract = contracts / "rate-limits.yaml"
    rate_contract.write_text(
        "version: 2\n"
        "defaults:\n"
        "  utilization: 0.20\n"
        "  global_min_interval_seconds: 30\n"
        "  max_calls_per_operation_per_run: 1\n"
        "operations:\n"
        "  authenticate:\n"
        "    test_budget:\n"
        "      min_interval_seconds: 30\n"
        "      source: synthetic\n"
        "      verified: true\n"
        "    server_limit:\n"
        "      calls: 1\n"
        "      per_seconds: 5\n"
        "      source: synthetic\n"
        "      verified: true\n",
        encoding="utf-8",
    )
    manual.write_bytes(rate_contract.read_bytes())
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
    manifest_value = load_generated_manifest(manifest)
    published_files = {
        **manifest_value["files"],
        "iikocloud_client/_contracts/rate-limits.yaml": sha256_bytes(
            (tmp_path / "src/iikocloud_client/_contracts/rate-limits.yaml").read_bytes()
        ),
    }
    assert hashes.generated_tree_sha256 == sha256_bytes(
        canonical_json_bytes(dict(sorted(published_files.items())))
    )
    assert hashes.generated_tree_sha256 != sha256_bytes(manifest.read_bytes())
    contract_hashes = {
        relative: sha256_bytes((tmp_path / relative).read_bytes())
        for relative in (
            "contracts/operation-safety.yaml",
            "contracts/live-operations.yaml",
            "contracts/rate-limits.yaml",
        )
    }
    assert hashes.live_contracts_sha256 == sha256_bytes(canonical_json_bytes(contract_hashes))


def test_manual_file_change_changes_logical_published_tree_hash(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _effective, package = _synthetic_artifacts(tmp_path, monkeypatch)
    first = verify_live_artifacts(tmp_path)
    receipt = LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="a" * 64,
        effective_schema_sha256=first.effective_schema_sha256,
        generated_tree_sha256=first.generated_tree_sha256,
        live_contracts_sha256=first.live_contracts_sha256,
        operations=("authenticate", "get_organizations"),
        had_429=False,
        completed=True,
    )

    rate_contract = tmp_path / "contracts/rate-limits.yaml"
    modified_rate_contract = rate_contract.read_text(encoding="utf-8").replace(
        "source: synthetic",
        "source: synthetic-v2",
    )
    rate_contract.write_text(modified_rate_contract, encoding="utf-8")
    (package / "_contracts/rate-limits.yaml").write_text(
        modified_rate_contract,
        encoding="utf-8",
    )
    second = verify_live_artifacts(tmp_path)

    assert second.generated_tree_sha256 != first.generated_tree_sha256
    assert not receipt.matches(
        "a" * 64,
        second.effective_schema_sha256,
        second.generated_tree_sha256,
        second.live_contracts_sha256,
    )


def test_valid_raw_live_contract_change_changes_combined_contract_hash(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _synthetic_artifacts(tmp_path, monkeypatch)
    first = verify_live_artifacts(tmp_path)
    safety_path = tmp_path / "contracts/operation-safety.yaml"
    safety_path.write_text(
        safety_path.read_text(encoding="utf-8").replace(
            "reviewed synthetic authentication",
            "reviewed synthetic authentication v2",
        ),
        encoding="utf-8",
    )

    second = verify_live_artifacts(tmp_path)

    assert second.effective_schema_sha256 == first.effective_schema_sha256
    assert second.generated_tree_sha256 == first.generated_tree_sha256
    assert second.live_contracts_sha256 != first.live_contracts_sha256


@pytest.mark.parametrize(
    "target",
    ["effective", "tree", "manifest", "manual-missing", "manual-symlink", "contract"],
)
def test_live_artifacts_fail_closed_when_missing_or_stale_before_http(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    _effective, package = _synthetic_artifacts(tmp_path, monkeypatch)
    if target == "effective":
        (tmp_path / "build/openapi/effective.json").write_text("{}\n", encoding="utf-8")
    elif target == "tree":
        (package / "__init__.py").write_text("changed\n", encoding="utf-8")
    elif target == "manifest":
        (tmp_path / "generator/generated-manifest.json").unlink()
    elif target == "manual-missing":
        (package / "_contracts/rate-limits.yaml").unlink()
    elif target == "manual-symlink":
        manual = package / "_contracts/rate-limits.yaml"
        manual.unlink()
        manual.symlink_to(package / "__init__.py")
    else:
        (tmp_path / "contracts/operation-safety.yaml").write_text(
            "version: invalid\n",
            encoding="utf-8",
        )

    with pytest.raises(SafetyError, match="artifact|verification|safety"):
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
        "version: 2\n"
        "defaults:\n"
        "  utilization: 0.20\n"
        "  global_min_interval_seconds: 30\n"
        "  max_calls_per_operation_per_run: 1\n"
        "operations:\n"
        "  authenticate:\n"
        "    test_budget:\n"
        "      min_interval_seconds: 30\n"
        "      source: synthetic\n"
        "      verified: false\n"
        "    server_limit:\n"
        "      calls: 1\n"
        "      per_seconds: 5\n"
        "      source: synthetic\n"
        "      verified: true\n",
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
            artifacts=LiveArtifactHashes("b" * 64, "c" * 64, "d" * 64),
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

    assert not finalize_live_receipt(
        receipt,
        path,
        live_reports_passed=True,
        circuit_closed=True,
        clients_closed=True,
        mutation_journals_clean=True,
    )
    assert not LiveReceipt.load(path).completed

    receipt = receipt.with_operation("get_organizations")
    receipt.write(path)

    assert finalize_live_receipt(
        receipt,
        path,
        live_reports_passed=True,
        circuit_closed=True,
        clients_closed=True,
        mutation_journals_clean=True,
    )
    assert LiveReceipt.load(path).completed


def test_receipt_completion_honors_required_verified_read_report_gate(
    tmp_path: Path,
) -> None:
    path = tmp_path / "receipt.json"
    receipt = LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="a" * 64,
        effective_schema_sha256="b" * 64,
        generated_tree_sha256="c" * 64,
        live_contracts_sha256="d" * 64,
        operations=("authenticate", "get_organizations"),
        had_429=False,
        completed=False,
    )
    receipt.write(path)
    gates = {
        "live_reports_passed": True,
        "circuit_closed": True,
        "clients_closed": True,
        "mutation_journals_clean": True,
    }

    assert not finalize_live_receipt(
        receipt,
        path,
        read_report_completed=False,
        **gates,
    )
    assert not LiveReceipt.load(path).completed
    assert finalize_live_receipt(
        receipt,
        path,
        read_report_completed=True,
        **gates,
    )


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
            artifacts=LiveArtifactHashes("b" * 64, "c" * 64, "d" * 64),
        )
    assert receipt.profile_fingerprint == profile.fingerprint
    assert path.exists()


def test_pytest_options_and_offline_collection_do_not_need_private_files() -> None:
    bytecode_before = set(Path("src/iikocloud_client").rglob("*.pyc"))
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
    assert set(Path("src/iikocloud_client").rglob("*.pyc")) == bytecode_before


@pytest.mark.parametrize(
    ("arguments", "mode", "message"),
    [
        (
            ("-m", "live_read_full", "tests/integration/read/test_all_reads.py"),
            "full",
            "single-process",
        ),
        (
            ("-m", "live_read_full", "-n0"),
            "full",
            "exact test path",
        ),
        (
            (
                "-m",
                "live_read_full",
                "-n0",
                "tests/integration/read/test_all_reads.py",
                "tests/pipeline/test_io.py",
            ),
            "full",
            "exact test path",
        ),
        (
            (
                "-m",
                "live_read_full or live_write",
                "-n0",
                "tests/integration/read/test_all_reads.py",
            ),
            "full",
            "exact marker",
        ),
        (
            (
                "-m",
                "live_read_full",
                "-n0",
                "--allow-live-write",
                "tests/integration/read/test_all_reads.py",
            ),
            "full",
            "write options",
        ),
        (
            (
                "-m",
                "live_read_full",
                "-n0",
                "--capture-http",
                "tests/integration/read/test_all_reads.py",
            ),
            "full",
            "capture",
        ),
        (
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--capture-http",
                "tests/integration/read/test_selected_read.py",
            ),
            "selected",
            "both capture",
        ),
        (
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--capture-operation",
                "get_organizations",
                "tests/integration/read/test_selected_read.py",
            ),
            "selected",
            "both capture",
        ),
    ],
)
def test_exact_live_read_invocation_rejects_unsafe_shapes(
    arguments: tuple[str, ...],
    mode: str,
    message: str,
) -> None:
    with pytest.raises(SafetyError, match=message):
        assert_exact_live_read_invocation(arguments, mode=mode)


def test_exact_live_read_invocation_accepts_only_the_two_reviewed_shapes() -> None:
    assert (
        assert_exact_live_read_invocation(
            (
                "-m",
                "live_read_full",
                "-n0",
                "--live-profile",
                "test-server",
                "--env-file",
                ".env",
                "tests/integration/read/test_all_reads.py",
            ),
            mode="full",
        )
        is None
    )
    assert (
        assert_exact_live_read_invocation(
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--live-profile",
                "test-server",
                "--env-file",
                ".env",
                "--capture-http",
                "--capture-operation",
                "get_organizations",
                "tests/integration/read/test_selected_read.py",
            ),
            mode="selected",
        )
        == "get_organizations"
    )


def test_exact_live_read_invocation_rejects_xdist_worker(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("PYTEST_XDIST_WORKER", "gw0")
    with pytest.raises(SafetyError, match="xdist worker"):
        assert_exact_live_read_invocation(
            (
                "-m",
                "live_read_full",
                "-n0",
                "tests/integration/read/test_all_reads.py",
            ),
            mode="full",
        )


def _read_case(operation_id: str) -> ReadCase:
    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=(),
        requires=(),
        provides=(),
        allowed_no_target_codes=frozenset(),
        binding=GeneratedReadBinding(
            api_module="iikocloud_client.api.synthetic_api",
            api_class="SyntheticApi",
            method_name=f"{operation_id}_with_http_info",
            request_module=None,
            request_class=None,
            request_keyword=None,
        ),
        build_values=lambda _view: NO_REQUEST,
        validate_response=lambda _data, _view: None,
        extract=lambda _data, _view: MappingProxyType({}),
    )


def _read_contracts(
    operation_ids: tuple[str, ...],
) -> tuple[
    OperationSafetyCatalog,
    Mapping[str, LiveOperation],
    RateCatalog,
    dict[str, object],
]:
    safety = OperationSafetyCatalog.from_mapping(
        {
            "version": 1,
            "operations": {
                operation_id: {
                    "effect": "read",
                    "live_policy": "automatic",
                    "reason": "reviewed synthetic read",
                }
                for operation_id in operation_ids
            },
        }
    )
    operations = MappingProxyType(
        {
            operation_id: LiveOperation(
                kind="read",
                cleanup=None,
                method="POST",
                path=f"/synthetic/{operation_id}",
            )
            for operation_id in operation_ids
        }
    )
    catalog = RateCatalog.from_mapping(
        {
            "version": 2,
            "defaults": {
                "utilization": 0.2,
                "global_min_interval_seconds": 30,
                "max_calls_per_operation_per_run": 1,
            },
            "operations": {
                operation_id: {
                    "test_budget": {
                        "min_interval_seconds": 30,
                        "source": "synthetic",
                        "verified": True,
                    },
                    "server_limit": None,
                }
                for operation_id in operation_ids
            },
        }
    )
    effective: dict[str, object] = {
        "paths": {
            f"/synthetic/{operation_id}": {"post": {"operationId": operation_id}}
            for operation_id in operation_ids
        }
    }
    return safety, operations, catalog, effective


def test_live_read_plan_preflight_returns_selected_closure_plus_canary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    operation_ids = ("get_organizations", "get_nomenclature")
    full_plan = ReadPlan.build(_read_case(value) for value in operation_ids)
    safety, operations, catalog, effective = _read_contracts(operation_ids)
    monkeypatch.setattr(GeneratedReadBinding, "resolve", lambda _self: object())

    full = validate_live_read_plan(
        full_plan,
        mode="full",
        selected_operation=None,
        safety=safety,
        operation_contract=operations,
        catalog=catalog,
        effective_schema=effective,
    )
    selected = validate_live_read_plan(
        full_plan,
        mode="selected",
        selected_operation="get_nomenclature",
        safety=safety,
        operation_contract=operations,
        catalog=catalog,
        effective_schema=effective,
    )

    assert full is full_plan
    assert selected.ordered_operation_ids == (
        "get_organizations",
        "get_nomenclature",
    )


def test_live_read_plan_preflight_rejects_any_four_way_parity_gap(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    operation_ids = ("get_organizations", "get_nomenclature")
    incomplete = ReadPlan.build((_read_case("get_organizations"),))
    safety, operations, catalog, effective = _read_contracts(operation_ids)
    monkeypatch.setattr(GeneratedReadBinding, "resolve", lambda _self: object())

    with pytest.raises(SafetyError, match="exact parity"):
        validate_live_read_plan(
            incomplete,
            mode="full",
            selected_operation=None,
            safety=safety,
            operation_contract=operations,
            catalog=catalog,
            effective_schema=effective,
        )


def test_real_repository_has_exact_executable_read_parity() -> None:
    root = Path.cwd()
    safety = OperationSafetyCatalog.load(root / "contracts/operation-safety.yaml")
    operations = load_operation_contract(root / "contracts/live-operations.yaml")
    catalog = RateCatalog.load(root / "contracts/rate-limits.yaml")
    effective = json.loads((root / "build/openapi/effective.json").read_text(encoding="utf-8"))

    validated = validate_live_read_plan(
        FULL_READ_PLAN,
        mode="full",
        selected_operation=None,
        safety=safety,
        operation_contract=operations,
        catalog=catalog,
        effective_schema=effective,
    )

    automatic_read_ids = safety.automatic_read_ids
    live_operation_ids = frozenset(operations)
    live_contract_read_ids = frozenset(
        operation_id for operation_id, operation in operations.items() if operation.kind == "read"
    )
    assert validated is FULL_READ_PLAN
    assert len(FULL_READ_PLAN.cases) == 91
    assert frozenset(FULL_READ_PLAN.ordered_operation_ids) == automatic_read_ids
    assert automatic_read_ids == live_contract_read_ids
    assert all(catalog.operation_budget(op) for op in automatic_read_ids)
    assert frozenset(catalog.operation_ids) <= live_operation_ids
    assert safety.operations["authenticate"].live_policy == "automatic"
    assert safety.operations["authenticate_v2"].live_policy == "blocked"
    assert "authenticate_v2" not in live_operation_ids


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [
        (
            (
                "-m",
                "live_read_full",
                "--live-profile",
                "test-server",
                "tests/integration/read/test_all_reads.py",
            ),
            "explicit single-process",
        ),
        (
            (
                "-m",
                "live_read_full",
                "-n0",
                "--live-profile",
                "test-server",
                "tests/pipeline/test_io.py",
            ),
            "exact test path",
        ),
        (
            (
                "-m",
                "live_read_full",
                "-n0",
                "--capture-http",
                "--live-profile",
                "test-server",
                "tests/integration/read/test_all_reads.py",
            ),
            "refuses capture",
        ),
        (
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--capture-http",
                "--live-profile",
                "test-server",
                "tests/integration/read/test_selected_read.py",
            ),
            "both capture options",
        ),
        (
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--capture-http",
                "--capture-operation",
                "unknown_synthetic_operation",
                "--live-profile",
                "test-server",
                "tests/integration/read/test_selected_read.py",
            ),
            "operation is unknown",
        ),
        (
            (
                "-m",
                "live_read_selected",
                "-n0",
                "--capture-http",
                "--capture-operation",
                "authenticate",
                "--live-profile",
                "test-server",
                "tests/integration/read/test_selected_read.py",
            ),
            "refuses authentication",
        ),
    ],
)
def test_invalid_live_read_commands_fail_during_collection_without_private_access(
    arguments: tuple[str, ...],
    expected: str,
) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment.pop("PYTEST_XDIST_WORKER", None)
    for name in ("IIKO_API_KEY", "IIKO_API_KEY_2"):
        environment.pop(name, None)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *arguments],
        cwd=Path.cwd(),
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )

    output = result.stdout + result.stderr
    assert result.returncode == int(pytest.ExitCode.USAGE_ERROR)
    assert expected in output
    assert "IIKO_API_KEY" not in output
    assert "private/profiles" not in output
