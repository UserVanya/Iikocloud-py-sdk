from __future__ import annotations

import socket
from types import MappingProxyType
from typing import Any, cast

import pytest

from iikocloud_client.api.customers_api import CustomersApi
from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.models.create_or_update_customer_request import (
    CreateOrUpdateCustomerRequest,
)
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import (
    CUSTOMER_MARKER_PHONE,
    GeneratedLiveSdk,
)
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard
from tools.openapi_pipeline.live.session import LiveOperation
from tools.openapi_pipeline.live.state import LiveStateStore

_ORGANIZATION_ID = "11111111-1111-4111-8111-111111111111"
_CUSTOMER_ID = "55555555-5555-4555-8555-555555555555"
_OTHER_ID = "99999999-9999-4999-8999-999999999999"


class _StubState:
    def __init__(self) -> None:
        self.statuses: list[tuple[str, str, int]] = []

    def record_status(
        self,
        profile_fingerprint: str,
        operation_id: str,
        status: int,
    ) -> None:
        self.statuses.append((profile_fingerprint, operation_id, status))


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
            raise AssertionError("generated write tests must not create a network socket")
        return real_socket(*args, **kwargs)

    monkeypatch.setattr(socket, "socket", guarded_socket)


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="write-server",
        base_url="https://api.example.invalid",
        api_login="fixture-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id=None,
        terminal_group_id=None,
        write_product_id=None,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="f" * 64,
    )


def _adapter(
    guard: _StubGuard,
    state: _StubState,
    *,
    contract: dict[str, LiveOperation] | None = None,
) -> GeneratedLiveSdk:
    return GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=_profile(),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        operation_contract=MappingProxyType(
            contract
            or {
                "create_or_update_customer": LiveOperation(
                    kind="compensating",
                    cleanup="delete_customers",
                    method="POST",
                    path="/api/1/loyalty/iiko/customer/create_or_update",
                ),
                "delete_customers": LiveOperation(
                    kind="cleanup",
                    cleanup=None,
                    method="POST",
                    path="/api/1/loyalty/iiko/delete_customers",
                ),
            }
        ),
    )


def _create_payload() -> dict[str, object]:
    return {
        "id": _CUSTOMER_ID,
        "name": "sdk-write-probe",
        "organizationId": _ORGANIZATION_ID,
        "phone": CUSTOMER_MARKER_PHONE,
    }


def _delete_payload() -> dict[str, object]:
    return {
        "customerIds": [_CUSTOMER_ID],
        "organizationId": _ORGANIZATION_ID,
    }


@pytest.mark.asyncio
async def test_execute_write_customer_create_and_delete_dispatch_exactly_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)
    created: list[CreateOrUpdateCustomerRequest] = []
    deleted: list[DeleteCustomersRequest] = []

    async def create(
        _api: CustomersApi,
        *,
        create_or_update_customer_request: CreateOrUpdateCustomerRequest,
        **_kwargs: object,
    ) -> ApiResponse[dict[str, str]]:
        created.append(create_or_update_customer_request)
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    async def delete(
        _api: CustomersApi,
        *,
        delete_customers_request: DeleteCustomersRequest,
        **_kwargs: object,
    ) -> ApiResponse[dict[str, str]]:
        deleted.append(delete_customers_request)
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    monkeypatch.setattr(CustomersApi, "create_or_update_customer_with_http_info", create)
    monkeypatch.setattr(CustomersApi, "delete_customers_with_http_info", delete)

    await adapter.execute_write("create_or_update_customer", _create_payload())
    await adapter.execute_write("delete_customers", _delete_payload())

    assert len(created) == 1
    assert str(created[0].id) == _CUSTOMER_ID
    assert created[0].phone == CUSTOMER_MARKER_PHONE
    assert len(deleted) == 1
    assert [str(value) for value in deleted[0].customer_ids] == [_CUSTOMER_ID]
    assert guard.acquired == ["create_or_update_customer", "delete_customers"]
    assert guard.statuses == [
        ("create_or_update_customer", 200),
        ("delete_customers", 200),
    ]


@pytest.mark.asyncio
async def test_execute_write_rejects_unknown_operation_before_live_work() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)

    with pytest.raises(SafetyError, match="approved write operation"):
        await adapter.execute_write("create_delivery_draft", {})
    with pytest.raises(SafetyError, match="approved write operation"):
        await adapter.execute_write("get_organizations", {})
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_execute_write_rejects_wrong_contract_kind_before_live_work() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(
        guard,
        state,
        contract={
            "create_or_update_customer": LiveOperation(
                kind="read",
                cleanup=None,
                method="POST",
                path="/api/1/loyalty/iiko/customer/create_or_update",
            )
        },
    )

    with pytest.raises(SafetyError, match="approved write operation"):
        await adapter.execute_write("create_or_update_customer", _create_payload())
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_customer_create_rejects_foreign_phone_and_organization() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)

    foreign_phone = {**_create_payload(), "phone": "+79999999999"}
    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_or_update_customer", foreign_phone)

    foreign_org = {**_create_payload(), "organizationId": _OTHER_ID}
    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_or_update_customer", foreign_org)

    with pytest.raises(SafetyError, match="compensating payload is invalid"):
        await adapter.execute_write("create_or_update_customer", {"broken": True})

    with pytest.raises(SafetyError, match="cleanup payload is invalid"):
        await adapter.execute_write("delete_customers", _create_payload())
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_customer_delete_rejects_multiple_or_foreign_targets() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _adapter(guard, state)

    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write(
            "delete_customers",
            {"customerIds": [_CUSTOMER_ID, _OTHER_ID], "organizationId": _ORGANIZATION_ID},
        )
    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write(
            "delete_customers",
            {"customerIds": [_CUSTOMER_ID], "organizationId": _OTHER_ID},
        )
    with pytest.raises(SafetyError, match="cleanup payload is invalid"):
        await adapter.execute_write("delete_customers", {"broken": True})

    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_or_update_customer", _delete_payload())
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_execute_write_rejects_when_profile_disallows_write() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=ResolvedLiveProfile(
            name="write-server",
            base_url="https://api.example.invalid",
            api_login="fixture-login",
            organization_id=_ORGANIZATION_ID,
            external_menu_id=None,
            terminal_group_id=None,
            write_product_id=None,
            allow_write=False,
            allowed_organization_ids=(_ORGANIZATION_ID,),
            fingerprint="f" * 64,
        ),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        operation_contract=MappingProxyType(
            {
                "create_or_update_customer": LiveOperation(
                    kind="compensating",
                    cleanup="delete_customers",
                    method="POST",
                    path="/api/1/loyalty/iiko/customer/create_or_update",
                )
            }
        ),
    )

    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_or_update_customer", _create_payload())
    assert guard.acquired == []
