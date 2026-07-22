from __future__ import annotations

from typing import Any

import pytest

from tests.integration.read.cases import FULL_READ_PLAN
from tools.openapi_pipeline.live.read_planner import ReadPlan


@pytest.mark.live_read_full
@pytest.mark.asyncio(loop_scope="session")
async def test_all_reviewed_reads(
    live_read_harness: Any,
    live_read_plan: ReadPlan,
) -> None:
    assert live_read_plan is FULL_READ_PLAN
    assert len(live_read_plan.cases) == 91
    summary = await live_read_harness.run()
    if not summary.success:
        pytest.fail(
            "live_read_full did not satisfy the safe outcome contract",
            pytrace=False,
        )
