from __future__ import annotations

from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.deliveries import DELIVERY_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.loyalty import LOYALTY_CASES
from tests.integration.read.cases.menu import MENU_CASES
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
from tools.openapi_pipeline.live.read_report import (
    ReadOutcome,
    ReadReport,
    ReadStatus,
)

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
PRODUCT_ID = UUID("22222222-2222-4222-8222-222222222222")
PRODUCT_SIZE_ID = UUID("33333333-3333-4333-8333-333333333333")
SEARCH_CUSTOMER_ID = UUID("44444444-4444-4444-8444-444444444444")
STATUS_CUSTOMER_ID = UUID("55555555-5555-4555-8555-555555555555")
TABLE_CUSTOMER_ID = UUID("66666666-6666-4666-8666-666666666666")
TRANSACTION_ID = UUID("77777777-7777-4777-8777-777777777777")
SMS_ID = UUID("88888888-8888-4888-8888-888888888888")
PRODUCT_PRICE = 199
SEARCH_PHONE = "+70000000001"
STATUS_PHONE = "+70000000002"
COUPON_SERIES = "private-series-marker"
COUPON_NUMBER = "private-coupon-marker"
OTHER_COUPON_SERIES = "other-series-marker"
PRIVATE_NAME = "private-customer-name-marker"
PRIVATE_EMAIL = "private-customer@example.invalid"
PRIVATE_CARD = "private-card-marker"
PERIOD_FROM = "2026-01-01"
PERIOD_TO = "2026-01-02"

PRIVATE_MARKERS = (
    str(ORGANIZATION_ID),
    str(PRODUCT_ID),
    str(PRODUCT_SIZE_ID),
    str(SEARCH_CUSTOMER_ID),
    str(STATUS_CUSTOMER_ID),
    str(TABLE_CUSTOMER_ID),
    str(TRANSACTION_ID),
    str(SMS_ID),
    SEARCH_PHONE,
    STATUS_PHONE,
    COUPON_SERIES,
    COUPON_NUMBER,
    PRIVATE_NAME,
    PRIVATE_EMAIL,
    PRIVATE_CARD,
)

LOYALTY_IDS = {
    "calculate_loyalty_checkin",
    "check_sms_sending_possibility",
    "check_sms_status",
    "get_coupon_info",
    "get_coupon_series",
    "get_customer_categories",
    "get_customer_info",
    "get_customer_transactions_by_date",
    "get_customer_transactions_by_revision",
    "get_loyalty_counters",
    "get_loyalty_manual_conditions",
    "get_loyalty_programs",
    "get_non_activated_coupons_by_series",
}

