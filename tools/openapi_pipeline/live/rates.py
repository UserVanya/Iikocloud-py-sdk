from __future__ import annotations

import asyncio
import math
import re
import time
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any

import yaml

from ..errors import SafetyError
from .lock import LiveProcessLock
from .state import LiveStateStore

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_MAX_CATALOG_BYTES = 1024 * 1024


def _safe_identifier(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise SafetyError(f"{label} must be a safe ASCII string of 1 to 128 characters")
    return value


def _finite_number(value: object, *, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SafetyError(f"{label} must be a finite number")
    result = float(value)
    if not math.isfinite(result):
        raise SafetyError(f"{label} must be a finite number")
    return result


def _exact_keys(value: Mapping[object, object], expected: set[str], *, label: str) -> None:
    keys = set(value)
    if keys != expected or any(not isinstance(key, str) for key in keys):
        wanted = ", ".join(sorted(expected))
        raise SafetyError(f"{label} keys must be exactly: {wanted}")


class _UniqueKeySafeLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: _UniqueKeySafeLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as error:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable key",
                key_node.start_mark,
            ) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


@dataclass(frozen=True)
class RateLimit:
    calls: int
    per_seconds: float


@dataclass(frozen=True)
class OperationBudget:
    operation_id: str
    safe_interval_seconds: float
    max_calls_per_run: int


@dataclass(frozen=True)
class RatePolicy:
    utilization: float
    global_min_interval_seconds: float

    def __post_init__(self) -> None:
        utilization = _finite_number(self.utilization, label="utilization")
        floor = _finite_number(
            self.global_min_interval_seconds,
            label="global minimum interval",
        )
        if not 0 < utilization <= 0.20:
            raise SafetyError("utilization must be greater than 0 and no more than 0.20")
        if floor < 15:
            raise SafetyError("global minimum interval must be at least 15 seconds")
        object.__setattr__(self, "utilization", utilization)
        object.__setattr__(self, "global_min_interval_seconds", floor)

    def operation_budget(
        self,
        operation_id: str,
        value: Mapping[str, Any],
        *,
        max_calls_per_run: int = 1,
    ) -> OperationBudget:
        operation_id = _safe_identifier(operation_id, label="operation ID")
        if not isinstance(value, Mapping):
            raise SafetyError(f"Rate entry for {operation_id!r} must be an object")
        if value.get("verified") is not True:
            raise SafetyError(f"Operation {operation_id!r} rate limit is not verified")
        if type(max_calls_per_run) is not int or max_calls_per_run != 1:
            raise SafetyError("max calls per operation per run must be exactly 1")
        limit = value.get("server_limit")
        if not isinstance(limit, Mapping):
            raise SafetyError(f"server_limit for {operation_id!r} must be an object")
        _exact_keys(limit, {"calls", "per_seconds"}, label=f"server_limit for {operation_id!r}")
        calls = limit["calls"]
        if type(calls) is not int or calls <= 0:
            raise SafetyError(
                f"server limit calls for {operation_id!r} must be a positive integer"
            )
        per_seconds = _finite_number(
            limit["per_seconds"],
            label=f"server limit per_seconds for {operation_id!r}",
        )
        if per_seconds <= 0:
            raise SafetyError(
                f"server limit per_seconds for {operation_id!r} must be greater than 0"
            )
        return OperationBudget(
            operation_id=operation_id,
            safe_interval_seconds=self.safe_interval(RateLimit(calls, per_seconds)),
            max_calls_per_run=max_calls_per_run,
        )

    def safe_interval(self, limit: RateLimit) -> float:
        if type(limit.calls) is not int or limit.calls <= 0:
            raise SafetyError("Invalid server limit: calls must be a positive integer")
        per_seconds = _finite_number(
            limit.per_seconds,
            label="Invalid server limit: per_seconds",
        )
        if per_seconds <= 0:
            raise SafetyError("Invalid server limit: per_seconds must be greater than 0")
        try:
            interval = per_seconds / (limit.calls * self.utilization)
        except OverflowError as error:
            raise SafetyError("Invalid server limit: calls are too large") from error
        if not math.isfinite(interval):
            raise SafetyError("Invalid server limit: calculated interval is not finite")
        return float(max(self.global_min_interval_seconds, math.ceil(interval)))


@dataclass(frozen=True)
class _CatalogOperation:
    server_limit: RateLimit
    source: str
    verified: bool


@dataclass(frozen=True)
class RateCatalog:
    policy: RatePolicy
    max_calls_per_operation_per_run: int
    _operations: Mapping[str, _CatalogOperation]

    @classmethod
    def load(cls, path: Path) -> RateCatalog:
        try:
            body = path.read_bytes()
        except OSError as error:
            raise SafetyError(f"Cannot read rate catalog: {path}") from error
        if len(body) > _MAX_CATALOG_BYTES:
            raise SafetyError(f"Rate catalog is larger than {_MAX_CATALOG_BYTES} bytes: {path}")
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError as error:
            raise SafetyError(f"Rate catalog is not valid UTF-8: {path}") from error
        try:
            value = yaml.load(text, Loader=_UniqueKeySafeLoader)
        except yaml.YAMLError as error:
            detail = "duplicate key" if "duplicate key" in str(error) else "invalid YAML"
            raise SafetyError(f"Rate catalog contains {detail}: {path}") from error
        return cls.from_mapping(value)

    @classmethod
    def from_mapping(cls, value: object) -> RateCatalog:
        if not isinstance(value, Mapping):
            raise SafetyError("Rate catalog root must be an object")
        _exact_keys(value, {"version", "defaults", "operations"}, label="Rate catalog root")

        version = value["version"]
        if type(version) is not int or version != 1:
            raise SafetyError("Rate catalog version must be the integer 1")
        defaults = value["defaults"]
        if not isinstance(defaults, Mapping):
            raise SafetyError("Rate catalog defaults must be an object")
        _exact_keys(
            defaults,
            {
                "utilization",
                "global_min_interval_seconds",
                "max_calls_per_operation_per_run",
            },
            label="Rate catalog defaults",
        )
        max_calls = defaults["max_calls_per_operation_per_run"]
        if type(max_calls) is not int or max_calls != 1:
            raise SafetyError("max calls per operation per run must be exactly 1")
        policy = RatePolicy(
            utilization=defaults["utilization"],
            global_min_interval_seconds=defaults["global_min_interval_seconds"],
        )

        operations = value["operations"]
        if not isinstance(operations, Mapping):
            raise SafetyError("Rate catalog operations must be an object")
        parsed: dict[str, _CatalogOperation] = {}
        for raw_operation_id, raw_entry in sorted(
            operations.items(), key=lambda item: str(item[0])
        ):
            operation_id = _safe_identifier(raw_operation_id, label="operation ID")
            if not isinstance(raw_entry, Mapping):
                raise SafetyError(f"Rate entry for {operation_id!r} must be an object")
            _exact_keys(
                raw_entry,
                {"server_limit", "source", "verified"},
                label=f"Rate entry for {operation_id!r}",
            )
            source = raw_entry["source"]
            if (
                not isinstance(source, str)
                or not source
                or len(source) > 256
                or any(ord(character) < 32 for character in source)
            ):
                raise SafetyError(
                    f"source for {operation_id!r} must be a non-empty safe string "
                    "up to 256 characters"
                )
            verified = raw_entry["verified"]
            if type(verified) is not bool:
                raise SafetyError(f"verified for {operation_id!r} must be a boolean")
            limit = raw_entry["server_limit"]
            if not isinstance(limit, Mapping):
                raise SafetyError(f"server_limit for {operation_id!r} must be an object")
            _exact_keys(
                limit,
                {"calls", "per_seconds"},
                label=f"server_limit for {operation_id!r}",
            )
            calls = limit["calls"]
            if type(calls) is not int or calls <= 0:
                raise SafetyError(
                    f"server limit calls for {operation_id!r} must be a positive integer"
                )
            per_seconds = _finite_number(
                limit["per_seconds"],
                label=f"server limit per_seconds for {operation_id!r}",
            )
            if per_seconds <= 0:
                raise SafetyError(
                    f"server limit per_seconds for {operation_id!r} must be greater than 0"
                )
            parsed[operation_id] = _CatalogOperation(
                server_limit=RateLimit(calls, per_seconds),
                source=source,
                verified=verified,
            )
        return cls(policy, max_calls, MappingProxyType(parsed))

    def operation_budget(self, operation_id: str) -> OperationBudget:
        operation_id = _safe_identifier(operation_id, label="operation ID")
        entry = self._operations.get(operation_id)
        if entry is None:
            raise SafetyError(
                f"Unknown live operation {operation_id!r}; add and verify it in the rate catalog"
            )
        return self.policy.operation_budget(
            operation_id,
            {
                "verified": entry.verified,
                "server_limit": {
                    "calls": entry.server_limit.calls,
                    "per_seconds": entry.server_limit.per_seconds,
                },
            },
            max_calls_per_run=self.max_calls_per_operation_per_run,
        )


class LiveRateGuard:
    """Reserve one persistent, rate-limited permission for each live call."""

    def __init__(
        self,
        *,
        profile_fingerprint: str,
        catalog: RateCatalog,
        state: LiveStateStore,
        process_lock: LiveProcessLock,
        wall_clock: Callable[[], float] = time.time,
        monotonic_clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self.profile_fingerprint = _safe_identifier(
            profile_fingerprint,
            label="profile fingerprint",
        )
        self.catalog = catalog
        self.state = state
        self.process_lock = process_lock
        self.wall_clock = wall_clock
        self.monotonic_clock = monotonic_clock
        self.sleeper = sleeper
        self._run_calls: dict[str, int] = {}
        self._acquire_in_progress = False
        self.state.bind_process_lock(process_lock)

    async def acquire(self, operation_id: str) -> OperationBudget:
        if not self.process_lock.held:
            raise SafetyError("live process lock must be held before acquiring a rate budget")
        if self._acquire_in_progress:
            raise SafetyError("a live rate acquisition is already in progress")
        self._acquire_in_progress = True
        try:
            now = _finite_number(self.wall_clock(), label="wall clock")
            if now < 0:
                raise SafetyError("wall clock must not be negative")

            self.state.assert_circuit_closed(
                self.profile_fingerprint,
                now=now,
                lock=self.process_lock,
            )
            budget = self.catalog.operation_budget(operation_id)
            count = self._run_calls.get(operation_id, 0)
            if count >= budget.max_calls_per_run:
                raise SafetyError(
                    f"Operation {operation_id!r} was already acquired in this live run"
                )

            wait_seconds = self.state.required_wait(
                self.profile_fingerprint,
                operation_id,
                now=now,
                global_interval_seconds=self.catalog.policy.global_min_interval_seconds,
                operation_interval_seconds=budget.safe_interval_seconds,
                lock=self.process_lock,
            )
            reservation_time = now
            if wait_seconds > 0:
                monotonic_before = _finite_number(
                    self.monotonic_clock(),
                    label="monotonic clock",
                )
                await self.sleeper(wait_seconds)
                monotonic_after = _finite_number(
                    self.monotonic_clock(),
                    label="monotonic clock",
                )
                if monotonic_after < monotonic_before:
                    raise SafetyError("monotonic clock moved backwards during rate-limit wait")
                if monotonic_after - monotonic_before + 1e-9 < wait_seconds:
                    raise SafetyError("rate-limit sleeper returned before the required interval")
                reservation_time = _finite_number(self.wall_clock(), label="wall clock")
                if reservation_time < now:
                    raise SafetyError("wall clock moved backwards during rate-limit wait")

            self.state.record_call(
                self.profile_fingerprint,
                operation_id,
                now=reservation_time,
                lock=self.process_lock,
            )
            self._run_calls[operation_id] = count + 1
            return budget
        finally:
            self._acquire_in_progress = False

    def record_status(self, operation_id: str, status: int) -> None:
        if not self.process_lock.held:
            raise SafetyError("live process lock must be held before recording an HTTP status")
        if self._run_calls.get(operation_id, 0) == 0:
            raise SafetyError(f"Operation {operation_id!r} has no acquired live-call budget")
        now = _finite_number(self.wall_clock(), label="wall clock")
        if now < 0:
            raise SafetyError("wall clock must not be negative")
        self.state.record_status(
            self.profile_fingerprint,
            operation_id,
            status,
            now=now,
            lock=self.process_lock,
        )
