from __future__ import annotations

from typing import Any

import pytest


@pytest.mark.live_read_full
@pytest.mark.asyncio(loop_scope="session")
async def test_all_reviewed_reads(live_read_harness: Any) -> None:
    summary = await live_read_harness.run()
    if not summary.success:
        pytest.fail(
            "live_read_full did not satisfy the safe outcome contract",
            pytrace=False,
        )
