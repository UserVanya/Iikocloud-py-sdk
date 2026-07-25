from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary, exec_write
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk


@pytest.mark.live_write
@pytest.mark.write_scenario("misc_ops")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_misc_ops_barcodes_webhook_awake_clear(
    live_sdk: GeneratedLiveSdk,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Misc sweep: product barcodes, webhook no-op update, awake, clear stop list."""
    from iikocloud_client import (
        AwakeTerminalGroupsRequest,
        ClearStopListRequest,
        StopListsRequest,
    )

    assert live_profile.terminal_group_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)

    await canary(live_sdk, organization_id)

    await exec_write(
        live_sdk,
        "awake_terminal_groups",
        AwakeTerminalGroupsRequest(
            organizationIds=[organization_id],
            terminalGroupIds=[terminal_group_id],
        ).model_dump(mode="json", by_alias=True),
    )

    await call_read(
        live_sdk,
        "get_stop_lists",
        api_module="iikocloud_client.api.menu_api",
        api_class="MenuApi",
        request_module="stop_lists_request",
        request_class="StopListsRequest",
        request_keyword="stop_lists_request",
        request=StopListsRequest(
            organizationIds=[organization_id],
            terminalGroupsIds=[terminal_group_id],
        ),
    )
    await exec_write(
        live_sdk,
        "clear_stop_list",
        ClearStopListRequest(
            organizationId=organization_id,
            terminalGroupId=terminal_group_id,
        ).model_dump(mode="json", by_alias=True),
    )
