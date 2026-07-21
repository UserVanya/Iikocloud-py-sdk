from __future__ import annotations

from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.reserves_orders import RESERVE_ORDER_CASES
from tools.openapi_pipeline.live.read_case import (
    ContextView,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
    ReadContext,
    build_generated_request,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
OTHER_ORGANIZATION_ID = UUID("22222222-2222-4222-8222-222222222222")
TERMINAL_GROUP_ID = UUID("33333333-3333-4333-8333-333333333333")
FALLBACK_TERMINAL_GROUP_ID = UUID("44444444-4444-4444-8444-444444444444")
SECTION_ID = UUID("55555555-5555-4555-8555-555555555555")
TABLE_ID = UUID("66666666-6666-4666-8666-666666666666")
RESERVE_ID = UUID("77777777-7777-4777-8777-777777777777")
TABLE_ORDER_ID = UUID("88888888-8888-4888-8888-888888888888")
CUSTOMER_ID = UUID("99999999-9999-4999-8999-999999999999")
WINDOW_FROM = "2026-01-01 00:00:00.000"
WINDOW_TO = "2026-01-02 00:00:00.000"

RESERVE_ORDER_IDS = {
    "get_reserve_available_organizations",
    "get_reserve_restaurant_sections",
    "get_reserve_statuses_by_id",
    "get_reserve_terminal_groups",
    "get_restaurant_sections_workload",
    "get_table_orders_by_id",
    "get_table_orders_by_table",
}

RESPONSE_MODELS = {
    "get_reserve_available_organizations": (
        "get_organizations_response",
        "GetOrganizationsResponse",
    ),
    "get_reserve_restaurant_sections": (
        "get_restaurant_sections_response",
        "GetRestaurantSectionsResponse",
    ),
    "get_reserve_statuses_by_id": ("reserves_response", "ReservesResponse"),
    "get_reserve_terminal_groups": (
        "terminal_groups_response",
        "TerminalGroupsResponse",
    ),
    "get_restaurant_sections_workload": (
        "get_restaurant_sections_workload_response",
        "GetRestaurantSectionsWorkloadResponse",
    ),
    "get_table_orders_by_id": ("table_orders_response", "TableOrdersResponse"),
    "get_table_orders_by_table": (
        "table_orders_response",
        "TableOrdersResponse",
    ),
}


def _class(module_name: str, class_name: str) -> type[object]:
    return getattr(import_module(f"iikocloud_client.models.{module_name}"), class_name)


def _model(module_name: str, class_name: str, **values: object) -> object:
    return _class(module_name, class_name).model_construct(**values)  # type: ignore[attr-defined]


def _jsonable(value: object) -> object:
    if type(value) is UUID:
        return str(value)
    if isinstance(value, Enum):
        return value.value
    if type(value) is list:
        return [_jsonable(item) for item in value]
    if type(value) is dict:
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _case(operation_id: str) -> ReadCase:
    return next(
        case for case in RESERVE_ORDER_CASES if case.operation_id == operation_id
    )


def _view(
    case: ReadCase,
    *,
    omit: frozenset[str] = frozenset(),
    **changes: object,
) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "terminal_group_id": TERMINAL_GROUP_ID,
        "reserve_terminal_group_id": TERMINAL_GROUP_ID,
        "restaurant_section_id": SECTION_ID,
        "table_id": TABLE_ID,
        "reserve_id": RESERVE_ID,
        "table_order_id": TABLE_ORDER_ID,
        "window_from_local": WINDOW_FROM,
        "window_to_local": WINDOW_TO,
    }
    values.update(changes)
    return ContextView(
        {
            key: values[key]
            for key in case.requires
            if key in values and key not in omit
        }
    )


def _organization_response(organization_id: UUID) -> object:
    organization = _model("organization_info", "OrganizationInfo", id=organization_id)
    return _model(
        "get_organizations_response",
        "GetOrganizationsResponse",
        organizations=[organization],
    )


def _terminal(
    terminal_group_id: UUID,
    *,
    organization_id: UUID = ORGANIZATION_ID,
) -> object:
    return _model(
        "terminal_group",
        "TerminalGroup",
        id=terminal_group_id,
        organization_id=organization_id,
    )


