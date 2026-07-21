from __future__ import annotations

from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.deliveries import DELIVERY_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
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
SEARCH_DELIVERY_ID = UUID("33333333-3333-4333-8333-333333333333")
STATUS_DELIVERY_ID = UUID("44444444-4444-4444-8444-444444444444")
CUSTOMER_ID = UUID("55555555-5555-4555-8555-555555555555")
DRAFT_ID = UUID("66666666-6666-4666-8666-666666666666")
PHONE = "+70000000001"
STATUS_PHONE = "+70000000002"
WINDOW_FROM = "2026-01-01 00:00:00.000"
WINDOW_TO = "2026-01-02 00:00:00.000"

DELIVERY_IDS = {
    "get_allowed_delivery_restrictions",
    "get_deliveries_by_delivery_date_and_phone",
    "get_deliveries_by_delivery_date_and_status",
    "get_deliveries_by_id",
    "get_deliveries_by_revision",
    "get_delivery_draft_by_id",
    "get_delivery_drafts_by_filter",
    "get_delivery_history_by_delivery_date_and_phone",
    "get_delivery_restrictions",
    "search_deliveries",
}

RESPONSE_MODELS = {
    "get_allowed_delivery_restrictions": (
        "get_allowed_restrictions_response",
        "GetAllowedRestrictionsResponse",
    ),
    "get_deliveries_by_delivery_date_and_phone": (
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
    ),
    "get_deliveries_by_delivery_date_and_status": (
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
    ),
    "get_deliveries_by_id": ("orders_response", "OrdersResponse"),
    "get_deliveries_by_revision": (
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
    ),
    "get_delivery_draft_by_id": ("get_draft_response", "GetDraftResponse"),
    "get_delivery_drafts_by_filter": (
        "filter_drafts_response",
        "FilterDraftsResponse",
    ),
    "get_delivery_history_by_delivery_date_and_phone": (
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
    ),
    "get_delivery_restrictions": (
        "get_delivery_restrictions_response",
        "GetDeliveryRestrictionsResponse",
    ),
    "search_deliveries": (
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
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
    return next(case for case in DELIVERY_CASES if case.operation_id == operation_id)


def _view(case: ReadCase, **changes: object) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "window_from_local": WINDOW_FROM,
        "window_to_local": WINDOW_TO,
        "search_delivery_id": SEARCH_DELIVERY_ID,
        "status_delivery_id": STATUS_DELIVERY_ID,
        "search_delivery_phone": PHONE,
        "status_delivery_phone": STATUS_PHONE,
        "search_delivery_revision": 17,
        "status_delivery_revision": 19,
        "draft_id": DRAFT_ID,
    }
    values.update(changes)
    return ContextView({key: values[key] for key in case.requires if key in values})


def _orders_response(
    *,
    organization_id: UUID = ORGANIZATION_ID,
    order_id: UUID = SEARCH_DELIVERY_ID,
    phone: str = PHONE,
    customer_id: UUID = CUSTOMER_ID,
    revision: int = 17,
) -> object:
    customer = _model(
        "delivery_order_response_regular_customer",
        "DeliveryOrderResponseRegularCustomer",
        id=customer_id,
        type="regular",
    )
    payload = _model(
        "delivery_order_response_payload",
        "DeliveryOrderResponsePayload",
        customer=customer,
        phone=phone,
    )
    order = _model(
        "order_info",
        "OrderInfo",
        id=order_id,
        order=payload,
        organization_id=organization_id,
    )
    group = _model(
        "orders_by_organization",
        "OrdersByOrganization",
        orders=[order],
        organization_id=organization_id,
    )
    return _model(
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        max_revision=revision,
        orders_by_organizations=[group],
    )


def _empty_orders_response(*, revision: int = 0) -> object:
    return _model(
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        max_revision=revision,
        orders_by_organizations=[],
    )


def _minimal_response(operation_id: str) -> object:
    if operation_id in {
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
        "get_deliveries_by_delivery_date_and_phone",
        "get_deliveries_by_revision",
        "get_delivery_history_by_delivery_date_and_phone",
    }:
        return _empty_orders_response()
    module_name, class_name = RESPONSE_MODELS[operation_id]
    if operation_id == "get_deliveries_by_id":
        return _model(module_name, class_name, orders=[])
    if operation_id == "get_delivery_drafts_by_filter":
        return _model(module_name, class_name, drafts=[])
    return _model(module_name, class_name)


def test_delivery_registry_is_exact_and_builds_with_foundation() -> None:
    assert type(DELIVERY_CASES) is tuple
    assert {case.operation_id for case in DELIVERY_CASES} == DELIVERY_IDS
    assert len(DELIVERY_CASES) == len(DELIVERY_IDS)
    assert set(
        ReadPlan.build((*FOUNDATION_CASES, *DELIVERY_CASES)).ordered_operation_ids
    ) > DELIVERY_IDS


def test_delivery_dependencies_and_provider_keys_are_exact() -> None:
    for operation_id in {
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
        "get_delivery_drafts_by_filter",
        "get_delivery_restrictions",
        "get_allowed_delivery_restrictions",
    }:
        assert _case(operation_id).depends_on == ("get_organizations",)

    search = _case("search_deliveries")
    assert search.requires == (
        "organization_id",
        "window_from_local",
        "window_to_local",
    )
    assert search.provides == (
        "search_delivery_id",
        "search_delivery_phone",
        "search_delivery_revision",
        "search_delivery_customer_id",
    )

    status = _case("get_deliveries_by_delivery_date_and_status")
    assert status.provides == (
        "status_delivery_id",
        "status_delivery_phone",
        "status_delivery_revision",
        "status_delivery_customer_id",
    )

    assert _case("get_delivery_drafts_by_filter").provides == ("draft_id",)
    assert _case("get_deliveries_by_id").depends_on == (
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
    )
    assert _case("get_deliveries_by_delivery_date_and_phone").depends_on == (
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
    )
    assert _case("get_delivery_history_by_delivery_date_and_phone").depends_on == (
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
    )
    assert _case("get_deliveries_by_revision").depends_on == (
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
    )
    assert _case("get_delivery_draft_by_id").depends_on == (
        "get_delivery_drafts_by_filter",
    )


@pytest.mark.parametrize("operation_id", sorted(DELIVERY_IDS))
def test_bindings_resolve_and_validators_fail_with_fixed_redacted_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id), _view(case))

    private_marker = "private-phone-customer-order"
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": private_marker}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert private_marker not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_foundation_delivery_requests_are_exactly_bounded() -> None:
    expected = {
        "search_deliveries": {
            "deliveryDateFrom": WINDOW_FROM,
            "deliveryDateTo": WINDOW_TO,
            "organizationIds": [str(ORGANIZATION_ID)],
            "rowsCount": 1,
            "sortDirection": "Ascending",
            "sortProperty": "CompleteBefore",
        },
        "get_deliveries_by_delivery_date_and_status": {
            "deliveryDateFrom": WINDOW_FROM,
            "deliveryDateTo": WINDOW_TO,
            "organizationIds": [str(ORGANIZATION_ID)],
        },
        "get_delivery_drafts_by_filter": {
            "dateFrom": WINDOW_FROM,
            "dateTo": WINDOW_TO,
            "limit": 1,
            "offset": 0,
            "organizationIds": [str(ORGANIZATION_ID)],
        },
        "get_delivery_restrictions": {
            "organizationIds": [str(ORGANIZATION_ID)]
        },
        "get_allowed_delivery_restrictions": {
            "deliverySum": 0,
            "discountSum": 0,
            "isCourierDelivery": False,
            "orderItems": [],
            "organizationId": str(ORGANIZATION_ID),
        },
    }

    for operation_id, expected_json in expected.items():
        case = _case(operation_id)
        request = build_generated_request(case.binding, case.build_values(_view(case)))
        assert request is not None
        assert _jsonable(request.to_dict()) == expected_json  # type: ignore[attr-defined]


