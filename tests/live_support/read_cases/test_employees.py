from __future__ import annotations

from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.employees import EMPLOYEE_CASES
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
from tools.openapi_pipeline.live.read_report import (
    ReadOutcome,
    ReadReport,
    ReadStatus,
)

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
OTHER_ORGANIZATION_ID = UUID("22222222-2222-4222-8222-222222222222")
TERMINAL_GROUP_ID = UUID("33333333-3333-4333-8333-333333333333")
EMPLOYEE_ID = UUID("44444444-4444-4444-8444-444444444444")
OTHER_EMPLOYEE_ID = UUID("55555555-5555-4555-8555-555555555555")
ROLE_CODE = "synthetic-reviewed-role"
PRIVATE_NAME = "private-courier-name-marker"
PRIVATE_PHONE = "+70000000999"
PRIVATE_EMAIL = "private-courier@example.invalid"
PRIVATE_COORDINATE = "55.755826-private-coordinate"
PRIVATE_MARKERS = (
    str(ORGANIZATION_ID),
    str(OTHER_ORGANIZATION_ID),
    str(TERMINAL_GROUP_ID),
    str(EMPLOYEE_ID),
    str(OTHER_EMPLOYEE_ID),
    ROLE_CODE,
    PRIVATE_NAME,
    PRIVATE_PHONE,
    PRIVATE_EMAIL,
    PRIVATE_COORDINATE,
)

EMPLOYEE_IDS = {
    "get_active_courier_locations",
    "get_active_courier_locations_by_terminal",
    "get_courier_location_history",
    "get_couriers",
    "get_couriers_by_role",
    "get_employee_info",
    "get_personal_session_info",
    "get_terminal_groups_of_employee",
}

