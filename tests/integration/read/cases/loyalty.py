"""Guarded loyalty, customer, coupon, SMS, and report read cases."""

from __future__ import annotations

import importlib
from collections.abc import Callable, Mapping
from typing import Any, cast
from uuid import UUID

from tools.openapi_pipeline.live.read_case import (
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
)


def _binding(
    operation_id: str,
    api_module: str,
    api_class: str,
    request_module: str,
    request_class: str,
    request_keyword: str,
) -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module=f"iikocloud_client.api.{api_module}",
        api_class=api_class,
        method_name=f"{operation_id}_with_http_info",
        request_module=f"iikocloud_client.models.{request_module}",
        request_class=request_class,
        request_keyword=request_keyword,
    )


def _generated_class(module_name: str, class_name: str) -> type[object] | None:
    try:
        module = importlib.import_module(f"iikocloud_client.models.{module_name}")
        candidate = getattr(module, class_name, None)
    except Exception:
        return None
    if not isinstance(candidate, type):
        return None
    return candidate


def _is_exact_model(response: object, module_name: str, class_name: str) -> bool:
    model = _generated_class(module_name, class_name)
    return model is not None and type(response) is model


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        if not _is_exact_model(response, module_name, class_name):
            raise ReadAssertionFailure()

    return validate


def _empty_extract(_response: object, _view: ContextView) -> Mapping[str, object]:
    return {}


def _organization_id(view: ContextView) -> Mapping[str, object]:
    return {"organization_id": view["organization_id"]}


