from __future__ import annotations

import socket
import traceback
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

import pytest

from iikocloud_client.api.menu_api import MenuApi
from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException
from iikocloud_client.models.remove_products_from_stop_list_request import (
    RemoveProductsFromStopListRequest,
)
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.state import LiveStateStore

_ORGANIZATION_ID = "11111111-1111-4111-8111-111111111111"
_TERMINAL_GROUP_ID = "22222222-2222-4222-8222-222222222222"
_PRODUCT_ID = "33333333-3333-4333-8333-333333333333"
_OTHER_ID = "99999999-9999-4999-8999-999999999999"


class _StubState:
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


class _StubGuard:
    def __init__(self, state: _StubState) -> None:
        self.state = state
        self.acquired: list[str] = []
        self.statuses: list[tuple[str, int]] = []

    async def acquire(self, operation_id: str) -> None:
        self.acquired.append(operation_id)

    def record_status(self, operation_id: str, status: int) -> None:
        self.statuses.append((operation_id, status))
        self.state.record_status("f" * 64, operation_id, status)


@pytest.fixture(autouse=True)
def _forbid_network(monkeypatch: pytest.MonkeyPatch) -> None:
    real_socket = socket.socket

    def guarded_socket(*args: Any, **kwargs: Any) -> socket.SocketType:
        family = kwargs.get("family", args[0] if args else socket.AF_INET)
        if family in {socket.AF_INET, socket.AF_INET6}:
            raise AssertionError("generated cleanup tests must not create a network socket")
        return real_socket(*args, **kwargs)

    monkeypatch.setattr(socket, "socket", guarded_socket)


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="fixture-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id="menu-id",
        terminal_group_id=_TERMINAL_GROUP_ID,
        write_product_id=_PRODUCT_ID,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="f" * 64,
    )


def _payload() -> dict[str, object]:
    return {
        "items": [{"productId": _PRODUCT_ID}],
        "organizationId": _ORGANIZATION_ID,
        "terminalGroupId": _TERMINAL_GROUP_ID,
    }


def _auth_receipt(path: Path) -> LiveReceipt:
    receipt = LiveReceipt(
        run_id="20260721T120000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=("authenticate",),
        had_429=False,
        completed=False,
    )
    receipt.write(path)
    return receipt


def _adapter(
    guard: _StubGuard,
    state: _StubState,
    *,
    profile: ResolvedLiveProfile | None = None,
    receipt: LiveReceipt | None = None,
    receipt_path: Path | None = None,
) -> GeneratedLiveSdk:
    return GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=profile or _profile(),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        receipt=receipt,
        receipt_path=receipt_path,
    )


