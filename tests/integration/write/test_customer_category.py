from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary
from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("customer_category")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_customer_category_add_and_remove(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Category lifecycle on an owned customer: add, then remove, then delete."""
    from iikocloud_client import (
        ChangeCategoryForCustomerRequest,
        CreateOrUpdateCustomerRequest,
        DeleteCustomersRequest,
        GetCategoriesRequest,
    )

    organization_id = UUID(live_profile.organization_id)

    try:
        await canary(live_sdk, organization_id)

        categories = await call_read(
            live_sdk,
            "get_customer_categories",
            api_module="iikocloud_client.api.customer_categories_api",
            api_class="CustomerCategoriesApi",
            request_module="get_categories_request",
            request_class="GetCategoriesRequest",
            request_keyword="get_categories_request",
            request=GetCategoriesRequest(organizationId=organization_id),
        )
        category_ids = [
            getattr(category, "id", None)
            for category in getattr(categories.data, "categories", []) or []
        ]
        category_ids = [value for value in category_ids if value is not None]
        assert category_ids, "no guest categories on the write stand; create one in iikoWeb"
        category_id = category_ids[0]

        created = await live_sdk.execute_write(
            "create_or_update_customer",
            CreateOrUpdateCustomerRequest(
                organizationId=organization_id,
                phone=CUSTOMER_MARKER_PHONE,
                name="sdk-write-probe",
                shouldReceiveLoyaltyInfo=False,
                shouldReceivePromoActionsInfo=False,
            ).model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        customer_id = getattr(created.data, "id", None)
        assert customer_id is not None
        mutation_journal.register(
            "delete_customers",
            DeleteCustomersRequest(
                customerIds=[customer_id], organizationId=organization_id
            ).model_dump(mode="json", by_alias=True),
        )

        change = ChangeCategoryForCustomerRequest(
            categoryId=category_id,
            customerId=customer_id,
            organizationId=organization_id,
        )
        mutation_journal.register(
            "remove_customer_category",
            change.model_dump(mode="json", by_alias=True),
        )
        await live_sdk.execute_write(
            "add_customer_category",
            change.model_dump(mode="json", by_alias=True),
        )
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
