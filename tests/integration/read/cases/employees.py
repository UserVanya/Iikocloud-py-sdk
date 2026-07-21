"""Guarded employee and courier read cases with PII-free context extraction."""

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
    request_module: str,
    request_class: str,
    request_keyword: str,
) -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module="iikocloud_client.api.employees_api",
        api_class="EmployeesApi",
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


def _organization_ids(view: ContextView) -> Mapping[str, object]:
    return {"organization_ids": [view["organization_id"]]}


def _build_active_by_terminal(view: ContextView) -> Mapping[str, object]:
    terminal_group_id = _required_uuid(
        view,
        "terminal_group_id",
        NoLiveTargetCode.TERMINAL_GROUP,
    )
    return {
        "organization_id": view["organization_id"],
        "terminal_group_id": terminal_group_id,
    }


def _build_location_history(view: ContextView) -> Mapping[str, object]:
    return {
        "offset_in_seconds": 0,
        "organization_ids": [view["organization_id"]],
    }


def _required_uuid(
    view: ContextView,
    key: str,
    code: NoLiveTargetCode,
) -> UUID:
    candidate = view.get(key)
    if type(candidate) is UUID:
        return candidate
    raise NoLiveTarget(code)


def _required_role_code(view: ContextView) -> str:
    candidate = view.get("employee_role_code")
    if type(candidate) is str and candidate.strip():
        return candidate
    raise NoLiveTarget(NoLiveTargetCode.EMPLOYEE_ROLE)


def _build_couriers_by_role(view: ContextView) -> Mapping[str, object]:
    role_code = _required_role_code(view)
    return {
        "organization_ids": [view["organization_id"]],
        "roles_to_check": [role_code],
    }


def _build_employee_info(view: ContextView) -> Mapping[str, object]:
    employee_id = _required_uuid(
        view,
        "courier_employee_id",
        NoLiveTargetCode.EMPLOYEE,
    )
    return {
        "id": employee_id,
        "organization_id": view["organization_id"],
    }


def _build_personal_session(view: ContextView) -> Mapping[str, object]:
    employee_id = _required_uuid(
        view,
        "courier_employee_id",
        NoLiveTargetCode.EMPLOYEE,
    )
    terminal_group_id = _required_uuid(
        view,
        "terminal_group_id",
        NoLiveTargetCode.TERMINAL_GROUP,
    )
    return {
        "employee_id": employee_id,
        "organization_id": view["organization_id"],
        "terminal_group_id": terminal_group_id,
    }


def _build_terminal_groups_of_employee(view: ContextView) -> Mapping[str, object]:
    employee_id = _required_uuid(
        view,
        "courier_employee_id",
        NoLiveTargetCode.EMPLOYEE,
    )
    return {"employee_id": employee_id}


def _validate_grouped_response(
    response: object,
    view: ContextView,
    *,
    response_module: str,
    response_class: str,
    groups_attribute: str,
) -> None:
    if not _is_exact_model(response, response_module, response_class):
        raise ReadAssertionFailure()
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        raise ReadAssertionFailure()
    groups: object = None
    groups_unavailable = False
    try:
        groups = getattr(response, groups_attribute)
    except Exception:
        groups_unavailable = True
    if groups_unavailable or type(groups) is not list:
        raise ReadAssertionFailure()
    for group in groups:
        group_organization_id: object = None
        items: object = None
        linkage_unavailable = False
        try:
            group_organization_id = group.organization_id
            items = group.items
        except Exception:
            linkage_unavailable = True
        if (
            linkage_unavailable
            or group_organization_id != organization_id
            or type(items) is not list
        ):
            raise ReadAssertionFailure()


def _grouped_validator(
    response_module: str,
    response_class: str,
    groups_attribute: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, view: ContextView) -> None:
        _validate_grouped_response(
            response,
            view,
            response_module=response_module,
            response_class=response_class,
            groups_attribute=groups_attribute,
        )

    return validate


def _extract_courier(response: object, view: ContextView) -> Mapping[str, object]:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        return {}
    try:
        groups = response.employees  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(groups) is not list:
        return {}
    for group in groups:
        try:
            group_organization_id = group.organization_id
            employees = group.items
        except Exception:
            continue
        if group_organization_id != organization_id or type(employees) is not list:
            continue
        for employee in employees:
            generated_employee = cast(Any, employee)
            try:
                employee_id = generated_employee.id
                is_deleted = generated_employee.is_deleted
            except Exception:
                continue
            if type(employee_id) is UUID and is_deleted is False:
                return {"courier_employee_id": employee_id}
    return {}


