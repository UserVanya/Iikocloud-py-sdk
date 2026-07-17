from __future__ import annotations

import socket
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
    def __init__(self, state: StubState) -> None:
        self.state = state
        self.acquired: list[str] = []
        self.statuses: list[tuple[str, int]] = []

    async def acquire(self, operation_id: str) -> None:
        self.acquired.append(operation_id)

    def record_status(self, operation_id: str, status: int) -> None:
        self.statuses.append((operation_id, status))
        self.state.record_status("f" * 64, operation_id, status)


class StubCapture:
    def __init__(self) -> None:
        self.pairs: list[tuple[str, object, object, Mapping[str, Any]]] = []

    def write_model_pair(
        self,
        operation_id: str,
        request_model: object,
        response_model: object,
        metadata: Mapping[str, Any],
    ) -> None:
        self.pairs.append((operation_id, request_model, response_model, metadata))


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
    capture = StubCapture()
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
    capture = StubCapture()
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
    capture = StubCapture()
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
    assert caught.value.__cause__ is error
    assert guard.acquired == ["get_external_menu_by_id"]
    assert guard.statuses == [("get_external_menu_by_id", 429)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_external_menu_by_id", 429)]
    assert state.circuit_open
    assert capture.pairs == []


def test_constructor_rejects_a_state_not_bound_to_the_guard() -> None:
    guard_state = StubState()
    guard = StubGuard(guard_state)

    with pytest.raises(SafetyError, match="same live state"):
        _adapter(guard=guard, state=StubState())