RESPONSE_MODELS = {
    "calculate_loyalty_checkin": (
        "calculate_checkin_response",
        "CalculateCheckinResponse",
    ),
    "check_sms_sending_possibility": (
        "sms_sending_possibility_response",
        "SmsSendingPossibilityResponse",
    ),
    "check_sms_status": ("check_sms_status_response", "CheckSmsStatusResponse"),
    "get_coupon_info": ("coupon_info_response", "CouponInfoResponse"),
    "get_coupon_series": (
        "series_with_not_activated_coupons_response",
        "SeriesWithNotActivatedCouponsResponse",
    ),
    "get_customer_categories": ("get_categories_response", "GetCategoriesResponse"),
    "get_customer_info": (
        "get_customer_info_response",
        "GetCustomerInfoResponse",
    ),
    "get_customer_transactions_by_date": (
        "get_transactions_report_by_period_response",
        "GetTransactionsReportByPeriodResponse",
    ),
    "get_customer_transactions_by_revision": (
        "get_transactions_report_by_revision_response",
        "GetTransactionsReportByRevisionResponse",
    ),
    "get_loyalty_counters": ("get_counters_response", "GetCountersResponse"),
    "get_loyalty_manual_conditions": (
        "get_manual_conditions_response",
        "GetManualConditionsResponse",
    ),
    "get_loyalty_programs": ("get_programs_response", "GetProgramsResponse"),
    "get_non_activated_coupons_by_series": (
        "not_activated_coupon_response",
        "NotActivatedCouponResponse",
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
    return next(case for case in LOYALTY_CASES if case.operation_id == operation_id)


def _view(
    case: ReadCase,
    *,
    omit: frozenset[str] = frozenset(),
    **changes: object,
) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "product_id": PRODUCT_ID,
        "product_price": PRODUCT_PRICE,
        "nomenclature_prices": ((PRODUCT_ID, PRODUCT_SIZE_ID, PRODUCT_PRICE),),
        "search_delivery_phone": SEARCH_PHONE,
        "status_delivery_phone": STATUS_PHONE,
        "search_delivery_customer_id": SEARCH_CUSTOMER_ID,
        "status_delivery_customer_id": STATUS_CUSTOMER_ID,
        "table_order_customer_id": TABLE_CUSTOMER_ID,
        "coupon_series": COUPON_SERIES,
        "coupon_number": COUPON_NUMBER,
        "customer_id": SEARCH_CUSTOMER_ID,
        "customer_transaction_revision": 17,
        "period_from_yyyy_mm_dd": PERIOD_FROM,
        "period_to_yyyy_mm_dd": PERIOD_TO,
    }
    values.update(changes)
    return ContextView(
        {
            key: values[key]
            for key in case.requires
            if key in values and key not in omit
        }
    )


def _series_response(*numbers: str | None) -> object:
    entries = [
        _model(
            "series_with_not_activated_coupons",
            "SeriesWithNotActivatedCoupons",
            number=number,
        )
        for number in numbers
    ]
    return _model(
        "series_with_not_activated_coupons_response",
        "SeriesWithNotActivatedCouponsResponse",
        series_with_not_activated_coupons=entries,
    )


def _non_activated_response(
    *items: tuple[str | None, str | None],
) -> object:
    coupons = [
        _model(
            "not_activated_coupon",
            "NotActivatedCoupon",
            number=number,
            series_name=series_name,
        )
        for number, series_name in items
    ]
    return _model(
        "not_activated_coupon_response",
        "NotActivatedCouponResponse",
        not_activated_coupon=coupons,
    )


def _coupon_info_response(
    *,
    number: str = COUPON_NUMBER,
    series_name: str = COUPON_SERIES,
) -> object:
    coupon = _model(
        "coupon_info",
        "CouponInfo",
        number=number,
        series_name=series_name,
    )
    return _model(
        "coupon_info_response",
        "CouponInfoResponse",
        coupon_info=[coupon],
    )


def _customer_response(customer_id: UUID | None = SEARCH_CUSTOMER_ID) -> object:
    return _model(
        "get_customer_info_response",
        "GetCustomerInfoResponse",
        cards=[PRIVATE_CARD],
        email=PRIVATE_EMAIL,
        id=customer_id,
        name=PRIVATE_NAME,
        phone=SEARCH_PHONE,
    )


def _date_response(*revisions: int) -> object:
    transactions = [
        _model(
            "transport_transactions_report_item",
            "TransportTransactionsReportItem",
            id=TRANSACTION_ID,
            revision=revision,
        )
        for revision in revisions
    ]
    return _model(
        "get_transactions_report_by_period_response",
        "GetTransactionsReportByPeriodResponse",
        transactions=transactions,
    )


def _minimal_response(operation_id: str) -> object:
    if operation_id == "get_coupon_series":
        return _series_response()
    if operation_id == "get_non_activated_coupons_by_series":
        return _non_activated_response()
    if operation_id == "get_coupon_info":
        return _model("coupon_info_response", "CouponInfoResponse", coupon_info=[])
    if operation_id == "get_customer_info":
        return _customer_response()
    if operation_id == "get_customer_transactions_by_date":
        return _date_response()
    if operation_id == "check_sms_status":
        return _model("check_sms_status_response", "CheckSmsStatusResponse", statuses=[])
    module_name, class_name = RESPONSE_MODELS[operation_id]
    values: dict[str, object] = {}
    if operation_id == "get_customer_transactions_by_revision":
        values["transactions"] = []
    return _model(module_name, class_name, **values)


def _request_json(case: ReadCase) -> object:
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    return _jsonable(request.to_dict())  # type: ignore[attr-defined]


def test_loyalty_registry_is_exact_and_builds_with_prior_cases() -> None:
    assert type(LOYALTY_CASES) is tuple
    assert {case.operation_id for case in LOYALTY_CASES} == LOYALTY_IDS
    assert len(LOYALTY_CASES) == len(LOYALTY_IDS)
    plan = ReadPlan.build(
        (
            *FOUNDATION_CASES,
            *MENU_CASES,
            *DELIVERY_CASES,
            *RESERVE_ORDER_CASES,
            *LOYALTY_CASES,
        )
    )
    assert set(plan.ordered_operation_ids) > LOYALTY_IDS


def test_loyalty_dependency_chain_and_provider_keys_are_exact() -> None:
    for operation_id in {
        "check_sms_sending_possibility",
        "get_coupon_series",
        "get_customer_categories",
        "get_loyalty_manual_conditions",
        "get_loyalty_programs",
    }:
        assert _case(operation_id).depends_on == ("get_organizations",)

    assert _case("get_coupon_series").provides == ("coupon_series",)
    assert _case("get_non_activated_coupons_by_series").depends_on == (
        "get_coupon_series",
    )
    assert _case("get_non_activated_coupons_by_series").provides == (
        "coupon_number",
    )
    assert _case("get_coupon_info").depends_on == (
        "get_non_activated_coupons_by_series",
    )
    assert _case("check_sms_status").depends_on == (
        "check_sms_sending_possibility",
    )
    assert _case("get_customer_info").depends_on == (
        "search_deliveries",
        "get_deliveries_by_delivery_date_and_status",
        "get_table_orders_by_table",
    )
    assert _case("get_customer_info").provides == ("customer_id",)
    assert _case("get_customer_transactions_by_date").provides == (
        "customer_transaction_revision",
    )
    assert _case("get_customer_transactions_by_revision").depends_on == (
        "get_customer_transactions_by_date",
    )


@pytest.mark.parametrize("operation_id", sorted(LOYALTY_IDS))
def test_bindings_resolve_and_validators_use_fixed_redacted_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id), _view(case))

    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": PRIVATE_NAME}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None
    for marker in PRIVATE_MARKERS:
        assert marker not in repr(raised.value)


