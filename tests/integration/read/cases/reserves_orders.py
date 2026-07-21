"""Guarded read cases for reserves, restaurant sections, and table orders."""

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


def _build_reserve_organizations(view: ContextView) -> Mapping[str, object]:
    return {
        "include_disabled": False,
        "organization_ids": [view["organization_id"]],
        "return_additional_info": False,
    }


def _has_selected_organization(response: object, view: ContextView) -> bool:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return False
    try:
        organizations = response.organizations  # type: ignore[attr-defined]
    except Exception:
        return False
    if type(organizations) is not list:
        return False
    for organization in organizations:
        try:
            candidate_id = organization.id
        except Exception:
            continue
        if type(candidate_id) is UUID and candidate_id == organization_id:
            return True
    return False


def _validate_reserve_organizations(response: object, view: ContextView) -> None:
    if not _is_exact_model(
        response,
        "get_organizations_response",
        "GetOrganizationsResponse",
    ) or not _has_selected_organization(response, view):
        raise ReadAssertionFailure()


def _build_reserve_terminal_groups(view: ContextView) -> Mapping[str, object]:
    return {"organization_ids": [view["organization_id"]]}


def _reserve_terminal_ids(response: object, organization_id: UUID) -> tuple[UUID, ...]:
    try:
        collections = (
            response.terminal_groups,  # type: ignore[attr-defined]
            response.terminal_groups_in_sleep,  # type: ignore[attr-defined]
        )
    except Exception:
        return ()
    terminal_ids: list[UUID] = []
    for groups in collections:
        if type(groups) is not list:
            continue
        for group in groups:
            try:
                group_organization_id = group.organization_id
                terminals = group.items
            except Exception:
                continue
            if group_organization_id != organization_id or type(terminals) is not list:
                continue
            for terminal in terminals:
                try:
                    terminal_id = terminal.id
                    terminal_organization_id = terminal.organization_id
                except Exception:
                    continue
                if (
                    type(terminal_id) is UUID
                    and terminal_organization_id == organization_id
                ):
                    terminal_ids.append(terminal_id)
    return tuple(terminal_ids)


