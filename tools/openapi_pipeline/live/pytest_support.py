from __future__ import annotations

import json
import os
import re
import stat
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..errors import SafetyError
from ..io import sha256_bytes
from .lock import LiveProcessLock, ensure_private_directory
from .profile import (
    ResolvedDiscoveryProfile,
    ResolvedLiveProfile,
    is_safe_profile_name,
    load_discovery_profile,
    load_profile,
)
from .rates import RateCatalog
from .read_planner import ReadPlan
from .receipt import LiveArtifactHashes, LiveReceipt, verify_live_artifacts
from .safety import OperationSafetyCatalog
from .session import LiveOperation, load_operation_contract

_RUN_ID = re.compile(r"[0-9]{8}T[0-9]{6}Z-[a-f0-9]{8,32}\Z")
_READ_MODES = frozenset({"full", "selected"})
_READ_MARKERS = {
    "full": "live_read_full",
    "selected": "live_read_selected",
}
_READ_PATHS = {
    "full": "tests/integration/read/test_all_reads.py",
    "selected": "tests/integration/read/test_selected_read.py",
}
_SAFE_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")


@dataclass(frozen=True)
class LivePreflight:
    catalog: RateCatalog
    artifacts: LiveArtifactHashes
    safety: OperationSafetyCatalog | None = None
    operation_contract: Mapping[str, LiveOperation] | None = None
    effective_schema: dict[str, Any] | None = None
    read_plan: ReadPlan | None = None
    read_mode: str | None = None
    selected_operation: str | None = None


def _option_values(arguments: tuple[str, ...], option: str) -> tuple[str, ...]:
    values: list[str] = []
    for index, argument in enumerate(arguments):
        if argument == option:
            if index + 1 == len(arguments):
                raise SafetyError(f"{option} requires a value")
            values.append(arguments[index + 1])
        elif argument.startswith(f"{option}="):
            values.append(argument.partition("=")[2])
    return tuple(values)


def assert_exact_live_read_invocation(
    arguments: Sequence[str],
    *,
    mode: str,
) -> str | None:
    """Validate one reviewed full/selected pytest command without private access."""

    if type(mode) is not str or mode not in _READ_MODES:
        raise SafetyError("Live read mode is invalid")
    assert_serial_live_invocation(arguments)
    args = tuple(arguments)

    marker_values = (*_option_values(args, "-m"), *_option_values(args, "--markexpr"))
    expected_marker = _READ_MARKERS[mode]
    if marker_values != (expected_marker,):
        raise SafetyError(f"Live read {mode} requires its exact marker expression")

    expected_path = _READ_PATHS[mode]
    supplied_paths = tuple(
        argument
        for argument in args
        if argument.startswith("tests/") or argument.endswith(".py")
    )
    if supplied_paths != (expected_path,):
        raise SafetyError(f"Live read {mode} requires its exact test path")

    write_options = {
        "--allow-live-write",
        "--allow-audit-residue",
        "--target-organization",
    }
    if any(
        argument in write_options
        or any(argument.startswith(f"{option}=") for option in write_options)
        for argument in args
    ):
        raise SafetyError("Live read commands refuse live write options")

    capture_http_count = args.count("--capture-http")
    capture_operations = _option_values(args, "--capture-operation")
    if mode == "full":
        if capture_http_count or capture_operations:
            raise SafetyError("Full live read refuses capture options")
        return None

    if capture_http_count != 1 or len(capture_operations) != 1:
        raise SafetyError("Selected live read requires both capture options exactly once")
    selected = capture_operations[0]
    if _SAFE_OPERATION_ID.fullmatch(selected) is None:
        raise SafetyError("Selected live read capture operation is invalid")
    return selected


def _load_verified_effective_schema(
    root: Path,
    artifacts: LiveArtifactHashes,
) -> dict[str, Any]:
    path = root / "build/openapi/effective.json"
    load_failed = False
    value: object = None
    body = b""
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise OSError
        body = path.read_bytes()
        if len(body) > 256 * 1024 * 1024:
            raise OSError
        value = json.loads(body)
    except (OSError, UnicodeError, ValueError):
        load_failed = True
    if load_failed or type(value) is not dict:
        raise SafetyError("Verified effective OpenAPI artifact cannot be loaded") from None
    if sha256_bytes(body) != artifacts.effective_schema_sha256:
        raise SafetyError("Verified effective OpenAPI artifact hash changed")
    return value


def _selected_plan(full_plan: ReadPlan, operation_id: str) -> ReadPlan:
    selected_ids = set(full_plan.dependency_closure(operation_id).ordered_operation_ids)
    canary_ids = set(
        full_plan.dependency_closure("get_organizations").ordered_operation_ids
    )
    selected_ids.update(canary_ids)
    combined = ReadPlan.build(
        case for case in full_plan.cases if case.operation_id in selected_ids
    )
    canary_first = tuple(
        case for case in combined.cases if case.operation_id in canary_ids
    ) + tuple(case for case in combined.cases if case.operation_id not in canary_ids)
    return ReadPlan._from_ordered_cases(canary_first)