def test_direct_coupon_customer_and_report_requests_are_exact() -> None:
    expected = {
        "check_sms_sending_possibility": {
            "organizationId": str(ORGANIZATION_ID)
        },
        "get_coupon_series": {"organizationId": str(ORGANIZATION_ID)},
        "get_customer_categories": {"organizationId": str(ORGANIZATION_ID)},
        "get_loyalty_manual_conditions": {
            "organizationId": str(ORGANIZATION_ID)
        },
        "get_loyalty_programs": {"organizationId": str(ORGANIZATION_ID)},
        "get_non_activated_coupons_by_series": {
            "organizationId": str(ORGANIZATION_ID),
            "page": 0,
            "pageSize": 1,
            "series": COUPON_SERIES,
        },
        "get_coupon_info": {
            "number": COUPON_NUMBER,
            "organizationId": str(ORGANIZATION_ID),
            "series": COUPON_SERIES,
        },
        "get_customer_info": {
            "id": str(SEARCH_CUSTOMER_ID),
            "organizationId": str(ORGANIZATION_ID),
            "type": "id",
        },
        "get_loyalty_counters": {
            "guestIds": [str(SEARCH_CUSTOMER_ID)],
            "organizationId": str(ORGANIZATION_ID),
        },
        "get_customer_transactions_by_date": {
            "customerId": str(SEARCH_CUSTOMER_ID),
            "dateFrom": PERIOD_FROM,
            "dateTo": PERIOD_TO,
            "organizationId": str(ORGANIZATION_ID),
            "pageNumber": 0,
            "pageSize": 1,
        },
        "get_customer_transactions_by_revision": {
            "customerId": str(SEARCH_CUSTOMER_ID),
            "organizationId": str(ORGANIZATION_ID),
            "pageSize": 1,
            "revision": 17,
        },
    }
    assert {
        operation_id: _request_json(_case(operation_id))
        for operation_id in expected
    } == expected


