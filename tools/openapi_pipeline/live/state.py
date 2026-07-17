from __future__ import annotations

import json
import math
import os
import re
import stat
import time
from collections.abc import Iterator
from contextlib import contextmanager, suppress
from pathlib import Path
from typing import Any

from ..errors import SafetyError
from ..io import canonical_json_bytes, write_json_atomic
from .lock import (
    LiveProcessLock,
    ensure_private_directory,
    validate_private_regular_file,
)

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_MAX_STATE_BYTES = 1024 * 1024


def _identifier(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise SafetyError(f"{label} must be a safe ASCII string of 1 to 128 characters")
    return value


def _timestamp(value: object, *, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SafetyError(f"live state {label} must be a finite non-negative number")
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise SafetyError(f"live state {label} must be a finite non-negative number")
    return result


def _exact_keys(value: dict[object, object], expected: set[str], *, label: str) -> None:
    if set(value) != expected or any(not isinstance(key, str) for key in value):
        wanted = ", ".join(sorted(expected))
        raise SafetyError(f"live state {label} keys must be exactly: {wanted}")


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


class LiveStateStore:
    """Canonical credential-free persistent state, serialized by a process lock."""

    def __init__(self, path: Path, process_lock: LiveProcessLock | None = None) -> None:
        self.path = path
        self._process_lock = process_lock
        if process_lock is not None:
            self._validate_lock_location(process_lock)

    def _validate_lock_location(self, lock: LiveProcessLock) -> None:
        if lock.path.parent.absolute() != self.path.parent.absolute():
            raise SafetyError("live state and process lock must use the same private directory")

    def bind_process_lock(self, lock: LiveProcessLock) -> None:
        self._validate_lock_location(lock)
        if self._process_lock is not None and self._process_lock is not lock:
            raise SafetyError("live state is already bound to a different process lock")
        self._process_lock = lock

    @contextmanager
    def _coordinated(self, lock: LiveProcessLock | None) -> Iterator[None]:
        selected = lock or self._process_lock
        if selected is not None:
            self._validate_lock_location(selected)
            if not selected.held:
                raise SafetyError("live process lock must be held before accessing live state")
            yield
            return
        with LiveProcessLock(self.path.parent / "live.lock"):
            yield

    def _read_bytes(self) -> bytes | None:
        ensure_private_directory(self.path.parent)
        try:
            expected = validate_private_regular_file(self.path, label="Live state file")
        except FileNotFoundError:
            return None
        flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
        try:
            fd = os.open(self.path, flags)
        except OSError as error:
            raise SafetyError(f"Cannot open live state safely: {self.path}") from error
        try:
            actual = os.fstat(fd)
            if not stat.S_ISREG(actual.st_mode):
                raise SafetyError(f"Live state file is not a regular file: {self.path}")
            if stat.S_IMODE(actual.st_mode) != 0o600:
                raise SafetyError(f"Live state file must have mode 0600: {self.path}")
            if actual.st_uid != os.getuid() or actual.st_nlink != 1:
                raise SafetyError(
                    f"Live state file ownership or link count is unsafe: {self.path}"
                )
            if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
                raise SafetyError("Live state file changed while it was being opened")
            chunks: list[bytes] = []
            remaining = _MAX_STATE_BYTES + 1
            while remaining > 0:
                chunk = os.read(fd, min(65536, remaining))
                if not chunk:
                    break
                chunks.append(chunk)
                remaining -= len(chunk)
            body = b"".join(chunks)
            if len(body) > _MAX_STATE_BYTES:
                raise SafetyError(f"Live state is larger than {_MAX_STATE_BYTES} bytes")
            return body
        finally:
            os.close(fd)

    def _load(self, *, now: float | None = None) -> dict[str, Any]:
        body = self._read_bytes()
        if body is None:
            return {"profiles": {}}
        try:
            text = body.decode("utf-8")
            raw = json.loads(
                text,
                parse_constant=_reject_constant,
                object_pairs_hook=_unique_object,
            )
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
            raise SafetyError(
                f"live state is corrupt or not valid strict JSON: {self.path}"
            ) from error
        if body != canonical_json_bytes(raw):
            raise SafetyError(f"live state is not canonical JSON: {self.path}")
        state = self._validate_shape(raw)
        if now is not None:
            checked_now = _timestamp(now, label="wall clock")
            for profile in state["profiles"].values():
                opened = profile["circuit_opened_at"]
                if opened is not None and opened > checked_now:
                    raise SafetyError("live state contains a future circuit timestamp")
                if any(timestamp > checked_now for timestamp in profile["last_calls"].values()):
                    raise SafetyError("live state contains a future call timestamp")
        return state

    def _validate_shape(self, raw: object) -> dict[str, Any]:
        if not isinstance(raw, dict):
            raise SafetyError("live state root must be an object")
        _exact_keys(raw, {"profiles"}, label="root")
        raw_profiles = raw["profiles"]
        if not isinstance(raw_profiles, dict):
            raise SafetyError("live state profiles must be an object")
        profiles: dict[str, Any] = {}
        for raw_profile_id, raw_profile in sorted(raw_profiles.items()):
            profile_id = _identifier(raw_profile_id, label="profile fingerprint")
            if not isinstance(raw_profile, dict):
                raise SafetyError(f"live state profile {profile_id!r} must be an object")
            _exact_keys(
                raw_profile,
                {"circuit_opened_at", "last_calls"},
                label=f"profile {profile_id!r}",
            )
            opened = raw_profile["circuit_opened_at"]
            if opened is not None:
                opened = _timestamp(opened, label="circuit timestamp")
            raw_calls = raw_profile["last_calls"]
            if not isinstance(raw_calls, dict):
                raise SafetyError(f"live state last_calls for {profile_id!r} must be an object")
            calls: dict[str, float] = {}
            for raw_operation_id, raw_call in sorted(raw_calls.items()):
                operation_id = _identifier(raw_operation_id, label="operation ID")
                calls[operation_id] = _timestamp(raw_call, label="call timestamp")
            profiles[profile_id] = {
                "circuit_opened_at": opened,
                "last_calls": calls,
            }
        return {"profiles": profiles}

    def _write(self, state: dict[str, Any]) -> None:
        validated = self._validate_shape(state)
        ensure_private_directory(self.path.parent)
        with suppress(FileNotFoundError):
            validate_private_regular_file(self.path, label="Live state file")
        write_json_atomic(self.path, validated, mode=0o600)
        validate_private_regular_file(self.path, label="Live state file")

    @staticmethod
    def _profile(state: dict[str, Any], profile_id: str) -> dict[str, Any] | None:
        value = state["profiles"].get(profile_id)
        return value if isinstance(value, dict) else None

    def assert_circuit_closed(
        self,
        profile_fingerprint: str,
        *,
        now: float | None = None,
        lock: LiveProcessLock | None = None,
    ) -> None:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        with self._coordinated(lock):
            state = self._load(now=time.time() if now is None else now)
            profile = self._profile(state, profile_id)
            if profile is not None and profile["circuit_opened_at"] is not None:
                raise SafetyError(
                    f"live circuit is open for profile {profile_id!r}; "
                    "investigate and reset manually"
                )

    def circuit_is_open(
        self,
        profile_fingerprint: str,
        *,
        now: float | None = None,
        lock: LiveProcessLock | None = None,
    ) -> bool:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        with self._coordinated(lock):
            state = self._load(now=time.time() if now is None else now)
            profile = self._profile(state, profile_id)
            return profile is not None and profile["circuit_opened_at"] is not None

    def record_status(
        self,
        profile_fingerprint: str,
        operation_id: str,
        status: int,
        *,
        now: float | None = None,
        lock: LiveProcessLock | None = None,
    ) -> None:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        _identifier(operation_id, label="operation ID")
        if type(status) is not int or status < 0 or status > 599:
            raise SafetyError("HTTP status must be an integer from 0 through 599")
        checked_now = _timestamp(time.time() if now is None else now, label="wall clock")
        with self._coordinated(lock):
            state = self._load(now=checked_now)
            if status != 429:
                return
            profile = self._profile(state, profile_id)
            if profile is None:
                profile = {"circuit_opened_at": None, "last_calls": {}}
                state["profiles"][profile_id] = profile
            if profile["circuit_opened_at"] is None:
                profile["circuit_opened_at"] = checked_now
                self._write(state)

    def reset_circuit(
        self,
        profile_fingerprint: str,
        *,
        lock: LiveProcessLock | None = None,
    ) -> None:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        with self._coordinated(lock):
            state = self._load()
            profile = self._profile(state, profile_id)
            if profile is not None and profile["circuit_opened_at"] is not None:
                profile["circuit_opened_at"] = None
                self._write(state)

    def required_wait(
        self,
        profile_fingerprint: str,
        operation_id: str,
        *,
        now: float,
        global_interval_seconds: float,
        operation_interval_seconds: float,
        lock: LiveProcessLock | None = None,
    ) -> float:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        operation_id = _identifier(operation_id, label="operation ID")
        checked_now = _timestamp(now, label="wall clock")
        global_interval = _timestamp(global_interval_seconds, label="global interval")
        operation_interval = _timestamp(operation_interval_seconds, label="operation interval")
        if global_interval < 15 or operation_interval < global_interval:
            raise SafetyError("live call intervals are below the configured safety floor")
        if lock is None and self._process_lock is None:
            raise SafetyError("persistent rate calculation requires a shared held process lock")
        with self._coordinated(lock):
            state = self._load(now=checked_now)
            profile = self._profile(state, profile_id)
            if profile is None:
                return 0.0
            if profile["circuit_opened_at"] is not None:
                raise SafetyError(f"live circuit is open for profile {profile_id!r}")
            calls: dict[str, float] = profile["last_calls"]
            global_last = max(calls.values(), default=None)
            global_wait = (
                0.0
                if global_last is None
                else max(0.0, global_last + global_interval - checked_now)
            )
            operation_last = calls.get(operation_id)
            operation_wait = (
                0.0
                if operation_last is None
                else max(0.0, operation_last + operation_interval - checked_now)
            )
            return float(max(global_wait, operation_wait))

    def record_call(
        self,
        profile_fingerprint: str,
        operation_id: str,
        *,
        now: float,
        lock: LiveProcessLock | None = None,
    ) -> None:
        profile_id = _identifier(profile_fingerprint, label="profile fingerprint")
        operation_id = _identifier(operation_id, label="operation ID")
        checked_now = _timestamp(now, label="wall clock")
        if lock is None and self._process_lock is None:
            raise SafetyError("persistent rate reservation requires a shared held process lock")
        with self._coordinated(lock):
            state = self._load(now=checked_now)
            profile = self._profile(state, profile_id)
            if profile is None:
                profile = {"circuit_opened_at": None, "last_calls": {}}
                state["profiles"][profile_id] = profile
            if profile["circuit_opened_at"] is not None:
                raise SafetyError(f"live circuit is open for profile {profile_id!r}")
            profile["last_calls"][operation_id] = checked_now
            self._write(state)