def _extract_reserve_terminal(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return {}
    terminal_ids = _reserve_terminal_ids(response, organization_id)
    if not terminal_ids:
        return {}
    preferred = view.get("terminal_group_id")
    if type(preferred) is UUID and preferred in terminal_ids:
        return {"reserve_terminal_group_id": preferred}
    return {"reserve_terminal_group_id": terminal_ids[0]}


def _required_uuid(
    view: ContextView,
    key: str,
    code: NoLiveTargetCode,
) -> UUID:
    candidate = view.get(key)
    if type(candidate) is UUID:
        return candidate
    raise NoLiveTarget(code)


def _build_restaurant_sections(view: ContextView) -> Mapping[str, object]:
    terminal_group_id = _required_uuid(
        view,
        "reserve_terminal_group_id",
        NoLiveTargetCode.TERMINAL_GROUP,
    )
    return {
        "return_schema": False,
        "terminal_group_ids": [terminal_group_id],
    }


def _extract_restaurant_section(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    terminal_group_id = view.get("reserve_terminal_group_id")
    if type(terminal_group_id) is not UUID:
        return {}
    try:
        sections = response.restaurant_sections  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(sections) is not list:
        return {}
    for section in sections:
        generated_section = cast(Any, section)
        try:
            section_id = generated_section.id
            section_terminal_group_id = generated_section.terminal_group_id
        except Exception:
            continue
        if (
            type(section_id) is not UUID
            or section_terminal_group_id != terminal_group_id
        ):
            continue
        extracted: dict[str, object] = {"restaurant_section_id": section_id}
        try:
            tables = generated_section.tables
        except Exception:
            return extracted
        if type(tables) is not list:
            return extracted
        for table in tables:
            try:
                table_id = table.id
            except Exception:
                continue
            if type(table_id) is UUID:
                extracted["table_id"] = table_id
                break
        return extracted
    return {}


def _build_workload(view: ContextView) -> Mapping[str, object]:
    restaurant_section_id = _required_uuid(
        view,
        "restaurant_section_id",
        NoLiveTargetCode.RESTAURANT_SECTION,
    )
    return {
        "date_from": view["window_from_local"],
        "date_to": view["window_to_local"],
        "restaurant_section_ids": [restaurant_section_id],
    }


def _extract_reserve(response: object, _view: ContextView) -> Mapping[str, object]:
    try:
        reserves = response.reserves  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(reserves) is not list:
        return {}
    for reserve in reserves:
        try:
            reserve_id = reserve.id
        except Exception:
            continue
        if type(reserve_id) is UUID:
            return {"reserve_id": reserve_id}
    return {}


def _build_reserve_status(view: ContextView) -> Mapping[str, object]:
    reserve_id = _required_uuid(view, "reserve_id", NoLiveTargetCode.RESERVE)
    return {
        "organization_id": view["organization_id"],
        "reserve_ids": [reserve_id],
    }


def _build_table_orders_by_table(view: ContextView) -> Mapping[str, object]:
    table_id = _required_uuid(view, "table_id", NoLiveTargetCode.TABLE)
    return {
        "date_from": view["window_from_local"],
        "date_to": view["window_to_local"],
        "organization_ids": [view["organization_id"]],
        "table_ids": [table_id],
    }


def _table_order_customer_id(order: object) -> UUID | None:
    regular_customer = _generated_class(
        "delivery_order_response_regular_customer",
        "DeliveryOrderResponseRegularCustomer",
    )
    if regular_customer is None:
        return None
    try:
        customer = cast(Any, order).order.customer
    except Exception:
        return None
    if type(customer) is not regular_customer:
        return None
    try:
        customer_id = cast(Any, customer).id
    except Exception:
        return None
    if type(customer_id) is UUID:
        return customer_id
    return None


def _extract_table_order(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return {}
    try:
        orders = response.orders  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(orders) is not list:
        return {}
    for order in orders:
        generated_order = cast(Any, order)
        try:
            order_id = generated_order.id
            order_organization_id = generated_order.organization_id
        except Exception:
            continue
        if type(order_id) is not UUID or order_organization_id != organization_id:
            continue
        extracted: dict[str, object] = {"table_order_id": order_id}
        customer_id = _table_order_customer_id(generated_order)
        if customer_id is not None:
            extracted["table_order_customer_id"] = customer_id
        return extracted
    return {}


def _build_table_orders_by_id(view: ContextView) -> Mapping[str, object]:
    table_order_id = _required_uuid(
        view,
        "table_order_id",
        NoLiveTargetCode.TABLE_ORDER,
    )
    return {
        "order_ids": [table_order_id],
        "organization_ids": [view["organization_id"]],
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


RESERVE_ORDER_CASES = (
    _case(
        "get_reserve_available_organizations",
        "banquets_reserves_api",
        "BanquetsReservesApi",
        "get_organizations_response",
        "GetOrganizationsResponse",
        "get_organizations_request",
        "GetOrganizationsRequest",
        "get_organizations_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_build_reserve_organizations,
        validate_response=_validate_reserve_organizations,
    ),
    _case(
        "get_reserve_terminal_groups",
        "banquets_reserves_api",
        "BanquetsReservesApi",
        "terminal_groups_response",
        "TerminalGroupsResponse",
        "get_terminal_groups_by_organizations_request",
        "GetTerminalGroupsByOrganizationsRequest",
        "get_terminal_groups_by_organizations_request",
        depends_on=(
            "get_reserve_available_organizations",
            "get_terminal_groups",
        ),
        requires=("organization_id", "terminal_group_id"),
        provides=("reserve_terminal_group_id",),
        build_values=_build_reserve_terminal_groups,
        extract=_extract_reserve_terminal,
    ),
    _case(
        "get_reserve_restaurant_sections",
        "banquets_reserves_api",
        "BanquetsReservesApi",
        "get_restaurant_sections_response",
        "GetRestaurantSectionsResponse",
        "get_restaurant_sections_request",
        "GetRestaurantSectionsRequest",
        "get_restaurant_sections_request",
        depends_on=("get_reserve_terminal_groups",),
        requires=("reserve_terminal_group_id",),
        provides=("restaurant_section_id", "table_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.TERMINAL_GROUP}),
        build_values=_build_restaurant_sections,
        extract=_extract_restaurant_section,
    ),
    _case(
        "get_restaurant_sections_workload",
        "banquets_reserves_api",
        "BanquetsReservesApi",
        "get_restaurant_sections_workload_response",
        "GetRestaurantSectionsWorkloadResponse",
        "get_restaurant_sections_workload_request",
        "GetRestaurantSectionsWorkloadRequest",
        "get_restaurant_sections_workload_request",
        depends_on=("get_reserve_restaurant_sections",),
        requires=(
            "restaurant_section_id",
            "window_from_local",
            "window_to_local",
        ),
        provides=("reserve_id",),
        allowed_no_target_codes=frozenset(
            {NoLiveTargetCode.RESTAURANT_SECTION}
        ),
        build_values=_build_workload,
        extract=_extract_reserve,
    ),
    _case(
        "get_reserve_statuses_by_id",
        "banquets_reserves_api",
        "BanquetsReservesApi",
        "reserves_response",
        "ReservesResponse",
        "reserves_by_id_request",
        "ReservesByIdRequest",
        "reserves_by_id_request",
        depends_on=("get_restaurant_sections_workload",),
        requires=("organization_id", "reserve_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.RESERVE}),
        build_values=_build_reserve_status,
    ),
    _case(
        "get_table_orders_by_table",
        "orders_api",
        "OrdersApi",
        "table_orders_response",
        "TableOrdersResponse",
        "get_table_orders_by_table_request",
        "GetTableOrdersByTableRequest",
        "get_table_orders_by_table_request",
        depends_on=("get_reserve_restaurant_sections",),
        requires=(
            "organization_id",
            "table_id",
            "window_from_local",
            "window_to_local",
        ),
        provides=("table_order_id", "table_order_customer_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.TABLE}),
        build_values=_build_table_orders_by_table,
        extract=_extract_table_order,
    ),
    _case(
        "get_table_orders_by_id",
        "orders_api",
        "OrdersApi",
        "table_orders_response",
        "TableOrdersResponse",
        "get_table_orders_by_id_request",
        "GetTableOrdersByIdRequest",
        "get_table_orders_by_id_request",
        depends_on=("get_table_orders_by_table",),
        requires=("organization_id", "table_order_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.TABLE_ORDER}),
        build_values=_build_table_orders_by_id,
    ),
)

__all__ = ["RESERVE_ORDER_CASES"]
