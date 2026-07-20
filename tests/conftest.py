from __future__ import annotations

import importlib.util
import secrets
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest

from iikocloud_client.api_client import ApiClient
from iikocloud_client.configuration import Configuration
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile, is_safe_profile_name
from tools.openapi_pipeline.live.pytest_support import (
    LivePreflight,
    finalize_live_receipt,
    initialize_receipt,
    mutation_journals_absent,
    prepare_live_preflight,
    resolve_locked_live_profile,
)
from tools.openapi_pipeline.live.rates import LiveRateGuard
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.session import SafeLiveSession, load_operation_contract
from tools.openapi_pipeline.live.state import LiveStateStore
from tools.openapi_pipeline.paths import RepoPaths

_LIVE_MARKERS = ("live_read_smoke", "live_read_full", "live_write")


@dataclass
class _LiveRunContext:
    receipt: LiveReceipt
    receipt_path: Path
    live_calls: int = 0
    live_calls_passed: int = 0
    live_failed: bool = False
    circuit_closed: bool = False
    session_client_closed: bool = False
    generated_client_required: bool = False
    generated_client_closed: bool = False
    mutation_journals_clean: bool = False

    @property
    def clients_closed(self) -> bool:
        return self.session_client_closed and (
            not self.generated_client_required or self.generated_client_closed
        )


@dataclass
class _LiveEnvironment:
    preflight: LivePreflight
    profile: ResolvedLiveProfile
    lock: LiveProcessLock
    state: LiveStateStore
    context: _LiveRunContext


def _is_live_item(item: pytest.Item) -> bool:
    return any(item.get_closest_marker(marker) is not None for marker in _LIVE_MARKERS)


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("iiko live safety")
    if importlib.util.find_spec("xdist") is None:
        group._addoption("-n", "--numprocesses", action="store")
    group.addoption("--live-profile", action="store")
    group.addoption("--env-file", action="store")
    group.addoption("--allow-live-write", action="store_true", default=False)
    group.addoption("--allow-audit-residue", action="store_true", default=False)
    group.addoption("--target-organization", action="store")
    group.addoption("--capture-http", action="store_true", default=False)
    group.addoption("--capture-operation", action="store")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    live_profile = config.getoption("--live-profile")
    if live_profile is not None and not is_safe_profile_name(live_profile):
        raise pytest.UsageError("--live-profile must be a safe lowercase profile name")
    for item in items:
        if _is_live_item(item) and not live_profile:
            item.add_marker(pytest.mark.skip(reason="live tests require --live-profile"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[Any]):
    outcome = yield
    report = outcome.get_result()
    if not _is_live_item(item):
        return
    context = getattr(item.config, "_iiko_live_run_context", None)
    if not isinstance(context, _LiveRunContext):
        return
    if report.failed:
        context.live_failed = True
    if report.when == "call":
        context.live_calls += 1
        if report.passed:
            context.live_calls_passed += 1


@pytest.fixture(scope="session")
def _live_environment(request: pytest.FixtureRequest) -> Iterator[_LiveEnvironment]:
    root = RepoPaths.discover().root
    preflight = prepare_live_preflight(
        root,
        invocation_args=request.config.invocation_params.args,
    )
    state_root = root / ".state"
    lock = LiveProcessLock(state_root / "live.lock")
    with lock:
        profile = resolve_locked_live_profile(
            root,
            process_lock=lock,
            profile_name=request.config.getoption("--live-profile"),
            env_file_option=request.config.getoption("--env-file"),
        )
        state = LiveStateStore(state_root / "live-rate-limits.json", process_lock=lock)
        receipt, receipt_path = initialize_receipt(
            state_root,
            process_lock=lock,
            run_id=_new_run_id(),
            profile=profile,
            artifacts=preflight.artifacts,
        )
        context = _LiveRunContext(receipt=receipt, receipt_path=receipt_path)
        request.config._iiko_live_run_context = context  # type: ignore[attr-defined]
        yield _LiveEnvironment(preflight, profile, lock, state, context)


@pytest.fixture(scope="session")
def live_profile(_live_environment: _LiveEnvironment) -> ResolvedLiveProfile:
    return _live_environment.profile


def _new_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}-{secrets.token_hex(4)}"


@pytest.fixture(scope="session")
async def live_session(
    _live_environment: _LiveEnvironment,
) -> AsyncIterator[SafeLiveSession]:
    root = RepoPaths.discover().root
    preflight = _live_environment.preflight
    live_profile = _live_environment.profile
    state_root = root / ".state"
    lock = _live_environment.lock
    state = _live_environment.state
    context = _live_environment.context
    guard = LiveRateGuard(
        profile_fingerprint=live_profile.fingerprint,
        catalog=preflight.catalog,
        state=state,
        process_lock=lock,
    )
    session = SafeLiveSession(
        profile=live_profile,
        guard=guard,
        state=state,
        operation_contract=load_operation_contract(root / "contracts/live-operations.yaml"),
        receipt=context.receipt,
        receipt_path=context.receipt_path,
    )
    try:
        await session.authenticate()
        yield session
    finally:
        session_client_closed = False
        try:
            await session.close()
            session_client_closed = session.is_closed
        finally:
            session_receipt = session.receipt
            if session_receipt is not None and len(session_receipt.operations) > len(
                context.receipt.operations
            ):
                context.receipt = session_receipt
            context.session_client_closed = session_client_closed
            context.circuit_closed = not state.circuit_is_open(
                live_profile.fingerprint,
                lock=lock,
            )
            context.mutation_journals_clean = mutation_journals_absent(state_root)


@pytest.fixture(scope="session")
async def live_sdk(
    _live_environment: _LiveEnvironment,
    live_session: SafeLiveSession,
) -> AsyncIterator[GeneratedLiveSdk]:
    profile = _live_environment.profile
    state = _live_environment.state
    context = _live_environment.context
    if live_session.profile is not profile or live_session.state is not state:
        raise SafetyError("Generated live SDK must share the authenticated live session")
    receipt = live_session.receipt
    if receipt is None:
        raise SafetyError("Generated live SDK requires the authenticated live receipt")

    configuration = Configuration(
        host=profile.base_url,
        access_token=live_session.access_token,
    )
    context.generated_client_required = True
    api_client = ApiClient(configuration)
    adapter: GeneratedLiveSdk | None = None
    try:
        adapter = GeneratedLiveSdk(
            api_client=api_client,
            profile=profile,
            guard=live_session.guard,
            state=state,
            receipt=receipt,
            receipt_path=context.receipt_path,
        )
        yield adapter
    finally:
        generated_client_closed = False
        try:
            await api_client.close()
            generated_client_closed = True
        finally:
            context.generated_client_closed = generated_client_closed
            if adapter is not None and adapter.receipt is not None:
                context.receipt = adapter.receipt


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    context = getattr(session.config, "_iiko_live_run_context", None)
    if not isinstance(context, _LiveRunContext):
        return
    reports_passed = (
        exitstatus == int(pytest.ExitCode.OK)
        and not context.live_failed
        and context.live_calls > 0
        and context.live_calls == context.live_calls_passed
    )
    try:
        root = RepoPaths.discover().root
        with LiveProcessLock(root / ".state/live.lock"):
            finalized = finalize_live_receipt(
                context.receipt,
                context.receipt_path,
                live_reports_passed=reports_passed,
                circuit_closed=context.circuit_closed,
                clients_closed=context.clients_closed,
                mutation_journals_clean=context.mutation_journals_clean,
            )
    except SafetyError:
        finalized = False
    if reports_passed and not finalized:
        session.exitstatus = pytest.ExitCode.TESTS_FAILED
