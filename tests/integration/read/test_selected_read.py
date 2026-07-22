from __future__ import annotations

from typing import Any

import pytest

from tests.integration.read.cases import FULL_READ_PLAN
from tools.openapi_pipeline.live.read_planner import ReadPlan


@pytest.mark.live_read_selected
@pytest.mark.asyncio(loop_scope="session")
async def test_one_selected_reviewed_read(
    live_read_harness: Any,
    live_read_plan: ReadPlan,
) -> None:
    assert 0 < len(live_read_plan.cases) < len(FULL_READ_PLAN.cases)
    assert set(live_read_plan.ordered_operation_ids) < set(FULL_READ_PLAN.ordered_operation_ids)
    summary = await live_read_harness.run()
    if not summary.success:
        pytest.fail(
            "live_read_selected did not satisfy the safe outcome contract",
            pytrace=False,
        )
