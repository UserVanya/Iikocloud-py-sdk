from __future__ import annotations

import asyncio
import dataclasses
import socket
import sys
import traceback
from collections.abc import Awaitable, Callable, Mapping
from pathlib import Path
from types import MappingProxyType, ModuleType
from typing import Any, cast

import pytest

from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException
from tools.openapi_pipeline.capture import LiveCapture
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import (
    GeneratedCallFailure,
    GeneratedCallResult,
    GeneratedLiveSdk,
)
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard
from tools.openapi_pipeline.live.read_case import (
    GeneratedReadBinding,
    ReadFailureCode,
)
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.session import LiveOperation
from tools.openapi_pipeline.live.state import LiveStateStore


class SyntheticRequest:
    def __init__(self, value: object) -> None:
        self.value = value

    @classmethod
    def model_validate(cls, value: object) -> SyntheticRequest:
        return cls(value)


class OtherSyntheticRequest:
    pass


class SyntheticApi:
    handlers: dict[str, Callable[[], Awaitable[ApiResponse[object]]]] = {}
    approved_calls: list[tuple[str, object | None, tuple[float, float]]] = []
    wrong_calls = 0
    clients: list[object] = []

    def __init__(self, api_client: object) -> None:
        self.clients.append(api_client)

    async def get_organizations_with_http_info(
        self,
        *,
        get_organizations_request: SyntheticRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        self.approved_calls.append(
            ("get_organizations", get_organizations_request, _request_timeout)
        )
        return await self.handlers["get_organizations"]()

    async def get_external_menu_by_id_with_http_info(
        self,
        *,
        get_external_menu_by_id_request: SyntheticRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        self.approved_calls.append(
            (
                "get_external_menu_by_id",
                get_external_menu_by_id_request,
                _request_timeout,
            )
        )
        return await self.handlers["get_external_menu_by_id"]()

    async def no_body_read_with_http_info(
        self,
        *,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        self.approved_calls.append(("no_body_read", None, _request_timeout))
        return await self.handlers["no_body_read"]()

    async def wrong_read_with_http_info(
        self,
        *,
        wrong_read_request: SyntheticRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        del wrong_read_request, _request_timeout
        type(self).wrong_calls += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")


class InheritedApiBase:
    async def get_organizations_with_http_info(
        self,
        *,
        get_organizations_request: SyntheticRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        del get_organizations_request, _request_timeout
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")


class InheritedApi(InheritedApiBase):
    def __init__(self, api_client: object) -> None:
        del api_client


class WrongKeywordApi:
    def __init__(self, api_client: object) -> None:
        del api_client

    async def get_organizations_with_http_info(
        self,
        *,
        other_request: SyntheticRequest,
        _request_timeout: tuple[float, float],
    ) -> ApiResponse[object]:
        del other_request, _request_timeout
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")


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

    def assert_selected(
        self,
        operation_id: str,
        *,
        method: str | None = None,
        path: str | None = None,
    ) -> None:
        del method, path
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
        self.assert_selected(operation_id)
        if isinstance(request_model, SyntheticRequest):
            request_model = request_model.value
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
    api_module = ModuleType("iikocloud_client.api.synthetic_api")
    api_module.SyntheticApi = SyntheticApi  # type: ignore[attr-defined]
    api_module.InheritedApi = InheritedApi  # type: ignore[attr-defined]
    api_module.WrongKeywordApi = WrongKeywordApi  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, api_module.__name__, api_module)
    request_module = ModuleType("iikocloud_client.models.synthetic_request")
    request_module.SyntheticRequest = SyntheticRequest  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, request_module.__name__, request_module)
    SyntheticApi.handlers = {}
    SyntheticApi.approved_calls = []
    SyntheticApi.wrong_calls = 0
    SyntheticApi.clients = []


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


def _operation_contract(
    *,
    get_organizations_kind: str = "read",
) -> Mapping[str, LiveOperation]:
    return MappingProxyType(
        {
            "get_organizations": LiveOperation(
                kind=get_organizations_kind,
                cleanup=None,
                method="POST",
                path="/api/1/organizations",
            ),
            "get_external_menu_by_id": LiveOperation(
                kind="read",
                cleanup=None,
                method="POST",
                path="/api/2/menu/by_id",
            ),
            "no_body_read": LiveOperation(
                kind="read",
                cleanup=None,
                method="GET",
                path="/api/1/no-body",
            ),
        }
    )


def _binding(
    operation_id: str = "get_organizations",
    *,
    api_class: str = "SyntheticApi",
    method_name: str | None = None,
    request_keyword: str | None = None,
) -> GeneratedReadBinding:
    keyword = request_keyword or f"{operation_id}_request"
    return GeneratedReadBinding(
        api_module="iikocloud_client.api.synthetic_api",
        api_class=api_class,
        method_name=method_name or f"{operation_id}_with_http_info",
        request_module="iikocloud_client.models.synthetic_request",
        request_class="SyntheticRequest",
        request_keyword=keyword,
    )


def _no_body_binding() -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module="iikocloud_client.api.synthetic_api",
        api_class="SyntheticApi",
        method_name="no_body_read_with_http_info",
        request_module=None,
        request_class=None,
        request_keyword=None,
    )


def _adapter(
    *,
    guard: StubGuard,
    state: StubState,
    capture: StubCapture | None = None,
    receipt: LiveReceipt | None = None,
    receipt_path: Path | None = None,
    operation_contract: Mapping[str, LiveOperation] | None = None,
) -> GeneratedLiveSdk:
    return GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=_profile(),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        operation_contract=operation_contract or _operation_contract(),
        capture=cast(LiveCapture, capture) if capture is not None else None,
        receipt=receipt,
        receipt_path=receipt_path,
    )


def _auth_receipt(path: Path) -> LiveReceipt:
    receipt = LiveReceipt(
        run_id="20260720T120000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=("authenticate",),
        had_429=False,
        completed=False,
    )
    receipt.write(path)
    return receipt


def test_generated_adapter_does_not_expose_arbitrary_read_callback() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)

    assert not hasattr(adapter, "call_generated")


