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
        MenuApi,
        RemoveProductsFromStopListItem,
        RemoveProductsFromStopListRequest,
        StopListsRequest,
    )

    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)
    product_id = UUID(live_profile.write_product_id)
    api = MenuApi(live_sdk.api_client)
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
        preflight_request = StopListsRequest(
            organizationIds=[organization_id],
            terminalGroupsIds=[terminal_group_id],
        )
        before = await live_sdk.call_generated(
            "get_stop_lists",
            preflight_request,
            lambda: api.get_stop_lists_with_http_info(
                stop_lists_request=preflight_request,
                _request_timeout=(10.0, 30.0),
            ),
        )
        assert not contains_product(
            before.model_dump(mode="json", by_alias=True),
            live_profile.write_product_id,
        ), "dedicated test product is already in the stop list"

        mutation_journal.register(
            "remove_products_from_stop_list",
            remove.model_dump(mode="json", by_alias=True),
        )
        added = await live_sdk.call_generated(
            "add_products_to_stop_list",
            add,
            lambda: api.add_products_to_stop_list_with_http_info(
                add_products_to_stop_list_request=add,
                _request_timeout=(10.0, 30.0),
            ),
        )
        assert added.correlation_id
    finally:
        await mutation_journal.cleanup(live_sdk.execute_cleanup)
