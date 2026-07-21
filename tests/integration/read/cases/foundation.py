"""Foundational guarded read cases for organizations and dictionaries."""

from __future__ import annotations

import importlib
from collections.abc import Callable, Mapping
from uuid import UUID

from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    NoRequest,
    ReadAssertionFailure,
    ReadCase,
)


def _binding(
    operation_id: str,
    api_module: str,
    api_class: str,
    *,
    request_module: str | None,
    request_class: str | None,
    request_keyword: str | None,
) -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module=f"iikocloud_client.api.{api_module}",
        api_class=api_class,
        method_name=f"{operation_id}_with_http_info",
        request_module=(
            f"iikocloud_client.models.{request_module}"
            if request_module is not None
            else None
        ),
        request_class=request_class,
        request_keyword=request_keyword,
    )


def _is_exact_model(response: object, module_name: str, class_name: str) -> bool:
    try:
        module = importlib.import_module(f"iikocloud_client.models.{module_name}")
        model = getattr(module, class_name, None)
        valid = isinstance(model, type) and type(response) is model
    except Exception:
        valid = False
    return valid


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


def _build_get_organizations(view: ContextView) -> Mapping[str, object]:
    return {
        "include_disabled": False,
        "organization_ids": [view["profile_organization_id"]],
        "return_additional_info": False,
    }


def _uuid(value: object) -> UUID | None:
    if type(value) is UUID:
        return value
    if type(value) is not str:
        return None
    try:
        parsed = UUID(value)
    except (TypeError, ValueError, AttributeError):
        return None
    return parsed


def _matching_organization_id(
    response: object,
    view: ContextView,
) -> UUID | None:
    target = _uuid(view.get("profile_organization_id"))
    if target is None:
        return None
    try:
        organizations = response.organizations  # type: ignore[attr-defined]
    except Exception:
        return None
    if type(organizations) is not list:
        return None
    for organization in organizations:
        try:
            candidate = organization.id
        except Exception:
            continue
        if type(candidate) is UUID and candidate == target:
            return candidate
    return None


def _validate_organizations(response: object, view: ContextView) -> None:
    valid_type = _is_exact_model(
        response,
        "get_organizations_response",
        "GetOrganizationsResponse",
    )
    if not valid_type or _matching_organization_id(response, view) is None:
        raise ReadAssertionFailure()


