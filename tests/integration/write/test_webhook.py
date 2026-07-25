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
async def test_webhook_settings_update(
    live_sdk: GeneratedLiveSdk,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Isolated webhook settings update (settings endpoints are rate-strict)."""
    from iikocloud_client import GetWebHookSettingsRequest, UpdateWebHookSettingsRequest

    organization_id = UUID(live_profile.organization_id)
    await canary(live_sdk, organization_id)

    webhook = await call_read(
        live_sdk,
        "get_webhook_settings",
        api_module="iikocloud_client.api.webhooks_api",
        api_class="WebhooksApi",
        request_module="get_web_hook_settings_request",
        request_class="GetWebHookSettingsRequest",
        request_keyword="get_web_hook_settings_request",
        request=GetWebHookSettingsRequest(organizationId=organization_id),
    )
    current = webhook.data.model_dump(mode="json", by_alias=True)
    # The server requires an HTTPS WebHooks URI; a placeholder on the write
    # stand is an accepted, documented residue.
    uri = current.get("webHooksUri") or "https://example.invalid/sdk-write-probe"
    await exec_write(
        live_sdk,
        "update_webhook_settings",
        UpdateWebHookSettingsRequest(
            organizationId=organization_id,
            webHooksUri=uri,
        ).model_dump(mode="json", by_alias=True, exclude_none=True),
    )
