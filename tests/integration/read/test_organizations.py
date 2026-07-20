from __future__ import annotations

from typing import Any
from uuid import UUID

import pytest

from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile


def contains_value(value: Any, expected: str) -> bool:
    if isinstance(value, dict):
        return any(contains_value(child, expected) for child in value.values())
    if isinstance(value, list):
        return any(contains_value(child, expected) for child in value)
    return value == expected


@pytest.mark.live_read_smoke
async def test_generated_sdk_lists_target_organization(
    live_sdk: GeneratedLiveSdk,
    live_profile: ResolvedLiveProfile,
) -> None:
    from iikocloud_client import GetOrganizationsRequest, OrganizationsApi

    api = OrganizationsApi(live_sdk.api_client)
    request = GetOrganizationsRequest(
        organizationIds=[UUID(live_profile.organization_id)],
        returnAdditionalInfo=False,
        includeDisabled=False,
    )
    response = await live_sdk.call_generated(
        "get_organizations",
        request,
        lambda: api.get_organizations_with_http_info(
            get_organizations_request=request,
            _request_timeout=(10.0, 30.0),
        ),
    )

    assert contains_value(
        response.model_dump(mode="json", by_alias=True),
        live_profile.organization_id,
    )
