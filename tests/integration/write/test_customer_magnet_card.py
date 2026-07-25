from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary
from tools.openapi_pipeline.live.generated import (
    CUSTOMER_MARKER_CARD,
    CUSTOMER_MARKER_PHONE,
)
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("customer_magnet_card")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_customer_magnet_card_add_and_remove(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Magnet card lifecycle on an owned customer: add, verify, remove, delete."""
    from iikocloud_client import (
        AddMagnetCardRequest,
        CreateOrUpdateCustomerRequest,
        DeleteCustomersRequest,
        DeleteMagnetCardRequest,
        GetCustomerInfoByIdRequest,
    )

    organization_id = UUID(live_profile.organization_id)
    card_track = "sdk-probe-track-0000042"

    try:
        await canary(live_sdk, organization_id)

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

        mutation_journal.register(
            "remove_customer_magnet_card",
            DeleteMagnetCardRequest(
                cardTrack=card_track,
                customerId=customer_id,
                organizationId=organization_id,
            ).model_dump(mode="json", by_alias=True),
        )
        await live_sdk.execute_write(
            "add_customer_magnet_card",
            AddMagnetCardRequest(
                cardNumber=CUSTOMER_MARKER_CARD,
                cardTrack=card_track,
                customerId=customer_id,
                organizationId=organization_id,
            ).model_dump(mode="json", by_alias=True),
        )

        verified = await call_read(
            live_sdk,
            "get_customer_info",
            api_module="iikocloud_client.api.customers_api",
            api_class="CustomersApi",
            request_module="get_customer_info_by_id_request",
            request_class="GetCustomerInfoByIdRequest",
            request_keyword="get_customer_info_request",
            request=GetCustomerInfoByIdRequest(
                organizationId=organization_id,
                type="id",
                id=str(customer_id),
            ),
        )
        assert CUSTOMER_MARKER_CARD in repr(
            verified.data.model_dump(mode="json", by_alias=True)
        )
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
