# ruff: noqa: E402
from __future__ import annotations

import hashlib
import importlib
import importlib.util
import secrets
import stat
import sys
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

# Project imports below must not populate the manifest-controlled generated tree.
sys.dont_write_bytecode = True

import pytest
import pytest_asyncio

from tools.openapi_pipeline.capture import CaptureWriter, LiveCapture, RedactionHints
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile, is_safe_profile_name
from tools.openapi_pipeline.live.pytest_support import (
    LivePreflight,
    assert_exact_live_read_invocation,
    assert_serial_live_invocation,
    finalize_live_receipt,
    initialize_receipt,
    mutation_journals_absent,
    prepare_live_preflight,
    resolve_locked_live_profile,
)
from tools.openapi_pipeline.live.rates import LiveRateGuard, RateCatalog
from tools.openapi_pipeline.live.read_case import ReadContext
from tools.openapi_pipeline.live.read_planner import ReadPlan
from tools.openapi_pipeline.live.read_report import ReadReportWriter
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.session import SafeLiveSession, load_operation_contract
from tools.openapi_pipeline.live.state import LiveStateStore
from tools.openapi_pipeline.paths import RepoPaths

_LIVE_MARKERS = (
    "live_read_smoke",
    "live_read_full",
    "live_read_selected",
    "live_write",
)
_WRITE_OPERATION_IDS = (
    "get_stop_lists",
    "add_products_to_stop_list",
    "remove_products_from_stop_list",
)
_READ_COLLECTION_PATHS = (
    "tests/integration/read/test_all_reads.py",
    "tests/integration/read/test_selected_read.py",
)


@dataclass
class _LiveRunContext:
    receipt: LiveReceipt
    receipt_path: Path
    read_report_path: Path | None = None
    read_report_completed: bool | None = None
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
    read_context: ReadContext | None = None
    read_report: ReadReportWriter | None = None
    capture: LiveCapture | None = None


@dataclass(frozen=True)
class _GeneratedRuntime:
    configuration: Any
    api_client: Any
    adapter: Any


@dataclass(frozen=True)
class _LiveWritePreflight:
    operation_ids: tuple[str, ...]
    target_organization_fingerprint: str


class LiveReadHarness:
    __slots__ = (
        "_context",
        "_operation_contract",
        "_plan",
        "_preflight",
        "_profile_fingerprint",
        "_report",
        "_run_context",
        "_sdk",
    )

    def __init__(
        self,
        *,
        plan: ReadPlan,
        context: ReadContext,
        sdk: Any,
        operation_contract: Any,
        report: ReadReportWriter,
        run_context: _LiveRunContext,
        preflight: LivePreflight,
        profile_fingerprint: str,
    ) -> None:
        self._plan = plan
        self._context = context
        self._sdk = sdk
        self._operation_contract = operation_contract
        self._report = report
        self._run_context = run_context
        self._preflight = preflight
        self._profile_fingerprint = profile_fingerprint

    def __repr__(self) -> str:
        return "LiveReadHarness()"

    async def run(self) -> Any:
        from tools.openapi_pipeline.live.read_runner import run_read_plan

        summary = await run_read_plan(
            self._plan,
            context=self._context,
            sdk=self._sdk,
            operation_contract=self._operation_contract,
            report=self._report,
        )
        loaded = self._report.load_and_verify()
        artifacts = self._preflight.artifacts
        self._run_context.read_report_completed = (
            loaded.matches(
                self._run_context.receipt.run_id,
                self._profile_fingerprint,
                artifacts.effective_schema_sha256,
                artifacts.generated_tree_sha256,
                artifacts.live_contracts_sha256,
                self._plan.registry_sha256,
            )
            and summary.success
        )
        return summary


