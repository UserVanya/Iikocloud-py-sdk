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


async def verified_compensation(
    live_sdk: GeneratedLiveSdk,
    journal: Any,
    operation_id: str,
    payload: dict[str, Any],
    organization_id: UUID,
) -> None:
    """Execute one compensation and prove the async command actually succeeded.

    iiko accepts commands such as cancel_delivery_order with HTTP 200 and then
    applies them asynchronously; HTTP 200 alone never meant "cancelled". The
    journal entry is marked done only after get_command_status reports
    ``Success``; on any failure the entry stays pending so orphan cleanup keeps
    tracking it. Commands still InProgress at check time are treated as
    unverified and fail loudly as well.
    """
    from iikocloud_client import GetCommandStatusRequest

    result = await exec_write(live_sdk, operation_id, payload)
    correlation_id = getattr(result.data, "correlation_id", None)
    if correlation_id is None:
        # Synchronous operation: HTTP success is the whole result.
        journal.complete(operation_id)
        return
    status = await call_read(
        live_sdk,
        "get_command_status",
        api_module="iikocloud_client.api.operations_api",
        api_class="OperationsApi",
        request_module="get_command_status_request",
        request_class="GetCommandStatusRequest",
        request_keyword="get_command_status_request",
        request=GetCommandStatusRequest(
            correlationId=correlation_id,
            organizationId=organization_id,
        ),
    )
    body = status.data.model_dump(mode="json", by_alias=True)
    state = body.get("state")
    if state != "Success":
        raise AssertionError(
            f"{operation_id} command did not succeed: state={state!r} details={body!r}"
        )
    journal.complete(operation_id)
