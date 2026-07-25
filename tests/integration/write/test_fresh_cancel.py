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
@pytest.mark.write_scenario("delivery_order")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_fresh_order_cancel_check(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Create a fresh order and cancel it, inspecting the command status."""
    from iikocloud_client import (
        CancelOrderRequest,
        CreateOrderRequest,
        DeliveryOrder,
        DeliveryOrderCreateProductItem,
        MenuRequest,
        OrderTypesRequest,
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

        created = await exec_write(
            live_sdk,
            "create_delivery_order",
            CreateOrderRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=DeliveryOrder(
                    phone=CUSTOMER_MARKER_PHONE,
                    comment="sdk-write-probe fresh-cancel-check",
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
        assert order_id is not None
        print(f"fresh order id: {order_id}")

        cancel_payload = CancelOrderRequest(
            orderId=order_id,
            organizationId=organization_id,
            cancelComment="sdk-write-probe cleanup",
        ).model_dump(mode="json", by_alias=True, exclude_none=True)
        mutation_journal.register("cancel_delivery_order", cancel_payload)
    finally:
        if cancel_payload is not None:
            await verified_compensation(
                live_sdk,
                mutation_journal,
                "cancel_delivery_order",
                cancel_payload,
                organization_id,
            )
        await mutation_journal.cleanup(live_sdk.execute_write)
