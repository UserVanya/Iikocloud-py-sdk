from __future__ import annotations

import asyncio
import socket
import traceback
from collections.abc import Mapping
from typing import Any, cast

import pytest

from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException
from tools.openapi_pipeline.capture import LiveCapture
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard
from tools.openapi_pipeline.live.state import LiveStateStore


class StubState:
    def __init__(self) -> None:
        self.statuses: list[tuple[str, str, int]] = []
        self.circuit_open = False

    def record_status(
        self,
        profile_fingerprint: str,
        operation_id: str,
        status: int,
    ) -> None:
        self.statuses.append((profile_fingerprint, operation_id, status))
        if status == 429:
            self.circuit_open = True


class StubGuard:
    def __init__(self, state: StubState, *, record_error: Exception | None = None) -> None:
        self.state = state
        self.record_error = record_error
        self.acquired: list[str] = []
        self.statuses: list[tuple[str, int]] = []

    async def acquire(self, operation_id: str) -> None:
        self.acquired.append(operation_id)

    def record_status(self, operation_id: str, status: int) -> None:
        self.statuses.append((operation_id, status))
        if self.record_error is not None:
            raise self.record_error
        self.state.record_status("f" * 64, operation_id, status)


class StubCapture:
    def __init__(
        self,
        selected_operation: str,
        *,
        write_error: Exception | None = None,
    ) -> None:
        self.selected_operation = selected_operation
        self.write_error = write_error
        self.selections: list[str] = []
        self.write_attempts: list[tuple[str, object, object, Mapping[str, Any]]] = []
        self.pairs: list[tuple[str, object, object, Mapping[str, Any]]] = []

    def assert_selected(self, operation_id: str) -> None:
        self.selections.append(operation_id)
        if operation_id != self.selected_operation:
            raise SafetyError("Live capture operation was not explicitly selected")

    def write_model_pair(
        self,
        operation_id: str,
        request_model: object,
        response_model: object,
        metadata: Mapping[str, Any],
    ) -> None:
        pair = (operation_id, request_model, response_model, metadata)
        self.write_attempts.append(pair)
        if self.write_error is not None:
            raise self.write_error
        self.pairs.append(pair)


class PrivateMalformedStatus:
    def __init__(self, marker: str) -> None:
        self.marker = marker

    def __int__(self) -> int:
        raise RuntimeError(self.marker)

    def __str__(self) -> str:
        return self.marker


class PrivateNonApiResponse:
    def __init__(self, marker: str) -> None:
        self.marker = marker
        self.accessed: list[str] = []

    @property
    def status_code(self) -> int:
        self.accessed.append("status_code")
        raise RuntimeError(self.marker)

    @property
    def data(self) -> object:
        self.accessed.append("data")
        raise RuntimeError(self.marker)


@pytest.fixture(autouse=True)
def _forbid_network(monkeypatch: pytest.MonkeyPatch) -> None:
    real_socket = socket.socket

    def guarded_socket(*args: Any, **kwargs: Any) -> socket.SocketType:
        family = kwargs.get("family", args[0] if args else socket.AF_INET)
        if family in {socket.AF_INET, socket.AF_INET6}:
            raise AssertionError("generated adapter tests must not create a network socket")
        return real_socket(*args, **kwargs)

    monkeypatch.setattr(socket, "socket", guarded_socket)


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="fixture-login",
        organization_id="organization-id",
        external_menu_id="menu-id",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=("organization-id",),
        fingerprint="f" * 64,
    )


def _adapter(
    *,
    guard: StubGuard,
    state: StubState,
    capture: StubCapture | None = None,
) -> GeneratedLiveSdk:
    return GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=_profile(),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        capture=cast(LiveCapture, capture) if capture is not None else None,
    )


async def _assert_next_call_is_blocked_before_work(
    adapter: GeneratedLiveSdk,
    guard: StubGuard,
    capture: StubCapture | None = None,
) -> None:
    acquired_before = list(guard.acquired)
    statuses_before = list(guard.statuses)
    selections_before = list(capture.selections) if capture is not None else None
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    with pytest.raises(SafetyError, match="unusable"):
        await adapter.call_generated("get_organizations", {}, invoke)

    assert guard.acquired == acquired_before
    assert guard.statuses == statuses_before
    if capture is not None:
        assert capture.selections == selections_before
    assert invocations == 0


