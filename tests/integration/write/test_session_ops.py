from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary, exec_write
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk


@pytest.mark.live_write
@pytest.mark.write_scenario("session_ops")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_personal_session_close_and_open(
    live_sdk: GeneratedLiveSdk,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Session sweep: close the open shift, then reopen it (ends open)."""
    from iikocloud_client import (
        ClosePersonalSessionRequest,
        CouriersRequest,
        GetPersonalSessionInfoRequest,
        OpenPersonalSessionRequest,
    )

    assert live_profile.terminal_group_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)

    await canary(live_sdk, organization_id)

    employees = await call_read(
        live_sdk,
        "get_couriers",
        api_module="iikocloud_client.api.employees_api",
        api_class="EmployeesApi",
        request_module="couriers_request",
        request_class="CouriersRequest",
        request_keyword="couriers_request",
        request=CouriersRequest(organizationIds=[organization_id]),
    )
    employee_ids: list[str] = []

    def _collect(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "id" and isinstance(child, str):
                    employee_ids.append(child)
                else:
                    _collect(child)
        elif isinstance(value, list):
            for child in value:
                _collect(child)

    _collect(employees.data.model_dump(mode="json", by_alias=True))
    assert employee_ids, "no employees on the write stand"
    employee_id = UUID(employee_ids[0])

    session = await call_read(
        live_sdk,
        "get_personal_session_info",
        api_module="iikocloud_client.api.employees_api",
        api_class="EmployeesApi",
        request_module="get_personal_session_info_request",
        request_class="GetPersonalSessionInfoRequest",
        request_keyword="get_personal_session_info_request",
        request=GetPersonalSessionInfoRequest(
            employeeId=employee_id,
            organizationId=organization_id,
            terminalGroupId=terminal_group_id,
        ),
    )
    session_json = session.data.model_dump(mode="json", by_alias=True)
    is_open = bool(
        session_json.get("isCurrentSessionOpen")
        or session_json.get("isOpen")
        or session_json.get("sessionIsOpen")
    )
    print(f"personal session state before: open={is_open} keys={sorted(session_json)}")

    if is_open:
        await exec_write(
            live_sdk,
            "close_personal_session",
            ClosePersonalSessionRequest(
                employeeId=employee_id,
                organizationId=organization_id,
                terminalGroupId=terminal_group_id,
            ).model_dump(mode="json", by_alias=True),
        )

    await exec_write(
        live_sdk,
        "open_personal_session",
        OpenPersonalSessionRequest(
            employeeId=employee_id,
            organizationId=organization_id,
            terminalGroupId=terminal_group_id,
        ).model_dump(mode="json", by_alias=True, exclude_none=True),
    )