def test_constructor_copies_and_freezes_operation_contract() -> None:
    state = StubState()
    guard = StubGuard(state)
    operations = {
        "get_organizations": LiveOperation(
            kind="read",
            cleanup=None,
            method="POST",
            path="/api/1/organizations",
        )
    }
    adapter = _adapter(
        guard=guard,
        state=state,
        operation_contract=operations,
    )

    operations.clear()

    assert tuple(adapter.operation_contract) == ("get_organizations",)
    with pytest.raises(TypeError):
        cast(Any, adapter.operation_contract)["other"] = LiveOperation(
            kind="read",
            cleanup=None,
            method="GET",
            path="/api/1/other",
        )


def test_generated_call_failure_has_only_fixed_code_message() -> None:
    failure = GeneratedCallFailure(ReadFailureCode.HTTP_ERROR, 400)

    assert failure.code is ReadFailureCode.HTTP_ERROR
    assert failure.status_code == 400
    assert str(failure) == "http_error"
    with pytest.raises(TypeError):
        GeneratedCallFailure(cast(Any, "private-error-detail"), 400)


async def _call_bound(
    adapter: GeneratedLiveSdk,
    operation_id: str,
    request_model: object,
    invoke: Callable[[], Awaitable[ApiResponse[Any]]],
) -> Any:
    SyntheticApi.handlers[operation_id] = cast(
        Callable[[], Awaitable[ApiResponse[object]]],
        invoke,
    )
    result = await adapter.call_bound_read(
        operation_id,
        _binding(operation_id),
        SyntheticRequest(request_model),
    )
    return result.data


@pytest.mark.asyncio
async def test_bound_success_uses_only_resolved_method_and_returns_metadata() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)
    request = SyntheticRequest({"organizationIds": ["organization-id"]})
    response_model = {"organizations": []}

    async def invoke() -> ApiResponse[object]:
        return ApiResponse(
            status_code=201,
            headers=None,
            data=response_model,
            raw_data=b"{}",
        )

    SyntheticApi.handlers["get_organizations"] = invoke

    result = await adapter.call_bound_read(
        "get_organizations",
        _binding(),
        request,
    )

    assert isinstance(result, GeneratedCallResult)
    assert result.data is response_model
    assert result.status_code == 201
    assert type(result.duration_ms) is int and result.duration_ms >= 0
    assert SyntheticApi.approved_calls == [
        ("get_organizations", request, (10.0, 30.0))
    ]
    assert SyntheticApi.wrong_calls == 0
    assert SyntheticApi.clients == [adapter.api_client]
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 201)]
    with pytest.raises(dataclasses.FrozenInstanceError):
        cast(Any, result).status_code = 200


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("operation_id", "binding", "request_model", "contract", "message"),
    [
        (
            "get_organizations",
            _binding(
                operation_id="wrong_read",
                method_name="wrong_read_with_http_info",
                request_keyword="wrong_read_request",
            ),
            SyntheticRequest({}),
            _operation_contract(),
            "Generated read binding does not match operation ID",
        ),
        (
            "get_organizations",
            _binding(api_class="InheritedApi"),
            SyntheticRequest({}),
            _operation_contract(),
            "Generated read API class does not own bound method",
        ),
        (
            "get_organizations",
            _binding(api_class="WrongKeywordApi"),
            SyntheticRequest({}),
            _operation_contract(),
            "Generated read binding resolution failed",
        ),
        (
            "absent_read",
            _binding(operation_id="absent_read"),
            SyntheticRequest({}),
            _operation_contract(),
            "Generated read operation is not allowlisted",
        ),
        (
            "get_organizations",
            _binding(),
            SyntheticRequest({}),
            _operation_contract(get_organizations_kind="cleanup"),
            "Generated read operation is not allowlisted",
        ),
        (
            "get_organizations",
            _binding(),
            OtherSyntheticRequest(),
            _operation_contract(),
            "Generated read request model does not match binding",
        ),
    ],
    ids=[
        "operation-id",
        "method-owner",
        "request-keyword",
        "allowlist",
        "read-kind",
        "request-type",
    ],
)
async def test_bound_substitution_is_rejected_before_guard_acquisition(
    operation_id: str,
    binding: GeneratedReadBinding,
    request_model: object,
    contract: Mapping[str, LiveOperation],
    message: str,
) -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(
        guard=guard,
        state=state,
        operation_contract=contract,
    )

    with pytest.raises(SafetyError) as caught:
        await adapter.call_bound_read(operation_id, binding, request_model)

    assert str(caught.value) == message
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert guard.acquired == []
    assert guard.statuses == []
    assert SyntheticApi.approved_calls == []
    assert SyntheticApi.wrong_calls == 0


