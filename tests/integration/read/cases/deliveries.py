"""Guarded read cases for delivery retrieval, restrictions, and drafts."""

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


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        model = _generated_class(module_name, class_name)
        if model is None or type(response) is not model:
            raise ReadAssertionFailure()

    return validate


def _empty_extract(_response: object, _view: ContextView) -> Mapping[str, object]:
    return {}


def _build_search(view: ContextView) -> Mapping[str, object]:
    return {
        "delivery_date_from": view["window_from_local"],
        "delivery_date_to": view["window_to_local"],
        "organization_ids": [view["organization_id"]],
        "rows_count": 1,
        "sort_direction": "Ascending",
        "sort_property": "CompleteBefore",
    }


def _build_status(view: ContextView) -> Mapping[str, object]:
    return {
        "delivery_date_from": view["window_from_local"],
        "delivery_date_to": view["window_to_local"],
        "organization_ids": [view["organization_id"]],
    }


def _target_orders(response: object, organization_id: UUID) -> tuple[object, ...]:
    try:
        groups = response.orders_by_organizations  # type: ignore[attr-defined]
    except Exception:
        return ()
    if type(groups) is not list:
        return ()
    orders: list[object] = []
    for group in groups:
        try:
            candidate_organization_id = group.organization_id
            candidate_orders = group.orders
        except Exception:
            continue
        if (
            candidate_organization_id != organization_id
            or type(candidate_orders) is not list
        ):
            continue
        orders.extend(candidate_orders)
    return tuple(orders)


def _regular_customer_id(customer: object) -> UUID | None:
    regular_customer = _generated_class(
        "delivery_order_response_regular_customer",
        "DeliveryOrderResponseRegularCustomer",
    )
    if regular_customer is None or type(customer) is not regular_customer:
        return None
    try:
        customer_id = customer.id  # type: ignore[attr-defined]
    except Exception:
        return None
    if type(customer_id) is not UUID:
        return None
    return customer_id


def _provider_values(
    response: object,
    view: ContextView,
    *,
    prefix: str,
) -> Mapping[str, object]:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return {}
    extracted: dict[str, object] = {}
    try:
        revision = response.max_revision  # type: ignore[attr-defined]
    except Exception:
        revision = None
    if type(revision) is int and revision >= 0:
        extracted[f"{prefix}_delivery_revision"] = revision

    fallback_order_id = None
    for order in _target_orders(response, organization_id):
        generated_order = cast(Any, order)
        try:
            order_id = generated_order.id
            order_organization_id = generated_order.organization_id
        except Exception:
            continue
        if type(order_id) is not UUID or order_organization_id != organization_id:
            continue
        if fallback_order_id is None:
            fallback_order_id = order_id
        try:
            payload = generated_order.order
            phone = payload.phone
            customer = payload.customer
        except Exception:
            continue
        if type(phone) is not str or not phone:
            continue
        extracted[f"{prefix}_delivery_id"] = order_id
        extracted[f"{prefix}_delivery_phone"] = phone
        customer_id = _regular_customer_id(customer)
        if customer_id is not None:
            extracted[f"{prefix}_delivery_customer_id"] = customer_id
        return extracted
    if fallback_order_id is not None:
        extracted[f"{prefix}_delivery_id"] = fallback_order_id
    return extracted


def _extract_search(response: object, view: ContextView) -> Mapping[str, object]:
    return _provider_values(response, view, prefix="search")


def _extract_status(response: object, view: ContextView) -> Mapping[str, object]:
    return _provider_values(response, view, prefix="status")


def _build_draft_filter(view: ContextView) -> Mapping[str, object]:
    return {
        "date_from": view["window_from_local"],
        "date_to": view["window_to_local"],
        "limit": 1,
        "offset": 0,
        "organization_ids": [view["organization_id"]],
    }


def _extract_draft(response: object, view: ContextView) -> Mapping[str, object]:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return {}
    try:
        drafts = response.drafts  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(drafts) is not list:
        return {}
    for draft in drafts:
        try:
            draft_id = draft.id
            draft_organization_id = draft.organization_id
        except Exception:
            continue
        if type(draft_id) is UUID and draft_organization_id == organization_id:
            return {"draft_id": draft_id}
    return {}