def test_customer_info_uses_concrete_id_discriminator_and_priority() -> None:
    case = _case("get_customer_info")
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert type(request).__name__ == "GetCustomerInfoByIdRequest"

    status_view = _view(case, omit=frozenset({"search_delivery_customer_id"}))
    status_request = build_generated_request(case.binding, case.build_values(status_view))
    assert status_request is not None
    assert status_request.to_dict()["id"] == str(STATUS_CUSTOMER_ID)  # type: ignore[attr-defined]

    table_view = _view(
        case,
        omit=frozenset(
            {"search_delivery_customer_id", "status_delivery_customer_id"}
        ),
    )
    table_request = build_generated_request(case.binding, case.build_values(table_view))
    assert table_request is not None
    assert table_request.to_dict()["id"] == str(TABLE_CUSTOMER_ID)  # type: ignore[attr-defined]


def test_coupon_chain_uses_explicit_series_and_coupon_fields_only() -> None:
    series_case = _case("get_coupon_series")
    assert series_case.extract(
        _series_response(None, "", COUPON_SERIES),
        _view(series_case),
    ) == {"coupon_series": COUPON_SERIES}
    assert series_case.extract(_series_response(), _view(series_case)) == {}

    coupon_case = _case("get_non_activated_coupons_by_series")
    response = _non_activated_response(
        ("foreign-coupon", OTHER_COUPON_SERIES),
        (None, COUPON_SERIES),
        (COUPON_NUMBER, COUPON_SERIES),
    )
    assert coupon_case.extract(response, _view(coupon_case)) == {
        "coupon_number": COUPON_NUMBER
    }
    assert coupon_case.extract(_non_activated_response(), _view(coupon_case)) == {}


def test_coupon_info_validator_rejects_unlinked_returned_coupon() -> None:
    case = _case("get_coupon_info")
    case.validate_response(_coupon_info_response(), _view(case))
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(
            _coupon_info_response(number="other-coupon"),
            _view(case),
        )


def test_customer_response_is_linked_and_only_id_is_published() -> None:
    case = _case("get_customer_info")
    response = _customer_response()
    case.validate_response(response, _view(case))
    assert case.extract(response, _view(case)) == {"customer_id": SEARCH_CUSTOMER_ID}

    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response(_customer_response(STATUS_CUSTOMER_ID), _view(case))
    assert raised.value.__context__ is None
    for marker in PRIVATE_MARKERS:
        assert marker not in repr(raised.value)


def test_date_report_publishes_first_non_negative_revision() -> None:
    case = _case("get_customer_transactions_by_date")
    assert case.extract(_date_response(-1, 23), _view(case)) == {
        "customer_transaction_revision": 23
    }
    assert case.extract(_date_response(), _view(case)) == {}

    revision = _case("get_customer_transactions_by_revision")
    zero_view = _view(revision, omit=frozenset({"customer_transaction_revision"}))
    request = build_generated_request(revision.binding, revision.build_values(zero_view))
    assert request is not None
    assert request.to_dict()["revision"] == 0  # type: ignore[attr-defined]


