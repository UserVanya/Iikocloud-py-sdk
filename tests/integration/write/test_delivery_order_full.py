from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING
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
@pytest.mark.write_scenario("delivery_order_full")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_delivery_order_full_lifecycle(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Full delivery-order sweep: create, all safe updates, payments, print, cancel."""
    from iikocloud_client import (
        AddOrderItemsRequest,
        AddOrderPaymentsRequest,
        CancelOrderRequest,
        ChangeCompleteBeforeRequest,
        ChangeDeliveryCommentRequest,
        ChangeDeliveryOperatorRequest,
        ChangeExternalDataRequest,
        CouriersRequest,
        CreateOrderRequest,
        DeliveryOrder,
        DeliveryOrderCreateExternalData,
        DeliveryOrderCreateProductItem,
        DeliveryStatusForUpdate,
        MenuRequest,
        OrdersByIdRequest,
        OrderTypesRequest,
        Payment,
        PaymentTypesRequest,
        PrintDeliveryBillRequest,
        UpdateDeliveryStatusRequest,
        UpdateOrderProblemRequest,
        UpdateTrackingLinkRequest,
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
        employee_ids: list[str] = []

        def _collect(value: object) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    if key == "id" and isinstance(child, str):
                        employee_ids.append(child)
                    else:
                        _collect(child)
            elif isinstance(value, list):
                for child in value:
                    _collect(child)

        _collect(employees.data.model_dump(mode="json", by_alias=True))
        assert employee_ids, "no employees on the write stand"
        employee_id = UUID(employee_ids[0])

        payment_types = await call_read(
            live_sdk,
            "get_payment_types",
            api_module="iikocloud_client.api.dictionaries_api",
            api_class="DictionariesApi",
            request_module="payment_types_request",
            request_class="PaymentTypesRequest",
            request_keyword="payment_types_request",
            request=PaymentTypesRequest(organizationIds=[organization_id]),
        )
        cash_type = None
        for item in payment_types.data.payment_types:
            kind = getattr(item.payment_type_kind, "value", item.payment_type_kind)
            if not item.is_deleted and kind == "Cash":
                cash_type = item
                break
        assert cash_type is not None, "no cash payment type on the write stand"

        created = await exec_write(
            live_sdk,
            "create_delivery_order",
            CreateOrderRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=DeliveryOrder(
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
                ),
            ).to_dict(),
        )
        order_info = getattr(created.data, "order_info", None)
        order_id = getattr(order_info, "id", None) if order_info is not None else None
        assert order_id is not None, "create response carries no order id"
        mutation_journal.register(
            "cancel_delivery_order",
            CancelOrderRequest(
                orderId=order_id,
                organizationId=organization_id,
                cancelComment="sdk-write-probe cleanup",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )

        await exec_write(
            live_sdk,
            "add_delivery_order_items",
            AddOrderItemsRequest(
                orderId=order_id,
                organizationId=organization_id,
                items=[
                    DeliveryOrderCreateProductItem(
                        type="Product",
                        productId=product_id,
                        price=price,
                        amount=1,
                    )
                ],
            ).to_dict(),
        )
        await exec_write(
            live_sdk,
            "change_delivery_comment",
            ChangeDeliveryCommentRequest(
                organizationId=organization_id,
                orderId=order_id,
                comment="sdk-write-probe comment",
            ).model_dump(mode="json", by_alias=True),
        )
        new_time = (datetime.now(timezone.utc) + timedelta(days=1)).strftime(
            "%Y-%m-%d %H:%M:%S.000"
        )
        await exec_write(
            live_sdk,
            "change_delivery_complete_before",
            ChangeCompleteBeforeRequest(
                organizationId=organization_id,
                orderId=order_id,
                newCompleteBefore=new_time,
            ).model_dump(mode="json", by_alias=True),
        )
        await exec_write(
            live_sdk,
            "change_delivery_operator",
            ChangeDeliveryOperatorRequest(
                organizationId=organization_id,
                orderId=order_id,
                operatorId=employee_id,
            ).model_dump(mode="json", by_alias=True),
        )
        await exec_write(
            live_sdk,
            "update_delivery_order_problem",
            UpdateOrderProblemRequest(
                organizationId=organization_id,
                orderId=order_id,
                hasProblem=True,
                problem="sdk-write-probe problem",
            ).model_dump(mode="json", by_alias=True),
        )
        await exec_write(
            live_sdk,
            "update_delivery_tracking_link",
            UpdateTrackingLinkRequest(
                organizationId=organization_id,
                orderId=order_id,
                trackingLink="https://example.invalid/sdk-write-probe",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        await exec_write(
            live_sdk,
            "change_delivery_external_data",
            ChangeExternalDataRequest(
                organizationId=organization_id,
                orderId=order_id,
                externalData=[
                    DeliveryOrderCreateExternalData(
                        key="sdk-write-probe",
                        value="probe",
                        isPublic=True,
                    )
                ],
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        await exec_write(
            live_sdk,
            "update_delivery_order_status",
            UpdateDeliveryStatusRequest(
                organizationId=organization_id,
                orderId=order_id,
                deliveryStatus=DeliveryStatusForUpdate.WAITING,
            ).model_dump(mode="json", by_alias=True),
        )
        await exec_write(
            live_sdk,
            "add_delivery_order_payments",
            AddOrderPaymentsRequest(
                orderId=order_id,
                organizationId=organization_id,
                payments=[
                    Payment(
                        paymentTypeId=cash_type.id,
                        paymentTypeKind="Cash",
                        sum=price * 2,
                        isProcessedExternally=True,
                        isFiscalizedExternally=True,
                    )
                ],
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        await exec_write(
            live_sdk,
            "print_delivery_bill",
            PrintDeliveryBillRequest(
                organizationId=organization_id,
                orderId=order_id,
            ).model_dump(mode="json", by_alias=True),
        )

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
