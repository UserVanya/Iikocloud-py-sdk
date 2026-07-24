from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


def contains_product(value: Any, product_id: str) -> bool:
    if isinstance(value, dict):
        return any(
            (key == "productId" and child == product_id) or contains_product(child, product_id)
            for key, child in value.items()
        )
    if isinstance(value, list):
        return any(contains_product(child, product_id) for child in value)
    return False


@pytest.mark.live_write
@pytest.mark.write_scenario("stop_list_product")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_stop_list_add_is_accepted_and_removed(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None

    from iikocloud_client import (
        AddProductsToStopListItem,
        AddProductsToStopListRequest,
        GetOrganizationsRequest,
        RemoveProductsFromStopListItem,
        RemoveProductsFromStopListRequest,
        StopListsRequest,
    )
    from tools.openapi_pipeline.live.read_case import GeneratedReadBinding

    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)
    add = AddProductsToStopListRequest(
        organizationId=organization_id,
        terminalGroupId=terminal_group_id,
        items=[AddProductsToStopListItem(productId=product_id, balance=0)],
    )
    remove = RemoveProductsFromStopListRequest(
        organizationId=organization_id,
        terminalGroupId=terminal_group_id,
        items=[RemoveProductsFromStopListItem(productId=product_id)],
    )

    try:
        # The completed-receipt canary requires get_organizations in every run.
        canary_request = GetOrganizationsRequest(
            organizationIds=[organization_id],
            returnAdditionalInfo=False,
            includeDisabled=False,
        )
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
            canary_request,
        )

        preflight_request = StopListsRequest(
            organizationIds=[organization_id],
            terminalGroupsIds=[terminal_group_id],
        )
        preflight = await live_sdk.call_bound_read(
            "get_stop_lists",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.menu_api",
                api_class="MenuApi",
                method_name="get_stop_lists_with_http_info",
                request_module="iikocloud_client.models.stop_lists_request",
                request_class="StopListsRequest",
                request_keyword="stop_lists_request",
            ),
            preflight_request,
        )
        assert not contains_product(
            preflight.data.model_dump(mode="json", by_alias=True),
            live_profile.write_product_id,
        ), "dedicated test product is already in the stop list"

        mutation_journal.register(
            "remove_products_from_stop_list",
            remove.model_dump(mode="json", by_alias=True),
        )
        await live_sdk.execute_compensating(
            "add_products_to_stop_list",
            add.model_dump(mode="json", by_alias=True),
        )
    finally:
        await mutation_journal.cleanup(live_sdk.execute_cleanup)