def test_calculation_request_is_one_exact_non_mutating_product_order() -> None:
    case = _case("calculate_loyalty_checkin")
    assert _request_json(case) == {
        "availablePaymentMarketingCampaignIds": [],
        "isLoyaltyTraceEnabled": False,
        "order": {
            "items": [
                {
                    "amount": 1,
                    "price": PRODUCT_PRICE,
                    "productId": str(PRODUCT_ID),
                    "productSizeId": str(PRODUCT_SIZE_ID),
                    "type": "Product",
                }
            ],
            "payments": [],
            "phone": SEARCH_PHONE,
        },
        "organizationId": str(ORGANIZATION_ID),
    }

    status_view = _view(case, omit=frozenset({"search_delivery_phone"}))
    request = build_generated_request(case.binding, case.build_values(status_view))
    assert request is not None
    assert request.to_dict()["order"]["phone"] == STATUS_PHONE  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    ("operation_id", "missing_keys", "expected_code"),
    [
        ("check_sms_status", frozenset(), NoLiveTargetCode.SMS),
        (
            "get_non_activated_coupons_by_series",
            frozenset({"coupon_series"}),
            NoLiveTargetCode.COUPON_SERIES,
        ),
        (
            "get_coupon_info",
            frozenset({"coupon_number"}),
            NoLiveTargetCode.COUPON,
        ),
        (
            "get_customer_info",
            frozenset(
                {
                    "search_delivery_customer_id",
                    "status_delivery_customer_id",
                    "table_order_customer_id",
                }
            ),
            NoLiveTargetCode.CUSTOMER,
        ),
        (
            "get_loyalty_counters",
            frozenset({"customer_id"}),
            NoLiveTargetCode.CUSTOMER,
        ),
        (
            "get_customer_transactions_by_date",
            frozenset({"customer_id"}),
            NoLiveTargetCode.CUSTOMER,
        ),
        (
            "get_customer_transactions_by_revision",
            frozenset({"customer_id"}),
            NoLiveTargetCode.CUSTOMER,
        ),
        (
            "calculate_loyalty_checkin",
            frozenset({"product_id"}),
            NoLiveTargetCode.PRODUCT,
        ),
        (
            "calculate_loyalty_checkin",
            frozenset({"search_delivery_phone", "status_delivery_phone"}),
            NoLiveTargetCode.DELIVERY_PHONE,
        ),
    ],
)
def test_missing_targets_fail_before_request_construction(
    operation_id: str,
    missing_keys: frozenset[str],
    expected_code: NoLiveTargetCode,
) -> None:
    case = _case(operation_id)
    with pytest.raises(NoLiveTarget) as raised:
        case.build_values(_view(case, omit=missing_keys))
    assert raised.value.code is expected_code
    assert expected_code in case.allowed_no_target_codes
    assert raised.value.__context__ is None
    for marker in PRIVATE_MARKERS:
        assert marker not in repr(raised.value)


@pytest.mark.parametrize(
    "missing_key",
    ["product_price", "nomenclature_prices"],
)
def test_incomplete_product_context_is_rejected(
    missing_key: str,
) -> None:
    case = _case("calculate_loyalty_checkin")
    with pytest.raises(NoLiveTarget) as raised:
        case.build_values(_view(case, omit=frozenset({missing_key})))
    assert raised.value.code is NoLiveTargetCode.PRODUCT


def test_hidden_loyalty_values_never_enter_safe_renderings() -> None:
    context = ReadContext.seed({"organization_id": ORGANIZATION_ID})
    for operation_id, extracted in (
        ("get_coupon_series", {"coupon_series": COUPON_SERIES}),
        ("get_non_activated_coupons_by_series", {"coupon_number": COUPON_NUMBER}),
        ("get_customer_info", {"customer_id": SEARCH_CUSTOMER_ID}),
        (
            "get_customer_transactions_by_date",
            {"customer_transaction_revision": 17},
        ),
    ):
        context.apply(_case(operation_id), extracted)

    outcome = ReadOutcome(
        operation_id="get_customer_info",
        method="POST",
        path="/api/1/loyalty/iiko/customer/info",
        status=ReadStatus.PASSED,
        reason=None,
        http_status=200,
        duration_ms=1,
    )
    report = ReadReport(
        version=1,
        run_id="20260101T000000Z-01234567",
        profile_fingerprint="0" * 64,
        effective_schema_sha256="1" * 64,
        generated_tree_sha256="2" * 64,
        live_contracts_sha256="3" * 64,
        registry_sha256="4" * 64,
        started_at="2026-01-01T00:00:00Z",
        finished_at="2026-01-01T00:00:01Z",
        completed=True,
        outcomes=(outcome,),
        counts={"passed": 1, "no_live_target": 0, "failed": 0, "aborted": 0},
    )
    rendered = repr(
        (
            context,
            context.view(("customer_id", "coupon_number")),
            outcome,
            outcome.to_json(),
            report,
            report.to_json(),
        )
    )
    for marker in PRIVATE_MARKERS:
        assert marker not in rendered