def _build_delivery_restrictions(view: ContextView) -> Mapping[str, object]:
    return {"organization_ids": [view["organization_id"]]}


def _build_allowed_restrictions(view: ContextView) -> Mapping[str, object]:
    return {
        "delivery_sum": 0,
        "discount_sum": 0,
        "is_courier_delivery": False,
        "order_items": [],
        "organization_id": view["organization_id"],
    }


def _first_uuid(
    view: ContextView,
    keys: tuple[str, ...],
    code: NoLiveTargetCode,
) -> UUID:
    for key in keys:
        candidate = view.get(key)
        if type(candidate) is UUID:
            return candidate
    raise NoLiveTarget(code)


def _first_phone(view: ContextView) -> str:
    for key in ("search_delivery_phone", "status_delivery_phone"):
        candidate = view.get(key)
        if type(candidate) is str and candidate:
            return candidate
    raise NoLiveTarget(NoLiveTargetCode.DELIVERY_PHONE)


def _first_revision(view: ContextView) -> int:
    for key in ("search_delivery_revision", "status_delivery_revision"):
        candidate = view.get(key)
        if type(candidate) is int and candidate >= 0:
            return candidate
    raise NoLiveTarget(NoLiveTargetCode.DELIVERY_REVISION)


def _build_by_id(view: ContextView) -> Mapping[str, object]:
    order_id = _first_uuid(
        view,
        ("search_delivery_id", "status_delivery_id"),
        NoLiveTargetCode.DELIVERY,
    )
    return {
        "order_ids": [order_id],
        "organization_id": view["organization_id"],
    }


def _build_by_phone(view: ContextView) -> Mapping[str, object]:
    return {
        "delivery_date_from": view["window_from_local"],
        "delivery_date_to": view["window_to_local"],
        "organization_ids": [view["organization_id"]],
        "phone": _first_phone(view),
        "rows_count": 1,
    }


def _build_by_revision(view: ContextView) -> Mapping[str, object]:
    return {
        "organization_ids": [view["organization_id"]],
        "start_revision": _first_revision(view),
    }


def _build_draft_by_id(view: ContextView) -> Mapping[str, object]:
    draft_id = _first_uuid(
        view,
        ("draft_id",),
        NoLiveTargetCode.DRAFT,
    )
    return {
        "order_id": draft_id,
        "organization_id": view["organization_id"],
    }


def _case(
    operation_id: str,
    api_module: str,
    api_class: str,
    request_module: str,
    request_class: str,
    request_keyword: str,
    response_module: str,
    response_class: str,
    *,
    depends_on: tuple[str, ...],
    requires: tuple[str, ...],
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
    build_values: Callable[[ContextView], Mapping[str, object]],
    extract: Callable[
        [object, ContextView], Mapping[str, object]
    ] = _empty_extract,
) -> ReadCase:
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
        validate_response=_typed_validator(response_module, response_class),
        extract=extract,
    )


_WINDOW_REQUIRES = (
    "organization_id",
    "window_from_local",
    "window_to_local",
)
_PROVIDER_DEPENDENCIES = (
    "search_deliveries",
    "get_deliveries_by_delivery_date_and_status",
)