@pytest.mark.asyncio
async def test_execute_cleanup_rebuilds_request_and_dispatches_exactly_once(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    adapter = _adapter(
        guard,
        state,
        receipt=_auth_receipt(receipt_path),
        receipt_path=receipt_path,
    )
    requests: list[RemoveProductsFromStopListRequest] = []
    request_timeouts: list[tuple[float, float]] = []

    async def remove_products(
        _api: MenuApi,
        *,
        remove_products_from_stop_list_request: RemoveProductsFromStopListRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[dict[str, str]]:
        recorded = adapter.receipt
        assert recorded is not None
        assert recorded.operations == ("authenticate", "remove_products_from_stop_list")
        assert LiveReceipt.load(receipt_path) == recorded
        requests.append(remove_products_from_stop_list_request)
        request_timeouts.append(_request_timeout)
        return ApiResponse(
            status_code=200,
            headers=None,
            data={"correlationId": "44444444-4444-4444-8444-444444444444"},
            raw_data=b"{}",
        )

    monkeypatch.setattr(
        MenuApi,
        "remove_products_from_stop_list_with_http_info",
        remove_products,
    )
    payload = _payload()

    await adapter.execute_cleanup("remove_products_from_stop_list", payload)

    assert len(requests) == 1
    assert requests[0].model_dump(mode="json", by_alias=True, exclude_none=True) == payload
    assert request_timeouts == [(10.0, 30.0)]
    assert guard.acquired == ["remove_products_from_stop_list"]
    assert guard.statuses == [("remove_products_from_stop_list", 200)]
    assert state.statuses == [("f" * 64, "remove_products_from_stop_list", 200)]


@pytest.mark.asyncio
async def test_execute_cleanup_preserves_429_terminal_semantics_without_retry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    adapter = _adapter(
        guard,
        state,
        receipt=_auth_receipt(receipt_path),
        receipt_path=receipt_path,
    )
    invocations = 0

    async def fail_with_429(
        _api: MenuApi,
        *,
        remove_products_from_stop_list_request: RemoveProductsFromStopListRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        nonlocal invocations
        assert isinstance(
            remove_products_from_stop_list_request,
            RemoveProductsFromStopListRequest,
        )
        assert _request_timeout == (10.0, 30.0)
        invocations += 1
        raise ApiException(status=429, reason="synthetic")

    monkeypatch.setattr(
        MenuApi,
        "remove_products_from_stop_list_with_http_info",
        fail_with_429,
    )

    with pytest.raises(SafetyError, match="circuit opened"):
        await adapter.execute_cleanup("remove_products_from_stop_list", _payload())

    assert invocations == 1
    assert guard.acquired == ["remove_products_from_stop_list"]
    assert guard.statuses == [("remove_products_from_stop_list", 429)]
    assert state.circuit_open
    recorded = adapter.receipt
    assert recorded is not None
    assert recorded.operations == ("authenticate", "remove_products_from_stop_list")
    assert recorded.had_429
    assert LiveReceipt.load(receipt_path) == recorded


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "operation_id",
    ["add_products_to_stop_list", "unknown_cleanup"],
    ids=["non-cleanup", "unknown"],
)
async def test_execute_cleanup_rejects_unapproved_operation_before_live_work(
    operation_id: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)
    invocations = 0

    async def invoke(
        _api: MenuApi,
        *,
        remove_products_from_stop_list_request: RemoveProductsFromStopListRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    monkeypatch.setattr(
        MenuApi,
        "remove_products_from_stop_list_with_http_info",
        invoke,
    )

    with pytest.raises(SafetyError, match="approved cleanup operation"):
        await adapter.execute_cleanup(operation_id, _payload())

    assert guard.acquired == []
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 0


@pytest.mark.asyncio
async def test_execute_cleanup_sanitizes_invalid_payload_before_live_work(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)
    invocations = 0

    async def invoke(
        _api: MenuApi,
        *,
        remove_products_from_stop_list_request: RemoveProductsFromStopListRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    monkeypatch.setattr(
        MenuApi,
        "remove_products_from_stop_list_with_http_info",
        invoke,
    )
    private_marker = "private-invalid-identifier"
    invalid_payload: Mapping[str, object] = {
        "items": [{"productId": private_marker}],
        "organizationId": _ORGANIZATION_ID,
        "terminalGroupId": _TERMINAL_GROUP_ID,
    }

    with pytest.raises(SafetyError) as caught:
        await adapter.execute_cleanup("remove_products_from_stop_list", invalid_payload)

    assert str(caught.value) == "Generated cleanup payload is invalid"
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_marker not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == []
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 0


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "boundary",
    [
        "organization",
        "terminal-group",
        "product",
        "multiple-items",
        "write-disabled",
        "organization-not-allowed",
        "malformed-profile-id",
    ],
)
async def test_execute_cleanup_rejects_payload_outside_selected_write_profile_before_live_work(
    boundary: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    profile = _profile()
    payload = _payload()
    private_marker = "private-malformed-profile-identifier"

    if boundary == "organization":
        payload["organizationId"] = _OTHER_ID
    elif boundary == "terminal-group":
        payload["terminalGroupId"] = _OTHER_ID
    elif boundary == "product":
        payload["items"] = [{"productId": _OTHER_ID}]
    elif boundary == "multiple-items":
        payload["items"] = [
            {"productId": _PRODUCT_ID},
            {"productId": _PRODUCT_ID},
        ]
    elif boundary == "write-disabled":
        profile = replace(profile, allow_write=False)
    elif boundary == "organization-not-allowed":
        profile = replace(profile, allowed_organization_ids=(_OTHER_ID,))
    elif boundary == "malformed-profile-id":
        profile = replace(profile, terminal_group_id=private_marker)
    else:  # pragma: no cover - exhaustive parametrization guard
        raise AssertionError(f"unknown boundary fixture: {boundary}")

    adapter = _adapter(guard, state, profile=profile)
    invocations = 0

    async def invoke(
        _api: MenuApi,
        *,
        remove_products_from_stop_list_request: RemoveProductsFromStopListRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    monkeypatch.setattr(
        MenuApi,
        "remove_products_from_stop_list_with_http_info",
        invoke,
    )

    with pytest.raises(SafetyError) as caught:
        await adapter.execute_cleanup("remove_products_from_stop_list", payload)

    assert str(caught.value) == ("Generated cleanup request is outside the selected write profile")
    assert caught.value.__cause__ is None
    assert caught.value.__suppress_context__
    assert private_marker not in "".join(traceback.format_exception(caught.value))
    assert guard.acquired == []
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 0
