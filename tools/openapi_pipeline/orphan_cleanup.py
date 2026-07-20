from __future__ import annotations

import re
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import SafetyError
from .live.lock import LiveProcessLock
from .live.profile import ResolvedLiveProfile, is_safe_profile_name
from .live.pytest_support import explicit_env_path, resolve_locked_live_profile
from .live.rates import LiveRateGuard, OperationBudget, RateCatalog
from .live.session import LiveOperation, SafeLiveSession, load_operation_contract
from .live.state import LiveStateStore
from .mutations import cleanup_orphans
from .paths import RepoPaths

_PROFILE_FINGERPRINT = re.compile(r"[a-f0-9]{64}\Z")
_AUTH_OPERATION = LiveOperation("auth", None, "POST", "/api/1/access_token")
CleanupRequestValidator = Callable[[str, object, ResolvedLiveProfile], object]


@dataclass(frozen=True)
class CleanupOrphansDependencies:
    paths: RepoPaths
    rate_catalog_loader: Callable[[Path], RateCatalog]
    operation_contract_loader: Callable[[Path], Mapping[str, LiveOperation]]
    env_file_validator: Callable[[Path, object], Path | None]
    lock_factory: Callable[[Path], LiveProcessLock]
    profile_resolver: Callable[..., ResolvedLiveProfile]
    state_factory: Callable[..., LiveStateStore]
    guard_factory: Callable[..., LiveRateGuard]
    session_factory: Callable[..., SafeLiveSession]
    runtime_loader: Callable[[], Any]
    cleanup_validator: CleanupRequestValidator
    cleanup_runner: Callable[..., Awaitable[int]]
    confirm: Callable[[str], str]
    emit: Callable[[str], object]


@dataclass(frozen=True)
class _GeneratedRuntime:
    configuration: Any
    api_client: Any
    adapter: Any


def _load_generated_runtime() -> _GeneratedRuntime:
    from iikocloud_client.api_client import ApiClient
    from iikocloud_client.configuration import Configuration

    from .live.generated import GeneratedLiveSdk

    return _GeneratedRuntime(
        configuration=Configuration,
        api_client=ApiClient,
        adapter=GeneratedLiveSdk,
    )


def _validate_generated_cleanup_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    from .live.generated import validate_generated_cleanup_request

    return validate_generated_cleanup_request(operation_id, payload, profile)


def default_cleanup_orphans_dependencies(
    paths: RepoPaths | None = None,
) -> CleanupOrphansDependencies:
    return CleanupOrphansDependencies(
        paths=paths or RepoPaths.discover(),
        rate_catalog_loader=RateCatalog.load,
        operation_contract_loader=load_operation_contract,
        env_file_validator=lambda root, value: explicit_env_path(root, value),
        lock_factory=LiveProcessLock,
        profile_resolver=resolve_locked_live_profile,
        state_factory=LiveStateStore,
        guard_factory=LiveRateGuard,
        session_factory=SafeLiveSession,
        runtime_loader=_load_generated_runtime,
        cleanup_validator=_validate_generated_cleanup_request,
        cleanup_runner=cleanup_orphans,
        confirm=input,
        emit=print,
    )


class _CleanupBudgetValidator:
    def __init__(self, catalog: RateCatalog) -> None:
        self._catalog = catalog
        self._counts: dict[str, int] = {}

    def __call__(self, operation_id: str) -> OperationBudget:
        budget = self._catalog.operation_budget(operation_id)
        count = self._counts.get(operation_id, 0)
        if count >= budget.max_calls_per_run:
            raise SafetyError("Orphan cleanup plan exceeds an operation run budget")
        self._counts[operation_id] = count + 1
        return budget


