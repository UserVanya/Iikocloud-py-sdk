from __future__ import annotations

import os
import re
import stat
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from ..errors import SafetyError
from .lock import LiveProcessLock, ensure_private_directory
from .profile import (
    ResolvedDiscoveryProfile,
    ResolvedLiveProfile,
    is_safe_profile_name,
    load_discovery_profile,
    load_profile,
)
from .rates import RateCatalog
from .receipt import LiveArtifactHashes, LiveReceipt, verify_live_artifacts

_RUN_ID = re.compile(r"[0-9]{8}T[0-9]{6}Z-[a-f0-9]{8,32}\Z")


@dataclass(frozen=True)
class LivePreflight:
    catalog: RateCatalog
    artifacts: LiveArtifactHashes


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
) -> LivePreflight:
    """Fail disabled/artifact gates without reading a profile or environment file."""
    assert_serial_live_invocation(invocation_args)
    catalog = RateCatalog.load(root / "contracts/rate-limits.yaml")
    catalog.operation_budget("authenticate")
    artifacts = verify_live_artifacts(root)
    return LivePreflight(catalog=catalog, artifacts=artifacts)


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
