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
@pytest.mark.write_scenario("table_order")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_table_order_create_and_cancel(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Table order lifecycle: create on a stand table, verify, cancel."""
    from iikocloud_client import (
        CancelTableOrderRequest,
        CreateTableOrderRequest,
        DeliveryOrderCreateProductItem,
        GetRestaurantSectionsRequest,
        GetTableOrdersByIdRequest,
        MenuRequest,
        TableOrderRequest,
    )

    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    assert live_profile.external_menu_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)

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

        mutation_journal.register(
            "cancel_table_order",
            CancelTableOrderRequest(
                orderId=order_id,
                organizationId=organization_id,
                removalComment="sdk-write-probe cleanup",
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
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
        await mutation_journal.cleanup(live_sdk.execute_write)
