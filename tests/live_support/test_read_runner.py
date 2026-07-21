from __future__ import annotations

import asyncio
from collections.abc import Callable, Mapping
from types import MappingProxyType
from typing import cast

import pytest

import tools.openapi_pipeline.live.read_runner as read_runner_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import (
    GeneratedCallFailure,
    GeneratedCallResult,
    GeneratedLiveSdk,
)
from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    NoRequest,
    ReadAssertionFailure,
    ReadCase,
    ReadContext,
    ReadExtractorFailure,
    ReadFailureCode,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan
from tools.openapi_pipeline.live.read_report import (
    ReadOutcome,
    ReadReportWriter,
    ReadStatus,
)
from tools.openapi_pipeline.live.read_runner import ReadRunSummary, run_read_plan
from tools.openapi_pipeline.live.session import LiveOperation


def test_read_runner_exports_approved_interface() -> None:
    assert ReadRunSummary.__dataclass_fields__.keys() == {
        "outcomes",
        "passed",
        "no_live_target",
        "failed",
        "aborted",
        "success",
    }
    assert callable(run_read_plan)


def _build_no_request(_view: ContextView) -> NoRequest:
    return NO_REQUEST


def _validate_ok(_data: object, _view: ContextView) -> None:
    return None


def _extract_empty(
    _data: object,
    _view: ContextView,
) -> Mapping[str, object]:
    return MappingProxyType({})


def _case(
    operation_id: str,
    *,
    depends_on: tuple[str, ...] = (),
    requires: tuple[str, ...] = (),
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
    build_values: Callable[[ContextView], Mapping[str, object] | NoRequest] = (
        _build_no_request
    ),
    validate_response: Callable[[object, ContextView], None] = _validate_ok,
    extract: Callable[[object, ContextView], Mapping[str, object]] = _extract_empty,
) -> ReadCase:
    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=depends_on,
        requires=requires,
        provides=provides,
        allowed_no_target_codes=allowed_no_target_codes,
        binding=GeneratedReadBinding(
            api_module="iikocloud_client.api.synthetic_api",
            api_class="SyntheticApi",
            method_name=f"{operation_id}_with_http_info",
            request_module=None,
            request_class=None,
            request_keyword=None,
        ),
        build_values=build_values,
        validate_response=validate_response,
        extract=extract,
    )


def _operation_contract(plan: ReadPlan) -> Mapping[str, LiveOperation]:
    return MappingProxyType(
        {
            case.operation_id: LiveOperation(
                kind="read",
                cleanup=None,
                method="POST",
                path=f"/synthetic/{case.operation_id}",
            )
            for case in plan.cases
        }
    )


class _FakeContext:
    def __init__(
        self,
        values: Mapping[str, object],
        events: list[str] | None = None,
        *,
        fail_apply: bool = False,
    ) -> None:
        self.inner = ReadContext.seed(values)
        self.events = events
        self.fail_apply = fail_apply

    def view(self, keys: tuple[str, ...]) -> ContextView:
        if self.events is not None:
            self.events.append("view")
        return self.inner.view(keys)

    def apply(self, case: ReadCase, extracted: Mapping[str, object]) -> None:
        if self.events is not None:
            self.events.append("apply")
        if self.fail_apply:
            raise SafetyError("synthetic apply failure")
        self.inner.apply(case, extracted)

    def __repr__(self) -> str:
        return "_FakeContext()"


class _FakeSdk:
    def __init__(
        self,
        actions: Mapping[str, GeneratedCallResult[object] | BaseException] | None = None,
        events: list[str] | None = None,
    ) -> None:
        self.actions = dict(actions or {})
        self.events = events
        self.calls: list[tuple[str, object | None]] = []

    async def call_bound_read(
        self,
        operation_id: str,
        _binding: GeneratedReadBinding,
        request_model: object | None,
    ) -> GeneratedCallResult[object]:
        if operation_id in {called for called, _request in self.calls}:
            raise AssertionError("synthetic SDK operation invoked more than once")
        self.calls.append((operation_id, request_model))
        if self.events is not None:
            self.events.append("sdk")
        action = self.actions.get(
            operation_id,
            GeneratedCallResult(data=object(), status_code=200, duration_ms=7),
        )
        if isinstance(action, BaseException):
            raise action
        return action