DELIVERY_CASES = (
    _case(
        "search_deliveries",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_by_delivery_date_and_filter_request",
        "OrdersByDeliveryDateAndFilterRequest",
        "orders_by_delivery_date_and_filter_request",
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        depends_on=("get_organizations",),
        requires=_WINDOW_REQUIRES,
        provides=(
            "search_delivery_id",
            "search_delivery_phone",
            "search_delivery_revision",
            "search_delivery_customer_id",
        ),
        build_values=_build_search,
        extract=_extract_search,
    ),
    _case(
        "get_deliveries_by_delivery_date_and_status",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_by_delivery_date_and_status_request",
        "OrdersByDeliveryDateAndStatusRequest",
        "orders_by_delivery_date_and_status_request",
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        depends_on=("get_organizations",),
        requires=_WINDOW_REQUIRES,
        provides=(
            "status_delivery_id",
            "status_delivery_phone",
            "status_delivery_revision",
            "status_delivery_customer_id",
        ),
        build_values=_build_status,
        extract=_extract_status,
    ),
    _case(
        "get_delivery_drafts_by_filter",
        "drafts_api",
        "DraftsApi",
        "filter_drafts_request",
        "FilterDraftsRequest",
        "filter_drafts_request",
        "filter_drafts_response",
        "FilterDraftsResponse",
        depends_on=("get_organizations",),
        requires=_WINDOW_REQUIRES,
        provides=("draft_id",),
        build_values=_build_draft_filter,
        extract=_extract_draft,
    ),
    _case(
        "get_delivery_restrictions",
        "delivery_restrictions_api",
        "DeliveryRestrictionsApi",
        "get_delivery_restrictions_request",
        "GetDeliveryRestrictionsRequest",
        "get_delivery_restrictions_request",
        "get_delivery_restrictions_response",
        "GetDeliveryRestrictionsResponse",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_build_delivery_restrictions,
    ),
    _case(
        "get_allowed_delivery_restrictions",
        "delivery_restrictions_api",
        "DeliveryRestrictionsApi",
        "get_allowed_restrictions_request",
        "GetAllowedRestrictionsRequest",
        "get_allowed_restrictions_request",
        "get_allowed_restrictions_response",
        "GetAllowedRestrictionsResponse",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_build_allowed_restrictions,
    ),
    _case(
        "get_deliveries_by_id",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_by_id_request",
        "OrdersByIdRequest",
        "orders_by_id_request",
        "orders_response",
        "OrdersResponse",
        depends_on=_PROVIDER_DEPENDENCIES,
        requires=(
            "organization_id",
            "search_delivery_id",
            "status_delivery_id",
        ),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.DELIVERY}),
        build_values=_build_by_id,
    ),
    _case(
        "get_deliveries_by_delivery_date_and_phone",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_by_delivery_date_and_phone_request",
        "OrdersByDeliveryDateAndPhoneRequest",
        "orders_by_delivery_date_and_phone_request",
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        depends_on=_PROVIDER_DEPENDENCIES,
        requires=(
            "organization_id",
            "window_from_local",
            "window_to_local",
            "search_delivery_phone",
            "status_delivery_phone",
        ),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.DELIVERY_PHONE}),
        build_values=_build_by_phone,
    ),
    _case(
        "get_delivery_history_by_delivery_date_and_phone",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_history_by_delivery_date_and_phone_request",
        "OrdersHistoryByDeliveryDateAndPhoneRequest",
        "orders_history_by_delivery_date_and_phone_request",
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        depends_on=_PROVIDER_DEPENDENCIES,
        requires=(
            "organization_id",
            "window_from_local",
            "window_to_local",
            "search_delivery_phone",
            "status_delivery_phone",
        ),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.DELIVERY_PHONE}),
        build_values=_build_by_phone,
    ),
    _case(
        "get_deliveries_by_revision",
        "deliveries_retrieve_api",
        "DeliveriesRetrieveApi",
        "orders_by_revision_request",
        "OrdersByRevisionRequest",
        "orders_by_revision_request",
        "orders_with_revision_response",
        "OrdersWithRevisionResponse",
        depends_on=_PROVIDER_DEPENDENCIES,
        requires=(
            "organization_id",
            "search_delivery_revision",
            "status_delivery_revision",
        ),
        allowed_no_target_codes=frozenset(
            {NoLiveTargetCode.DELIVERY_REVISION}
        ),
        build_values=_build_by_revision,
    ),
    _case(
        "get_delivery_draft_by_id",
        "drafts_api",
        "DraftsApi",
        "get_draft_request",
        "GetDraftRequest",
        "get_draft_request",
        "get_draft_response",
        "GetDraftResponse",
        depends_on=("get_delivery_drafts_by_filter",),
        requires=("organization_id", "draft_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.DRAFT}),
        build_values=_build_draft_by_id,
    ),
)

__all__ = ["DELIVERY_CASES"]