def _assert_generated_package_origin(root: Path) -> None:
    expected = root / "src/iikocloud_client/__init__.py"
    expected_metadata: Any = None
    expected_resolved: Path | None = None
    spec: Any = None
    initial_lookup_failed = False
    try:
        expected_metadata = expected.lstat()
        expected_resolved = expected.resolve(strict=True)
        spec = importlib.util.find_spec("iikocloud_client")
    except (ImportError, OSError, ValueError):
        initial_lookup_failed = True
    if initial_lookup_failed:
        raise SafetyError("Generated package origin is not the exact src package") from None
    origin = spec.origin if spec is not None else None
    if (
        stat.S_ISLNK(expected_metadata.st_mode)
        or not stat.S_ISREG(expected_metadata.st_mode)
        or expected_resolved != expected
        or not isinstance(origin, str)
        or not origin
    ):
        raise SafetyError("Generated package origin is not the exact src package")
    origin_path = Path(origin)
    origin_metadata: Any = None
    origin_resolved: Path | None = None
    origin_lookup_failed = False
    try:
        origin_metadata = origin_path.lstat()
        origin_resolved = origin_path.resolve(strict=True)
    except OSError:
        origin_lookup_failed = True
    if origin_lookup_failed:
        raise SafetyError("Generated package origin is not the exact src package") from None
    if (
        stat.S_ISLNK(origin_metadata.st_mode)
        or not stat.S_ISREG(origin_metadata.st_mode)
        or origin_path != expected
        or origin_resolved != expected
    ):
        raise SafetyError("Generated package origin is not the exact src package")


def _load_generated_runtime() -> _GeneratedRuntime:
    from iikocloud_client.api_client import ApiClient
    from iikocloud_client.configuration import Configuration
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk

    return _GeneratedRuntime(
        configuration=Configuration,
        api_client=ApiClient,
        adapter=GeneratedLiveSdk,
    )


def _load_full_read_plan() -> ReadPlan:
    import_failed = False
    candidate: object = None
    try:
        module = importlib.import_module("tests.integration.read.cases")
        candidate = getattr(module, "FULL_READ_PLAN", None)
    except (ImportError, AttributeError):
        import_failed = True
    if import_failed or type(candidate) is not ReadPlan or len(candidate.cases) != 91:
        raise SafetyError("The exhaustive live read registry is unavailable") from None
    return candidate


def _selected_operation_is_statically_safe(root: Path, operation_id: str) -> None:
    from tools.openapi_pipeline.live.safety import OperationSafetyCatalog

    safety = OperationSafetyCatalog.load(root / "contracts/operation-safety.yaml")
    entry = safety.operations.get(operation_id)
    if entry is None:
        raise SafetyError("Selected live read operation is unknown")
    if entry.effect == "auth":
        raise SafetyError("Selected live read refuses authentication operations")
    if entry.effect != "read" or entry.live_policy != "automatic":
        raise SafetyError("Selected live read operation is not an automatic read")
    operation_contract = load_operation_contract(root / "contracts/live-operations.yaml")
    operation = operation_contract.get(operation_id)
    if operation is None or operation.kind != "read":
        raise SafetyError("Selected live read operation is not allowlisted")
    catalog = RateCatalog.load(root / "contracts/rate-limits.yaml")
    catalog.operation_budget(operation_id)
    _load_full_read_plan().case_for(operation_id)


def _read_mode_from_items(
    config: pytest.Config,
    items: list[pytest.Item],
) -> str | None:
    explicit_markers: list[str] = []
    arguments = tuple(config.invocation_params.args)
    for index, argument in enumerate(arguments):
        if argument in {"-m", "--markexpr"} and index + 1 < len(arguments):
            explicit_markers.append(arguments[index + 1])
        elif argument.startswith(("-m=", "--markexpr=")):
            explicit_markers.append(argument.partition("=")[2])
    explicit_expression = " ".join(explicit_markers)
    full = any(item.get_closest_marker("live_read_full") is not None for item in items)
    selected = any(item.get_closest_marker("live_read_selected") is not None for item in items)
    full = full or "live_read_full" in explicit_expression
    selected = selected or "live_read_selected" in explicit_expression
    if full and selected:
        raise pytest.UsageError("Live read modes cannot be combined")
    if full:
        return "full"
    if selected:
        return "selected"
    return None


def _is_live_item(item: pytest.Item) -> bool:
    return any(item.get_closest_marker(marker) is not None for marker in _LIVE_MARKERS)


def _assert_live_write_cli_gates(
    config: pytest.Config,
    *,
    audit_residue: bool,
) -> None:
    if config.getoption("--allow-live-write") is not True:
        raise pytest.UsageError("live_write requires explicit --allow-live-write")
    target = config.getoption("--target-organization")
    if not isinstance(target, str) or not target:
        raise pytest.UsageError("live_write requires explicit --target-organization")
    if audit_residue and config.getoption("--allow-audit-residue") is not True:
        raise pytest.UsageError("audit_residue requires explicit --allow-audit-residue")
    serial_error: str | None = None
    try:
        assert_serial_live_invocation(config.invocation_params.args)
    except SafetyError as error:
        serial_error = str(error)
    if serial_error is not None:
        raise pytest.UsageError(serial_error) from None


