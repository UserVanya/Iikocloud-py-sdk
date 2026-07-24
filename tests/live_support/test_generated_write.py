from __future__ import annotations

import socket
from types import MappingProxyType
from typing import Any, cast

import pytest

from iikocloud_client.api.customers_api import CustomersApi
from iikocloud_client.api.drafts_api import DraftsApi
from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.models.create_draft_request import CreateDraftRequest
from iikocloud_client.models.create_or_update_customer_request import (
    CreateOrUpdateCustomerRequest,
)
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest
from iikocloud_client.models.delete_draft_request import DeleteDraftRequest
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
        await adapter.execute_write("create_delivery_order", {})
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


_TERMINAL_GROUP_ID = "22222222-2222-4222-8222-222222222222"
_PRODUCT_ID = "33333333-3333-4333-8333-333333333333"
_MENU_ID = "external-menu-1"
_DRAFT_ID = "66666666-6666-4666-8666-666666666666"


def _draft_profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="write-server",
        base_url="https://api.example.invalid",
        api_login="fixture-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id=_MENU_ID,
        terminal_group_id=_TERMINAL_GROUP_ID,
        write_product_id=_PRODUCT_ID,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="f" * 64,
    )


def _draft_adapter(
    guard: _StubGuard,
    state: _StubState,
    *,
    contract: dict[str, LiveOperation] | None = None,
) -> GeneratedLiveSdk:
    return GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=_draft_profile(),
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        operation_contract=MappingProxyType(
            contract
            or {
                "create_delivery_draft": LiveOperation(
                    kind="compensating",
                    cleanup="delete_delivery_draft",
                    method="POST",
                    path="/api/1/deliveries/drafts/create",
                ),
                "delete_delivery_draft": LiveOperation(
                    kind="cleanup",
                    cleanup=None,
                    method="POST",
                    path="/api/1/deliveries/drafts/delete",
                ),
            }
        ),
    )


def _draft_create_payload() -> dict[str, object]:
    return {
        "organizationId": _ORGANIZATION_ID,
        "terminalGroupId": _TERMINAL_GROUP_ID,
        "order": {
            "menuId": _MENU_ID,
            "phone": CUSTOMER_MARKER_PHONE,
            "comment": "sdk-write-probe",
            "items": [
                {
                    "type": "Product",
                    "productId": _PRODUCT_ID,
                    "price": 1.0,
                    "amount": 1,
                }
            ],
        },
    }


@pytest.mark.asyncio
async def test_execute_write_draft_create_and_delete_dispatch_exactly_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _draft_adapter(guard, state)
    created: list[CreateDraftRequest] = []
    deleted: list[DeleteDraftRequest] = []

    async def create(
        _api: DraftsApi,
        *,
        create_draft_request: CreateDraftRequest,
        **_kwargs: object,
    ) -> ApiResponse[dict[str, str]]:
        created.append(create_draft_request)
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    async def delete(
        _api: DraftsApi,
        *,
        delete_draft_request: DeleteDraftRequest,
        **_kwargs: object,
    ) -> ApiResponse[dict[str, str]]:
        deleted.append(delete_draft_request)
        return ApiResponse(status_code=200, headers=None, data={}, raw_data=b"{}")

    monkeypatch.setattr(DraftsApi, "create_delivery_draft_with_http_info", create)
    monkeypatch.setattr(DraftsApi, "delete_delivery_draft_with_http_info", delete)

    await adapter.execute_write("create_delivery_draft", _draft_create_payload())
    await adapter.execute_write(
        "delete_delivery_draft",
        {"organizationId": _ORGANIZATION_ID, "orderId": _DRAFT_ID},
    )

    assert len(created) == 1
    assert created[0].order.menu_id == _MENU_ID
    assert created[0].order.phone == CUSTOMER_MARKER_PHONE
    assert len(deleted) == 1
    assert str(deleted[0].order_id) == _DRAFT_ID
    assert guard.acquired == ["create_delivery_draft", "delete_delivery_draft"]


@pytest.mark.asyncio
async def test_draft_create_rejects_foreign_values() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _draft_adapter(guard, state)

    def with_order(**changes: object) -> dict[str, object]:
        payload = _draft_create_payload()
        order = dict(payload["order"])  # type: ignore[arg-type]
        order.update(changes)
        payload["order"] = order
        return payload

    for payload in (
        with_order(phone="+79999999999"),
        with_order(menuId="other-menu"),
        {**_draft_create_payload(), "organizationId": _OTHER_ID},
        {**_draft_create_payload(), "terminalGroupId": _OTHER_ID},
    ):
        with pytest.raises(SafetyError, match="outside the selected write profile"):
            await adapter.execute_write("create_delivery_draft", payload)

    foreign_product = with_order()
    foreign_product["order"]["items"] = [  # type: ignore[index]
        {"type": "Product", "productId": _OTHER_ID, "price": 1.0, "amount": 1}
    ]
    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_delivery_draft", foreign_product)

    with pytest.raises(SafetyError, match="compensating payload is invalid"):
        await adapter.execute_write("create_delivery_draft", {"broken": True})
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_draft_create_requires_external_menu_in_profile() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    profile = ResolvedLiveProfile(
        name="write-server",
        base_url="https://api.example.invalid",
        api_login="fixture-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id=None,
        terminal_group_id=_TERMINAL_GROUP_ID,
        write_product_id=_PRODUCT_ID,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="f" * 64,
    )
    adapter = GeneratedLiveSdk(
        api_client=cast(ApiClient, object()),
        profile=profile,
        guard=cast(LiveRateGuard, guard),
        state=cast(LiveStateStore, state),
        operation_contract=MappingProxyType(
            {
                "create_delivery_draft": LiveOperation(
                    kind="compensating",
                    cleanup="delete_delivery_draft",
                    method="POST",
                    path="/api/1/deliveries/drafts/create",
                )
            }
        ),
    )

    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write("create_delivery_draft", _draft_create_payload())
    assert guard.acquired == []


@pytest.mark.asyncio
async def test_draft_delete_rejects_foreign_organization_and_invalid_payload() -> None:
    state = _StubState()
    guard = _StubGuard(state)
    adapter = _draft_adapter(guard, state)

    with pytest.raises(SafetyError, match="outside the selected write profile"):
        await adapter.execute_write(
            "delete_delivery_draft",
            {"organizationId": _OTHER_ID, "orderId": _DRAFT_ID},
        )
    with pytest.raises(SafetyError, match="cleanup payload is invalid"):
        await adapter.execute_write("delete_delivery_draft", {"broken": True})
    assert guard.acquired == []