def test_search_and_status_extract_only_target_response_values() -> None:
    search = _case("search_deliveries")
    search_values = search.extract(_orders_response(), _view(search))
    assert search_values == {
        "search_delivery_id": SEARCH_DELIVERY_ID,
        "search_delivery_phone": PHONE,
        "search_delivery_revision": 17,
        "search_delivery_customer_id": CUSTOMER_ID,
    }

    status = _case("get_deliveries_by_delivery_date_and_status")
    status_values = status.extract(
        _orders_response(
            order_id=STATUS_DELIVERY_ID,
            phone=STATUS_PHONE,
            revision=19,
        ),
        _view(status),
    )
    assert status_values == {
        "status_delivery_id": STATUS_DELIVERY_ID,
        "status_delivery_phone": STATUS_PHONE,
        "status_delivery_revision": 19,
        "status_delivery_customer_id": CUSTOMER_ID,
    }

    foreign = _orders_response(organization_id=OTHER_ORGANIZATION_ID)
    assert search.extract(foreign, _view(search)) == {
        "search_delivery_revision": 17
    }


def test_empty_order_providers_publish_only_non_negative_response_revision() -> None:
    search = _case("search_deliveries")
    assert search.extract(_empty_orders_response(revision=7), _view(search)) == {
        "search_delivery_revision": 7
    }
    assert search.extract(_empty_orders_response(revision=-1), _view(search)) == {}

    status = _case("get_deliveries_by_delivery_date_and_status")
    assert status.extract(_empty_orders_response(revision=9), _view(status)) == {
        "status_delivery_revision": 9
    }
    assert status.extract(_empty_orders_response(revision=-1), _view(status)) == {}


