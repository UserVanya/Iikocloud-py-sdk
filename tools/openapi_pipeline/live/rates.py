from __future__ import annotations

import asyncio
import math
import time
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

from ..errors import SafetyError
from .contract_io import exact_keys, load_yaml_mapping, safe_identifier, safe_source
from .lock import LiveProcessLock
from .state import LiveStateStore

_MAX_CATALOG_BYTES = 1024 * 1024


def _finite_number(value: object, *, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SafetyError(f"{label} must be a finite number")
    result = float(value)
    if not math.isfinite(result):
        raise SafetyError(f"{label} must be a finite number")
    return result


@dataclass(frozen=True)
class RateLimit:
    calls: int
    per_seconds: float


@dataclass(frozen=True, slots=True)
class TestBudget:
    min_interval_seconds: float
    source: str
    verified: bool


@dataclass(frozen=True, slots=True)
class ServerLimit:
    calls: int
    per_seconds: float
    source: str
    verified: bool


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
        if floor < 30:
            raise SafetyError("global minimum interval must be at least 30 seconds")
        object.__setattr__(self, "utilization", utilization)
        object.__setattr__(self, "global_min_interval_seconds", floor)

    def operation_budget(
        self,
        operation_id: str,
        test_budget: TestBudget,
        server_limit: ServerLimit | None,
        *,
        max_calls_per_run: int = 1,
    ) -> OperationBudget:
        operation_id = safe_identifier(operation_id, label="operation ID")
        if test_budget.verified is not True:
            raise SafetyError(f"Operation {operation_id!r} test budget is not verified")
        if server_limit is not None and server_limit.verified is not True:
            raise SafetyError(f"Operation {operation_id!r} server limit is not verified")
        if type(max_calls_per_run) is not int or max_calls_per_run != 1:
            raise SafetyError("max calls per operation per run must be exactly 1")
        try:
            server_interval = (
                math.ceil(
                    server_limit.per_seconds
                    / server_limit.calls
                    / self.utilization
                )
                if server_limit is not None
                else 0
            )
        except (OverflowError, ValueError) as error:
            raise SafetyError(
                f"Operation {operation_id!r} calculated server interval is not finite"
            ) from error
        safe_interval_seconds = max(
            self.global_min_interval_seconds,
            test_budget.min_interval_seconds,
            server_interval,
        )
        return OperationBudget(
            operation_id=operation_id,
            safe_interval_seconds=float(safe_interval_seconds),
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


@dataclass(frozen=True, slots=True)
class _CatalogOperation:
    test_budget: TestBudget
    server_limit: ServerLimit | None


@dataclass(frozen=True)
class RateCatalog:
    policy: RatePolicy
    max_calls_per_operation_per_run: int
    _operations: Mapping[str, _CatalogOperation]

    @classmethod
    def load(cls, path: Path) -> RateCatalog:
        value = load_yaml_mapping(
            path,
            label="rate catalog",
            maximum_bytes=_MAX_CATALOG_BYTES,
        )
        return cls.from_mapping(value)

    @classmethod
    def from_mapping(cls, value: object) -> RateCatalog:
        if not isinstance(value, Mapping):
            raise SafetyError("Rate catalog root must be an object")
        exact_keys(value, {"version", "defaults", "operations"}, label="Rate catalog root")

        version = value["version"]
        if type(version) is not int or version != 2:
            raise SafetyError("Rate catalog version must be the integer 2")
        defaults = value["defaults"]
        if not isinstance(defaults, Mapping):
            raise SafetyError("Rate catalog defaults must be an object")
        exact_keys(
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
            operation_id = safe_identifier(raw_operation_id, label="operation ID")
            if not isinstance(raw_entry, Mapping):
                raise SafetyError(f"Rate entry for {operation_id!r} must be an object")
            exact_keys(
                raw_entry,
                {"test_budget", "server_limit"},
                label=f"Rate entry for {operation_id!r}",
            )

            raw_test_budget = raw_entry["test_budget"]
            if not isinstance(raw_test_budget, Mapping):
                raise SafetyError(
                    f"test_budget for {operation_id!r} must be an object"
                )
            exact_keys(
                raw_test_budget,
                {"min_interval_seconds", "source", "verified"},
                label=f"test_budget for {operation_id!r}",
            )
            test_interval = _finite_number(
                raw_test_budget["min_interval_seconds"],
                label=f"test budget min_interval_seconds for {operation_id!r}",
            )
            if test_interval < 30:
                raise SafetyError(
                    f"test budget for {operation_id!r} must be at least 30 seconds"
                )
            test_source = safe_source(
                raw_test_budget["source"],
                label=f"test budget source for {operation_id!r}",
            )
            test_verified = raw_test_budget["verified"]
            if type(test_verified) is not bool:
                raise SafetyError(
                    f"test budget verified for {operation_id!r} must be a boolean"
                )
            test_budget = TestBudget(test_interval, test_source, test_verified)

            raw_server_limit = raw_entry["server_limit"]
            server_limit: ServerLimit | None
            if raw_server_limit is None:
                server_limit = None
            elif not isinstance(raw_server_limit, Mapping):
                raise SafetyError(
                    f"server_limit for {operation_id!r} must be an object or null"
                )
            else:
                exact_keys(
                    raw_server_limit,
                    {"calls", "per_seconds", "source", "verified"},
                    label=f"server_limit for {operation_id!r}",
                )
                calls = raw_server_limit["calls"]
                if type(calls) is not int or calls <= 0:
                    raise SafetyError(
                        f"server limit calls for {operation_id!r} must be a positive integer"
                    )
                per_seconds = _finite_number(
                    raw_server_limit["per_seconds"],
                    label=f"server limit per_seconds for {operation_id!r}",
                )
                if per_seconds <= 0:
                    raise SafetyError(
                        f"server limit per_seconds for {operation_id!r} "
                        "must be greater than 0"
                    )
                server_source = safe_source(
                    raw_server_limit["source"],
                    label=f"server limit source for {operation_id!r}",
                )
                server_verified = raw_server_limit["verified"]
                if type(server_verified) is not bool:
                    raise SafetyError(
                        f"server limit verified for {operation_id!r} must be a boolean"
                    )
                server_limit = ServerLimit(
                    calls,
                    per_seconds,
                    server_source,
                    server_verified,
                )
            parsed[operation_id] = _CatalogOperation(
                test_budget=test_budget,
                server_limit=server_limit,
            )
        return cls(policy, max_calls, MappingProxyType(parsed))

    @property
    def operation_ids(self) -> tuple[str, ...]:
        return tuple(self._operations)

    def operation_budget(self, operation_id: str) -> OperationBudget:
        operation_id = safe_identifier(operation_id, label="operation ID")
        entry = self._operations.get(operation_id)
        if entry is None:
            raise SafetyError(
                f"Unknown live operation {operation_id!r}; add and verify it in the rate catalog"
            )
        return self.policy.operation_budget(
            operation_id,
            entry.test_budget,
            entry.server_limit,
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
        self.profile_fingerprint = safe_identifier(
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
