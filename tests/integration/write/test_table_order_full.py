from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tests.integration.write._support import (
    call_read,
    canary,
    exec_write,
    verified_compensation,
)
from tests.integration.write.test_delivery_order import _find_product_price
from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("table_order")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_table_order_full_lifecycle(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Full table-order sweep: create, items, customer, data, payments, print, cancel."""
    from iikocloud_client import (
        AddCustomerToTableOrderRequest,
        AddItemsToTableOrderRequest,
        AddOrderPaymentsRequest,
        CancelTableOrderRequest,
        ChangeExternalDataRequest,
        CreateTableOrderRequest,
        DeliveryOrderCreateExternalData,
        DeliveryOrderCreateProductItem,
        GetRestaurantSectionsRequest,
        GetTableOrdersByIdRequest,
        MenuRequest,
        Payment,
        PaymentTypesRequest,
        PrintBillRequest,
        TableOrderCustomer,
        TableOrderRequest,
    )

    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    assert live_profile.external_menu_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)
    cancel_payload: dict[str, Any] | None = None

    try:
        await canary(live_sdk, organization_id)

        sections = await call_read(
            live_sdk,
            "get_reserve_restaurant_sections",
            api_module="iikocloud_client.api.banquets_reserves_api",
            api_class="BanquetsReservesApi",
            request_module="get_restaurant_sections_request",
            request_class="GetRestaurantSectionsRequest",
            request_keyword="get_restaurant_sections_request",
            request=GetRestaurantSectionsRequest(terminalGroupIds=[terminal_group_id]),
        )
        table_ids = [
            table.id
            for section in sections.data.restaurant_sections
            for table in section.tables
        ]
        assert table_ids, "no tables on the write stand"
        table_id = table_ids[0]

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
            "create_table_order",
            CreateTableOrderRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=TableOrderRequest(
                    phone=CUSTOMER_MARKER_PHONE,
                    tableIds=[table_id],
                    guestCount=1,
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
        cancel_payload = CancelTableOrderRequest(
            orderId=order_id,
            organizationId=organization_id,
            removalComment="sdk-write-probe cleanup",
        ).model_dump(mode="json", by_alias=True, exclude_none=True)
        mutation_journal.register("cancel_table_order", cancel_payload)

        await exec_write(
            live_sdk,
            "add_items_to_table_order",
            AddItemsToTableOrderRequest(
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
            "add_customer_to_table_order",
            AddCustomerToTableOrderRequest(
                organizationId=organization_id,
                orderId=order_id,
                customer=TableOrderCustomer(
                    name="sdk-write-probe",
                    phone=CUSTOMER_MARKER_PHONE,
                    shouldReceiveOrderStatusNotifications=False,
                ),
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        await exec_write(
            live_sdk,
            "change_table_order_external_data",
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
            "add_table_order_payments",
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
            "print_table_order_bill",
            PrintBillRequest(
                organizationId=organization_id,
                orderId=order_id,
            ).model_dump(mode="json", by_alias=True),
        )

        verified = await call_read(
            live_sdk,
            "get_table_orders_by_id",
            api_module="iikocloud_client.api.orders_api",
            api_class="OrdersApi",
            request_module="get_table_orders_by_id_request",
            request_class="GetTableOrdersByIdRequest",
            request_keyword="get_table_orders_by_id_request",
            request=GetTableOrdersByIdRequest(
                organizationIds=[organization_id],
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
        if cancel_payload is not None:
            await verified_compensation(
                live_sdk,
                mutation_journal,
                "cancel_table_order",
                cancel_payload,
                organization_id,
            )
        await mutation_journal.cleanup(live_sdk.execute_write)