def test_provider_skips_incomplete_order_before_selecting_one_complete_order() -> None:
    incomplete = _model(
        "order_info",
        "OrderInfo",
        id=UUID("77777777-7777-4777-8777-777777777777"),
        order=None,
        organization_id=ORGANIZATION_ID,
    )
    complete_response = _orders_response()
    complete_group = complete_response.orders_by_organizations[0]  # type: ignore[attr-defined]
    group = _model(
        "orders_by_organization",
        "OrdersByOrganization",
        orders=[incomplete, *complete_group.orders],
        organization_id=ORGANIZATION_ID,
    )
    response = _model(
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        max_revision=17,
        orders_by_organizations=[group],
    )

    extracted = _case("search_deliveries").extract(
        response,
        _view(_case("search_deliveries")),
    )

    assert extracted["search_delivery_id"] == SEARCH_DELIVERY_ID
    assert extracted["search_delivery_phone"] == PHONE


def test_delivery_provider_values_remain_hidden_in_context_repr() -> None:
    case = _case("search_deliveries")
    extracted = case.extract(_orders_response(), _view(case))
    context = ReadContext.seed(
        {
            "organization_id": ORGANIZATION_ID,
            "window_from_local": WINDOW_FROM,
            "window_to_local": WINDOW_TO,
        }
    )
    context.apply(case, extracted)
    hidden_view = context.view(case.provides)

    rendered = repr(context) + repr(hidden_view) + repr(case)
    for private_value in (PHONE, str(CUSTOMER_ID), str(SEARCH_DELIVERY_ID)):
        assert private_value not in rendered