class _FakeReport:
    def __init__(
        self,
        events: list[str] | None = None,
        *,
        fail_next_append: bool = False,
    ) -> None:
        self.events = events
        self.fail_next_append = fail_next_append
        self.outcomes: list[ReadOutcome] = []
        self.finished: list[bool] = []

    def append(self, outcome: ReadOutcome) -> object:
        if self.events is not None:
            self.events.append("report")
        if self.fail_next_append:
            self.fail_next_append = False
            raise SafetyError("synthetic report failure")
        self.outcomes.append(outcome)
        return object()

    def finish(self, success: bool) -> object:
        self.finished.append(success)
        return object()


async def _run(
    plan: ReadPlan,
    *,
    context: _FakeContext | None = None,
    sdk: _FakeSdk | None = None,
    report: _FakeReport | None = None,
    operation_contract: Mapping[str, LiveOperation] | None = None,
) -> tuple[ReadRunSummary, _FakeContext, _FakeSdk, _FakeReport]:
    selected_context = context or _FakeContext({})
    selected_sdk = sdk or _FakeSdk()
    selected_report = report or _FakeReport()
    summary = await run_read_plan(
        plan,
        context=cast(ReadContext, selected_context),
        sdk=cast(GeneratedLiveSdk, selected_sdk),
        operation_contract=operation_contract or _operation_contract(plan),
        report=cast(ReadReportWriter, selected_report),
    )
    return summary, selected_context, selected_sdk, selected_report


def _outcome_by_id(summary: ReadRunSummary) -> dict[str, ReadOutcome]:
    return {outcome.operation_id: outcome for outcome in summary.outcomes}


