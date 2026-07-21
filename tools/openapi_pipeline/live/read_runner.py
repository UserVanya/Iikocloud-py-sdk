"""Sequential, fail-closed execution for planned live reads."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from contextlib import suppress
from dataclasses import dataclass
from types import MappingProxyType

from ..errors import SafetyError
from .generated import GeneratedCallFailure, GeneratedCallResult, GeneratedLiveSdk
from .read_case import (
    NoLiveTarget,
    ReadAssertionFailure,
    ReadCase,
    ReadContext,
    ReadExtractorFailure,
    ReadFailureCode,
    build_generated_request,
)
from .read_planner import ReadPlan
from .read_report import ReadOutcome, ReadReportWriter, ReadStatus
from .session import LiveOperation

_PREFLIGHT_FAILURE = "Live read preflight failed"
_REPORT_PERSISTENCE_FAILURE = "Read report terminal outcome persistence failed"
_OPERATION_KINDS = frozenset({"auth", "read", "compensating", "cleanup"})


@dataclass(frozen=True, slots=True)
class ReadRunSummary:
    outcomes: tuple[ReadOutcome, ...]
    passed: int
    no_live_target: int
    failed: int
    aborted: int
    success: bool


def _contract_snapshot(
    value: object,
    *,
    require_immutable: bool,
) -> dict[str, LiveOperation]:
    if require_immutable and type(value) is not MappingProxyType:
        raise SafetyError(_PREFLIGHT_FAILURE)
    if not isinstance(value, Mapping):
        raise SafetyError(_PREFLIGHT_FAILURE)
    snapshot_failed = False
    items: tuple[tuple[object, object], ...] = ()
    try:
        items = tuple(value.items())
    except Exception:
        snapshot_failed = True
    if snapshot_failed:
        raise SafetyError(_PREFLIGHT_FAILURE) from None

    snapshot: dict[str, LiveOperation] = {}
    for operation_id, operation in items:
        if (
            type(operation_id) is not str
            or operation_id in snapshot
            or type(operation) is not LiveOperation
            or type(operation.kind) is not str
            or operation.kind not in _OPERATION_KINDS
            or (
                operation.cleanup is not None
                and type(operation.cleanup) is not str
            )
            or type(operation.method) is not str
            or operation.method not in {"GET", "POST"}
            or type(operation.path) is not str
        ):
            raise SafetyError(_PREFLIGHT_FAILURE)
        snapshot[operation_id] = operation
    return snapshot


def _same_operation(left: LiveOperation, right: LiveOperation) -> bool:
    return (
        left.kind == right.kind
        and left.cleanup == right.cleanup
        and left.method == right.method
        and left.path == right.path
    )


def _validated_plan_contract(
    plan: ReadPlan,
    operation_contract: Mapping[str, LiveOperation],
    sdk: GeneratedLiveSdk,
) -> Mapping[str, LiveOperation]:
    validation_failed = False
    validated: dict[str, LiveOperation] = {}
    try:
        supplied = _contract_snapshot(
            operation_contract,
            require_immutable=False,
        )
        bound = _contract_snapshot(
            sdk.operation_contract,
            require_immutable=True,
        )
        if supplied.keys() != bound.keys() or any(
            not _same_operation(operation, bound[operation_id])
            for operation_id, operation in supplied.items()
        ):
            raise SafetyError(_PREFLIGHT_FAILURE)

        for case in plan.cases:
            operation = bound[case.operation_id]
            if operation.kind != "read":
                raise SafetyError(_PREFLIGHT_FAILURE)
            _aborted_outcome(
                case,
                operation,
                ReadFailureCode.SAFETY_INVARIANT,
            )
            validated[case.operation_id] = operation
    except Exception:
        validation_failed = True

    if validation_failed:
        raise SafetyError(_PREFLIGHT_FAILURE) from None
    return MappingProxyType(validated)


def _outcome(
    case: ReadCase,
    operation: LiveOperation,
    status: ReadStatus,
    reason: str | None,
    *,
    http_status: int | None = None,
    duration_ms: int | None = None,
) -> ReadOutcome:
    return ReadOutcome(
        operation_id=case.operation_id,
        method=operation.method,
        path=operation.path,
        status=status,
        reason=reason,
        http_status=http_status,
        duration_ms=duration_ms,
    )


def _aborted_outcome(
    case: ReadCase,
    operation: LiveOperation,
    code: ReadFailureCode,
    *,
    http_status: int | None = None,
    duration_ms: int | None = None,
) -> ReadOutcome:
    return _outcome(
        case,
        operation,
        ReadStatus.ABORTED,
        code.value,
        http_status=http_status,
        duration_ms=duration_ms,
    )


def _generated_failure_details(
    failure: GeneratedCallFailure,
) -> tuple[ReadFailureCode, int | None]:
    code = failure.code
    if code in {
        ReadFailureCode.ASSERTION_FAILED,
        ReadFailureCode.EXTRACTOR_FAILED,
    }:
        return ReadFailureCode.SAFETY_INVARIANT, None
    status = failure.status_code
    if status is None or status == 0:
        return code, None
    if type(status) is not int or not 100 <= status <= 599:
        return ReadFailureCode.SAFETY_INVARIANT, None
    return code, status


def _append_outcome(
    report: ReadReportWriter,
    outcome: ReadOutcome,
    case: ReadCase,
    operation: LiveOperation,
) -> tuple[ReadOutcome, ReadFailureCode | None]:
    try:
        report.append(outcome)
        return outcome, None
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
    except Exception:
        code = ReadFailureCode.REPORT_FAILED

    replacement = _aborted_outcome(
        case,
        operation,
        code,
        http_status=outcome.http_status,
        duration_ms=outcome.duration_ms,
    )
    append_failed = False
    try:
        report.append(replacement)
    except BaseException:
        append_failed = True
    if append_failed:
        raise SafetyError(_REPORT_PERSISTENCE_FAILURE) from None
    return replacement, code


async def _run_case(
    case: ReadCase,
    operation: LiveOperation,
    *,
    context: ReadContext,
    sdk: GeneratedLiveSdk,
) -> tuple[ReadOutcome, ReadFailureCode | None]:
    try:
        view = context.view(case.requires)
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return _aborted_outcome(case, operation, code), code
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return _aborted_outcome(case, operation, code), code

    try:
        values = case.build_values(view)
    except NoLiveTarget as missing:
        if missing.code not in case.allowed_no_target_codes:
            code = ReadFailureCode.SAFETY_INVARIANT
            return _aborted_outcome(case, operation, code), code
        return (
            _outcome(
                case,
                operation,
                ReadStatus.NO_LIVE_TARGET,
                missing.code.value,
            ),
            None,
        )
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return _aborted_outcome(case, operation, code), code
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return _aborted_outcome(case, operation, code), code

    try:
        request = build_generated_request(case.binding, values)
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return _aborted_outcome(case, operation, code), code
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return _aborted_outcome(case, operation, code), code

    try:
        result = await sdk.call_bound_read(
            case.operation_id,
            case.binding,
            request,
        )
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return _aborted_outcome(case, operation, code), code
    except GeneratedCallFailure as failure:
        code, http_status = _generated_failure_details(failure)
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
            ),
            code,
        )
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return _aborted_outcome(case, operation, code), code

    if (
        type(result) is not GeneratedCallResult
        or type(result.status_code) is not int
        or not 200 <= result.status_code <= 299
        or type(result.duration_ms) is not int
        or result.duration_ms < 0
    ):
        code = ReadFailureCode.SAFETY_INVARIANT
        return _aborted_outcome(case, operation, code), code
    http_status = result.status_code
    duration_ms = result.duration_ms

    try:
        case.validate_response(result.data, view)
    except ReadAssertionFailure:
        return (
            _outcome(
                case,
                operation,
                ReadStatus.FAILED,
                ReadFailureCode.ASSERTION_FAILED.value,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            None,
        )
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )

    try:
        extracted = case.extract(result.data, view)
    except ReadExtractorFailure:
        return (
            _outcome(
                case,
                operation,
                ReadStatus.FAILED,
                ReadFailureCode.EXTRACTOR_FAILED.value,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            None,
        )
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )

    try:
        context.apply(case, extracted)
    except asyncio.CancelledError:
        code = ReadFailureCode.CANCELLED
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )
    except Exception:
        code = ReadFailureCode.SAFETY_INVARIANT
        return (
            _aborted_outcome(
                case,
                operation,
                code,
                http_status=http_status,
                duration_ms=duration_ms,
            ),
            code,
        )

    return (
        _outcome(
            case,
            operation,
            ReadStatus.PASSED,
            None,
            http_status=http_status,
            duration_ms=duration_ms,
        ),
        None,
    )


async def run_read_plan(
    plan: ReadPlan,
    *,
    context: ReadContext,
    sdk: GeneratedLiveSdk,
    operation_contract: Mapping[str, LiveOperation],
    report: ReadReportWriter,
) -> ReadRunSummary:
    preflight_failed = False
    trusted_contract: Mapping[str, LiveOperation] = MappingProxyType({})
    try:
        trusted_contract = _validated_plan_contract(
            plan,
            operation_contract,
            sdk,
        )
    except Exception:
        preflight_failed = True

    if preflight_failed:
        with suppress(BaseException):
            report.finish(False)
        raise SafetyError(_PREFLIGHT_FAILURE) from None

    outcomes: list[ReadOutcome] = []
    outcome_by_id: dict[str, ReadOutcome] = {}
    abort_code: ReadFailureCode | None = None

    for case in plan.cases:
        operation = trusted_contract[case.operation_id]
        case_abort: ReadFailureCode | None = None

        if abort_code is not None:
            candidate = _aborted_outcome(case, operation, abort_code)
        elif any(
            outcome_by_id[dependency_id].status
            in {ReadStatus.FAILED, ReadStatus.ABORTED}
            for dependency_id in case.depends_on
        ):
            candidate = _aborted_outcome(
                case,
                operation,
                ReadFailureCode.DEPENDENCY_FAILED,
            )
        else:
            candidate, case_abort = await _run_case(
                case,
                operation,
                context=context,
                sdk=sdk,
            )

        recorded, report_abort = _append_outcome(
            report,
            candidate,
            case,
            operation,
        )
        outcomes.append(recorded)
        outcome_by_id[case.operation_id] = recorded
        if report_abort is not None:
            abort_code = report_abort
        elif case_abort is not None:
            abort_code = case_abort

    frozen_outcomes = tuple(outcomes)
    passed = sum(outcome.status is ReadStatus.PASSED for outcome in frozen_outcomes)
    no_live_target = sum(
        outcome.status is ReadStatus.NO_LIVE_TARGET for outcome in frozen_outcomes
    )
    failed = sum(outcome.status is ReadStatus.FAILED for outcome in frozen_outcomes)
    aborted = sum(outcome.status is ReadStatus.ABORTED for outcome in frozen_outcomes)
    success = passed >= 1 and failed == 0 and aborted == 0
    summary = ReadRunSummary(
        outcomes=frozen_outcomes,
        passed=passed,
        no_live_target=no_live_target,
        failed=failed,
        aborted=aborted,
        success=success,
    )
    finalization_failed = False
    try:
        report.finish(success)
    except Exception:
        finalization_failed = True
    if finalization_failed:
        raise SafetyError("Read report finalization failed") from None
    return summary


__all__ = ["ReadRunSummary", "run_read_plan"]