def test_draft_provider_uses_only_top_level_target_organization_draft_id() -> None:
    case = _case("get_delivery_drafts_by_filter")
    draft = _model(
        "order_draft",
        "OrderDraft",
        id=DRAFT_ID,
        organization_id=ORGANIZATION_ID,
    )
    response = _model(
        "filter_drafts_response",
        "FilterDraftsResponse",
        drafts=[draft],
    )
    assert case.extract(response, _view(case)) == {"draft_id": DRAFT_ID}

    foreign = _model(
        "order_draft",
        "OrderDraft",
        id=DRAFT_ID,
        organization_id=OTHER_ORGANIZATION_ID,
    )
    foreign_response = _model(
        "filter_drafts_response",
        "FilterDraftsResponse",
        drafts=[foreign],
    )
    assert case.extract(foreign_response, _view(case)) == {}
    assert case.extract(_minimal_response(case.operation_id), _view(case)) == {}


def test_delivery_id_priority_and_missing_target_are_fixed() -> None:
    case = _case("get_deliveries_by_id")
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "orderIds": [str(SEARCH_DELIVERY_ID)],
        "organizationId": str(ORGANIZATION_ID),
    }

    status_only = ContextView(
        {
            "organization_id": ORGANIZATION_ID,
            "status_delivery_id": STATUS_DELIVERY_ID,
        }
    )
    request = build_generated_request(case.binding, case.build_values(status_only))
    assert request is not None
    assert _jsonable(request.to_dict())["orderIds"] == [str(STATUS_DELIVERY_ID)]  # type: ignore[index,attr-defined]

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(ContextView({"organization_id": ORGANIZATION_ID}))
    assert missing.value.code is NoLiveTargetCode.DELIVERY


@pytest.mark.parametrize(
    "operation_id",
    [
        "get_deliveries_by_delivery_date_and_phone",
        "get_delivery_history_by_delivery_date_and_phone",
    ],
)
def test_phone_queries_use_search_priority_and_one_bounded_row(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "deliveryDateFrom": WINDOW_FROM,
        "deliveryDateTo": WINDOW_TO,
        "organizationIds": [str(ORGANIZATION_ID)],
        "phone": PHONE,
        "rowsCount": 1,
    }

    status_only = ContextView(
        {
            "organization_id": ORGANIZATION_ID,
            "window_from_local": WINDOW_FROM,
            "window_to_local": WINDOW_TO,
            "status_delivery_phone": STATUS_PHONE,
        }
    )
    status_request = build_generated_request(
        case.binding,
        case.build_values(status_only),
    )
    assert status_request is not None
    assert _jsonable(status_request.to_dict())["phone"] == STATUS_PHONE  # type: ignore[index,attr-defined]

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(
            ContextView(
                {
                    "organization_id": ORGANIZATION_ID,
                    "window_from_local": WINDOW_FROM,
                    "window_to_local": WINDOW_TO,
                }
            )
        )
    assert missing.value.code is NoLiveTargetCode.DELIVERY_PHONE


def test_revision_query_uses_search_priority_and_rejects_negative_values() -> None:
    case = _case("get_deliveries_by_revision")
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "organizationIds": [str(ORGANIZATION_ID)],
        "startRevision": 17,
    }

    status_only = ContextView(
        {
            "organization_id": ORGANIZATION_ID,
            "status_delivery_revision": 19,
        }
    )
    status_request = build_generated_request(
        case.binding,
        case.build_values(status_only),
    )
    assert status_request is not None
    assert _jsonable(status_request.to_dict())["startRevision"] == 19  # type: ignore[index,attr-defined]

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(
            ContextView(
                {
                    "organization_id": ORGANIZATION_ID,
                    "search_delivery_revision": -1,
                    "status_delivery_revision": -2,
                }
            )
        )
    assert missing.value.code is NoLiveTargetCode.DELIVERY_REVISION


def test_draft_by_id_uses_only_response_derived_draft_target() -> None:
    case = _case("get_delivery_draft_by_id")
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "orderId": str(DRAFT_ID),
        "organizationId": str(ORGANIZATION_ID),
    }

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(ContextView({"organization_id": ORGANIZATION_ID}))
    assert missing.value.code is NoLiveTargetCode.DRAFT
