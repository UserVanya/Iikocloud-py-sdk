from __future__ import annotations

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
@pytest.mark.write_scenario("finalization")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_finalization_confirm_close_delivery_and_table(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Finalization sweep: confirm/cancel-confirmation pair, then real closes.

    The first delivery order is confirmed and un-confirmed, then cancelled
    cleanly. Two further orders are deliberately left closed — the accepted
    audit residue of finalization; their cancel compensations are marked
    moot through the journal once the close succeeded.
    """
    from iikocloud_client import (
        CancelDeliveryConfirmationRequest,
        CancelOrderRequest,
        CancelTableOrderRequest,
        CloseTableOrderRequest,
        ConfirmDeliveryRequest,
        CreateOrderRequest,
        CreateTableOrderRequest,
        DeliveryOrder,
        DeliveryOrderCreateProductItem,
        GetRestaurantSectionsRequest,
        MenuRequest,
        OrderTypesRequest,
        TableOrderRequest,
    )

    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    assert live_profile.external_menu_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)

    def build_delivery_order() -> CreateOrderRequest:
        return CreateOrderRequest(
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
        )

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

        # 1. confirm / cancel-confirmation pair on a cancellable order.
        created = await exec_write(
            live_sdk, "create_delivery_order", build_delivery_order().to_dict()
        )
        order_info = getattr(created.data, "order_info", None)
        delivery_id = getattr(order_info, "id", None) if order_info is not None else None
        assert delivery_id is not None
        mutation_journal.register(
            "cancel_delivery_order",
            CancelOrderRequest(
                orderId=delivery_id,
                organizationId=organization_id,
                cancelComment="sdk-write-probe cleanup",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        confirm_payload = ConfirmDeliveryRequest(
            organizationId=organization_id,
            orderId=delivery_id,
        ).model_dump(mode="json", by_alias=True)
        mutation_journal.register(
            "cancel_delivery_confirmation",
            CancelDeliveryConfirmationRequest(
                organizationId=organization_id,
                orderId=delivery_id,
            ).model_dump(mode="json", by_alias=True),
        )
        await exec_write(live_sdk, "confirm_delivery", confirm_payload)
        await exec_write(live_sdk, "cancel_delivery_confirmation", confirm_payload)
        mutation_journal.complete("cancel_delivery_confirmation")

        # 3. a table order deliberately left closed.
        created_table = await exec_write(
            live_sdk,
            "create_table_order",
            CreateTableOrderRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=TableOrderRequest(
                    phone=CUSTOMER_MARKER_PHONE,
                    tableIds=[table_ids[0]],
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
        table_info = getattr(created_table.data, "order_info", None)
        table_order_id = getattr(table_info, "id", None) if table_info is not None else None
        assert table_order_id is not None
        mutation_journal.register(
            "cancel_table_order",
            CancelTableOrderRequest(
                orderId=table_order_id,
                organizationId=organization_id,
                removalComment="sdk-write-probe cleanup",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        await exec_write(
            live_sdk,
            "close_table_order",
            CloseTableOrderRequest(
                organizationId=organization_id,
                orderId=table_order_id,
            ).model_dump(mode="json", by_alias=True),
        )
        mutation_journal.complete("cancel_table_order")
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