def _terminal_group(
    *terminals: object,
    organization_id: UUID = ORGANIZATION_ID,
) -> object:
    return _model(
        "rms_terminal_group_items_response",
        "RmsTerminalGroupItemsResponse",
        items=list(terminals),
        organization_id=organization_id,
    )


def _terminal_response(
    *groups: object,
    sleeping: tuple[object, ...] = (),
) -> object:
    return _model(
        "terminal_groups_response",
        "TerminalGroupsResponse",
        terminal_groups=list(groups),
        terminal_groups_in_sleep=list(sleeping),
    )


def _section(
    section_id: UUID,
    *,
    terminal_group_id: UUID = TERMINAL_GROUP_ID,
    table_ids: tuple[UUID, ...] = (TABLE_ID,),
) -> object:
    tables = [
        _model("table", "Table", id=table_id, is_deleted=False)
        for table_id in table_ids
    ]
    return _model(
        "restaurant_section",
        "RestaurantSection",
        id=section_id,
        tables=tables,
        terminal_group_id=terminal_group_id,
    )


def _sections_response(*sections: object) -> object:
    return _model(
        "get_restaurant_sections_response",
        "GetRestaurantSectionsResponse",
        restaurant_sections=list(sections),
    )


def _workload_response(*reserve_ids: UUID) -> object:
    reserves = [
        _model("reserve_in_workload", "ReserveInWorkload", id=reserve_id)
        for reserve_id in reserve_ids
    ]
    return _model(
        "get_restaurant_sections_workload_response",
        "GetRestaurantSectionsWorkloadResponse",
        reserves=reserves,
    )


def _reserves_response(*reserve_ids: UUID) -> object:
    reserves = [
        _model(
            "reserve_info",
            "ReserveInfo",
            id=reserve_id,
            organization_id=ORGANIZATION_ID,
        )
        for reserve_id in reserve_ids
    ]
    return _model("reserves_response", "ReservesResponse", reserves=reserves)


def _table_order(
    order_id: UUID,
    *,
    organization_id: UUID = ORGANIZATION_ID,
    customer_id: UUID | None = CUSTOMER_ID,
) -> object:
    payload = None
    if customer_id is not None:
        customer = _model(
            "delivery_order_response_regular_customer",
            "DeliveryOrderResponseRegularCustomer",
            id=customer_id,
        )
        payload = _model(
            "table_order_response_payload",
            "TableOrderResponsePayload",
            customer=customer,
            table_ids=[TABLE_ID],
        )
    return _model(
        "table_order_info",
        "TableOrderInfo",
        id=order_id,
        order=payload,
        organization_id=organization_id,
    )


def _table_orders_response(*orders: object) -> object:
    return _model("table_orders_response", "TableOrdersResponse", orders=list(orders))


def _minimal_response(operation_id: str) -> object:
    if operation_id == "get_reserve_available_organizations":
        return _organization_response(ORGANIZATION_ID)
    if operation_id == "get_reserve_terminal_groups":
        return _terminal_response()
    if operation_id == "get_reserve_restaurant_sections":
        return _sections_response()
    if operation_id == "get_restaurant_sections_workload":
        return _workload_response()
    if operation_id == "get_reserve_statuses_by_id":
        return _reserves_response()
    return _table_orders_response()


def _request_json(case: ReadCase) -> object:
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    return _jsonable(request.to_dict())  # type: ignore[attr-defined]


def test_reserve_order_registry_is_exact_and_builds_with_foundation() -> None:
    assert type(RESERVE_ORDER_CASES) is tuple
    assert {case.operation_id for case in RESERVE_ORDER_CASES} == RESERVE_ORDER_IDS
    assert len(RESERVE_ORDER_CASES) == len(RESERVE_ORDER_IDS)
    assert set(
        ReadPlan.build((*FOUNDATION_CASES, *RESERVE_ORDER_CASES)).ordered_operation_ids
    ) > RESERVE_ORDER_IDS