def _extract_coupon_series(
    response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    try:
        entries = response.series_with_not_activated_coupons  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(entries) is not list:
        return {}
    for entry in entries:
        try:
            series = entry.number
        except Exception:
            continue
        if type(series) is str and series:
            return {"coupon_series": series}
    return {}


def _required_text(
    view: ContextView,
    key: str,
    code: NoLiveTargetCode,
) -> str:
    candidate = view.get(key)
    if type(candidate) is str and candidate:
        return candidate
    raise NoLiveTarget(code)


def _required_uuid(
    view: ContextView,
    key: str,
    code: NoLiveTargetCode,
) -> UUID:
    candidate = view.get(key)
    if type(candidate) is UUID:
        return candidate
    raise NoLiveTarget(code)


def _build_non_activated_coupons(view: ContextView) -> Mapping[str, object]:
    series = _required_text(
        view,
        "coupon_series",
        NoLiveTargetCode.COUPON_SERIES,
    )
    return {
        "organization_id": view["organization_id"],
        "page": 0,
        "page_size": 1,
        "series": series,
    }


def _extract_coupon_number(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    series = view.get("coupon_series")
    if type(series) is not str or not series:
        return {}
    try:
        coupons = response.not_activated_coupon  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(coupons) is not list:
        return {}
    for coupon in coupons:
        try:
            number = coupon.number
            series_name = coupon.series_name
        except Exception:
            continue
        if type(number) is not str or not number:
            continue
        if (
            type(series_name) is str
            and series_name
            and series_name != series
        ):
            continue
        if series_name is not None and type(series_name) is not str:
            continue
        return {"coupon_number": number}
    return {}


def _build_coupon_info(view: ContextView) -> Mapping[str, object]:
    number = _required_text(view, "coupon_number", NoLiveTargetCode.COUPON)
    values: dict[str, object] = {
        "number": number,
        "organization_id": view["organization_id"],
    }
    series = view.get("coupon_series")
    if type(series) is str and series:
        values["series"] = series
    return values


def _validate_coupon_info(response: object, view: ContextView) -> None:
    if not _is_exact_model(response, "coupon_info_response", "CouponInfoResponse"):
        raise ReadAssertionFailure()
    number = view.get("coupon_number")
    series = view.get("coupon_series")
    if type(number) is not str or not number:
        raise ReadAssertionFailure()
    coupons: object = None
    coupons_unavailable = False
    try:
        coupons = response.coupon_info  # type: ignore[attr-defined]
    except Exception:
        coupons_unavailable = True
    if coupons_unavailable:
        raise ReadAssertionFailure()
    if coupons is None:
        return
    if type(coupons) is not list:
        raise ReadAssertionFailure()
    for coupon in coupons:
        coupon_number: object = None
        coupon_series: object = None
        fields_unavailable = False
        try:
            coupon_number = coupon.number
            coupon_series = coupon.series_name
        except Exception:
            fields_unavailable = True
        if (
            fields_unavailable
            or coupon_number != number
            or (
                type(series) is str
                and series
                and coupon_series is not None
                and coupon_series != series
            )
        ):
            raise ReadAssertionFailure()


def _build_sms_status(_view: ContextView) -> Mapping[str, object]:
    raise NoLiveTarget(NoLiveTargetCode.SMS)


def _customer_target(view: ContextView) -> UUID:
    for key in (
        "search_delivery_customer_id",
        "status_delivery_customer_id",
        "table_order_customer_id",
    ):
        candidate = view.get(key)
        if type(candidate) is UUID:
            return candidate
    raise NoLiveTarget(NoLiveTargetCode.CUSTOMER)


def _build_customer_info(view: ContextView) -> Mapping[str, object]:
    customer_id = _customer_target(view)
    return {
        "id": str(customer_id),
        "organization_id": view["organization_id"],
        "type": "id",
    }


def _response_customer_id(response: object) -> UUID | None:
    try:
        customer_id = response.id  # type: ignore[attr-defined]
    except Exception:
        return None
    if type(customer_id) is UUID:
        return customer_id
    return None


def _validate_customer(response: object, view: ContextView) -> None:
    if not _is_exact_model(
        response,
        "get_customer_info_response",
        "GetCustomerInfoResponse",
    ):
        raise ReadAssertionFailure()
    requested: UUID | None = None
    try:
        requested = _customer_target(view)
    except NoLiveTarget:
        requested = None
    if requested is None or _response_customer_id(response) != requested:
        raise ReadAssertionFailure()


def _extract_customer(response: object, view: ContextView) -> Mapping[str, object]:
    try:
        requested = _customer_target(view)
    except NoLiveTarget:
        return {}
    customer_id = _response_customer_id(response)
    if customer_id != requested:
        return {}
    return {"customer_id": customer_id}


def _customer_id(view: ContextView) -> UUID:
    return _required_uuid(view, "customer_id", NoLiveTargetCode.CUSTOMER)


def _build_counters(view: ContextView) -> Mapping[str, object]:
    # The endpoint rejects integer enums and requests without metrics/periods;
    # only the live-verified string values below are accepted (2026-07-23).
    return {
        "guest_ids": [_customer_id(view)],
        "organization_id": view["organization_id"],
        "metrics": ["OrdersCount", "OrdersSum"],
        "periods": ["AllTime"],
    }


def _build_transactions_by_date(view: ContextView) -> Mapping[str, object]:
    return {
        "customer_id": _customer_id(view),
        "date_from": view["period_from_yyyy_mm_dd"],
        "date_to": view["period_to_yyyy_mm_dd"],
        "organization_id": view["organization_id"],
        "page_number": 0,
        "page_size": 1,
    }


def _extract_transaction_revision(
    response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    try:
        transactions = response.transactions  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(transactions) is not list:
        return {}
    for transaction in transactions:
        try:
            revision = transaction.revision
        except Exception:
            continue
        if type(revision) is int and revision >= 0:
            return {"customer_transaction_revision": revision}
    return {}


def _build_transactions_by_revision(view: ContextView) -> Mapping[str, object]:
    revision = view.get("customer_transaction_revision")
    if type(revision) is not int or revision < 0:
        revision = 0
    return {
        "customer_id": _customer_id(view),
        "organization_id": view["organization_id"],
        "page_size": 1,
        "revision": revision,
    }


def _product_target(view: ContextView) -> tuple[UUID, UUID | None, int | float]:
    product_id = view.get("product_id")
    product_price = view.get("product_price")
    prices = view.get("nomenclature_prices")
    if type(product_price) not in (int, float):
        raise NoLiveTarget(NoLiveTargetCode.PRODUCT)
    checked_price = cast(int | float, product_price)
    if type(product_id) is not UUID or checked_price < 0 or type(prices) is not tuple:
        raise NoLiveTarget(NoLiveTargetCode.PRODUCT)
    for entry in prices:
        if type(entry) is not tuple or len(entry) != 3:
            continue
        candidate_id, size_id, price = entry
        if (
            candidate_id == product_id
            and type(candidate_id) is UUID
            and (size_id is None or type(size_id) is UUID)
            and type(price) in (int, float)
            and type(price) is type(checked_price)
            and price == checked_price
        ):
            return product_id, size_id, checked_price
    raise NoLiveTarget(NoLiveTargetCode.PRODUCT)


def _delivery_phone(view: ContextView) -> str:
    for key in ("search_delivery_phone", "status_delivery_phone"):
        candidate = view.get(key)
        if (
            type(candidate) is str
            and candidate.startswith("+")
            and 8 <= len(candidate) <= 40
        ):
            return candidate
    raise NoLiveTarget(NoLiveTargetCode.DELIVERY_PHONE)


def _build_calculation(view: ContextView) -> Mapping[str, object]:
    product_id, product_size_id, price = _product_target(view)
    phone = _delivery_phone(view)
    product_model = _generated_class(
        "delivery_order_create_product_item",
        "DeliveryOrderCreateProductItem",
    )
    order_model = _generated_class(
        "delivery_order_create_payload",
        "DeliveryOrderCreatePayload",
    )
    if product_model is None or order_model is None:
        raise RuntimeError("generated loyalty order models unavailable")
    product_values: dict[str, object] = {
        "amount": 1,
        "price": price,
        "product_id": product_id,
        "type": "Product",
    }
    if product_size_id is not None:
        product_values["product_size_id"] = product_size_id
    product = cast(Any, product_model).model_validate(product_values)
    order = cast(Any, order_model).model_validate(
        {
            "items": [product],
            "payments": [],
            "phone": phone,
        }
    )
    return {
        "available_payment_marketing_campaign_ids": [],
        "is_loyalty_trace_enabled": False,
        "order": order,
        "organization_id": view["organization_id"],
    }


def _case(
    operation_id: str,
    api_module: str,
    api_class: str,
    response_module: str,
    response_class: str,
    request_module: str,
    request_class: str,
    request_keyword: str,
    *,
    depends_on: tuple[str, ...],
    requires: tuple[str, ...],
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
    build_values: Callable[[ContextView], Mapping[str, object]],
    validate_response: Callable[[object, ContextView], None] | None = None,
    extract: Callable[
        [object, ContextView], Mapping[str, object]
    ] = _empty_extract,
) -> ReadCase:
    validator = validate_response or _typed_validator(response_module, response_class)
    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=depends_on,
        requires=requires,
        provides=provides,
        allowed_no_target_codes=allowed_no_target_codes,
        binding=_binding(
            operation_id,
            api_module,
            api_class,
            request_module,
            request_class,
            request_keyword,
        ),
        build_values=build_values,
        validate_response=validator,
        extract=extract,
    )


LOYALTY_CASES = (
    _case(
        "check_sms_sending_possibility",
        "messages_api",
        "MessagesApi",
        "sms_sending_possibility_response",
        "SmsSendingPossibilityResponse",
        "sms_sending_possibility_request",
        "SmsSendingPossibilityRequest",
        "sms_sending_possibility_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_organization_id,
    ),
    _case(
        "check_sms_status",
        "messages_api",
        "MessagesApi",
        "check_sms_status_response",
        "CheckSmsStatusResponse",
        "check_sms_status_request",
        "CheckSmsStatusRequest",
        "check_sms_status_request",
        depends_on=("check_sms_sending_possibility",),
        requires=("organization_id",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.SMS}),
        build_values=_build_sms_status,
    ),
    _case(
        "get_coupon_series",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "series_with_not_activated_coupons_response",
        "SeriesWithNotActivatedCouponsResponse",
        "series_with_not_activated_coupons_request",
        "SeriesWithNotActivatedCouponsRequest",
        "series_with_not_activated_coupons_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        provides=("coupon_series",),
        build_values=_organization_id,
        extract=_extract_coupon_series,
    ),
    _case(
        "get_non_activated_coupons_by_series",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "not_activated_coupon_response",
        "NotActivatedCouponResponse",
        "not_activated_coupon_request",
        "NotActivatedCouponRequest",
        "not_activated_coupon_request",
        depends_on=("get_coupon_series",),
        requires=("organization_id", "coupon_series"),
        provides=("coupon_number",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.COUPON_SERIES}),
        build_values=_build_non_activated_coupons,
        extract=_extract_coupon_number,
    ),
    _case(
        "get_coupon_info",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "coupon_info_response",
        "CouponInfoResponse",
        "coupon_info_request",
        "CouponInfoRequest",
        "coupon_info_request",
        depends_on=("get_non_activated_coupons_by_series",),
        requires=("organization_id", "coupon_number", "coupon_series"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.COUPON}),
        build_values=_build_coupon_info,
        validate_response=_validate_coupon_info,
    ),
    _case(
        "get_customer_categories",
        "customer_categories_api",
        "CustomerCategoriesApi",
        "get_categories_response",
        "GetCategoriesResponse",
        "get_categories_request",
        "GetCategoriesRequest",
        "get_categories_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_organization_id,
    ),
    _case(
        "get_loyalty_manual_conditions",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "get_manual_conditions_response",
        "GetManualConditionsResponse",
        "get_by_organization_id_request",
        "GetByOrganizationIdRequest",
        "get_by_organization_id_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_organization_id,
    ),
    _case(
        "get_loyalty_programs",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "get_programs_response",
        "GetProgramsResponse",
        "get_programs_request",
        "GetProgramsRequest",
        "get_programs_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_organization_id,
    ),
    _case(
        "get_customer_info",
        "customers_api",
        "CustomersApi",
        "get_customer_info_response",
        "GetCustomerInfoResponse",
        "get_customer_info_by_id_request",
        "GetCustomerInfoByIdRequest",
        "get_customer_info_request",
        depends_on=(
            "search_deliveries",
            "get_deliveries_by_delivery_date_and_status",
            "get_table_orders_by_table",
        ),
        requires=(
            "organization_id",
            "search_delivery_customer_id",
            "status_delivery_customer_id",
            "table_order_customer_id",
        ),
        provides=("customer_id",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.CUSTOMER}),
        build_values=_build_customer_info,
        validate_response=_validate_customer,
        extract=_extract_customer,
    ),
    _case(
        "get_loyalty_counters",
        "customers_api",
        "CustomersApi",
        "get_counters_response",
        "GetCountersResponse",
        "get_counters_request",
        "GetCountersRequest",
        "get_counters_request",
        depends_on=("get_customer_info",),
        requires=("organization_id", "customer_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.CUSTOMER}),
        build_values=_build_counters,
    ),
    _case(
        "get_customer_transactions_by_date",
        "report_api",
        "ReportApi",
        "get_transactions_report_by_period_response",
        "GetTransactionsReportByPeriodResponse",
        "get_transactions_report_by_period_request",
        "GetTransactionsReportByPeriodRequest",
        "get_transactions_report_by_period_request",
        depends_on=("get_customer_info",),
        requires=(
            "organization_id",
            "customer_id",
            "period_from_yyyy_mm_dd",
            "period_to_yyyy_mm_dd",
        ),
        provides=("customer_transaction_revision",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.CUSTOMER}),
        build_values=_build_transactions_by_date,
        extract=_extract_transaction_revision,
    ),
    _case(
        "get_customer_transactions_by_revision",
        "report_api",
        "ReportApi",
        "get_transactions_report_by_revision_response",
        "GetTransactionsReportByRevisionResponse",
        "get_transactions_report_by_revision_request",
        "GetTransactionsReportByRevisionRequest",
        "get_transactions_report_by_revision_request",
        depends_on=("get_customer_transactions_by_date",),
        requires=("organization_id", "customer_id", "customer_transaction_revision"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.CUSTOMER}),
        build_values=_build_transactions_by_revision,
    ),
    _case(
        "calculate_loyalty_checkin",
        "discounts_and_promotions_api",
        "DiscountsAndPromotionsApi",
        "calculate_checkin_response",
        "CalculateCheckinResponse",
        "calculate_checkin_request",
        "CalculateCheckinRequest",
        "calculate_checkin_request",
        depends_on=(
            "get_nomenclature",
            "search_deliveries",
            "get_deliveries_by_delivery_date_and_status",
        ),
        requires=(
            "organization_id",
            "product_id",
            "product_price",
            "nomenclature_prices",
            "search_delivery_phone",
            "status_delivery_phone",
        ),
        allowed_no_target_codes=frozenset(
            {NoLiveTargetCode.PRODUCT, NoLiveTargetCode.DELIVERY_PHONE}
        ),
        build_values=_build_calculation,
    ),
)

__all__ = ["LOYALTY_CASES"]