def _prepare_live_write_setup(
    config: pytest.Config,
    profile: ResolvedLiveProfile,
    catalog: RateCatalog,
) -> _LiveWritePreflight:
    if config.getoption("--allow-live-write") is not True:
        raise SafetyError("live_write requires explicit --allow-live-write")
    if profile.allow_write is not True:
        raise SafetyError("Live profile must set allow_write=true for live_write")
    target = config.getoption("--target-organization")
    if target != profile.organization_id:
        raise SafetyError("Target organization does not match the selected live profile")
    if profile.organization_id not in profile.allowed_organization_ids:
        raise SafetyError("Target organization is not in the live profile allowlist")
    if profile.terminal_group_id is None:
        raise SafetyError("Live write profile requires a terminal group")
    if profile.write_product_id is None:
        raise SafetyError("Live write profile requires a dedicated write product")
    assert_serial_live_invocation(config.invocation_params.args)
    for operation_id in _WRITE_OPERATION_IDS:
        catalog.operation_budget(operation_id)
    return _LiveWritePreflight(
        operation_ids=_WRITE_OPERATION_IDS,
        target_organization_fingerprint=hashlib.sha256(
            profile.organization_id.encode("utf-8")
        ).hexdigest(),
    )


def _seed_live_read_context(
    profile: ResolvedLiveProfile,
    *,
    now: datetime | None = None,
) -> ReadContext:
    current = now or datetime.now(timezone.utc)
    today = current.date()
    tomorrow = today + timedelta(days=1)
    seed: dict[str, object] = {
        "profile_organization_id": profile.organization_id,
        "profile_external_menu_id": profile.external_menu_id,
        "date_yyyy_mm_dd": today.isoformat(),
        "period_from_yyyy_mm_dd": today.isoformat(),
        "period_to_yyyy_mm_dd": tomorrow.isoformat(),
        "window_from_local": f"{today.isoformat()} 00:00:00.000",
        "window_to_local": f"{tomorrow.isoformat()} 00:00:00.000",
    }
    if profile.terminal_group_id is not None:
        seed["profile_terminal_group_id"] = profile.terminal_group_id
    return ReadContext.seed(seed)


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


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "audit_residue: write test whose compensating cleanup can leave an audit trail",
    )
    arguments = tuple(config.invocation_params.args)
    supplied_paths = tuple(
        argument
        for argument in arguments
        if argument.startswith("tests/") or argument.endswith(".py")
    )
    explicit_marker = any(
        argument in {"-m", "--markexpr"} or argument.startswith(("-m=", "--markexpr="))
        for argument in arguments
    )
    collect_only = "--collect-only" in arguments or "--co" in arguments
    read_collection_only = (
        collect_only and not explicit_marker and supplied_paths == _READ_COLLECTION_PATHS
    )
    if read_collection_only:
        config.option.markexpr = ""
    config._iiko_read_collection_only = read_collection_only  # type: ignore[attr-defined]


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    live_profile = config.getoption("--live-profile")
    if live_profile is not None and not is_safe_profile_name(live_profile):
        raise pytest.UsageError("--live-profile must be a safe lowercase profile name")
    if getattr(config, "_iiko_read_collection_only", False):
        config._iiko_live_write_selected = False  # type: ignore[attr-defined]
        config._iiko_live_read_report_required = False  # type: ignore[attr-defined]
        config._iiko_live_read_mode = None  # type: ignore[attr-defined]
        config._iiko_live_read_selected_operation = None  # type: ignore[attr-defined]
        return
    read_mode = _read_mode_from_items(config, items)
    selected_operation: str | None = None
    usage_error: str | None = None
    if read_mode is not None:
        try:
            selected_operation = assert_exact_live_read_invocation(
                config.invocation_params.args,
                mode=read_mode,
            )
            root = RepoPaths.discover().root
            _assert_generated_package_origin(root)
            if read_mode == "selected":
                assert selected_operation is not None
                _selected_operation_is_statically_safe(
                    root,
                    selected_operation,
                )
        except SafetyError as error:
            usage_error = str(error)
    if usage_error is not None:
        raise pytest.UsageError(usage_error) from None

    live_write_selected = False
    live_read_report_required = read_mode is not None
    for item in items:
        if _is_live_item(item) and not live_profile:
            item.add_marker(pytest.mark.skip(reason="live tests require --live-profile"))
            continue
        if item.get_closest_marker("live_write") is not None:
            audit_residue = item.get_closest_marker("audit_residue") is not None
            _assert_live_write_cli_gates(config, audit_residue=audit_residue)
            item.add_marker(pytest.mark.usefixtures("_live_environment"))
            live_write_selected = True
    config._iiko_live_write_selected = live_write_selected  # type: ignore[attr-defined]
    config._iiko_live_read_report_required = live_read_report_required  # type: ignore[attr-defined]
    config._iiko_live_read_mode = read_mode  # type: ignore[attr-defined]
    config._iiko_live_read_selected_operation = selected_operation  # type: ignore[attr-defined]


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
    read_mode = getattr(request.config, "_iiko_live_read_mode", None)
    selected_operation = getattr(
        request.config,
        "_iiko_live_read_selected_operation",
        None,
    )
    full_read_plan: ReadPlan | None = None
    if read_mode is not None:
        _assert_generated_package_origin(root)
        full_read_plan = _load_full_read_plan()
    preflight = prepare_live_preflight(
        root,
        invocation_args=request.config.invocation_params.args,
        read_plan=full_read_plan,
        read_mode=read_mode,
        selected_operation=selected_operation,
    )
    if read_mode is None:
        _assert_generated_package_origin(root)
    state_root = root / ".state"
    lock = LiveProcessLock(state_root / "live.lock")
    with lock:
        profile = resolve_locked_live_profile(
            root,
            process_lock=lock,
            profile_name=request.config.getoption("--live-profile"),
            env_file_option=request.config.getoption("--env-file"),
        )
        if read_mode is not None and (
            profile.organization_id not in profile.allowed_organization_ids
        ):
            raise SafetyError("Live read profile organization is not in its exact allowlist")
        if getattr(request.config, "_iiko_live_write_selected", False):
            write_preflight = _prepare_live_write_setup(
                request.config,
                profile,
                preflight.catalog,
            )
            print(
                "live-write preflight: operations="
                + ",".join(write_preflight.operation_ids)
                + "; target-organization-sha256="
                + write_preflight.target_organization_fingerprint
            )
        state = LiveStateStore(state_root / "live-rate-limits.json", process_lock=lock)
        receipt, receipt_path = initialize_receipt(
            state_root,
            process_lock=lock,
            run_id=_new_run_id(),
            profile=profile,
            artifacts=preflight.artifacts,
        )
        read_context: ReadContext | None = None
        read_report: ReadReportWriter | None = None
        capture: LiveCapture | None = None
        context = _LiveRunContext(
            receipt=receipt,
            receipt_path=receipt_path,
            read_report_completed=(
                False
                if getattr(request.config, "_iiko_live_read_report_required", False)
                else None
            ),
        )
        if read_mode is not None:
            plan = preflight.read_plan
            operation_contract = preflight.operation_contract
            effective_schema = preflight.effective_schema
            if (
                type(plan) is not ReadPlan
                or operation_contract is None
                or effective_schema is None
            ):
                raise SafetyError("Live read preflight did not produce exact runtime inputs")
            read_context = _seed_live_read_context(profile)
            read_report = ReadReportWriter.create(
                root / "private",
                operation_contract=operation_contract,
                run_id=receipt.run_id,
                profile_fingerprint=profile.fingerprint,
                effective_schema_sha256=preflight.artifacts.effective_schema_sha256,
                generated_tree_sha256=preflight.artifacts.generated_tree_sha256,
                live_contracts_sha256=preflight.artifacts.live_contracts_sha256,
                registry_sha256=plan.registry_sha256,
            )
            context.read_report_path = read_report.path
            if read_mode == "selected":
                if type(selected_operation) is not str:
                    raise SafetyError("Selected live read operation is unavailable")
                hints = RedactionHints.for_operation(
                    effective_schema,
                    selected_operation,
                )
                capture = LiveCapture(
                    writer=CaptureWriter(
                        root / "private/captures",
                        known_secrets=(profile.api_login,),
                    ),
                    run_id=receipt.run_id,
                    selected_operation=selected_operation,
                    operation_catalog=operation_contract,
                    hints=hints,
                )
        request.config._iiko_live_run_context = context  # type: ignore[attr-defined]
        yield _LiveEnvironment(
            preflight,
            profile,
            lock,
            state,
            context,
            read_context=read_context,
            read_report=read_report,
            capture=capture,
        )


