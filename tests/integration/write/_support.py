"""Shared helpers for guarded live write lifecycle tests."""

from __future__ import annotations

from typing import Any
from uuid import UUID

from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
from tools.openapi_pipeline.live.read_case import GeneratedReadBinding


async def canary(live_sdk: GeneratedLiveSdk, organization_id: UUID) -> None:
    """The completed-receipt canary requires get_organizations in every run."""
    from iikocloud_client import GetOrganizationsRequest

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


async def call_read(
    live_sdk: GeneratedLiveSdk,
    operation_id: str,
    *,
    api_module: str,
    api_class: str,
    method_name: str | None = None,
    request_module: str | None = None,
    request_class: str | None = None,
    request_keyword: str | None = None,
    request: object | None = None,
) -> Any:
    """Call one allowlisted read through its exact generated binding."""
    return await live_sdk.call_bound_read(
        operation_id,
        GeneratedReadBinding(
            api_module=api_module,
            api_class=api_class,
            method_name=method_name or f"{operation_id}_with_http_info",
            request_module=(
                f"iikocloud_client.models.{request_module}" if request_module else None
            ),
            request_class=request_class,
            request_keyword=request_keyword,
        ),
        request,
    )


async def exec_write(live_sdk: GeneratedLiveSdk, operation_id: str, payload: object) -> object:
    """execute_write with sanitized error details printed on failure."""
    from tools.openapi_pipeline.live.generated import GeneratedCallFailure

    try:
        return await live_sdk.execute_write(operation_id, payload)
    except GeneratedCallFailure as error:
        print(
            f"write {operation_id} failed: status={error.status_code} "
            f"details={error.error_details!r}"
        )
        raise
