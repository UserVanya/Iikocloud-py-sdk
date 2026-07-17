from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.rates import LiveRateGuard, RateCatalog
from tools.openapi_pipeline.live.state import LiveStateStore


def test_429_opens_profile_circuit_until_manual_reset(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    store.record_status("profile-hash", "get_organizations", 429, now=100.0)
    with pytest.raises(SafetyError, match="circuit is open"):
        store.assert_circuit_closed("profile-hash")
    store.reset_circuit("profile-hash")
    store.assert_circuit_closed("profile-hash")


def _catalog(*, verified: bool = True) -> RateCatalog:
    return RateCatalog.from_mapping(
        {
            "version": 1,
            "defaults": {
                "utilization": 0.20,
                "global_min_interval_seconds": 15,
                "max_calls_per_operation_per_run": 1,
            },
            "operations": {
                "slow": {
                    "server_limit": {"calls": 1, "per_seconds": 60},
                    "source": "test-fixture",
                    "verified": verified,
                },
                "fast": {
                    "server_limit": {"calls": 100, "per_seconds": 60},
                    "source": "test-fixture",
                    "verified": True,
                },
            },
        }
    )


class FakeTime:
    def __init__(self, value: float = 100.0) -> None:
        self.wall = value
        self.monotonic = value
        self.sleeps: list[float] = []

    def wall_clock(self) -> float:
        return self.wall

    def monotonic_clock(self) -> float:
        return self.monotonic

    async def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.wall += seconds
        self.monotonic += seconds


def _guard(
    tmp_path: Path,
    fake: FakeTime,
    lock: LiveProcessLock,
    *,
    catalog: RateCatalog | None = None,
) -> LiveRateGuard:
    return LiveRateGuard(
        profile_fingerprint="profile-hash",
        catalog=catalog or _catalog(),
        state=LiveStateStore(tmp_path / "live.json"),
        process_lock=lock,
        wall_clock=fake.wall_clock,
        monotonic_clock=fake.monotonic_clock,
        sleeper=fake.sleep,
    )


@pytest.mark.asyncio
async def test_guard_requires_held_process_lock_before_other_checks(tmp_path: Path) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    guard = _guard(tmp_path, fake, lock)
    with pytest.raises(SafetyError, match="must be held"):
        await guard.acquire("missing")
    assert fake.sleeps == []
    assert not (tmp_path / "live.json").exists()


def test_state_accepts_only_the_exact_canonical_process_lock_path(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")

    for alternate in ("a.lock", "b.lock"):
        with pytest.raises(SafetyError, match="canonical.*live.lock"):
            store.bind_process_lock(LiveProcessLock(tmp_path / alternate))

    canonical = LiveProcessLock(tmp_path / "live.lock")
    store.bind_process_lock(canonical)
    with canonical:
        store.assert_circuit_closed("profile-hash", now=100)


def test_state_rejects_canonical_lock_path_through_symlink_before_io(
    tmp_path: Path,
) -> None:
    target = tmp_path / "target.lock"
    target.touch(mode=0o600)
    canonical = tmp_path / "live.lock"
    canonical.symlink_to(target)
    store = LiveStateStore(tmp_path / "live.json")

    with pytest.raises(SafetyError, match="symlink"):
        store.bind_process_lock(LiveProcessLock(canonical))

    assert not (tmp_path / "live.json").exists()


@pytest.mark.asyncio
async def test_unknown_and_unverified_operations_do_not_sleep_or_mutate(tmp_path: Path) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        guard = _guard(tmp_path, fake, lock, catalog=_catalog(verified=False))
        with pytest.raises(SafetyError, match="Unknown live operation"):
            await guard.acquire("missing")
        with pytest.raises(SafetyError, match="not verified"):
            await guard.acquire("slow")
    assert fake.sleeps == []
    assert not (tmp_path / "live.json").exists()


@pytest.mark.asyncio
async def test_guard_enforces_one_call_per_run_across_http_failures(tmp_path: Path) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        guard = _guard(tmp_path, fake, lock)
        await guard.acquire("fast")
        guard.record_status("fast", 500)
        with pytest.raises(SafetyError, match="already acquired"):
            await guard.acquire("fast")
    assert fake.sleeps == []


@pytest.mark.asyncio
async def test_guard_persists_global_and_operation_intervals_across_instances(
    tmp_path: Path,
) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        await _guard(tmp_path, fake, lock).acquire("slow")
        await _guard(tmp_path, fake, lock).acquire("fast")
        await _guard(tmp_path, fake, lock).acquire("slow")
    assert fake.sleeps == [15.0, 285.0]


@pytest.mark.asyncio
async def test_guard_sleeps_once_for_maximum_required_interval(tmp_path: Path) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        await _guard(tmp_path, fake, lock).acquire("slow")
        fake.wall += 1
        fake.monotonic += 1
        await _guard(tmp_path, fake, lock).acquire("slow")
    assert fake.sleeps == [299.0]


@pytest.mark.asyncio
async def test_sleep_failure_does_not_reserve_persistent_call(tmp_path: Path) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        await _guard(tmp_path, fake, lock).acquire("slow")
    before = (tmp_path / "live.json").read_bytes()

    async def fail_sleep(seconds: float) -> NoReturn:
        raise RuntimeError(f"synthetic sleep failure after request for {seconds}")

    with lock:
        guard = LiveRateGuard(
            profile_fingerprint="profile-hash",
            catalog=_catalog(),
            state=LiveStateStore(tmp_path / "live.json"),
            process_lock=lock,
            wall_clock=fake.wall_clock,
            monotonic_clock=fake.monotonic_clock,
            sleeper=fail_sleep,
        )
        with pytest.raises(RuntimeError, match="synthetic sleep failure"):
            await guard.acquire("slow")
    assert (tmp_path / "live.json").read_bytes() == before


@pytest.mark.asyncio
async def test_wall_clock_rollback_after_sleep_fails_without_reservation(
    tmp_path: Path,
) -> None:
    fake = FakeTime()
    lock = LiveProcessLock(tmp_path / "live.lock")
    with lock:
        await _guard(tmp_path, fake, lock).acquire("slow")
    before = (tmp_path / "live.json").read_bytes()

    async def roll_back(seconds: float) -> None:
        fake.monotonic += seconds
        fake.wall -= 1

    with lock:
        guard = LiveRateGuard(
            profile_fingerprint="profile-hash",
            catalog=_catalog(),
            state=LiveStateStore(tmp_path / "live.json"),
            process_lock=lock,
            wall_clock=fake.wall_clock,
            monotonic_clock=fake.monotonic_clock,
            sleeper=roll_back,
        )
        with pytest.raises(SafetyError, match="wall clock moved backwards"):
            await guard.acquire("slow")
    assert (tmp_path / "live.json").read_bytes() == before


def test_non_429_status_never_closes_circuit(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    store.record_status("profile-hash", "slow", 429, now=100)
    before = (tmp_path / "live.json").read_bytes()
    store.record_status("profile-hash", "slow", 200, now=101)
    assert (tmp_path / "live.json").read_bytes() == before
    assert store.circuit_is_open("profile-hash")


def test_429_circuit_is_global_to_profile(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    store.record_status("profile-hash", "slow", 429, now=100)
    with pytest.raises(SafetyError, match="circuit is open"):
        store.assert_circuit_closed("profile-hash", now=101)
    store.assert_circuit_closed("another-profile", now=101)


def test_state_is_canonical_private_json_without_credentials(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    store.record_status("profile-hash", "slow", 429, now=100)
    path = tmp_path / "live.json"
    parsed = json.loads(path.read_text(encoding="utf-8"))
    assert path.read_bytes() == canonical_json_bytes(parsed)
    assert path.stat().st_mode & 0o777 == 0o600
    assert tmp_path.stat().st_mode & 0o777 == 0o700
    assert "token" not in path.read_text(encoding="utf-8").lower()
    assert "login" not in path.read_text(encoding="utf-8").lower()


@pytest.mark.parametrize(
    "body",
    [
        b"not-json\n",
        b'{"profiles":{},"extra":true}\n',
        b'{"profiles":{"p":{"circuit_opened_at":null,"last_calls":{},"extra":1}}}\n',
        b'{"profiles":{"p":{"circuit_opened_at":null,"last_calls":{"op":-1}}}}\n',
        b'{"profiles":{"p":{"circuit_opened_at":null,"last_calls":{"op":NaN}}}}\n',
        b'{ "profiles": {} }\n',
    ],
)
def test_state_rejects_corruption_unknown_shape_and_noncanonical_json(
    tmp_path: Path, body: bytes
) -> None:
    path = tmp_path / "live.json"
    path.write_bytes(body)
    path.chmod(0o600)
    with pytest.raises(SafetyError, match="live state"):
        LiveStateStore(path).circuit_is_open("profile-hash")


def test_state_rejects_future_persistent_timestamp(tmp_path: Path) -> None:
    path = tmp_path / "live.json"
    value = {
        "profiles": {
            "profile-hash": {
                "circuit_opened_at": None,
                "last_calls": {"slow": 101.0},
            }
        }
    }
    path.write_bytes(canonical_json_bytes(value))
    path.chmod(0o600)
    with pytest.raises(SafetyError, match="future"):
        LiveStateStore(path).assert_circuit_closed("profile-hash", now=100)


def test_state_rejects_unsafe_identifiers(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    with pytest.raises(SafetyError, match="profile fingerprint"):
        store.record_status("../profile", "slow", 429, now=100)
    with pytest.raises(SafetyError, match="operation ID"):
        store.record_status("profile", "x" * 129, 429, now=100)


def test_state_rejects_symlink_special_file_and_wide_permissions(tmp_path: Path) -> None:
    target = tmp_path / "target.json"
    target.write_bytes(canonical_json_bytes({"profiles": {}}))
    target.chmod(0o600)
    symlink = tmp_path / "live.json"
    symlink.symlink_to(target)
    with pytest.raises(SafetyError, match="symlink"):
        LiveStateStore(symlink).circuit_is_open("profile")
    symlink.unlink()

    path = tmp_path / "live.json"
    path.write_bytes(canonical_json_bytes({"profiles": {}}))
    path.chmod(0o644)
    with pytest.raises(SafetyError, match="0600"):
        LiveStateStore(path).circuit_is_open("profile")
    path.unlink()
    os.mkfifo(path, mode=0o600)
    with pytest.raises(SafetyError, match="regular file"):
        LiveStateStore(path).circuit_is_open("profile")


def test_private_parent_permissions_fail_closed(tmp_path: Path) -> None:
    state_dir = tmp_path / "state"
    state_dir.mkdir(mode=0o755)
    with pytest.raises(SafetyError, match="0700"):
        LiveStateStore(state_dir / "live.json").circuit_is_open("profile")
    with pytest.raises(SafetyError, match="0700"):
        LiveProcessLock(state_dir / "live.lock").acquire()


def test_lock_rejects_second_independent_fd_in_same_process(tmp_path: Path) -> None:
    first = LiveProcessLock(tmp_path / "live.lock")
    second = LiveProcessLock(tmp_path / "live.lock")
    with first:
        assert first.held
        with pytest.raises(SafetyError, match="another live test process is active"):
            second.acquire()
        assert not second.held
    assert not first.held


def test_lock_public_binding_check_rejects_replaced_current_inode(tmp_path: Path) -> None:
    path = tmp_path / "live.lock"
    displaced = tmp_path / "displaced.lock"
    first = LiveProcessLock(path)
    replacement = LiveProcessLock(path)
    first.acquire()
    try:
        assert callable(getattr(first, "assert_current_binding", None))
        first.assert_current_binding()
        path.rename(displaced)
        replacement.acquire()
        try:
            replacement.assert_current_binding()
            with pytest.raises(SafetyError, match="binding|inode|changed"):
                first.assert_current_binding()
        finally:
            replacement.release()
    finally:
        first.release()


def test_lock_is_exclusive_across_processes(tmp_path: Path) -> None:
    path = tmp_path / "live.lock"
    with LiveProcessLock(path):
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "from pathlib import Path; "
                    "from tools.openapi_pipeline.live.lock import LiveProcessLock; "
                    "LiveProcessLock(Path(__import__('sys').argv[1])).acquire()"
                ),
                str(path),
            ],
            cwd=Path.cwd(),
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode != 0
    assert "another live test process is active" in result.stderr


def test_lock_cleanup_on_context_exception(tmp_path: Path) -> None:
    lock = LiveProcessLock(tmp_path / "live.lock")
    with pytest.raises(RuntimeError, match="boom"), lock:
        raise RuntimeError("boom")
    assert not lock.held
    with LiveProcessLock(tmp_path / "live.lock") as reacquired:
        assert reacquired.held


def test_lock_rejects_symlink_and_wide_existing_file(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.touch(mode=0o600)
    path = tmp_path / "live.lock"
    path.symlink_to(target)
    with pytest.raises(SafetyError, match="symlink"):
        LiveProcessLock(path).acquire()
    path.unlink()
    path.touch(mode=0o644)
    with pytest.raises(SafetyError, match="0600"):
        LiveProcessLock(path).acquire()