def _validate_employee_info(response: object, view: ContextView) -> None:
    if not _is_exact_model(
        response,
        "employee_info_response",
        "EmployeeInfoResponse",
    ):
        raise ReadAssertionFailure()
    employee_id = view.get("courier_employee_id")
    if type(employee_id) is not UUID:
        raise ReadAssertionFailure()
    response_employee_id: object = None
    employee_info_unavailable = False
    try:
        response_employee_id = response.employee_info.id  # type: ignore[attr-defined]
    except Exception:
        employee_info_unavailable = True
    if (
        employee_info_unavailable
        or type(response_employee_id) is not UUID
        or response_employee_id != employee_id
    ):
        raise ReadAssertionFailure()


def _case(
    operation_id: str,
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
            request_module,
            request_class,
            request_keyword,
        ),
        build_values=build_values,
        validate_response=validator,
        extract=extract,
    )


EMPLOYEE_CASES = (
    _case(
        "get_active_courier_locations",
        "active_courier_locations_response",
        "ActiveCourierLocationsResponse",
        "couriers_request",
        "CouriersRequest",
        "couriers_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_organization_ids,
        validate_response=_grouped_validator(
            "active_courier_locations_response",
            "ActiveCourierLocationsResponse",
            "active_courier_locations",
        ),
    ),
    _case(
        "get_active_courier_locations_by_terminal",
        "active_courier_locations_response",
        "ActiveCourierLocationsResponse",
        "active_courier_locations_by_terminal_group_request",
        "ActiveCourierLocationsByTerminalGroupRequest",
        "active_courier_locations_by_terminal_group_request",
        depends_on=("get_terminal_groups",),
        requires=("organization_id", "terminal_group_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.TERMINAL_GROUP}),
        build_values=_build_active_by_terminal,
        validate_response=_grouped_validator(
            "active_courier_locations_response",
            "ActiveCourierLocationsResponse",
            "active_courier_locations",
        ),
    ),
    _case(
        "get_courier_location_history",
        "courier_locations_by_time_offset_response",
        "CourierLocationsByTimeOffsetResponse",
        "courier_locations_by_time_offset_request",
        "CourierLocationsByTimeOffsetRequest",
        "courier_locations_by_time_offset_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        build_values=_build_location_history,
        validate_response=_grouped_validator(
            "courier_locations_by_time_offset_response",
            "CourierLocationsByTimeOffsetResponse",
            "courier_locations",
        ),
    ),
    _case(
        "get_couriers",
        "employees_response",
        "EmployeesResponse",
        "couriers_request",
        "CouriersRequest",
        "couriers_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        provides=("courier_employee_id", "employee_role_code"),
        build_values=_organization_ids,
        validate_response=_grouped_validator(
            "employees_response",
            "EmployeesResponse",
            "employees",
        ),
        extract=_extract_courier,
    ),
    _case(
        "get_couriers_by_role",
        "employees_with_role_sign_response",
        "EmployeesWithRoleSignResponse",
        "couriers_and_check_role_request",
        "CouriersAndCheckRoleRequest",
        "couriers_and_check_role_request",
        depends_on=("get_couriers",),
        requires=("organization_id", "employee_role_code"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.EMPLOYEE_ROLE}),
        build_values=_build_couriers_by_role,
        validate_response=_grouped_validator(
            "employees_with_role_sign_response",
            "EmployeesWithRoleSignResponse",
            "employees_with_check_roles",
        ),
    ),
    _case(
        "get_employee_info",
        "employee_info_response",
        "EmployeeInfoResponse",
        "employee_info_request",
        "EmployeeInfoRequest",
        "employee_info_request",
        depends_on=("get_couriers",),
        requires=("organization_id", "courier_employee_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.EMPLOYEE}),
        build_values=_build_employee_info,
        validate_response=_validate_employee_info,
    ),
    _case(
        "get_personal_session_info",
        "get_personal_session_info_response",
        "GetPersonalSessionInfoResponse",
        "get_personal_session_info_request",
        "GetPersonalSessionInfoRequest",
        "get_personal_session_info_request",
        depends_on=("get_couriers", "get_terminal_groups"),
        requires=("organization_id", "courier_employee_id", "terminal_group_id"),
        allowed_no_target_codes=frozenset(
            {NoLiveTargetCode.EMPLOYEE, NoLiveTargetCode.TERMINAL_GROUP}
        ),
        build_values=_build_personal_session,
    ),
    _case(
        "get_terminal_groups_of_employee",
        "get_terminal_groups_of_employee_response",
        "GetTerminalGroupsOfEmployeeResponse",
        "get_terminal_groups_of_employee_request",
        "GetTerminalGroupsOfEmployeeRequest",
        "get_terminal_groups_of_employee_request",
        depends_on=("get_couriers",),
        requires=("courier_employee_id",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.EMPLOYEE}),
        build_values=_build_terminal_groups_of_employee,
    ),
)

__all__ = ["EMPLOYEE_CASES"]