@pytest.mark.asyncio
async def test_bound_no_body_request_requires_none() -> None:
    state = StubState()
    guard = StubGuard(state)
    adapter = _adapter(guard=guard, state=state)

    async def invoke() -> ApiResponse[object]:
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    SyntheticApi.handlers["no_body_read"] = invoke

    with pytest.raises(SafetyError, match="request model"):
        await adapter.call_bound_read("no_body_read", _no_body_binding(), object())
    assert guard.acquired == []

    result = await adapter.call_bound_read("no_body_read", _no_body_binding(), None)

    assert result.status_code == 200
    assert SyntheticApi.approved_calls == [
        ("no_body_read", None, (10.0, 30.0))
    ]


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
        await _call_bound(adapter, "get_organizations", {}, invoke)

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

    result: dict[str, object] = await _call_bound(
        adapter, "get_organizations", request_model, invoke
    )

    assert result is response_model
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 200)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_organizations", 200)]


@pytest.mark.asyncio
async def test_success_persists_generated_operation_in_live_receipt(tmp_path: Path) -> None:
    state = StubState()
    guard = StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)
    adapter = _adapter(
        guard=guard,
        state=state,
        receipt=receipt,
        receipt_path=receipt_path,
    )

    async def invoke() -> ApiResponse[dict[str, object]]:
        recorded = adapter.receipt
        assert recorded is not None
        assert recorded.operations == ("authenticate", "get_organizations")
        assert LiveReceipt.load(receipt_path) == recorded
        return ApiResponse(
            status_code=200,
            headers=None,
            data={"organizations": []},
            raw_data=b'{"organizations":[]}',
        )

    await _call_bound(adapter, "get_organizations", {}, invoke)

    recorded = adapter.receipt
    assert recorded is not None
    assert recorded.operations == ("authenticate", "get_organizations")
    assert LiveReceipt.load(receipt_path) == recorded


@pytest.mark.asyncio
async def test_429_persists_failed_generated_operation_and_receipt_flag(
    tmp_path: Path,
) -> None:
    state = StubState()
    guard = StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)
    adapter = _adapter(
        guard=guard,
        state=state,
        receipt=receipt,
        receipt_path=receipt_path,
    )

    async def invoke() -> ApiResponse[object]:
        raise ApiException(status=429, reason="synthetic")

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 429
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    recorded = adapter.receipt
    assert recorded is not None
    assert recorded.operations == ("authenticate", "get_organizations")
    assert recorded.had_429
    assert LiveReceipt.load(receipt_path) == recorded


@pytest.mark.asyncio
async def test_429_still_opens_circuit_when_receipt_flag_write_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = StubState()
    guard = StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)
    adapter = _adapter(
        guard=guard,
        state=state,
        receipt=receipt,
        receipt_path=receipt_path,
    )
    original_write = LiveReceipt.write

    def fail_429_write(self: LiveReceipt, path: Path) -> None:
        if self.had_429:
            raise RuntimeError("synthetic receipt failure")
        original_write(self, path)

    monkeypatch.setattr(LiveReceipt, "write", fail_429_write)

    async def invoke() -> ApiResponse[object]:
        raise ApiException(status=429, reason="synthetic")

    with pytest.raises(SafetyError, match="429 receipt recording failed"):
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert guard.statuses == [("get_organizations", 429)]
    assert state.circuit_open
    await _assert_next_call_is_blocked_before_work(adapter, guard)


