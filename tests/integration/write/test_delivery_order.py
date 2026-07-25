from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary, verified_compensation
from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


def _find_product_price(value: Any, product_id: str) -> float | None:
    if isinstance(value, dict):
        identifiers = [
            child
            for key, child in value.items()
            if key in {"itemId", "productId", "id"} and isinstance(child, str)
        ]
        if product_id in identifiers:
            return _price_in_subtree(value)
        for child in value.values():
            found = _find_product_price(child, product_id)
            if found is not None:
                return found
    if isinstance(value, list):
        for child in value:
            found = _find_product_price(child, product_id)
            if found is not None:
                return found
    return None


def _price_in_subtree(value: Any) -> float | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "price" and type(child) in {int, float}:
                return float(child)
            found = _price_in_subtree(child)
            if found is not None:
                return found
    if isinstance(value, list):
        for child in value:
            found = _price_in_subtree(child)
            if found is not None:
                return found
    return None


@pytest.mark.live_write
@pytest.mark.write_scenario("delivery_order")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_delivery_order_create_and_cancel(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Delivery order lifecycle: create a pickup order, verify, cancel it."""
    from iikocloud_client import (
        CancelOrderRequest,
        CreateOrderRequest,
        DeliveryOrder,
        DeliveryOrderCreateProductItem,
        MenuRequest,
        OrdersByIdRequest,
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

        order = DeliveryOrder(
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
        create_request = CreateOrderRequest(
            organizationId=organization_id,
            terminalGroupId=terminal_group_id,
            order=order,
        )
        from tools.openapi_pipeline.live.generated import GeneratedCallFailure

        try:
            created = await live_sdk.execute_write(
                "create_delivery_order",
                create_request.to_dict(),
            )
        except GeneratedCallFailure as error:
            print(
                f"order create failed: status={error.status_code} "
                f"details={error.error_details!r}"
            )
            raise
        order_info = getattr(created.data, "order_info", None)
        order_id = getattr(order_info, "id", None) if order_info is not None else None
        assert order_id is not None, "create response carries no order id"

        cancel_payload = CancelOrderRequest(
            orderId=order_id,
            organizationId=organization_id,
            cancelComment="sdk-write-probe cleanup",
        ).model_dump(mode="json", by_alias=True, exclude_none=True)
        mutation_journal.register("cancel_delivery_order", cancel_payload)

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
        verified_json = verified.data.model_dump(mode="json", by_alias=True)
        returned_ids = {
            str(order.get("id"))
            for order in verified_json.get("orders", [])
            if isinstance(order, dict)
        }
        assert str(order_id) in returned_ids, (
            f"created order {order_id} not returned by get_deliveries_by_id"
        )
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
