from __future__ import annotations

from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.addresses import ADDRESS_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    ContextView,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
    build_generated_request,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
OTHER_ORGANIZATION_ID = UUID("22222222-2222-4222-8222-222222222222")
TERMINAL_GROUP_ID = UUID("33333333-3333-4333-8333-333333333333")
CITY_ID = UUID("44444444-4444-4444-8444-444444444444")
STREET_ID = UUID("55555555-5555-4555-8555-555555555555")

FOUNDATION_IDS = {
    "get_cancel_causes",
    "get_cities",
    "get_command_status",
    "get_delivery_order_types",
    "get_discounts",
    "get_marketing_sources",
    "get_organization_settings",
    "get_organizations",
    "get_payment_types",
    "get_regions",
    "get_removal_types",
    "get_terminal_groups",
    "check_terminal_groups_availability",
    "get_tips_types",
    "get_webhook_settings",
    "list_organizations",
    "get_streets_by_city",
    "get_streets_by_id",
}

RESPONSE_MODELS = {
    "get_cancel_causes": ("cancel_causes_response", "CancelCausesResponse"),
    "get_cities": ("cities_response", "CitiesResponse"),
    "get_command_status": (
        "get_command_status_response",
        "GetCommandStatusResponse",
    ),
    "get_delivery_order_types": ("order_types_response", "OrderTypesResponse"),
    "get_discounts": ("discounts_response", "DiscountsResponse"),
    "get_marketing_sources": (
        "marketing_sources_response",
        "MarketingSourcesResponse",
    ),
    "get_organization_settings": (
        "organizations_settings_response",
        "OrganizationsSettingsResponse",
    ),
    "get_organizations": (
        "get_organizations_response",
        "GetOrganizationsResponse",
    ),
    "get_payment_types": ("payment_types_response", "PaymentTypesResponse"),
    "get_regions": ("regions_response", "RegionsResponse"),
    "get_removal_types": ("removal_types_response", "RemovalTypesResponse"),
    "get_terminal_groups": ("terminal_groups_response", "TerminalGroupsResponse"),
    "check_terminal_groups_availability": (
        "terminal_groups_is_alive_response",
        "TerminalGroupsIsAliveResponse",
    ),
    "get_tips_types": ("tips_types_response", "TipsTypesResponse"),
    "get_webhook_settings": (
        "get_web_hook_settings_response",
        "GetWebHookSettingsResponse",
    ),
    "list_organizations": (
        "get_simple_organizations_response",
        "GetSimpleOrganizationsResponse",
    ),
    "get_streets_by_city": ("streets_response", "StreetsResponse"),
    "get_streets_by_id": (
        "streets_by_id_response",
        "StreetsByIdResponse",
    ),
}


def _all_cases() -> tuple[ReadCase, ...]:
    return (*FOUNDATION_CASES, *ADDRESS_CASES)


def _case(operation_id: str) -> ReadCase:
    return next(case for case in _all_cases() if case.operation_id == operation_id)


def _model(module_name: str, class_name: str, **values: object) -> object:
    module = import_module(f"iikocloud_client.models.{module_name}")
    model = getattr(module, class_name)
    return model.model_construct(**values)


def _view(case: ReadCase, *, with_terminal: bool = False) -> ContextView:
    values: dict[str, object] = {
        "profile_organization_id": str(ORGANIZATION_ID),
        "organization_id": ORGANIZATION_ID,
        "city_id": CITY_ID,
        "street_id": STREET_ID,
    }
    if with_terminal:
        values["profile_terminal_group_id"] = str(TERMINAL_GROUP_ID)
        values["terminal_group_id"] = TERMINAL_GROUP_ID
    return ContextView({key: values[key] for key in case.requires if key in values})


def _organization_response(organization_id: UUID) -> object:
    organization = _model("organization_info", "OrganizationInfo", id=organization_id)
    return _model(
        "get_organizations_response",
        "GetOrganizationsResponse",
        organizations=[organization],
    )


def _terminal_response(organization_id: UUID, terminal_group_id: UUID) -> object:
    terminal = _model(
        "terminal_group",
        "TerminalGroup",
        id=terminal_group_id,
        organization_id=organization_id,
    )
    group = _model(
        "rms_terminal_group_items_response",
        "RmsTerminalGroupItemsResponse",
        organization_id=organization_id,
        items=[terminal],
    )
    return _model(
        "terminal_groups_response",
        "TerminalGroupsResponse",
        terminal_groups=[group],
        terminal_groups_in_sleep=[],
    )