RESPONSE_MODELS = {
    "get_active_courier_locations": (
        "active_courier_locations_response",
        "ActiveCourierLocationsResponse",
    ),
    "get_active_courier_locations_by_terminal": (
        "active_courier_locations_response",
        "ActiveCourierLocationsResponse",
    ),
    "get_courier_location_history": (
        "courier_locations_by_time_offset_response",
        "CourierLocationsByTimeOffsetResponse",
    ),
    "get_couriers": ("employees_response", "EmployeesResponse"),
    "get_couriers_by_role": (
        "employees_with_role_sign_response",
        "EmployeesWithRoleSignResponse",
    ),
    "get_employee_info": ("employee_info_response", "EmployeeInfoResponse"),
    "get_personal_session_info": (
        "get_personal_session_info_response",
        "GetPersonalSessionInfoResponse",
    ),
    "get_terminal_groups_of_employee": (
        "get_terminal_groups_of_employee_response",
        "GetTerminalGroupsOfEmployeeResponse",
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
    return next(case for case in EMPLOYEE_CASES if case.operation_id == operation_id)


def _view(
    case: ReadCase,
    *,
    omit: frozenset[str] = frozenset(),
    **changes: object,
) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "terminal_group_id": TERMINAL_GROUP_ID,
        "courier_employee_id": EMPLOYEE_ID,
        "employee_role_code": ROLE_CODE,
    }
    values.update(changes)
    return ContextView(
        {
            key: values[key]
            for key in case.requires
            if key in values and key not in omit
        }
    )


def _employee(
    employee_id: UUID,
    *,
    is_deleted: bool | None = False,
) -> object:
    return _model(
        "employee_directory_entry",
        "EmployeeDirectoryEntry",
        code="employee-code-is-not-a-role",
        display_name=PRIVATE_NAME,
        first_name=PRIVATE_NAME,
        id=employee_id,
        is_deleted=is_deleted,
        last_name=PRIVATE_NAME,
        middle_name=PRIVATE_NAME,
    )


def _employee_group(
    *employees: object,
    organization_id: UUID = ORGANIZATION_ID,
) -> object:
    return _model(
        "rms_employee_items_response",
        "RmsEmployeeItemsResponse",
        items=list(employees),
        organization_id=organization_id,
    )


def _employees_response(*groups: object) -> object:
    return _model(
        "employees_response",
        "EmployeesResponse",
        employees=list(groups),
    )


def _active_response(*groups: object) -> object:
    return _model(
        "active_courier_locations_response",
        "ActiveCourierLocationsResponse",
        active_courier_locations=list(groups),
    )


def _history_response(*groups: object) -> object:
    return _model(
        "courier_locations_by_time_offset_response",
        "CourierLocationsByTimeOffsetResponse",
        courier_locations=list(groups),
    )


def _role_response(*groups: object) -> object:
    return _model(
        "employees_with_role_sign_response",
        "EmployeesWithRoleSignResponse",
        employees_with_check_roles=list(groups),
    )


def _employee_info_response(employee_id: UUID = EMPLOYEE_ID) -> object:
    employee_info = _model(
        "employee_info",
        "EmployeeInfo",
        cell_phone=PRIVATE_PHONE,
        display_name=PRIVATE_NAME,
        email=PRIVATE_EMAIL,
        first_name=PRIVATE_NAME,
        id=employee_id,
        last_name=PRIVATE_NAME,
        middle_name=PRIVATE_NAME,
        phone=PRIVATE_PHONE,
    )
    return _model(
        "employee_info_response",
        "EmployeeInfoResponse",
        employee_info=employee_info,
    )


def _minimal_response(operation_id: str) -> object:
    if operation_id in {
        "get_active_courier_locations",
        "get_active_courier_locations_by_terminal",
    }:
        return _active_response()
    if operation_id == "get_courier_location_history":
        return _history_response()
    if operation_id == "get_couriers":
        return _employees_response()
    if operation_id == "get_couriers_by_role":
        return _role_response()
    if operation_id == "get_employee_info":
        return _employee_info_response()
    module_name, class_name = RESPONSE_MODELS[operation_id]
    if operation_id == "get_terminal_groups_of_employee":
        return _model(module_name, class_name, terminal_group_ids=[])
    return _model(module_name, class_name)


def test_employee_registry_is_exact_and_builds_with_foundation() -> None:
    assert type(EMPLOYEE_CASES) is tuple
    assert {case.operation_id for case in EMPLOYEE_CASES} == EMPLOYEE_IDS
    assert len(EMPLOYEE_CASES) == len(EMPLOYEE_IDS)
    assert set(
        ReadPlan.build((*FOUNDATION_CASES, *EMPLOYEE_CASES)).ordered_operation_ids
    ) > EMPLOYEE_IDS


def test_employee_dependencies_and_provider_keys_are_exact() -> None:
    for operation_id in {
        "get_active_courier_locations",
        "get_courier_location_history",
        "get_couriers",
    }:
        assert _case(operation_id).depends_on == ("get_organizations",)

    terminal = _case("get_active_courier_locations_by_terminal")
    assert terminal.depends_on == ("get_terminal_groups",)
    assert terminal.requires == ("organization_id", "terminal_group_id")

    couriers = _case("get_couriers")
    assert couriers.provides == ("courier_employee_id", "employee_role_code")

    assert _case("get_couriers_by_role").depends_on == ("get_couriers",)
    assert _case("get_employee_info").depends_on == ("get_couriers",)
    assert _case("get_terminal_groups_of_employee").depends_on == ("get_couriers",)
    assert _case("get_personal_session_info").depends_on == (
        "get_couriers",
        "get_terminal_groups",
    )


@pytest.mark.parametrize("operation_id", sorted(EMPLOYEE_IDS))
def test_bindings_resolve_and_validators_fail_with_fixed_redacted_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id), _view(case))

    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": PRIVATE_NAME}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert PRIVATE_NAME not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_employee_requests_are_exactly_scoped_and_linked() -> None:
    expected = {
        "get_active_courier_locations": {
            "organizationIds": [str(ORGANIZATION_ID)]
        },
        "get_active_courier_locations_by_terminal": {
            "organizationId": str(ORGANIZATION_ID),
            "terminalGroupId": str(TERMINAL_GROUP_ID),
        },
        "get_courier_location_history": {
            "offsetInSeconds": 0,
            "organizationIds": [str(ORGANIZATION_ID)],
        },
        "get_couriers": {"organizationIds": [str(ORGANIZATION_ID)]},
        "get_couriers_by_role": {
            "organizationIds": [str(ORGANIZATION_ID)],
            "rolesToCheck": [ROLE_CODE],
        },
        "get_employee_info": {
            "id": str(EMPLOYEE_ID),
            "organizationId": str(ORGANIZATION_ID),
        },
        "get_personal_session_info": {
            "employeeId": str(EMPLOYEE_ID),
            "organizationId": str(ORGANIZATION_ID),
            "terminalGroupId": str(TERMINAL_GROUP_ID),
        },
        "get_terminal_groups_of_employee": {"employeeId": str(EMPLOYEE_ID)},
    }

    for operation_id, expected_json in expected.items():
        case = _case(operation_id)
        request = build_generated_request(case.binding, case.build_values(_view(case)))
        assert request is not None
        assert _jsonable(request.to_dict()) == expected_json  # type: ignore[attr-defined]


def test_courier_provider_selects_one_live_target_employee_without_pii() -> None:
    case = _case("get_couriers")
    response = _employees_response(
        _employee_group(
            _employee(OTHER_EMPLOYEE_ID, is_deleted=True),
            _employee(OTHER_EMPLOYEE_ID, is_deleted=None),
            _employee(EMPLOYEE_ID),
        )
    )
    assert case.extract(response, _view(case)) == {
        "courier_employee_id": EMPLOYEE_ID
    }

    context = ReadContext.seed({"organization_id": ORGANIZATION_ID})
    context.apply(case, case.extract(response, _view(case)))
    rendered = repr(context)
    for marker in PRIVATE_MARKERS:
        assert marker not in rendered


