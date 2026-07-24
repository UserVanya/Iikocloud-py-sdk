"""Contract test for the CounterMetric/CounterPeriod upstream defect.

The upstream schema declares both enums as integer enums, but the real
`/api/1/loyalty/iiko/get_counters` endpoint accepts only string names.
Live-verified accepted sets (guarded probes, 2026-07-23):
metrics: "All counter metrics must be in the set [OrdersCount, OrdersSum]";
periods: "All counter periods must be in the set
[AllTime, Day, Week, Month, Quarter, Year]".
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


def test_generated_counter_enums_serialize_as_strings() -> None:
    from iikocloud_client.models.counter_metric import CounterMetric
    from iikocloud_client.models.counter_period import CounterPeriod
    from iikocloud_client.models.get_counters_request import GetCountersRequest
    from iikocloud_client.models.guest_counter import GuestCounter

    assert issubclass(CounterMetric, str)
    assert issubclass(CounterPeriod, str)
    assert {member.value for member in CounterMetric} == set(_COUNTER_METRIC_VALUES)
    assert {member.value for member in CounterPeriod} == set(_COUNTER_PERIOD_VALUES)

    request = GetCountersRequest(
        organizationId="00000000-0000-0000-0000-000000000001",
        guestIds=["00000000-0000-0000-0000-000000000002"],
        metrics=[CounterMetric("OrdersCount")],
        periods=[CounterPeriod("Week")],
    )
    dumped = request.model_dump(mode="json", by_alias=True)
    assert dumped["metrics"] == ["OrdersCount"]
    assert dumped["periods"] == ["Week"]

    counter = GuestCounter.model_validate(
        {
            "guestId": "00000000-0000-0000-0000-000000000002",
            "period": "Week",
            "metric": "OrdersCount",
            "value": 1.5,
        }
    )
    assert counter.period is CounterPeriod("Week")
    assert counter.metric is CounterMetric("OrdersCount")