def test_dependency_chain_and_provider_keys_are_exact() -> None:
    assert _case("get_reserve_available_organizations").depends_on == (
        "get_organizations",
    )
    assert _case("get_reserve_terminal_groups").depends_on == (
        "get_reserve_available_organizations",
        "get_terminal_groups",
    )
    assert _case("get_reserve_terminal_groups").provides == (
        "reserve_terminal_group_id",
    )
    assert _case("get_reserve_restaurant_sections").depends_on == (
        "get_reserve_terminal_groups",
    )
    assert _case("get_reserve_restaurant_sections").provides == (
        "restaurant_section_id",
        "table_id",
    )
    assert _case("get_restaurant_sections_workload").depends_on == (
        "get_reserve_restaurant_sections",
    )
    assert _case("get_restaurant_sections_workload").provides == ("reserve_id",)
    assert _case("get_reserve_statuses_by_id").depends_on == (
        "get_restaurant_sections_workload",
    )
    assert _case("get_table_orders_by_table").depends_on == (
        "get_reserve_restaurant_sections",
    )
    assert _case("get_table_orders_by_table").provides == (
        "table_order_id",
        "table_order_customer_id",
    )
    assert _case("get_table_orders_by_id").depends_on == (
        "get_table_orders_by_table",
    )


@pytest.mark.parametrize("operation_id", sorted(RESERVE_ORDER_IDS))
def test_bindings_resolve_and_validators_use_fixed_redacted_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id), _view(case))

    private_marker = "private-reserve-table-order-customer"
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": private_marker}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert private_marker not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_all_requests_are_exactly_scoped_to_response_derived_targets() -> None:
    expected = {
        "get_reserve_available_organizations": {
            "includeDisabled": False,
            "organizationIds": [str(ORGANIZATION_ID)],
            "returnAdditionalInfo": False,
        },
        "get_reserve_terminal_groups": {
            "organizationIds": [str(ORGANIZATION_ID)]
        },
        "get_reserve_restaurant_sections": {
            "returnSchema": False,
            "terminalGroupIds": [str(TERMINAL_GROUP_ID)],
        },
        "get_restaurant_sections_workload": {
            "dateFrom": WINDOW_FROM,
            "dateTo": WINDOW_TO,
            "restaurantSectionIds": [str(SECTION_ID)],
        },
        "get_reserve_statuses_by_id": {
            "organizationId": str(ORGANIZATION_ID),
            "reserveIds": [str(RESERVE_ID)],
        },
        "get_table_orders_by_table": {
            "dateFrom": WINDOW_FROM,
            "dateTo": WINDOW_TO,
            "organizationIds": [str(ORGANIZATION_ID)],
            "tableIds": [str(TABLE_ID)],
        },
        "get_table_orders_by_id": {
            "orderIds": [str(TABLE_ORDER_ID)],
            "organizationIds": [str(ORGANIZATION_ID)],
        },
    }
    assert {
        operation_id: _request_json(_case(operation_id))
        for operation_id in sorted(RESERVE_ORDER_IDS)
    } == expected


def test_reserve_organization_requires_the_selected_organization() -> None:
    case = _case("get_reserve_available_organizations")
    case.validate_response(_organization_response(ORGANIZATION_ID), _view(case))
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(
            _organization_response(OTHER_ORGANIZATION_ID),
            _view(case),
        )


def test_reserve_terminal_prefers_validated_target_then_falls_back_in_org() -> None:
    case = _case("get_reserve_terminal_groups")
    fallback = _terminal(FALLBACK_TERMINAL_GROUP_ID)
    preferred = _terminal(TERMINAL_GROUP_ID)
    response = _terminal_response(_terminal_group(fallback, preferred))
    assert case.extract(response, _view(case)) == {
        "reserve_terminal_group_id": TERMINAL_GROUP_ID
    }

    without_preferred = _terminal_response(_terminal_group(fallback))
    assert case.extract(without_preferred, _view(case)) == {
        "reserve_terminal_group_id": FALLBACK_TERMINAL_GROUP_ID
    }

    foreign = _terminal_response(
        _terminal_group(
            _terminal(FALLBACK_TERMINAL_GROUP_ID, organization_id=OTHER_ORGANIZATION_ID),
            organization_id=OTHER_ORGANIZATION_ID,
        )
    )
    assert case.extract(foreign, _view(case)) == {}
    assert case.extract(_terminal_response(), _view(case)) == {}