@pytest.mark.asyncio
async def test_success_acquires_invokes_records_and_returns_data_once() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    request_model = {"organizationIds": ["organization-id"]}
    response_model: dict[str, object] = {"organizations": []}
    invocations = 0

    async def invoke() -> ApiResponse[dict[str, object]]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(
            status_code=200,
            headers={"content-type": "application/json"},
            data=response_model,
            raw_data=b'{"organizations":[]}',
        )

    result: dict[str, object] = await adapter.call_generated(
        "get_organizations", request_model, invoke
    )

    assert result is response_model
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 200)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_organizations", 200)]


@pytest.mark.asyncio
async def test_success_captures_completed_model_pair_with_status() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_external_menu_by_id")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    request_model = {"menuId": "menu-id"}
    response_model: dict[str, object] = {"formatVersion": 4}

    async def invoke() -> ApiResponse[dict[str, object]]:
        return ApiResponse(
            status_code=201,
            headers=None,
            data=response_model,
            raw_data=b'{"formatVersion":4}',
        )

    result: dict[str, object] = await adapter.call_generated(
        "get_external_menu_by_id", request_model, invoke
    )

    assert result is response_model
    assert capture.pairs == [
        (
            "get_external_menu_by_id",
            request_model,
            response_model,
            {"status": 201},
        )
    ]


@pytest.mark.asyncio
async def test_non_429_api_exception_is_recorded_then_propagated() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_organizations")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    error = ApiException(status=503, reason="fixture service unavailable")
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise error

    with pytest.raises(ApiException) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert caught.value is error
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 503)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_organizations", 503)]
    assert not state.circuit_open
    assert capture.pairs == []


@pytest.mark.asyncio
async def test_429_opens_circuit_and_raises_sanitized_error_without_retry() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_external_menu_by_id")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    private_detail = "private-upstream-response"
    error = ApiException(status=429, reason=private_detail, body=private_detail)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise error

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_external_menu_by_id", {}, invoke)

    assert str(caught.value) == "iiko returned 429; live circuit opened"
    assert private_detail not in str(caught.value)
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == ["get_external_menu_by_id"]
    assert guard.statuses == [("get_external_menu_by_id", 429)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_external_menu_by_id", 429)]
    assert state.circuit_open
    assert capture.pairs == []
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


def test_constructor_rejects_a_state_not_bound_to_the_guard() -> None:
    guard_state = StubState()
    guard = StubGuard(guard_state)

    with pytest.raises(SafetyError, match="same live state"):
        _adapter(guard=guard, state=StubState())


@pytest.mark.asyncio
async def test_capture_selection_mismatch_fails_before_acquire_or_invoke() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_external_menu_by_id")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    with pytest.raises(SafetyError, match="explicitly selected"):
        await adapter.call_generated("get_organizations", {}, invoke)

    assert capture.selections == ["get_organizations"]
    assert capture.pairs == []
    assert guard.acquired == []
    assert guard.statuses == []
    assert invocations == 0


@pytest.mark.asyncio
async def test_response_429_records_opens_circuit_and_poison_adapter_without_retry() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_external_menu_by_id")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(
            status_code=429,
            headers={"content-type": "application/json"},
            data={"private": "response-marker"},
            raw_data=b'{"private":"response-marker"}',
        )

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_external_menu_by_id", {}, invoke)

    assert str(caught.value) == "iiko returned 429; live circuit opened"
    assert caught.value.__suppress_context__
    assert capture.selections == ["get_external_menu_by_id"]
    assert capture.pairs == []
    assert guard.acquired == ["get_external_menu_by_id"]
    assert guard.statuses == [("get_external_menu_by_id", 429)]
    assert invocations == 1
    assert state.circuit_open
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


@pytest.mark.asyncio
async def test_cancelled_invoke_is_reraised_and_poison_adapter() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise asyncio.CancelledError

    with pytest.raises(asyncio.CancelledError):
        await adapter.call_generated("get_organizations", {}, invoke)

    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