def test_courier_provider_ignores_empty_foreign_and_employee_code_values() -> None:
    case = _case("get_couriers")
    assert case.extract(_employees_response(), _view(case)) == {}
    assert case.extract(
        _employees_response(
            _employee_group(
                _employee(EMPLOYEE_ID),
                organization_id=OTHER_ORGANIZATION_ID,
            )
        ),
        _view(case),
    ) == {}
    assert "employee_role_code" not in case.extract(
        _employees_response(_employee_group(_employee(EMPLOYEE_ID))),
        _view(case),
    )


@pytest.mark.parametrize(
    ("operation_id", "missing_key", "code"),
    [
        (
            "get_active_courier_locations_by_terminal",
            "terminal_group_id",
            NoLiveTargetCode.TERMINAL_GROUP,
        ),
        (
            "get_couriers_by_role",
            "employee_role_code",
            NoLiveTargetCode.EMPLOYEE_ROLE,
        ),
        ("get_employee_info", "courier_employee_id", NoLiveTargetCode.EMPLOYEE),
        (
            "get_personal_session_info",
            "courier_employee_id",
            NoLiveTargetCode.EMPLOYEE,
        ),
        (
            "get_personal_session_info",
            "terminal_group_id",
            NoLiveTargetCode.TERMINAL_GROUP,
        ),
        (
            "get_terminal_groups_of_employee",
            "courier_employee_id",
            NoLiveTargetCode.EMPLOYEE,
        ),
    ],
)
def test_missing_targets_fail_before_generated_request_build(
    operation_id: str,
    missing_key: str,
    code: NoLiveTargetCode,
) -> None:
    case = _case(operation_id)
    with pytest.raises(NoLiveTarget) as raised:
        case.build_values(_view(case, omit=frozenset({missing_key})))
    assert raised.value.code is code
    assert str(raised.value) == code.value
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_empty_and_non_string_role_codes_are_rejected_without_payloads() -> None:
    case = _case("get_couriers_by_role")
    for role_code in ("", 17, EMPLOYEE_ID):
        with pytest.raises(NoLiveTarget) as raised:
            case.build_values(_view(case, employee_role_code=role_code))
        assert raised.value.code is NoLiveTargetCode.EMPLOYEE_ROLE
        assert ROLE_CODE not in repr(raised.value)


def test_employee_info_validator_requires_the_response_derived_employee() -> None:
    case = _case("get_employee_info")
    case.validate_response(_employee_info_response(), _view(case))

    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response(
            _employee_info_response(OTHER_EMPLOYEE_ID),
            _view(case),
        )
    assert str(raised.value) == "assertion_failed"
    for marker in PRIVATE_MARKERS:
        assert marker not in repr(raised.value)


@pytest.mark.parametrize(
    ("operation_id", "response"),
    [
        (
            "get_couriers",
            _model("employees_response", "EmployeesResponse"),
        ),
        (
            "get_employee_info",
            _model("employee_info_response", "EmployeeInfoResponse"),
        ),
    ],
)
def test_malformed_exact_responses_do_not_attach_source_exceptions(
    operation_id: str,
    response: object,
) -> None:
    case = _case(operation_id)
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response(response, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_grouped_employee_responses_reject_foreign_organization_linkage() -> None:
    grouped_responses = {
        "get_active_courier_locations": _active_response(
            _model(
                "rms_active_courier_location_items_response",
                "RmsActiveCourierLocationItemsResponse",
                items=[],
                organization_id=OTHER_ORGANIZATION_ID,
            )
        ),
        "get_active_courier_locations_by_terminal": _active_response(
            _model(
                "rms_active_courier_location_items_response",
                "RmsActiveCourierLocationItemsResponse",
                items=[],
                organization_id=OTHER_ORGANIZATION_ID,
            )
        ),
        "get_courier_location_history": _history_response(
            _model(
                "rms_courier_locations_items_response",
                "RmsCourierLocationsItemsResponse",
                items=[],
                organization_id=OTHER_ORGANIZATION_ID,
            )
        ),
        "get_couriers": _employees_response(
            _employee_group(organization_id=OTHER_ORGANIZATION_ID)
        ),
        "get_couriers_by_role": _role_response(
            _model(
                "rms_employee_with_checked_role_items_response",
                "RmsEmployeeWithCheckedRoleItemsResponse",
                items=[],
                organization_id=OTHER_ORGANIZATION_ID,
            )
        ),
    }
    for operation_id, response in grouped_responses.items():
        case = _case(operation_id)
        with pytest.raises(ReadAssertionFailure):
            case.validate_response(response, _view(case))


def test_pii_markers_never_enter_outcome_or_report_renderings() -> None:
    outcome = ReadOutcome(
        operation_id="get_couriers",
        method="POST",
        path="/api/1/employees/couriers",
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
        counts={
            "passed": 1,
            "no_live_target": 0,
            "failed": 0,
            "aborted": 0,
        },
    )
    rendered = repr((outcome, outcome.to_json(), report, report.to_json()))
    for marker in PRIVATE_MARKERS:
        assert marker not in rendered