def validate_live_read_plan(
    full_plan: ReadPlan,
    *,
    mode: str,
    selected_operation: str | None,
    safety: OperationSafetyCatalog,
    operation_contract: Mapping[str, LiveOperation],
    catalog: RateCatalog,
    effective_schema: dict[str, Any],
) -> ReadPlan:
    """Validate four-way read parity and return the exact executable plan."""

    if type(full_plan) is not ReadPlan or type(mode) is not str or mode not in _READ_MODES:
        raise SafetyError("Live read plan preflight is invalid")
    if not isinstance(operation_contract, Mapping) or type(effective_schema) is not dict:
        raise SafetyError("Live read contracts are invalid")

    safety.assert_matches_openapi(effective_schema)
    automatic_read_ids = safety.automatic_read_ids
    allowlisted_read_ids = frozenset(
        operation_id
        for operation_id, operation in operation_contract.items()
        if type(operation) is LiveOperation and operation.kind == "read"
    )
    registered_ids = frozenset(full_plan.ordered_operation_ids)
    if not automatic_read_ids or not (
        automatic_read_ids == allowlisted_read_ids == registered_ids
    ):
        raise SafetyError("Live read operation sets do not have exact parity")
    if not set(catalog.operation_ids).issubset(operation_contract):
        raise SafetyError("Live rate catalog contains an unallowlisted operation")

    for operation_id in sorted(automatic_read_ids):
        catalog.operation_budget(operation_id)
        case = full_plan.case_for(operation_id)
        binding_failed = False
        try:
            case.binding.resolve()
        except Exception:
            binding_failed = True
        if binding_failed:
            raise SafetyError("Live read generated binding resolution failed") from None

    if mode == "full":
        if selected_operation is not None:
            raise SafetyError("Full live read cannot select one operation")
        return full_plan

    if type(selected_operation) is not str:
        raise SafetyError("Selected live read requires one operation")
    safety_entry = safety.operations.get(selected_operation)
    if safety_entry is None:
        raise SafetyError("Selected live read operation is unknown")
    if safety_entry.effect == "auth":
        raise SafetyError("Selected live read refuses authentication operations")
    if safety_entry.effect != "read" or safety_entry.live_policy != "automatic":
        raise SafetyError("Selected live read operation is not an automatic read")
    operation = operation_contract.get(selected_operation)
    if type(operation) is not LiveOperation or operation.kind != "read":
        raise SafetyError("Selected live read operation is not allowlisted")
    catalog.operation_budget(selected_operation)
    full_plan.case_for(selected_operation)
    return _selected_plan(full_plan, selected_operation)


def assert_serial_live_invocation(arguments: Sequence[str]) -> None:
    if os.environ.get("PYTEST_XDIST_WORKER"):
        raise SafetyError("Live tests cannot run inside an xdist worker")
    args = tuple(arguments)
    explicit_n0 = (
        "-n0" in args
        or "--numprocesses=0" in args
        or any(args[index : index + 2] == ("-n", "0") for index in range(len(args) - 1))
    )
    if not explicit_n0:
        raise SafetyError("Live tests require an explicit single-process -n0 invocation")
    for index, argument in enumerate(args):
        if argument == "-n":
            if index + 1 == len(args) or args[index + 1] != "0":
                raise SafetyError("Live tests refuse parallel xdist execution")
            continue
        if argument.startswith("-n") and argument != "-n0":
            raise SafetyError("Live tests refuse parallel xdist execution")
        if argument == "--numprocesses" and (index + 1 == len(args) or args[index + 1] != "0"):
            raise SafetyError("Live tests refuse parallel xdist execution")
        if argument.startswith("--numprocesses=") and argument != "--numprocesses=0":
            raise SafetyError("Live tests refuse parallel xdist execution")


def _existing_private_directory(path: Path, *, label: str) -> None:
    try:
        metadata = path.lstat()
    except FileNotFoundError as error:
        raise SafetyError(f"{label} is missing: {path}") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError(f"{label} must be a non-symlink directory: {path}")
    if stat.S_IMODE(metadata.st_mode) != 0o700:
        raise SafetyError(f"{label} must have mode 0700: {path}")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user: {path}")


def profile_path_for_name(root: Path, name: object) -> Path:
    if not is_safe_profile_name(name):
        raise SafetyError("--live-profile must be a safe lowercase profile name")
    private = root / "private"
    profiles = private / "profiles"
    _existing_private_directory(private, label="Private directory")
    _existing_private_directory(profiles, label="Private profile directory")
    path = profiles / f"{name}.toml"
    expected = Path(os.path.abspath(path))
    if path.resolve(strict=False) != expected:
        raise SafetyError("Live profile path must resolve inside private/profiles")
    return path


def explicit_env_path(root: Path, value: object, *, cwd: Path | None = None) -> Path | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise SafetyError("--env-file must name the repository root .env")
    supplied = Path(value)
    if not supplied.is_absolute():
        supplied = (cwd or Path.cwd()) / supplied
    supplied = Path(os.path.abspath(supplied))
    expected = Path(os.path.abspath(root / ".env"))
    if supplied != expected or supplied.resolve(strict=False) != expected:
        raise SafetyError("--env-file must resolve exactly to the repository root .env")
    return expected