@pytest.mark.asyncio
async def test_run_read_plan_preserves_the_approved_case_order(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    events: list[str] = []
    private_value = "private-context-value"

    def build_values(_view: ContextView) -> NoRequest:
        events.append("values")
        return NO_REQUEST

    def validate_response(_data: object, _view: ContextView) -> None:
        events.append("validate")

    def extract(
        _data: object,
        _view: ContextView,
    ) -> Mapping[str, object]:
        events.append("extract")
        return MappingProxyType({"derived_value": private_value})

    case = _case(
        "a_read",
        provides=("derived_value",),
        build_values=build_values,
        validate_response=validate_response,
        extract=extract,
    )
    plan = ReadPlan.build((case,))

    def build_request(
        _binding: GeneratedReadBinding,
        values: Mapping[str, object] | NoRequest,
    ) -> object | None:
        events.append("request")
        assert values is NO_REQUEST
        return None

    monkeypatch.setattr(read_runner_module, "build_generated_request", build_request)
    summary, context, sdk, report = await _run(
        plan,
        context=_FakeContext({}, events),
        sdk=_FakeSdk(events=events),
        report=_FakeReport(events),
    )

    assert events == [
        "view",
        "values",
        "request",
        "sdk",
        "validate",
        "extract",
        "apply",
        "report",
    ]
    assert summary == ReadRunSummary(
        outcomes=(
            ReadOutcome(
                operation_id="a_read",
                method="POST",
                path="/synthetic/a_read",
                status=ReadStatus.PASSED,
                reason=None,
                http_status=200,
                duration_ms=7,
            ),
        ),
        passed=1,
        no_live_target=0,
        failed=0,
        aborted=0,
        success=True,
    )
    assert sdk.calls == [("a_read", None)]
    assert report.outcomes == list(summary.outcomes)
    assert report.finished == [True]
    assert private_value not in repr(summary)
    assert private_value not in repr(report.outcomes)
    assert private_value not in repr(context)


@pytest.mark.asyncio
async def test_declared_no_live_targets_do_not_consume_calls_or_block_dependents() -> None:
    def city_missing(_view: ContextView) -> NoRequest:
        raise NoLiveTarget(NoLiveTargetCode.CITY)

    def street_missing(_view: ContextView) -> NoRequest:
        raise NoLiveTarget(NoLiveTargetCode.STREET)

    plan = ReadPlan.build(
        (
            _case(
                "a_city",
                allowed_no_target_codes=frozenset({NoLiveTargetCode.CITY}),
                build_values=city_missing,
            ),
            _case("b_independent"),
            _case(
                "c_street",
                depends_on=("a_city",),
                allowed_no_target_codes=frozenset({NoLiveTargetCode.STREET}),
                build_values=street_missing,
            ),
        )
    )

    summary, _context, sdk, report = await _run(plan)
    outcomes = _outcome_by_id(summary)

    assert outcomes["a_city"].status is ReadStatus.NO_LIVE_TARGET
    assert outcomes["a_city"].reason == NoLiveTargetCode.CITY.value
    assert outcomes["c_street"].status is ReadStatus.NO_LIVE_TARGET
    assert outcomes["c_street"].reason == NoLiveTargetCode.STREET.value
    assert outcomes["b_independent"].status is ReadStatus.PASSED
    assert [operation_id for operation_id, _request in sdk.calls] == ["b_independent"]
    assert (summary.passed, summary.no_live_target, summary.failed, summary.aborted) == (
        1,
        2,
        0,
        0,
    )
    assert summary.success is True
    assert report.finished == [True]


@pytest.mark.asyncio
async def test_a_plan_with_only_no_live_targets_is_not_successful() -> None:
    def missing(_view: ContextView) -> NoRequest:
        raise NoLiveTarget(NoLiveTargetCode.CITY)

    plan = ReadPlan.build(
        (
            _case(
                "a_missing",
                allowed_no_target_codes=frozenset({NoLiveTargetCode.CITY}),
                build_values=missing,
            ),
        )
    )

    summary, _context, sdk, report = await _run(plan)

    assert summary.passed == 0
    assert summary.no_live_target == 1
    assert summary.success is False
    assert sdk.calls == []
    assert report.finished == [False]


@pytest.mark.parametrize(
    ("failure_phase", "reason"),
    [
        ("validator", ReadFailureCode.ASSERTION_FAILED.value),
        ("extractor", ReadFailureCode.EXTRACTOR_FAILED.value),
    ],
)
@pytest.mark.asyncio
async def test_explicit_response_failures_only_abort_dependents(
    failure_phase: str,
    reason: str,
) -> None:
    built: list[str] = []

    def build(operation_id: str) -> Callable[[ContextView], NoRequest]:
        def inner(_view: ContextView) -> NoRequest:
            built.append(operation_id)
            return NO_REQUEST

        return inner

    def validate(_data: object, _view: ContextView) -> None:
        if failure_phase == "validator":
            raise ReadAssertionFailure()

    def extract(
        _data: object,
        _view: ContextView,
    ) -> Mapping[str, object]:
        if failure_phase == "extractor":
            raise ReadExtractorFailure()
        return MappingProxyType({})

    plan = ReadPlan.build(
        (
            _case(
                "a_fails",
                build_values=build("a_fails"),
                validate_response=validate,
                extract=extract,
            ),
            _case("b_independent", build_values=build("b_independent")),
            _case(
                "c_dependent",
                depends_on=("a_fails",),
                build_values=build("c_dependent"),
            ),
        )
    )

    summary, _context, sdk, report = await _run(plan)
    outcomes = _outcome_by_id(summary)

    assert outcomes["a_fails"].status is ReadStatus.FAILED
    assert outcomes["a_fails"].reason == reason
    assert outcomes["a_fails"].http_status == 200
    assert outcomes["a_fails"].duration_ms == 7
    assert outcomes["b_independent"].status is ReadStatus.PASSED
    assert outcomes["c_dependent"].status is ReadStatus.ABORTED
    assert outcomes["c_dependent"].reason == ReadFailureCode.DEPENDENCY_FAILED.value
    assert built == ["a_fails", "b_independent"]
    assert [operation_id for operation_id, _request in sdk.calls] == [
        "a_fails",
        "b_independent",
    ]
    assert summary.success is False
    assert report.outcomes == list(summary.outcomes)
    assert report.finished == [False]


@pytest.mark.asyncio
async def test_request_validation_failure_aborts_all_unvisited_cases(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    built: list[str] = []

    def build(operation_id: str) -> Callable[[ContextView], NoRequest]:
        def inner(_view: ContextView) -> NoRequest:
            built.append(operation_id)
            return NO_REQUEST

        return inner

    plan = ReadPlan.build(
        (
            _case("a_invalid", build_values=build("a_invalid")),
            _case("b_unvisited", build_values=build("b_unvisited")),
        )
    )

    def reject_request(
        _binding: GeneratedReadBinding,
        _values: Mapping[str, object] | NoRequest,
    ) -> object | None:
        raise SafetyError("synthetic request rejection")

    monkeypatch.setattr(read_runner_module, "build_generated_request", reject_request)
    summary, _context, sdk, report = await _run(plan)

    assert [outcome.status for outcome in summary.outcomes] == [
        ReadStatus.ABORTED,
        ReadStatus.ABORTED,
    ]
    assert {outcome.reason for outcome in summary.outcomes} == {
        ReadFailureCode.SAFETY_INVARIANT.value
    }
    assert built == ["a_invalid"]
    assert sdk.calls == []
    assert report.finished == [False]


@pytest.mark.parametrize(
    ("failure", "reason", "http_status"),
    [
        (
            GeneratedCallFailure(ReadFailureCode.INVOCATION_FAILED),
            ReadFailureCode.INVOCATION_FAILED.value,
            None,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.HTTP_ERROR, 429),
            ReadFailureCode.HTTP_ERROR.value,
            429,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.TRANSPORT_ERROR, 0),
            ReadFailureCode.TRANSPORT_ERROR.value,
            None,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.RATE_GUARD_FAILED),
            ReadFailureCode.RATE_GUARD_FAILED.value,
            None,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.RECEIPT_FAILED),
            ReadFailureCode.RECEIPT_FAILED.value,
            None,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.DEPENDENCY_FAILED),
            ReadFailureCode.DEPENDENCY_FAILED.value,
            None,
        ),
        (
            GeneratedCallFailure(ReadFailureCode.CAPTURE_FAILED, 200),
            ReadFailureCode.CAPTURE_FAILED.value,
            200,
        ),
        (
            SafetyError("synthetic invariant failure"),
            ReadFailureCode.SAFETY_INVARIANT.value,
            None,
        ),
        (
            asyncio.CancelledError(),
            ReadFailureCode.CANCELLED.value,
            None,
        ),
    ],
)
@pytest.mark.asyncio
async def test_sdk_failures_abort_the_current_and_all_unvisited_cases(
    failure: BaseException,
    reason: str,
    http_status: int | None,
) -> None:
    built: list[str] = []

    def build(operation_id: str) -> Callable[[ContextView], NoRequest]:
        def inner(_view: ContextView) -> NoRequest:
            built.append(operation_id)
            return NO_REQUEST

        return inner

    plan = ReadPlan.build(
        (
            _case("a_stops", build_values=build("a_stops")),
            _case("b_unvisited", build_values=build("b_unvisited")),
        )
    )
    sdk = _FakeSdk({"a_stops": failure})

    summary, _context, _sdk, report = await _run(plan, sdk=sdk)

    assert [outcome.status for outcome in summary.outcomes] == [
        ReadStatus.ABORTED,
        ReadStatus.ABORTED,
    ]
    assert [outcome.reason for outcome in summary.outcomes] == [reason, reason]
    assert summary.outcomes[0].http_status == http_status
    assert summary.outcomes[1].http_status is None
    assert built == ["a_stops"]
    assert [operation_id for operation_id, _request in sdk.calls] == ["a_stops"]
    assert report.finished == [False]