def _minimal_response(operation_id: str) -> object:
    if operation_id == "get_organizations":
        return _organization_response(ORGANIZATION_ID)
    if operation_id == "get_terminal_groups":
        return _model(
            "terminal_groups_response",
            "TerminalGroupsResponse",
            terminal_groups=[],
            terminal_groups_in_sleep=[],
        )
    module_name, class_name = RESPONSE_MODELS[operation_id]
    if operation_id == "get_cities":
        return _model(module_name, class_name, cities=[])
    if operation_id == "get_regions":
        return _model(module_name, class_name, regions=[])
    if operation_id == "get_streets_by_city":
        return _model(module_name, class_name, streets=[])
    if operation_id == "get_streets_by_id":
        return _model(module_name, class_name, streets=[])
    return _model(module_name, class_name)


def test_foundation_registry_has_exact_operations_and_builds_one_valid_plan() -> None:
    cases = _all_cases()

    assert {case.operation_id for case in cases} == FOUNDATION_IDS
    assert len(cases) == len(FOUNDATION_IDS)
    assert set(ReadPlan.build(cases).ordered_operation_ids) == FOUNDATION_IDS


def test_exact_foundation_and_address_dependencies() -> None:
    organizations = _case("get_organizations")
    assert organizations.depends_on == ()
    assert organizations.requires == ("profile_organization_id",)
    assert organizations.provides == ("organization_id",)

    for operation_id in {
        "get_cancel_causes",
        "get_command_status",
        "get_delivery_order_types",
        "get_discounts",
        "get_marketing_sources",
        "get_organization_settings",
        "get_payment_types",
        "get_removal_types",
        "get_webhook_settings",
    }:
        case = _case(operation_id)
        assert case.depends_on == ("get_organizations",)
        assert "organization_id" in case.requires

    terminal_groups = _case("get_terminal_groups")
    assert terminal_groups.depends_on == ("get_organizations",)
    assert terminal_groups.requires == (
        "organization_id",
        "profile_terminal_group_id",
    )
    assert terminal_groups.provides == ("terminal_group_id",)

    availability = _case("check_terminal_groups_availability")
    assert availability.depends_on == ("get_terminal_groups",)
    assert availability.requires == ("organization_id", "terminal_group_id")

    assert _case("get_tips_types").depends_on == ()
    assert _case("list_organizations").depends_on == ()
    assert _case("get_cities").depends_on == ("get_organizations",)
    assert _case("get_cities").provides == ("city_id",)
    assert _case("get_regions").depends_on == ("get_organizations",)
    assert _case("get_streets_by_city").depends_on == ("get_cities",)
    assert _case("get_streets_by_city").requires == (
        "organization_id",
        "city_id",
    )
    assert _case("get_streets_by_city").provides == ("street_id",)
    assert _case("get_streets_by_id").depends_on == ("get_streets_by_city",)
    assert _case("get_streets_by_id").requires == (
        "organization_id",
        "street_id",
    )


@pytest.mark.parametrize("operation_id", sorted(FOUNDATION_IDS))
def test_bindings_resolve_and_validators_require_exact_response_models(
    operation_id: str,
) -> None:
    case = _case(operation_id)

    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id), _view(case))

    private_marker = "must-not-appear"
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": private_marker}, _view(case))

    assert str(raised.value) == "assertion_failed"
    assert private_marker not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_every_request_has_the_exact_bounded_generated_json_shape() -> None:
    organization = str(ORGANIZATION_ID)
    terminal = str(TERMINAL_GROUP_ID)
    expected = {
        "get_cancel_causes": {"organizationIds": [organization]},
        "get_cities": {
            "includeDeleted": False,
            "organizationIds": [organization],
        },
        "get_delivery_order_types": {"organizationIds": [organization]},
        "get_discounts": {"organizationIds": [organization]},
        "get_marketing_sources": {"organizationIds": [organization]},
        "get_organization_settings": {"organizationIds": [organization]},
        "get_organizations": {
            "includeDisabled": False,
            "organizationIds": [organization],
            "returnAdditionalInfo": False,
        },
        "get_payment_types": {"organizationIds": [organization]},
        "get_regions": {"organizationIds": [organization]},
        "get_removal_types": {"organizationIds": [organization]},
        "get_terminal_groups": {
            "includeDisabled": False,
            "organizationIds": [organization],
        },
        "check_terminal_groups_availability": {
            "organizationIds": [organization],
            "terminalGroupIds": [terminal],
        },
        "get_webhook_settings": {"organizationId": organization},
        "get_streets_by_city": {
            "cityId": str(CITY_ID),
            "includeDeleted": False,
            "organizationId": organization,
        },
        "get_streets_by_id": {
            "ids": [str(STREET_ID)],
            "organizationId": organization,
        },
    }

    for operation_id, expected_json in expected.items():
        case = _case(operation_id)
        values = case.build_values(_view(case, with_terminal=True))
        request = build_generated_request(case.binding, values)
        assert request is not None
        assert request.model_dump(  # type: ignore[attr-defined]
            by_alias=True,
            exclude_none=True,
            mode="json",
        ) == expected_json