def _extract_organization(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    organization_id = _matching_organization_id(response, view)
    if organization_id is None:
        return {}
    return {"organization_id": organization_id}


def _build_terminal_groups(view: ContextView) -> Mapping[str, object]:
    return {
        "include_disabled": False,
        "organization_ids": [view["organization_id"]],
    }


def _matching_terminal_group_id(
    response: object,
    view: ContextView,
) -> UUID | None:
    organization_id = _uuid(view.get("organization_id"))
    terminal_group_id = _uuid(view.get("profile_terminal_group_id"))
    if organization_id is None or terminal_group_id is None:
        return None
    try:
        collections = (
            response.terminal_groups,  # type: ignore[attr-defined]
            response.terminal_groups_in_sleep,  # type: ignore[attr-defined]
        )
    except Exception:
        return None
    for groups in collections:
        if type(groups) is not list:
            return None
        for group in groups:
            try:
                group_organization_id = group.organization_id
                items = group.items
            except Exception:
                continue
            if group_organization_id != organization_id or type(items) is not list:
                continue
            for terminal in items:
                try:
                    candidate_id = terminal.id
                    candidate_organization_id = terminal.organization_id
                except Exception:
                    continue
                if (
                    type(candidate_id) is UUID
                    and candidate_id == terminal_group_id
                    and candidate_organization_id == organization_id
                ):
                    return candidate_id
    return None


def _validate_terminal_groups(response: object, view: ContextView) -> None:
    if not _is_exact_model(
        response,
        "terminal_groups_response",
        "TerminalGroupsResponse",
    ):
        raise ReadAssertionFailure()
    if "profile_terminal_group_id" not in view:
        return
    if _matching_terminal_group_id(response, view) is None:
        raise ReadAssertionFailure()


def _extract_terminal_group(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    if "profile_terminal_group_id" not in view:
        return {}
    terminal_group_id = _matching_terminal_group_id(response, view)
    if terminal_group_id is None:
        return {}
    return {"terminal_group_id": terminal_group_id}


def _build_terminal_availability(view: ContextView) -> Mapping[str, object]:
    if "terminal_group_id" not in view:
        raise NoLiveTarget(NoLiveTargetCode.TERMINAL_GROUP)
    return {
        "organization_ids": [view["organization_id"]],
        "terminal_group_ids": [view["terminal_group_id"]],
    }


def _build_command_status(_view: ContextView) -> Mapping[str, object]:
    raise NoLiveTarget(NoLiveTargetCode.COMMAND)


def _build_webhook_settings(view: ContextView) -> Mapping[str, object]:
    return {"organization_id": view["organization_id"]}


def _case(
    operation_id: str,
    api_module: str,
    api_class: str,
    response_module: str,
    response_class: str,
    *,
    request_module: str | None,
    request_class: str | None,
    request_keyword: str | None,
    depends_on: tuple[str, ...] = ("get_organizations",),
    requires: tuple[str, ...] = ("organization_id",),
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
    build_values: Callable[
        [ContextView], Mapping[str, object] | NoRequest
    ] = _organization_ids,
    validate_response: Callable[
        [object, ContextView], None
    ] | None = None,
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
            request_module=request_module,
            request_class=request_class,
            request_keyword=request_keyword,
        ),
        build_values=build_values,
        validate_response=validator,
        extract=extract,
    )


FOUNDATION_CASES = (
    _case(
        "get_organizations",
        "organizations_api",
        "OrganizationsApi",
        "get_organizations_response",
        "GetOrganizationsResponse",
        request_module="get_organizations_request",
        request_class="GetOrganizationsRequest",
        request_keyword="get_organizations_request",
        depends_on=(),
        requires=("profile_organization_id",),
        provides=("organization_id",),
        build_values=_build_get_organizations,
        validate_response=_validate_organizations,
        extract=_extract_organization,
    ),
    _case(
        "list_organizations",
        "deprecated_api",
        "DeprecatedApi",
        "get_simple_organizations_response",
        "GetSimpleOrganizationsResponse",
        request_module=None,
        request_class=None,
        request_keyword=None,
        depends_on=(),
        requires=(),
        build_values=lambda _view: NO_REQUEST,
    ),
    _case(
        "get_tips_types",
        "dictionaries_api",
        "DictionariesApi",
        "tips_types_response",
        "TipsTypesResponse",
        request_module=None,
        request_class=None,
        request_keyword=None,
        depends_on=(),
        requires=(),
        build_values=lambda _view: NO_REQUEST,
    ),
    _case(
        "get_cancel_causes",
        "dictionaries_api",
        "DictionariesApi",
        "cancel_causes_response",
        "CancelCausesResponse",
        request_module="cancel_causes_request",
        request_class="CancelCausesRequest",
        request_keyword="cancel_causes_request",
    ),
    _case(
        "get_delivery_order_types",
        "dictionaries_api",
        "DictionariesApi",
        "order_types_response",
        "OrderTypesResponse",
        request_module="order_types_request",
        request_class="OrderTypesRequest",
        request_keyword="order_types_request",
    ),
    _case(
        "get_discounts",
        "dictionaries_api",
        "DictionariesApi",
        "discounts_response",
        "DiscountsResponse",
        request_module="discounts_request",
        request_class="DiscountsRequest",
        request_keyword="discounts_request",
    ),
    _case(
        "get_marketing_sources",
        "marketing_sources_api",
        "MarketingSourcesApi",
        "marketing_sources_response",
        "MarketingSourcesResponse",
        request_module="marketing_sources_request",
        request_class="MarketingSourcesRequest",
        request_keyword="marketing_sources_request",
    ),
    _case(
        "get_organization_settings",
        "organizations_api",
        "OrganizationsApi",
        "organizations_settings_response",
        "OrganizationsSettingsResponse",
        request_module="organizations_settings_request",
        request_class="OrganizationsSettingsRequest",
        request_keyword="organizations_settings_request",
    ),
    _case(
        "get_payment_types",
        "dictionaries_api",
        "DictionariesApi",
        "payment_types_response",
        "PaymentTypesResponse",
        request_module="payment_types_request",
        request_class="PaymentTypesRequest",
        request_keyword="payment_types_request",
    ),
    _case(
        "get_removal_types",
        "dictionaries_api",
        "DictionariesApi",
        "removal_types_response",
        "RemovalTypesResponse",
        request_module="removal_types_request",
        request_class="RemovalTypesRequest",
        request_keyword="removal_types_request",
    ),
    _case(
        "get_terminal_groups",
        "terminal_groups_api",
        "TerminalGroupsApi",
        "terminal_groups_response",
        "TerminalGroupsResponse",
        request_module="terminal_groups_request",
        request_class="TerminalGroupsRequest",
        request_keyword="terminal_groups_request",
        requires=("organization_id", "profile_terminal_group_id"),
        provides=("terminal_group_id",),
        build_values=_build_terminal_groups,
        validate_response=_validate_terminal_groups,
        extract=_extract_terminal_group,
    ),
    _case(
        "check_terminal_groups_availability",
        "terminal_groups_api",
        "TerminalGroupsApi",
        "terminal_groups_is_alive_response",
        "TerminalGroupsIsAliveResponse",
        request_module="terminal_groups_is_alive_request",
        request_class="TerminalGroupsIsAliveRequest",
        request_keyword="terminal_groups_is_alive_request",
        depends_on=("get_terminal_groups",),
        requires=("organization_id", "terminal_group_id"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.TERMINAL_GROUP}),
        build_values=_build_terminal_availability,
    ),
    _case(
        "get_command_status",
        "operations_api",
        "OperationsApi",
        "get_command_status_response",
        "GetCommandStatusResponse",
        request_module="get_command_status_request",
        request_class="GetCommandStatusRequest",
        request_keyword="get_command_status_request",
        allowed_no_target_codes=frozenset({NoLiveTargetCode.COMMAND}),
        build_values=_build_command_status,
    ),
    _case(
        "get_webhook_settings",
        "webhooks_api",
        "WebhooksApi",
        "get_web_hook_settings_response",
        "GetWebHookSettingsResponse",
        request_module="get_web_hook_settings_request",
        request_class="GetWebHookSettingsRequest",
        request_keyword="get_web_hook_settings_request",
        build_values=_build_webhook_settings,
    ),
)

__all__ = ["FOUNDATION_CASES"]
