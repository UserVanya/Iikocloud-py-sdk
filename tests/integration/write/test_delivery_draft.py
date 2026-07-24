from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


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


@pytest.mark.live_write
@pytest.mark.write_scenario("delivery_draft")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_delivery_draft_create_verify_and_delete(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Delivery-draft lifecycle: create with marker phone, verify, delete.

    The marker phone comes from the reviewed write-lifecycle contract; the
    adapter refuses any other phone, menu, or product. iiko assigns the draft
    order id; the compensation is registered with the returned id.
    """
    from iikocloud_client import (
        CreateDraftRequest,
        DeleteDraftRequest,
        DeliveryOrderCreateProductItem,
        DeliveryOrderDraft,
        GetDraftRequest,
        GetOrganizationsRequest,
        MenuRequest,
        OrderTypesRequest,
    )
    from tools.openapi_pipeline.live.read_case import GeneratedReadBinding

    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    assert live_profile.external_menu_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)

    try:
        # The completed-receipt canary requires get_organizations in every run.
        await live_sdk.call_bound_read(
            "get_organizations",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.organizations_api",
                api_class="OrganizationsApi",
                method_name="get_organizations_with_http_info",
                request_module="iikocloud_client.models.get_organizations_request",
                request_class="GetOrganizationsRequest",
                request_keyword="get_organizations_request",
            ),
            GetOrganizationsRequest(
                organizationIds=[organization_id],
                returnAdditionalInfo=False,
                includeDisabled=False,
            ),
        )

        menu = await live_sdk.call_bound_read(
            "get_external_menu_by_id",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.menu_api",
                api_class="MenuApi",
                method_name="get_external_menu_by_id_with_http_info",
                request_module="iikocloud_client.models.menu_request",
                request_class="MenuRequest",
                request_keyword="menu_request",
            ),
            MenuRequest(
                asyncMode=False,
                externalMenuId=live_profile.external_menu_id,
                organizationIds=[organization_id],
            ),
        )
        menu_json = menu.data.model_dump(mode="json", by_alias=True)
        price = _find_product_price(menu_json, live_profile.write_product_id)
        if price is None:
            present = live_profile.write_product_id in repr(menu_json)
            top = sorted(menu_json) if isinstance(menu_json, dict) else type(menu_json).__name__
            print(f"menu dump diagnostics: product_in_dump={present} top_keys={top}")
        assert price is not None, (
            "dedicated write product is not in the external menu; "
            "add it with a price in iikoWeb first"
        )

        order_types = await live_sdk.call_bound_read(
            "get_delivery_order_types",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.dictionaries_api",
                api_class="DictionariesApi",
                method_name="get_delivery_order_types_with_http_info",
                request_module="iikocloud_client.models.order_types_request",
                request_class="OrderTypesRequest",
                request_keyword="order_types_request",
            ),
            OrderTypesRequest(organizationIds=[organization_id]),
        )
        pickup_type_id = None
        for wrapper in order_types.data.order_types:
            for item in wrapper.items:
                if item.order_service_type.value == "DeliveryPickUp" and not item.is_deleted:
                    pickup_type_id = item.id
                    break
            if pickup_type_id is not None:
                break
        assert pickup_type_id is not None, (
            "no pickup (DeliveryPickUp) order type on the write stand; "
            "create one in iikoOffice/iikoWeb first"
        )

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
        create_request = CreateDraftRequest(
            organizationId=organization_id,
            terminalGroupId=terminal_group_id,
            order=draft_order,
        )
        from tools.openapi_pipeline.live.generated import GeneratedCallFailure

        try:
            created = await live_sdk.execute_write(
                "create_delivery_draft",
                # to_dict() (not model_dump) preserves union subclass fields.
                create_request.to_dict(),
            )
        except GeneratedCallFailure as error:
            print(
                f"draft create failed: status={error.status_code} "
                f"details={error.error_details!r}"
            )
            raise
        order_id = getattr(created.data, "order_id", None)
        assert order_id is not None, "create response carries no order id"

        delete_request = DeleteDraftRequest(
            organizationId=organization_id,
            orderId=order_id,
        )
        mutation_journal.register(
            "delete_delivery_draft",
            delete_request.model_dump(mode="json", by_alias=True),
        )

        verify_request = GetDraftRequest(
            organizationId=organization_id,
            orderId=order_id,
        )
        verified = await live_sdk.call_bound_read(
            "get_delivery_draft_by_id",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.drafts_api",
                api_class="DraftsApi",
                method_name="get_delivery_draft_by_id_with_http_info",
                request_module="iikocloud_client.models.get_draft_request",
                request_class="GetDraftRequest",
                request_keyword="get_draft_request",
            ),
            verify_request,
        )
        verified_json = verified.data.model_dump(mode="json", by_alias=True)
        assert CUSTOMER_MARKER_PHONE in repr(verified_json)
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