def prepare_live_preflight(
    root: Path,
    *,
    invocation_args: Sequence[str],
    read_plan: ReadPlan | None = None,
    read_mode: str | None = None,
    selected_operation: str | None = None,
) -> LivePreflight:
    """Fail disabled/artifact gates without reading a profile or environment file."""
    assert_serial_live_invocation(invocation_args)
    if (read_plan is None) != (read_mode is None):
        raise SafetyError("Live read preflight requires both a plan and mode")
    if read_mode is not None:
        selected_from_arguments = assert_exact_live_read_invocation(
            invocation_args,
            mode=read_mode,
        )
        if selected_operation != selected_from_arguments:
            raise SafetyError("Live read selection does not match the reviewed command")
    catalog = RateCatalog.load(root / "contracts/rate-limits.yaml")
    catalog.operation_budget("authenticate")
    artifacts = verify_live_artifacts(root)
    safety = OperationSafetyCatalog.load(root / "contracts/operation-safety.yaml")
    operation_contract = load_operation_contract(root / "contracts/live-operations.yaml")
    effective_schema = _load_verified_effective_schema(root, artifacts)
    executable_plan = (
        validate_live_read_plan(
            read_plan,
            mode=read_mode,
            selected_operation=selected_operation,
            safety=safety,
            operation_contract=operation_contract,
            catalog=catalog,
            effective_schema=effective_schema,
        )
        if read_plan is not None and read_mode is not None
        else None
    )
    return LivePreflight(
        catalog=catalog,
        artifacts=artifacts,
        safety=safety,
        operation_contract=operation_contract,
        effective_schema=effective_schema,
        read_plan=executable_plan,
        read_mode=read_mode,
        selected_operation=selected_operation,
    )


def _assert_canonical_held_lock(
    root: Path,
    process_lock: LiveProcessLock,
) -> None:
    expected = root / ".state/live.lock"
    if process_lock.path != expected or not process_lock.held:
        raise SafetyError(
            f"Canonical live process lock must be held before private live setup: {expected}"
        )


def resolve_locked_live_profile(
    root: Path,
    *,
    process_lock: LiveProcessLock,
    profile_name: object,
    env_file_option: object,
    cwd: Path | None = None,
) -> ResolvedLiveProfile:
    _assert_canonical_held_lock(root, process_lock)
    profile_path = profile_path_for_name(root, profile_name)
    env_file = explicit_env_path(root, env_file_option, cwd=cwd)
    return load_profile(
        profile_path,
        env_file=env_file,
        required_api_login_env="IIKO_API_KEY",
    )


def resolve_locked_discovery_profile(
    root: Path,
    *,
    process_lock: LiveProcessLock,
    profile_name: object,
    env_file_option: object,
    cwd: Path | None = None,
) -> ResolvedDiscoveryProfile:
    _assert_canonical_held_lock(root, process_lock)
    profile_path = profile_path_for_name(root, profile_name)
    env_file = explicit_env_path(root, env_file_option, cwd=cwd)
    return load_discovery_profile(
        profile_path,
        env_file=env_file,
        required_api_login_env="IIKO_API_KEY",
    )


def mutation_journals_absent(state_root: Path) -> bool:
    path = state_root / "mutations"
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return True
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        return False
    return not any(path.iterdir())


def finalize_live_receipt(
    receipt: LiveReceipt,
    path: Path,
    *,
    live_reports_passed: bool,
    circuit_closed: bool,
    clients_closed: bool,
    mutation_journals_clean: bool,
    read_report_completed: bool | None = None,
) -> bool:
    if not (
        live_reports_passed
        and circuit_closed
        and clients_closed
        and mutation_journals_clean
        and (read_report_completed is None or read_report_completed is True)
        and not receipt.had_429
        and receipt.has_required_read_canary
    ):
        return False
    completed = receipt.as_completed()
    completed.write(path)
    return True


def initialize_receipt(
    state_root: Path,
    *,
    process_lock: LiveProcessLock,
    run_id: str,
    profile: ResolvedLiveProfile,
    artifacts: LiveArtifactHashes,
) -> tuple[LiveReceipt, Path]:
    _assert_canonical_held_lock(state_root.parent, process_lock)
    if _RUN_ID.fullmatch(run_id) is None:
        raise SafetyError("Generated live run ID is invalid")
    runs = state_root / "live-runs"
    ensure_private_directory(runs)
    path = runs / f"{run_id}.json"
    receipt = LiveReceipt(
        run_id=run_id,
        profile_fingerprint=profile.fingerprint,
        effective_schema_sha256=artifacts.effective_schema_sha256,
        generated_tree_sha256=artifacts.generated_tree_sha256,
        live_contracts_sha256=artifacts.live_contracts_sha256,
        operations=(),
        had_429=False,
        completed=False,
    )
    receipt.write(path)
    return receipt, path