@pytest.mark.parametrize("operation_id", ["get_tips_types", "list_organizations"])
def test_no_body_operations_use_the_single_no_request_sentinel(
    operation_id: str,
) -> None:
    case = _case(operation_id)

    assert case.binding.request_module is None
    assert case.binding.request_class is None
    assert case.binding.request_keyword is None
    assert case.build_values(ContextView({})) is NO_REQUEST


def test_command_and_terminal_targets_fail_before_request_construction() -> None:
    command = _case("get_command_status")
    with pytest.raises(NoLiveTarget) as missing_command:
        command.build_values(_view(command))
    assert missing_command.value.code is NoLiveTargetCode.COMMAND
    assert command.allowed_no_target_codes == frozenset({NoLiveTargetCode.COMMAND})

    availability = _case("check_terminal_groups_availability")
    with pytest.raises(NoLiveTarget) as missing_terminal:
        availability.build_values(_view(availability))
    assert missing_terminal.value.code is NoLiveTargetCode.TERMINAL_GROUP
    assert availability.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.TERMINAL_GROUP}
    )


def test_organization_is_published_only_after_target_is_returned() -> None:
    case = _case("get_organizations")
    view = _view(case)
    matching = _organization_response(ORGANIZATION_ID)

    case.validate_response(matching, view)
    assert case.extract(matching, view) == {"organization_id": ORGANIZATION_ID}

    missing = _organization_response(OTHER_ORGANIZATION_ID)
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(missing, view)
    assert case.extract(missing, view) == {}


def test_optional_terminal_target_is_validated_before_it_is_published() -> None:
    case = _case("get_terminal_groups")
    targeted_view = _view(case, with_terminal=True)
    matching = _terminal_response(ORGANIZATION_ID, TERMINAL_GROUP_ID)

    case.validate_response(matching, targeted_view)
    assert case.extract(matching, targeted_view) == {
        "terminal_group_id": TERMINAL_GROUP_ID
    }

    foreign = _terminal_response(OTHER_ORGANIZATION_ID, TERMINAL_GROUP_ID)
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(foreign, targeted_view)
    assert case.extract(foreign, targeted_view) == {}

    untargeted_view = _view(case)
    empty = _minimal_response("get_terminal_groups")
    case.validate_response(empty, untargeted_view)
    assert case.extract(empty, untargeted_view) == {}


def test_empty_city_and_street_results_are_valid_and_gate_dependents() -> None:
    cities = _case("get_cities")
    empty_cities = _minimal_response("get_cities")
    cities.validate_response(empty_cities, _view(cities))
    assert cities.extract(empty_cities, _view(cities)) == {}

    by_city = _case("get_streets_by_city")
    with pytest.raises(NoLiveTarget) as missing_city:
        by_city.build_values(ContextView({"organization_id": ORGANIZATION_ID}))
    assert missing_city.value.code is NoLiveTargetCode.CITY

    empty_streets = _minimal_response("get_streets_by_city")
    by_city.validate_response(empty_streets, _view(by_city))
    assert by_city.extract(empty_streets, _view(by_city)) == {}

    by_id = _case("get_streets_by_id")
    with pytest.raises(NoLiveTarget) as missing_street:
        by_id.build_values(ContextView({"organization_id": ORGANIZATION_ID}))
    assert missing_street.value.code is NoLiveTargetCode.STREET


def test_first_city_and_street_ids_are_extracted_from_typed_responses() -> None:
    city = _model(
        "address_directory_city",
        "AddressDirectoryCity",
        id=CITY_ID,
    )
    city_group = _model(
        "rms_city_items_response",
        "RmsCityItemsResponse",
        organization_id=ORGANIZATION_ID,
        items=[city],
    )
    cities_response = _model(
        "cities_response",
        "CitiesResponse",
        cities=[city_group],
    )
    cities = _case("get_cities")
    assert cities.extract(cities_response, _view(cities)) == {"city_id": CITY_ID}

    street = _model("address_street", "AddressStreet", id=STREET_ID)
    streets_response = _model(
        "streets_response",
        "StreetsResponse",
        streets=[street],
    )
    streets = _case("get_streets_by_city")
    assert streets.extract(streets_response, _view(streets)) == {
        "street_id": STREET_ID
    }


def test_webhook_auth_token_is_never_extracted_or_rendered_on_failure() -> None:
    case = _case("get_webhook_settings")
    private_marker = "private-webhook-token"
    response = _model(
        "get_web_hook_settings_response",
        "GetWebHookSettingsResponse",
        auth_token=private_marker,
    )

    case.validate_response(response, _view(case))
    assert case.extract(response, _view(case)) == {}

    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"authToken": private_marker}, _view(case))
    assert private_marker not in str(raised.value)
    assert private_marker not in repr(raised.value)


def test_case_module_exports_are_immutable_tuples() -> None:
    assert type(FOUNDATION_CASES) is tuple
    assert type(ADDRESS_CASES) is tuple
    with pytest.raises(TypeError):
        FOUNDATION_CASES[0] = _case("get_organizations")  # type: ignore[index]
