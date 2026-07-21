from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

import pytest

from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.read_case import GeneratedReadBinding

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk


def contains_value(value: Any, expected: str) -> bool:
    if isinstance(value, dict):
        return any(contains_value(child, expected) for child in value.values())
    if isinstance(value, list):
        return any(contains_value(child, expected) for child in value)
    return value == expected


@pytest.mark.live_read_smoke
@pytest.mark.asyncio(loop_scope="session")
async def test_generated_sdk_lists_target_organization(
    live_sdk: GeneratedLiveSdk,
    live_profile: ResolvedLiveProfile,
) -> None:
    from iikocloud_client import GetOrganizationsRequest

    request = GetOrganizationsRequest(
        organizationIds=[UUID(live_profile.organization_id)],
        returnAdditionalInfo=False,
        includeDisabled=False,
    )
    result = await live_sdk.call_bound_read(
        "get_organizations",
        GeneratedReadBinding(
            api_module="iikocloud_client.api.organizations_api",
            api_class="OrganizationsApi",
            method_name="get_organizations_with_http_info",
            request_module="iikocloud_client.models.get_organizations_request",
            request_class="GetOrganizationsRequest",
            request_keyword="get_organizations_request",
        ),
        request,
    )
    response = result.data

    assert contains_value(
        response.model_dump(mode="json", by_alias=True),
        live_profile.organization_id,
    )