async def test_unknown_invoke_error_is_sanitized_and_poison_adapter_without_retry() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    private_detail = "private-transport-marker"
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise RuntimeError(private_detail)

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK invocation failed without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
async def test_response_status_recording_failure_is_sanitized_and_poison_adapter() -> None:
    state = StubState()
    private_detail = "private-record-response-marker"
    guard = StubGuard(state, record_error=RuntimeError(private_detail))
    adapter = _adapter(guard=guard, state=state)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK status recording failed without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 200)]
    assert state.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
async def test_api_exception_status_recording_failure_is_sanitized_and_poison_adapter() -> None:
    state = StubState()
    private_detail = "private-record-exception-marker"
    guard = StubGuard(state, record_error=RuntimeError(private_detail))
    adapter = _adapter(guard=guard, state=state)
    api_error = ApiException(status=503, reason="private-api-reason")
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise api_error

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK status recording failed without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    formatted = "".join(traceback.format_exception(caught.value))
    assert private_detail not in formatted
    assert "private-api-reason" not in formatted
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 503)]
    assert state.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
async def test_capture_failure_after_response_is_sanitized_and_poison_adapter() -> None:
    state = StubState()
    guard = StubGuard(state)
    private_detail = "private-capture-marker"
    capture = StubCapture(
        "get_external_menu_by_id",
        write_error=RuntimeError(private_detail),
    )
    adapter = _adapter(guard=guard, state=state, capture=capture)
    request_model = {"menuId": "menu-id"}
    response_model = {"formatVersion": 4}
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(
            status_code=200,
            headers=None,
            data=response_model,
            raw_data=b'{"formatVersion":4}',
        )

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_external_menu_by_id", request_model, invoke)

    assert str(caught.value) == "Generated SDK capture failed after response without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert capture.selections == ["get_external_menu_by_id"]
    assert len(capture.write_attempts) == 1
    assert capture.pairs == []
    assert guard.acquired == ["get_external_menu_by_id"]
    assert guard.statuses == [("get_external_menu_by_id", 200)]
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


@pytest.mark.asyncio
async def test_ascii_string_429_is_normalized_and_opens_persistent_circuit() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    private_detail = "private-string-status-marker"
    api_error = ApiException(status="429", reason=private_detail, body=private_detail)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise api_error

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "iiko returned 429; live circuit opened"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 429)]
    assert state.circuit_open
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "malformed_status",
    [
        True,
        -1,
        600,
        "private-status-marker",
        PrivateMalformedStatus("private-status-marker"),
    ],
    ids=["bool", "negative", "too-large", "string", "custom-object"],
)
async def test_malformed_api_exception_status_is_safely_rejected(
    malformed_status: object,
) -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    private_detail = "private-status-marker"
    api_error = ApiException(
        status=malformed_status,
        reason=private_detail,
        body=private_detail,
    )
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise api_error

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK exception has an invalid HTTP status"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard)


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [None, 0], ids=["missing", "zero"])
async def test_statusless_api_exception_records_zero_then_poison_adapter(
    status: int | None,
) -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_organizations")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    private_detail = "private-statusless-marker"
    api_error = ApiException(status=status, reason=private_detail, body=private_detail)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        raise api_error

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK exception has no usable HTTP status"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert capture.selections == ["get_organizations"]
    assert capture.write_attempts == []
    assert capture.pairs == []
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 0)]
    assert state.statuses == [("f" * 64, "get_organizations", 0)]
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


@pytest.mark.asyncio
async def test_non_api_response_is_rejected_before_status_capture_or_data_access() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_organizations")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    private_detail = "private-invalid-response-marker"
    invalid_response = PrivateNonApiResponse(private_detail)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return cast(ApiResponse[object], invalid_response)

    with pytest.raises(SafetyError) as caught:
        await adapter.call_generated("get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK invocation returned an invalid response"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert invalid_response.accessed == []
    assert capture.selections == ["get_organizations"]
    assert capture.write_attempts == []
    assert capture.pairs == []
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)
