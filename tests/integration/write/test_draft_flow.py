from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary, exec_write
from tests.integration.write.test_delivery_order import _find_product_price
from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("draft_flow")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_draft_flow_lock_save_commit_and_cancel(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Full draft flow: create, lock, unlock, save, commit to order, cancel."""
    from iikocloud_client import (
        CancelOrderRequest,
        CommitDraftRequest,
        CouriersRequest,
        CreateDraftRequest,
        CreateOrderSettings,
        DeleteDraftRequest,
        DeliveryOrderCreateProductItem,
        DeliveryOrderDraft,
        LockOrUnlockDraftRequest,
        MenuRequest,
        OrdersByIdRequest,
        OrderTypesRequest,
        SaveDraftRequest,
    )

    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    assert live_profile.external_menu_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)

    try:
        await canary(live_sdk, organization_id)

        menu = await call_read(
            live_sdk,
            "get_external_menu_by_id",
            api_module="iikocloud_client.api.menu_api",
            api_class="MenuApi",
            request_module="menu_request",
            request_class="MenuRequest",
            request_keyword="menu_request",
            request=MenuRequest(
                asyncMode=False,
                externalMenuId=live_profile.external_menu_id,
                organizationIds=[organization_id],
            ),
        )
        price = _find_product_price(
            menu.data.model_dump(mode="json", by_alias=True),
            live_profile.write_product_id,
        )
        assert price is not None, "write product is not in the external menu"

        order_types = await call_read(
            live_sdk,
            "get_delivery_order_types",
            api_module="iikocloud_client.api.dictionaries_api",
            api_class="DictionariesApi",
            request_module="order_types_request",
            request_class="OrderTypesRequest",
            request_keyword="order_types_request",
            request=OrderTypesRequest(organizationIds=[organization_id]),
        )
        pickup_type_id = None
        for wrapper in order_types.data.order_types:
            for item in wrapper.items:
                if item.order_service_type.value == "DeliveryPickUp" and not item.is_deleted:
                    pickup_type_id = item.id
                    break
            if pickup_type_id is not None:
                break
        assert pickup_type_id is not None, "no pickup order type on the write stand"

        employees = await call_read(
            live_sdk,
            "get_couriers",
            api_module="iikocloud_client.api.employees_api",
            api_class="EmployeesApi",
            request_module="couriers_request",
            request_class="CouriersRequest",
            request_keyword="couriers_request",
            request=CouriersRequest(organizationIds=[organization_id]),
        )
        employee_ids: list[Any] = []

        def _collect_ids(value: Any) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    if key == "id" and isinstance(child, str):
                        employee_ids.append(child)
                    else:
                        _collect_ids(child)
            elif isinstance(value, list):
                for child in value:
                    _collect_ids(child)

        _collect_ids(employees.data.model_dump(mode="json", by_alias=True))
        assert employee_ids, "no employees on the write stand"
        employee_id = UUID(employee_ids[0])

        draft_order = DeliveryOrderDraft(
            menuId=live_profile.external_menu_id,
            phone=CUSTOMER_MARKER_PHONE,
            comment="sdk-write-probe",
            orderTypeId=pickup_type_id,
            items=[
                DeliveryOrderCreateProductItem(
                    type="Product",
                    productId=product_id,
                    price=price,
                    amount=1,
                )
            ],
        )
        created = await exec_write(
            live_sdk,
            "create_delivery_draft",
            CreateDraftRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=draft_order,
            ).to_dict(),
        )
        order_id = getattr(created.data, "order_id", None)
        assert order_id is not None
        mutation_journal.register(
            "delete_delivery_draft",
            DeleteDraftRequest(
                organizationId=organization_id, orderId=order_id
            ).model_dump(mode="json", by_alias=True),
        )

        # lock/unlock is a self-compensating pair executed inline; the
        # journal covers only the entity-level compensations below.
        lock_payload = LockOrUnlockDraftRequest(
            employeeId=employee_id,
            orderId=order_id,
            organizationId=organization_id,
        ).model_dump(mode="json", by_alias=True)
        await exec_write(live_sdk, "lock_delivery_draft", lock_payload)
        await exec_write(live_sdk, "unlock_delivery_draft", lock_payload)

        await exec_write(
            live_sdk,
            "save_delivery_draft",
            SaveDraftRequest(
                employeeId=employee_id,
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=DeliveryOrderDraft(
                    menuId=live_profile.external_menu_id,
                    phone=CUSTOMER_MARKER_PHONE,
                    comment="sdk-write-probe saved",
                    orderTypeId=pickup_type_id,
                    items=[
                        DeliveryOrderCreateProductItem(
                            type="Product",
                            productId=product_id,
                            price=price,
                            amount=1,
                        )
                    ],
                ),
            ).to_dict(),
        )

        await exec_write(
            live_sdk,
            "commit_delivery_draft",
            CommitDraftRequest(
                createOrderSettings=CreateOrderSettings(),
                orderId=order_id,
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        mutation_journal.register(
            "cancel_delivery_order",
            CancelOrderRequest(
                orderId=order_id,
                organizationId=organization_id,
                cancelComment="sdk-write-probe cleanup",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        # The committed draft is consumed by the order, so its delete
        # compensation is provably moot once commit succeeded.
        mutation_journal.complete("delete_delivery_draft")

        verified = await call_read(
            live_sdk,
            "get_deliveries_by_id",
            api_module="iikocloud_client.api.deliveries_retrieve_api",
            api_class="DeliveriesRetrieveApi",
            request_module="orders_by_id_request",
            request_class="OrdersByIdRequest",
            request_keyword="orders_by_id_request",
            request=OrdersByIdRequest(
                organizationId=organization_id,
                orderIds=[order_id],
            ),
        )
        returned_ids = {
            str(order.get("id"))
            for order in verified.data.model_dump(mode="json", by_alias=True).get(
                "orders", []
            )
            if isinstance(order, dict)
        }
        assert str(order_id) in returned_ids
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