@pytest.fixture(scope="session")
def live_profile(_live_environment: _LiveEnvironment) -> ResolvedLiveProfile:
    return _live_environment.profile


@pytest.fixture(scope="session")
def live_read_plan(_live_environment: _LiveEnvironment) -> ReadPlan:
    plan = _live_environment.preflight.read_plan
    if type(plan) is not ReadPlan:
        raise SafetyError("Live read plan is available only to guarded read tests")
    return plan


@pytest.fixture(scope="session")
def live_read_context(_live_environment: _LiveEnvironment) -> ReadContext:
    context = _live_environment.read_context
    if type(context) is not ReadContext:
        raise SafetyError("Live read context is available only to guarded read tests")
    return context


@pytest.fixture(scope="session")
def live_read_report(_live_environment: _LiveEnvironment) -> ReadReportWriter:
    report = _live_environment.read_report
    if type(report) is not ReadReportWriter:
        raise SafetyError("Live read report is available only to guarded read tests")
    return report


def _new_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}-{secrets.token_hex(4)}"


@pytest_asyncio.fixture(scope="session", loop_scope="session")
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
    operation_contract = preflight.operation_contract or load_operation_contract(
        root / "contracts/live-operations.yaml"
    )
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
        operation_contract=operation_contract,
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


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def live_sdk(
    _live_environment: _LiveEnvironment,
    live_session: SafeLiveSession,
) -> AsyncIterator[Any]:
    profile = _live_environment.profile
    state = _live_environment.state
    context = _live_environment.context
    if live_session.profile is not profile or live_session.state is not state:
        raise SafetyError("Generated live SDK must share the authenticated live session")
    receipt = live_session.receipt
    if receipt is None:
        raise SafetyError("Generated live SDK requires the authenticated live receipt")
    operation_contract = _live_environment.preflight.operation_contract
    if operation_contract is None:
        operation_contract = load_operation_contract(
            RepoPaths.discover().root / "contracts/live-operations.yaml"
        )
    capture = _live_environment.capture
    if capture is not None:
        capture.add_known_secret(live_session.access_token)

    runtime = _load_generated_runtime()
    configuration = runtime.configuration(
        host=profile.base_url,
        access_token=live_session.access_token,
    )
    context.generated_client_required = True
    api_client = runtime.api_client(configuration)
    adapter: Any | None = None
    try:
        adapter = runtime.adapter(
            api_client=api_client,
            profile=profile,
            guard=live_session.guard,
            state=state,
            operation_contract=operation_contract,
            capture=capture,
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


@pytest.fixture(scope="session")
def live_read_harness(
    _live_environment: _LiveEnvironment,
    live_read_plan: ReadPlan,
    live_read_context: ReadContext,
    live_read_report: ReadReportWriter,
    live_sdk: Any,
) -> LiveReadHarness:
    operation_contract = _live_environment.preflight.operation_contract
    if operation_contract is None:
        raise SafetyError("Live read operation contract is unavailable")
    return LiveReadHarness(
        plan=live_read_plan,
        context=live_read_context,
        sdk=live_sdk,
        operation_contract=operation_contract,
        report=live_read_report,
        run_context=_live_environment.context,
        preflight=_live_environment.preflight,
        profile_fingerprint=_live_environment.profile.fingerprint,
    )


@pytest_asyncio.fixture(loop_scope="session")
async def mutation_journal(
    request: pytest.FixtureRequest,
    _live_environment: _LiveEnvironment,
) -> AsyncIterator[Any]:
    if request.node.get_closest_marker("live_write") is None:
        raise SafetyError("Mutation journals are available only to live_write tests")

    from tools.openapi_pipeline.mutations import MutationJournal

    environment = _live_environment
    journal = MutationJournal.create(
        RepoPaths.discover().root / ".state",
        environment.context.receipt.run_id,
        environment.profile.fingerprint,
    )
    try:
        yield journal
    finally:
        if journal.pending_count == 0 and journal.path.exists():

            async def reject_unexpected_cleanup(
                _operation_id: str,
                _payload: dict[str, Any],
            ) -> None:
                raise SafetyError("Empty mutation journal unexpectedly requested cleanup")

            await journal.cleanup(reject_unexpected_cleanup)


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
                read_report_completed=context.read_report_completed,
            )
    except SafetyError:
        finalized = False
    if reports_passed and not finalized:
        session.exitstatus = pytest.ExitCode.TESTS_FAILED