@pytest.mark.parametrize("phase", ["validator", "extractor", "apply"])
@pytest.mark.asyncio
async def test_unexpected_post_response_failures_abort_the_run(phase: str) -> None:
    def validate(_data: object, _view: ContextView) -> None:
        if phase == "validator":
            raise RuntimeError("synthetic validator defect")

    def extract(
        _data: object,
        _view: ContextView,
    ) -> Mapping[str, object]:
        if phase == "extractor":
            raise RuntimeError("synthetic extractor defect")
        return MappingProxyType({})

    plan = ReadPlan.build(
        (
            _case(
                "a_stops",
                validate_response=validate,
                extract=extract,
            ),
            _case("b_unvisited"),
        )
    )
    context = _FakeContext({}, fail_apply=phase == "apply")

    summary, _context, sdk, report = await _run(plan, context=context)

    assert [outcome.reason for outcome in summary.outcomes] == [
        ReadFailureCode.SAFETY_INVARIANT.value,
        ReadFailureCode.SAFETY_INVARIANT.value,
    ]
    assert summary.outcomes[0].http_status == 200
    assert summary.outcomes[0].duration_ms == 7
    assert summary.outcomes[1].http_status is None
    assert [operation_id for operation_id, _request in sdk.calls] == ["a_stops"]
    assert report.finished == [False]


@pytest.mark.asyncio
async def test_report_failure_replaces_the_current_outcome_and_aborts_the_rest() -> None:
    plan = ReadPlan.build((_case("a_stops"), _case("b_unvisited")))
    report = _FakeReport(fail_next_append=True)

    summary, _context, sdk, selected_report = await _run(plan, report=report)

    assert [outcome.reason for outcome in summary.outcomes] == [
        ReadFailureCode.REPORT_FAILED.value,
        ReadFailureCode.REPORT_FAILED.value,
    ]
    assert [outcome.status for outcome in summary.outcomes] == [
        ReadStatus.ABORTED,
        ReadStatus.ABORTED,
    ]
    assert [operation_id for operation_id, _request in sdk.calls] == ["a_stops"]
    assert selected_report.outcomes == list(summary.outcomes)
    assert selected_report.finished == [False]