def test_first_target_section_and_its_first_table_are_published() -> None:
    case = _case("get_reserve_restaurant_sections")
    foreign = _section(SECTION_ID, terminal_group_id=FALLBACK_TERMINAL_GROUP_ID)
    target = _section(SECTION_ID)
    assert case.extract(_sections_response(foreign, target), _view(case)) == {
        "restaurant_section_id": SECTION_ID,
        "table_id": TABLE_ID,
    }

    no_tables = _section(SECTION_ID, table_ids=())
    assert case.extract(_sections_response(no_tables), _view(case)) == {
        "restaurant_section_id": SECTION_ID
    }
    assert case.extract(_sections_response(foreign), _view(case)) == {}


def test_workload_publishes_only_the_first_response_reserve() -> None:
    case = _case("get_restaurant_sections_workload")
    other = UUID("aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa")
    assert case.extract(_workload_response(RESERVE_ID, other), _view(case)) == {
        "reserve_id": RESERVE_ID
    }
    assert case.extract(_workload_response(), _view(case)) == {}


def test_table_order_provider_is_org_scoped_and_keeps_optional_customer_hidden() -> None:
    case = _case("get_table_orders_by_table")
    foreign = _table_order(
        TABLE_ORDER_ID,
        organization_id=OTHER_ORGANIZATION_ID,
    )
    target = _table_order(TABLE_ORDER_ID)
    values = case.extract(_table_orders_response(foreign, target), _view(case))
    assert values == {
        "table_order_id": TABLE_ORDER_ID,
        "table_order_customer_id": CUSTOMER_ID,
    }

    context = ReadContext.seed({"organization_id": ORGANIZATION_ID})
    context.apply(case, values)
    assert repr(context) == "ReadContext()"
    assert repr(context.view(("table_order_customer_id",))) == "ContextView()"
    assert str(CUSTOMER_ID) not in repr(context)


def test_table_order_provider_preserves_id_when_customer_is_absent() -> None:
    case = _case("get_table_orders_by_table")
    without_customer = _table_order(TABLE_ORDER_ID, customer_id=None)
    assert case.extract(_table_orders_response(without_customer), _view(case)) == {
        "table_order_id": TABLE_ORDER_ID
    }
    assert case.extract(_table_orders_response(), _view(case)) == {}


@pytest.mark.parametrize(
    ("operation_id", "missing_key", "expected_code"),
    [
        (
            "get_reserve_restaurant_sections",
            "reserve_terminal_group_id",
            NoLiveTargetCode.TERMINAL_GROUP,
        ),
        (
            "get_restaurant_sections_workload",
            "restaurant_section_id",
            NoLiveTargetCode.RESTAURANT_SECTION,
        ),
        ("get_reserve_statuses_by_id", "reserve_id", NoLiveTargetCode.RESERVE),
        ("get_table_orders_by_table", "table_id", NoLiveTargetCode.TABLE),
        (
            "get_table_orders_by_id",
            "table_order_id",
            NoLiveTargetCode.TABLE_ORDER,
        ),
    ],
)
def test_empty_results_gate_dependents_before_sdk_invocation(
    operation_id: str,
    missing_key: str,
    expected_code: NoLiveTargetCode,
) -> None:
    case = _case(operation_id)
    with pytest.raises(NoLiveTarget) as raised:
        case.build_values(_view(case, omit=frozenset({missing_key})))
    assert raised.value.code is expected_code
    assert case.allowed_no_target_codes == frozenset({expected_code})


def test_missing_target_wins_before_window_access() -> None:
    workload = _case("get_restaurant_sections_workload")
    with pytest.raises(NoLiveTarget) as missing_section:
        workload.build_values(
            _view(
                workload,
                omit=frozenset(
                    {"restaurant_section_id", "window_from_local", "window_to_local"}
                ),
            )
        )
    assert missing_section.value.code is NoLiveTargetCode.RESTAURANT_SECTION

    by_table = _case("get_table_orders_by_table")
    with pytest.raises(NoLiveTarget) as missing_table:
        by_table.build_values(
            _view(
                by_table,
                omit=frozenset({"table_id", "window_from_local", "window_to_local"}),
            )
        )
    assert missing_table.value.code is NoLiveTargetCode.TABLE
