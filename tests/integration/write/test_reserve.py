from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.integration.write._support import call_read, canary, exec_write
from tools.openapi_pipeline.live.generated import CUSTOMER_MARKER_PHONE
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile

if TYPE_CHECKING:
    from tools.openapi_pipeline.live.generated import GeneratedLiveSdk
    from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.live_write
@pytest.mark.write_scenario("reserve")
@pytest.mark.audit_residue
@pytest.mark.asyncio(loop_scope="session")
async def test_reserve_create_and_cancel(
    live_sdk: GeneratedLiveSdk,
    mutation_journal: MutationJournal,
    live_profile: ResolvedLiveProfile,
) -> None:
    """Reserve lifecycle: create on a stand table, verify status, cancel."""
    from iikocloud_client import (
        CancelReserveRequest,
        CreateReserveRequest,
        DeliveryOrderCreateRegularCustomer,
        GetRestaurantSectionsRequest,
        GetRestaurantSectionsWorkloadRequest,
        ReserveCancelReason,
        ReservesByIdRequest,
    )

    assert live_profile.terminal_group_id is not None
    organization_id = UUID(live_profile.organization_id)
    terminal_group_id = UUID(live_profile.terminal_group_id)

    try:
        await canary(live_sdk, organization_id)

        sections = await call_read(
            live_sdk,
            "get_reserve_restaurant_sections",
            api_module="iikocloud_client.api.banquets_reserves_api",
            api_class="BanquetsReservesApi",
            request_module="get_restaurant_sections_request",
            request_class="GetRestaurantSectionsRequest",
            request_keyword="get_restaurant_sections_request",
            request=GetRestaurantSectionsRequest(
                terminalGroupIds=[terminal_group_id],
            ),
        )
        table_ids = [
            table.id
            for section in sections.data.restaurant_sections
            for table in section.tables
        ]
        assert table_ids, (
            "no reservable tables on the write stand; "
            "create a restaurant section with a table in iikoWeb first"
        )
        table_id = table_ids[0]

        estimated_start = (
            (datetime.now(timezone.utc) + timedelta(days=1))
            .replace(hour=12, minute=0, second=0, microsecond=0)
            .strftime("%Y-%m-%d %H:%M:%S.000")
        )
        created = await exec_write(
            live_sdk,
            "create_reserve",
            CreateReserveRequest(
                organizationId=organization_id,
                phone=CUSTOMER_MARKER_PHONE,
                customer=DeliveryOrderCreateRegularCustomer(
                    type="regular",
                    name="sdk-write-probe",
                    shouldReceiveOrderStatusNotifications=False,
                ),
                durationInMinutes=60,
                shouldRemind=False,
                tableIds=[table_id],
                estimatedStartTime=estimated_start,
                guestsCount=1,
                comment="sdk-write-probe",
                externalNumber=f"sdk-write-probe-{datetime.now(timezone.utc):%H%M%S}",
            ).to_dict(),
        )
        correlation = getattr(created.data, "correlation_id", None)
        assert correlation is not None

        # create_reserve is asynchronous: discover the assigned id via the
        # section workload by table and estimated start time.
        today = datetime.now(timezone.utc).date()
        table_section_ids = {
            section.id
            for section in sections.data.restaurant_sections
            if any(table.id == table_id for table in section.tables)
        }
        workload = await call_read(
            live_sdk,
            "get_restaurant_sections_workload",
            api_module="iikocloud_client.api.banquets_reserves_api",
            api_class="BanquetsReservesApi",
            request_module="get_restaurant_sections_workload_request",
            request_class="GetRestaurantSectionsWorkloadRequest",
            request_keyword="get_restaurant_sections_workload_request",
            request=GetRestaurantSectionsWorkloadRequest(
                restaurantSectionIds=sorted(table_section_ids),
                dateFrom=f"{today.isoformat()} 00:00:00.000",
                dateTo=f"{(today + timedelta(days=30)).isoformat()} 00:00:00.000",
            ),
        )
        candidates = [
            reserve.id
            for reserve in workload.data.reserves
            if table_id in reserve.table_ids
            and reserve.duration_in_minutes == 60
            and reserve.guests_count == 1
        ]
        if len(candidates) != 1:
            from iikocloud_client import GetCommandStatusRequest

            command_status = await call_read(
                live_sdk,
                "get_command_status",
                api_module="iikocloud_client.api.operations_api",
                api_class="OperationsApi",
                request_module="get_command_status_request",
                request_class="GetCommandStatusRequest",
                request_keyword="get_command_status_request",
                request=GetCommandStatusRequest(
                    correlationId=correlation,
                    organizationId=organization_id,
                ),
            )
            print(
                "create_reserve command status: "
                f"{command_status.data.model_dump(mode='json', by_alias=True)!r}"
            )
        assert len(candidates) == 1, (
            f"expected exactly one created reserve, got {len(candidates)}"
        )
        reserve_id = candidates[0]

        mutation_journal.register(
            "cancel_reserve",
            CancelReserveRequest(
                organizationId=organization_id,
                reserveId=reserve_id,
                cancelReason=ReserveCancelReason.OTHER,
            ).model_dump(mode="json", by_alias=True),
        )

        verified = await call_read(
            live_sdk,
            "get_reserve_statuses_by_id",
            api_module="iikocloud_client.api.banquets_reserves_api",
            api_class="BanquetsReservesApi",
            request_module="reserves_by_id_request",
            request_class="ReservesByIdRequest",
            request_keyword="reserves_by_id_request",
            request=ReservesByIdRequest(
                organizationId=organization_id,
                reserveIds=[reserve_id],
            ),
        )
        returned_ids = {
            str(reserve.get("id"))
            for reserve in verified.data.model_dump(mode="json", by_alias=True).get(
                "reserves", []
            )
            if isinstance(reserve, dict)
        }
        assert str(reserve_id) in returned_ids
    finally:
        await mutation_journal.cleanup(live_sdk.execute_write)