class _LazyGeneratedCleanupExecutor:
    def __init__(
        self,
        *,
        dependencies: CleanupOrphansDependencies,
        profile: ResolvedLiveProfile,
        catalog: RateCatalog,
        operations: Mapping[str, LiveOperation],
        process_lock: LiveProcessLock,
    ) -> None:
        self._dependencies = dependencies
        self._profile = profile
        self._catalog = catalog
        self._operations = operations
        self._process_lock = process_lock
        self._session: Any | None = None
        self._api_client: Any | None = None
        self._adapter: Any | None = None

    async def _start(self) -> None:
        state = self._dependencies.state_factory(
            self._dependencies.paths.root / ".state/live-rate-limits.json",
            process_lock=self._process_lock,
        )
        guard = self._dependencies.guard_factory(
            profile_fingerprint=self._profile.fingerprint,
            catalog=self._catalog,
            state=state,
            process_lock=self._process_lock,
        )
        session = self._dependencies.session_factory(
            profile=self._profile,
            guard=guard,
            state=state,
            operation_contract=self._operations,
        )
        self._session = session
        await session.authenticate()

        runtime = self._dependencies.runtime_loader()
        configuration = runtime.configuration(
            host=self._profile.base_url,
            access_token=session.access_token,
        )
        api_client = runtime.api_client(configuration)
        self._api_client = api_client
        self._adapter = runtime.adapter(
            api_client=api_client,
            profile=self._profile,
            guard=guard,
            state=state,
        )

    async def execute(self, operation_id: str, payload: dict[str, Any]) -> None:
        validated_payload = self._dependencies.cleanup_validator(
            operation_id,
            payload,
            self._profile,
        )
        adapter = self._adapter
        if adapter is None:
            await self._start()
            adapter = self._adapter
        if adapter is None:
            raise SafetyError("Generated cleanup client did not initialize")
        await adapter.execute_cleanup(operation_id, validated_payload)

    async def close(self) -> None:
        try:
            if self._api_client is not None:
                await self._api_client.close()
        finally:
            if self._session is not None:
                await self._session.close()


def _validated_env_option(
    dependencies: CleanupOrphansDependencies,
    value: object,
) -> str | None:
    validated = dependencies.env_file_validator(dependencies.paths.root, value)
    return None if validated is None else str(validated)


async def cleanup_orphans_command(
    *,
    live_profile: str,
    env_file: str | None,
    dependencies: CleanupOrphansDependencies | None = None,
) -> int:
    selected = dependencies or default_cleanup_orphans_dependencies()
    paths = selected.paths
    if not is_safe_profile_name(live_profile):
        raise SafetyError("--live-profile must be a safe lowercase profile name")

    catalog = selected.rate_catalog_loader(paths.root / "contracts/rate-limits.yaml")
    operations = selected.operation_contract_loader(paths.root / "contracts/live-operations.yaml")
    if operations.get("authenticate") != _AUTH_OPERATION:
        raise SafetyError("Orphan cleanup authentication contract is not approved")
    try:
        catalog.operation_budget("authenticate")
    except Exception:
        raise SafetyError("Orphan cleanup authentication rate budget is not verified") from None
    env_option = _validated_env_option(selected, env_file)

    process_lock = selected.lock_factory(paths.root / ".state/live.lock")
    with process_lock:
        profile = selected.profile_resolver(
            paths.root,
            process_lock=process_lock,
            profile_name=live_profile,
            env_file_option=env_option,
        )
        if (
            not isinstance(profile, ResolvedLiveProfile)
            or _PROFILE_FINGERPRINT.fullmatch(profile.fingerprint) is None
        ):
            raise SafetyError("Orphan cleanup resolved profile is invalid")
        try:
            selected.emit(f"orphan cleanup profile fingerprint: {profile.fingerprint}")
        except Exception:
            raise SafetyError("Cannot render orphan cleanup profile safely") from None

        executor = _LazyGeneratedCleanupExecutor(
            dependencies=selected,
            profile=profile,
            catalog=catalog,
            operations=operations,
            process_lock=process_lock,
        )
        try:
            return await selected.cleanup_runner(
                paths.root / ".state",
                profile_fingerprint=profile.fingerprint,
                operation_contract=operations,
                reserve_budget=_CleanupBudgetValidator(catalog),
                execute=executor.execute,
                confirm=selected.confirm,
                emit=selected.emit,
            )
        finally:
            await executor.close()
