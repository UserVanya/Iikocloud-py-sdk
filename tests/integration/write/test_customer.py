from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

import pytest

from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("customer")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_customer_create_info_and_delete(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Owned-customer lifecycle: create with a marker phone, verify, delete.

    The marker phone comes from the reviewed write-lifecycle contract; the
    adapter refuses any other phone, so the test can only touch its own
    synthetic customer.
    """
    from iikocloud_client import (
        CreateOrUpdateCustomerRequest,
        DeleteCustomersRequest,
        GetCustomerInfoByIdRequest,
        GetCustomerInfoByPhoneRequest,
        GetOrganizationsRequest,
    )
    from tools.openapi_pipeline.live.read_case import GeneratedReadBinding

    organization_id = UUID(live_profile.organization_id)
    customer_id = uuid4()

    async def customer_by_phone() -> object:
        request = GetCustomerInfoByPhoneRequest(
            organizationId=organization_id,
            type="phone",
            phone=CUSTOMER_MARKER_PHONE,
        )
        result = await live_sdk.call_bound_read(
            "get_customer_info",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.customers_api",
                api_class="CustomersApi",
                method_name="get_customer_info_with_http_info",
                request_module="iikocloud_client.models.get_customer_info_by_phone_request",
                request_class="GetCustomerInfoByPhoneRequest",
                request_keyword="get_customer_info_request",
            ),
            request,
        )
        return result.data

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

        before = await customer_by_phone()
        assert getattr(before, "id", None) is None, (
            "marker phone is already registered; refusing to touch a foreign customer"
        )

        delete_request = DeleteCustomersRequest(
            customerIds=[customer_id],
            organizationId=organization_id,
        )
        mutation_journal.register(
            "delete_customers",
            delete_request.model_dump(mode="json", by_alias=True),
        )
        create_request = CreateOrUpdateCustomerRequest(
            id=customer_id,
            organizationId=organization_id,
            phone=CUSTOMER_MARKER_PHONE,
            name="sdk-write-probe",
            shouldReceiveLoyaltyInfo=False,
            shouldReceivePromoActionsInfo=False,
        )
        await live_sdk.execute_write(
            "create_or_update_customer",
            create_request.model_dump(mode="json", by_alias=True, exclude_none=True),
        )

        verify_request = GetCustomerInfoByIdRequest(
            organizationId=organization_id,
            type="id",
            id=str(customer_id),
        )
        verified = await live_sdk.call_bound_read(
            "get_customer_info",
            GeneratedReadBinding(
                api_module="iikocloud_client.api.customers_api",
                api_class="CustomersApi",
                method_name="get_customer_info_with_http_info",
                request_module="iikocloud_client.models.get_customer_info_by_id_request",
                request_class="GetCustomerInfoByIdRequest",
                request_keyword="get_customer_info_request",
            ),
            verify_request,
        )
        assert str(getattr(verified.data, "id", "")) == str(customer_id)
        assert getattr(verified.data, "phone", None) == CUSTOMER_MARKER_PHONE
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
