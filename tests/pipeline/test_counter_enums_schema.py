"""Effective-schema contract for the CounterMetric/CounterPeriod upstream defect.

See tests/contracts/test_counter_enums.py for the live-verified accepted sets
and the generated-model half of this contract.
"""

from __future__ import annotations

from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_committed_effective_schema

_COUNTER_METRIC_VALUES = ("OrdersCount", "OrdersSum")
_COUNTER_PERIOD_VALUES = ("AllTime", "Day", "Week", "Month", "Quarter", "Year")


def test_counter_enums_are_string_enums_in_effective_schema() -> None:
    effective = compose_committed_effective_schema(RepoPaths.discover())
    schemas = effective["components"]["schemas"]
    metric = schemas["iikoNet.Common.Enums.CounterMetric"]
    period = schemas["iikoNet.Common.Enums.CounterPeriod"]
    assert metric == {
        "title": " ",
        "type": "string",
        "enum": list(_COUNTER_METRIC_VALUES),
    }
    assert period == {
        "title": " ",
        "type": "string",
        "enum": list(_COUNTER_PERIOD_VALUES),
    }