def test_constructor_rejects_incomplete_receipt_binding(tmp_path: Path) -> None:
    state = StubState()
    guard = StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)

    with pytest.raises(SafetyError, match="receipt and path"):
        _adapter(guard=guard, state=state, receipt=receipt)
    with pytest.raises(SafetyError, match="receipt and path"):
        _adapter(guard=guard, state=state, receipt_path=receipt_path)


def test_constructor_rejects_receipt_for_another_profile(tmp_path: Path) -> None:
    state = StubState()
    guard = StubGuard(state)
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = LiveReceipt(
        run_id="20260720T120000Z-a1b2c3d4",
        profile_fingerprint="e" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=("authenticate",),
        had_429=False,
        completed=False,
    )
    receipt.write(receipt_path)

    with pytest.raises(SafetyError, match="profile"):
        _adapter(
            guard=guard,
            state=state,
            receipt=receipt,
            receipt_path=receipt_path,
        )


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

    result: dict[str, object] = await _call_bound(
        adapter, "get_external_menu_by_id", request_model, invoke
    )

    assert result is response_model
    assert len(capture.pairs) == 1
    operation_id, captured_request, captured_response, metadata = capture.pairs[0]
    assert operation_id == "get_external_menu_by_id"
    assert captured_request is request_model
    assert captured_response is response_model
    assert metadata["method"] == "POST"
    assert metadata["path"] == "/api/2/menu/by_id"
    assert metadata["status"] == 201
    assert type(metadata["duration_ms"]) is int


@pytest.mark.asyncio
async def test_non_429_api_exception_is_sanitized_and_poison_adapter() -> None:
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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 503
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 503)]
    assert invocations == 1
    assert state.statuses == [("f" * 64, "get_organizations", 503)]
    assert not state.circuit_open
    assert capture.pairs == []
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_external_menu_by_id", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 429
    assert str(caught.value) == "http_error"
    assert private_detail not in str(caught.value)
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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
async def test_non_selected_dependency_read_skips_capture() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_external_menu_by_id")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    invocations = 0

    async def invoke() -> ApiResponse[object]:
        nonlocal invocations
        invocations += 1
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    result = await _call_bound(adapter, "get_organizations", {}, invoke)

    assert result == {}
    assert capture.selections == []
    assert capture.pairs == []
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == [("get_organizations", 200)]
    assert invocations == 1


@pytest.mark.asyncio
async def test_non_success_response_is_sanitized_and_poison_adapter() -> None:
    state = StubState()
    guard = StubGuard(state)
    capture = StubCapture("get_organizations")
    adapter = _adapter(guard=guard, state=state, capture=capture)
    private_markers = (
        "private-response-body",
        "https://private.example.invalid/path",
        "private-token-value",
        "11111111-2222-4333-8444-555555555555",
    )

    async def invoke() -> ApiResponse[object]:
        return ApiResponse(
            status_code=400,
            headers={"x-private": private_markers[2]},
            data={"detail": list(private_markers)},
            raw_data=private_markers[0].encode(),
        )

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 400
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    formatted = "".join(traceback.format_exception(caught.value))
    assert all(marker not in formatted for marker in private_markers)
    assert guard.statuses == [("get_organizations", 400)]
    assert capture.selections == []
    assert capture.pairs == []
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)


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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_external_menu_by_id", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 429
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert caught.value.__suppress_context__
    assert capture.selections == []
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
        await _call_bound(adapter, "get_organizations", {}, invoke)

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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.TRANSPORT_ERROR
    assert caught.value.status_code is None
    assert str(caught.value) == "transport_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK status recording failed without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK status recording failed without a retry"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_external_menu_by_id", request_model, invoke)

    assert caught.value.code is ReadFailureCode.CAPTURE_FAILED
    assert caught.value.status_code == 200
    assert str(caught.value) == "capture_failed"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 429
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert str(caught.value) == "Generated SDK exception has an invalid HTTP status"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.HTTP_ERROR
    assert caught.value.status_code == 0
    assert str(caught.value) == "http_error"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert capture.selections == []
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

    with pytest.raises(GeneratedCallFailure) as caught:
        await _call_bound(adapter, "get_organizations", {}, invoke)

    assert caught.value.code is ReadFailureCode.INVOCATION_FAILED
    assert caught.value.status_code is None
    assert str(caught.value) == "invocation_failed"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert caught.value.__suppress_context__
    assert private_detail not in "".join(traceback.format_exception(caught.value))
    assert invalid_response.accessed == []
    assert capture.selections == []
    assert capture.write_attempts == []
    assert capture.pairs == []
    assert guard.acquired == ["get_organizations"]
    assert guard.statuses == []
    assert state.statuses == []
    assert invocations == 1
    await _assert_next_call_is_blocked_before_work(adapter, guard, capture)
