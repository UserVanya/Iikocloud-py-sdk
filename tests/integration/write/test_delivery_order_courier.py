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
@pytest.mark.write_scenario("delivery_order_courier")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_delivery_order_courier_lifecycle(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Courier delivery lifecycle: create with address, assign courier, cancel."""
    from iikocloud_client import (
        AddressLegacy,
        CancelOrderRequest,
        ChangeDriverInfoRequest,
        CitiesRequest,
        CouriersRequest,
        CreateOrderRequest,
        DeliveryOrder,
        DeliveryOrderCreatePoint,
        DeliveryOrderCreateProductItem,
        DeliveryOrderCreateStreet,
        MenuRequest,
        OrdersByIdRequest,
        OrderTypesRequest,
        StreetsByCityRequest,
        UpdateOrderCourierRequest,
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
        courier_type_id = None
        for wrapper in order_types.data.order_types:
            for item in wrapper.items:
                if (
                    item.order_service_type.value == "DeliveryByCourier"
                    and not item.is_deleted
                ):
                    courier_type_id = item.id
                    break
            if courier_type_id is not None:
                break
        assert courier_type_id is not None, "no courier order type on the write stand"

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

        city_id = None
        cities = await call_read(
            live_sdk,
            "get_cities",
            api_module="iikocloud_client.api.addresses_api",
            api_class="AddressesApi",
            request_module="cities_request",
            request_class="CitiesRequest",
            request_keyword="cities_request",
            request=CitiesRequest(organizationIds=[organization_id]),
        )
        for wrapper in cities.data.cities:
            for item in wrapper.items:
                if isinstance(item.name, str) and "скол" in item.name.lower():
                    city_id = item.id
                    break
            if city_id is not None:
                break

        street_id = None
        street_name = "микрорайон Дубрава"
        if city_id is not None:
            streets = await call_read(
                live_sdk,
                "get_streets_by_city",
                api_module="iikocloud_client.api.addresses_api",
                api_class="AddressesApi",
                request_module="streets_by_city_request",
                request_class="StreetsByCityRequest",
                request_keyword="streets_by_city_request",
                request=StreetsByCityRequest(
                    cityId=city_id,
                    organizationId=organization_id,
                ),
            )
            for wrapper in streets.data.streets:
                for item in wrapper.items:
                    if isinstance(item.name, str) and "дубрав" in item.name.lower():
                        street_id = item.id
                        street_name = item.name
                        break
                if street_id is not None:
                    break

        street = (
            DeliveryOrderCreateStreet(id=street_id, name=street_name)
            if street_id is not None
            else DeliveryOrderCreateStreet(name=street_name, city="Старый Оскол")
        )

        created = await exec_write(
            live_sdk,
            "create_delivery_order",
            CreateOrderRequest(
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
                order=DeliveryOrder(
                    phone=CUSTOMER_MARKER_PHONE,
                    comment="sdk-write-probe",
                    orderTypeId=courier_type_id,
                    deliveryPoint=DeliveryOrderCreatePoint(
                        address=AddressLegacy(
                            type="legacy",
                            street=street,
                            house="квартал 1",
                            flat="1",
                        ),
                        comment="sdk-write-probe",
                    ),
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
            "update_delivery_order_courier",
            UpdateOrderCourierRequest(
                organizationId=organization_id,
                orderId=order_id,
                employeeId=employee_id,
            ).model_dump(mode="json", by_alias=True),
        )
        new_time = (datetime.now(timezone.utc) + timedelta(hours=2)).strftime(
            "%Y-%m-%d %H:%M:%S.000"
        )
        await exec_write(
            live_sdk,
            "change_delivery_driver_info",
            ChangeDriverInfoRequest(
                organizationId=organization_id,
                orderId=order_id,
                driverId=employee_id,
                estimatedTime=new_time,
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
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
