from __future__ import annotations

import dataclasses
import sys
from collections.abc import Mapping
from enum import Enum
from types import ModuleType
from typing import Any, cast

import pytest

from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    READ_SEED_KEYS,
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    NoRequest,
    ReadAssertionFailure,
    ReadCase,
    ReadContext,
    ReadExtractorFailure,
    ReadFailureCode,
    build_generated_request,
)

EXPECTED_NO_TARGET_CODES = {
    "ENDPOINT": "endpoint_unavailable",
    "CITY": "city_unavailable",
    "STREET": "street_unavailable",
    "TERMINAL_GROUP": "terminal_group_unavailable",
    "PRODUCT": "product_unavailable",
    "COMBO": "combo_unavailable",
    "DELIVERY": "delivery_unavailable",
    "DELIVERY_PHONE": "delivery_phone_unavailable",
    "DELIVERY_REVISION": "delivery_revision_unavailable",
    "DRAFT": "draft_unavailable",
    "RESERVE": "reserve_unavailable",
    "RESTAURANT_SECTION": "restaurant_section_unavailable",
    "TABLE": "table_unavailable",
    "TABLE_ORDER": "table_order_unavailable",
    "EMPLOYEE": "employee_unavailable",
    "EMPLOYEE_ROLE": "employee_role_unavailable",
    "SMS": "sms_unavailable",
    "COMMAND": "command_unavailable",
    "COUPON_SERIES": "coupon_series_unavailable",
    "COUPON": "coupon_unavailable",
    "CUSTOMER": "customer_unavailable",
    "DOCUMENT": "document_unavailable",
    "ACCOUNT": "account_unavailable",
    "STORE": "store_unavailable",
}

EXPECTED_FAILURE_CODES = {
    "DEPENDENCY_FAILED": "dependency_failed",
    "ASSERTION_FAILED": "assertion_failed",
    "EXTRACTOR_FAILED": "extractor_failed",
    "INVOCATION_FAILED": "invocation_failed",
    "HTTP_ERROR": "http_error",
    "TRANSPORT_ERROR": "transport_error",
    "RATE_GUARD_FAILED": "rate_guard_failed",
    "RECEIPT_FAILED": "receipt_failed",
    "REPORT_FAILED": "report_failed",
    "CAPTURE_FAILED": "capture_failed",
    "CANCELLED": "cancelled",
    "SAFETY_INVARIANT": "safety_invariant",
}

EXPECTED_SEED_KEYS = frozenset(
    {
        "profile_organization_id",
        "profile_external_menu_id",
        "profile_terminal_group_id",
        "date_yyyy_mm_dd",
        "period_from_yyyy_mm_dd",
        "period_to_yyyy_mm_dd",
        "window_from_local",
        "window_to_local",
    }
)


def _enum_values(enum: type[Enum]) -> dict[str, object]:
    return {member.name: member.value for member in enum}


def _no_request_binding(**changes: object) -> GeneratedReadBinding:
    values: dict[str, object] = {
        "api_module": "iikocloud_client.api.synthetic_api",
        "api_class": "SyntheticApi",
        "method_name": "synthetic_read_with_http_info",
        "request_module": None,
        "request_class": None,
        "request_keyword": None,
    }
    values.update(changes)
    return GeneratedReadBinding(**cast(Any, values))


def _body_binding(**changes: object) -> GeneratedReadBinding:
    values: dict[str, object] = {
        "api_module": "iikocloud_client.api.synthetic_api",
        "api_class": "SyntheticApi",
        "method_name": "synthetic_read_with_http_info",
        "request_module": "iikocloud_client.models.synthetic_request",
        "request_class": "SyntheticRequest",
        "request_keyword": "synthetic_request",
    }
    values.update(changes)
    return GeneratedReadBinding(**cast(Any, values))


def _case(**changes: object) -> ReadCase:
    values: dict[str, object] = {
        "operation_id": "synthetic_read",
        "revision": 1,
        "depends_on": (),
        "requires": (),
        "provides": (),
        "allowed_no_target_codes": frozenset(),
        "binding": _no_request_binding(),
        "build_values": lambda _view: NO_REQUEST,
        "validate_response": lambda _response, _view: None,
        "extract": lambda _response, _view: {},
    }
    values.update(changes)
    return ReadCase(**cast(Any, values))


def _install_synthetic_generated_modules(
    monkeypatch: pytest.MonkeyPatch,
    *,
    api_class: object,
    request_class: object,
) -> None:
    package_names = (
        "iikocloud_client",
        "iikocloud_client.api",
        "iikocloud_client.models",
    )
    for package_name in package_names:
        package = ModuleType(package_name)
        package.__path__ = []  # type: ignore[attr-defined]
        monkeypatch.setitem(sys.modules, package_name, package)

    api_module = ModuleType("iikocloud_client.api.synthetic_api")
    api_module.SyntheticApi = api_class  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, api_module.__name__, api_module)

    request_module = ModuleType("iikocloud_client.models.synthetic_request")
    request_module.SyntheticRequest = request_class  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, request_module.__name__, request_module)


def test_exact_enums_and_seed_keys() -> None:
    assert issubclass(NoLiveTargetCode, str)
    assert issubclass(ReadFailureCode, str)
    assert _enum_values(NoLiveTargetCode) == EXPECTED_NO_TARGET_CODES
    assert _enum_values(ReadFailureCode) == EXPECTED_FAILURE_CODES
    assert READ_SEED_KEYS == EXPECTED_SEED_KEYS


def test_context_view_is_declared_only_immutable_and_redacted() -> None:
    organization = object()
    terminal_group = object()
    source = {
        "organization_id": organization,
        "terminal_group_id": terminal_group,
    }
    context = ReadContext.seed(source)
    source.clear()

    view = context.view(("organization_id",))

    assert isinstance(view, ContextView)
    assert isinstance(view, Mapping)
    assert tuple(view) == ("organization_id",)
    assert view["organization_id"] is organization
    assert "terminal_group_id" not in view
    with pytest.raises(KeyError):
        _ = view["terminal_group_id"]
    with pytest.raises(TypeError):
        cast(Any, view)["organization_id"] = terminal_group
    assert "object" not in repr(context)
    assert "object" not in repr(view)


def test_direct_read_context_construction_owns_and_validates_mapping() -> None:
    supplied_value = object()
    backing = {"organization_id": supplied_value}
    context = ReadContext(backing)

    backing.clear()

    assert context.view(("organization_id",))["organization_id"] is supplied_value
    with pytest.raises(AttributeError):
        cast(Any, context)._values = {}
    with pytest.raises((TypeError, ValueError)):
        ReadContext({"unsafe-key": supplied_value})
    assert "object" not in repr(context)


def test_direct_context_view_construction_is_proxied_and_validated() -> None:
    supplied_value = object()
    backing = {"organization_id": supplied_value}
    view = ContextView(backing)

    backing.clear()

    assert tuple(view) == ("organization_id",)
    assert view["organization_id"] is supplied_value
    with pytest.raises(TypeError):
        cast(Any, view)["organization_id"] = object()
    with pytest.raises(AttributeError):
        cast(Any, view)._values = {}
    with pytest.raises((TypeError, ValueError)):
        ContextView({"unsafe-key": supplied_value})
    assert "object" not in repr(view)


def test_context_types_cannot_be_traversed_by_dataclasses_asdict() -> None:
    supplied_value = "supplied-live-value"
    context = ReadContext({"organization_id": supplied_value})
    view = ContextView({"organization_id": supplied_value})

    assert not dataclasses.is_dataclass(context)
    assert not dataclasses.is_dataclass(view)
    with pytest.raises(TypeError):
        dataclasses.asdict(context)
    with pytest.raises(TypeError):
        dataclasses.asdict(view)
    assert supplied_value not in repr(context)
    assert supplied_value not in repr(view)


@pytest.mark.parametrize("key", ["", "unsafe-key", "with.dot", "_private", "UpperCase"])
def test_context_rejects_unsafe_keys(key: str) -> None:
    with pytest.raises((TypeError, ValueError)):
        ReadContext.seed({key: object()})


def test_context_view_rejects_duplicate_declared_keys() -> None:
    context = ReadContext.seed({"organization_id": object()})

    with pytest.raises((TypeError, ValueError)):
        context.view(("organization_id", "organization_id"))


def test_context_apply_rejects_undeclared_extractor_output() -> None:
    context = ReadContext.seed({})
    case = _case(provides=("organization_id",))

    with pytest.raises((TypeError, ValueError)):
        context.apply(case, {"terminal_group_id": object()})


def test_context_apply_rejects_overwrite_but_allows_equal_immutable_value() -> None:
    context = ReadContext.seed({"organization_id": ("stable",)})
    case = _case(provides=("organization_id",))

    context.apply(case, {"organization_id": ("stable",)})
    with pytest.raises((TypeError, ValueError)):
        context.apply(case, {"organization_id": ("different",)})

    assert context.view(("organization_id",))["organization_id"] == ("stable",)


@pytest.mark.parametrize("revision", [0, -1])
def test_read_case_rejects_non_positive_revision(revision: int) -> None:
    with pytest.raises((TypeError, ValueError)):
        _case(revision=revision)


@pytest.mark.parametrize(
    ("field", "values"),
    [
        ("depends_on", ("first_read", "first_read")),
        ("requires", ("organization_id", "organization_id")),
        ("provides", ("terminal_group_id", "terminal_group_id")),
    ],
)
def test_read_case_rejects_duplicate_tuple_members(field: str, values: tuple[str, ...]) -> None:
    with pytest.raises((TypeError, ValueError)):
        _case(**{field: values})


@pytest.mark.parametrize(
    ("field", "values"),
    [
        ("depends_on", ("../first",)),
        ("requires", ("unsafe-key",)),
        ("provides", ("_private",)),
    ],
)
def test_read_case_rejects_unsafe_names(field: str, values: tuple[str, ...]) -> None:
    with pytest.raises((TypeError, ValueError)):
        _case(**{field: values})


@pytest.mark.parametrize(
    "changes",
    [
        {"request_module": "iikocloud_client.models.synthetic_request"},
        {"request_class": "SyntheticRequest"},
        {"request_keyword": "synthetic_request"},
        {
            "request_module": "iikocloud_client.models.synthetic_request",
            "request_class": "SyntheticRequest",
        },
        {
            "request_module": "iikocloud_client.models.synthetic_request",
            "request_keyword": "synthetic_request",
        },
        {"request_class": "SyntheticRequest", "request_keyword": "synthetic_request"},
    ],
)
def test_generated_binding_requires_request_triple_all_null_or_all_present(
    changes: dict[str, object],
) -> None:
    with pytest.raises((TypeError, ValueError)):
        _no_request_binding(**changes)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("api_module", "outside.api.synthetic_api"),
        ("api_module", "iikocloud_client.api"),
        ("api_module", "iikocloud_client.api.synthetic-api"),
        ("api_class", "SyntheticApi.member"),
        ("api_class", "_SyntheticApi"),
        ("method_name", "synthetic_read"),
        ("method_name", "_synthetic_read_with_http_info"),
    ],
)
def test_generated_binding_rejects_unsafe_api_names(field: str, value: str) -> None:
    with pytest.raises((TypeError, ValueError)):
        _no_request_binding(**{field: value})


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("request_module", "outside.models.synthetic_request"),
        ("request_module", "iikocloud_client.models"),
        ("request_module", "iikocloud_client.models.synthetic-request"),
        ("request_class", "SyntheticRequest.member"),
        ("request_class", "_SyntheticRequest"),
        ("request_keyword", "request-keyword"),
        ("request_keyword", "_request"),
    ],
)
def test_generated_binding_rejects_unsafe_request_names(field: str, value: str) -> None:
    with pytest.raises((TypeError, ValueError)):
        _body_binding(**{field: value})


def test_read_case_requires_exact_generated_method_name() -> None:
    with pytest.raises((TypeError, ValueError)):
        _case(binding=_no_request_binding(method_name="other_read_with_http_info"))


def test_no_request_is_frozen_and_slotted() -> None:
    assert isinstance(NO_REQUEST, NoRequest)
    with pytest.raises((dataclasses.FrozenInstanceError, AttributeError, TypeError)):
        cast(Any, NO_REQUEST).value = "live-value"
    with pytest.raises(TypeError):
        vars(NO_REQUEST)


def test_fixed_code_exceptions_reject_free_form_live_values() -> None:
    no_target = NoLiveTarget(NoLiveTargetCode.CITY)
    assertion = ReadAssertionFailure()
    extractor = ReadExtractorFailure()

    assert no_target.code is NoLiveTargetCode.CITY
    assert str(no_target) == "city_unavailable"
    assert str(assertion) == "assertion_failed"
    assert str(extractor) == "extractor_failed"
    with pytest.raises(TypeError):
        NoLiveTarget(cast(Any, "supplied-live-value"))
    with pytest.raises(TypeError):
        ReadAssertionFailure(cast(Any, "supplied-live-value"))
    with pytest.raises(TypeError):
        ReadExtractorFailure(cast(Any, "supplied-live-value"))


def test_generated_binding_resolves_classes_and_request_keyword_lazily(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class SyntheticApi:
        def synthetic_read_with_http_info(self, *, synthetic_request: object) -> None:
            del synthetic_request

    class SyntheticRequest:
        @classmethod
        def model_validate(cls, values: object) -> object:
            return values

    binding = _body_binding()
    _install_synthetic_generated_modules(
        monkeypatch,
        api_class=SyntheticApi,
        request_class=SyntheticRequest,
    )

    resolved = binding.resolve()

    assert resolved.api_class is SyntheticApi
    assert resolved.request_class is SyntheticRequest
    assert resolved.method is SyntheticApi.synthetic_read_with_http_info


def test_generated_binding_rejects_missing_method(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class SyntheticApi:
        pass

    class SyntheticRequest:
        pass

    _install_synthetic_generated_modules(
        monkeypatch,
        api_class=SyntheticApi,
        request_class=SyntheticRequest,
    )

    with pytest.raises(Exception, match="^[a-z_ ]+$"):
        _body_binding().resolve()


def test_generated_binding_rejects_missing_request_keyword(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class SyntheticApi:
        def synthetic_read_with_http_info(self, *, other_request: object) -> None:
            del other_request

    class SyntheticRequest:
        pass

    _install_synthetic_generated_modules(
        monkeypatch,
        api_class=SyntheticApi,
        request_class=SyntheticRequest,
    )

    with pytest.raises(Exception, match="^[a-z_ ]+$"):
        _body_binding().resolve()


def test_build_generated_request_returns_none_only_for_no_request() -> None:
    assert build_generated_request(_no_request_binding(), NO_REQUEST) is None

    with pytest.raises((TypeError, ValueError)):
        build_generated_request(_no_request_binding(), {})
    with pytest.raises((TypeError, ValueError)):
        build_generated_request(_body_binding(), NO_REQUEST)


def test_build_generated_request_calls_model_validate_with_a_detached_dict(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: list[dict[str, object]] = []

    class SyntheticApi:
        def synthetic_read_with_http_info(self, *, synthetic_request: object) -> None:
            del synthetic_request

    class SyntheticRequest:
        @classmethod
        def model_validate(cls, values: object) -> object:
            assert type(values) is dict
            seen.append(cast(dict[str, object], values))
            return cls()

    _install_synthetic_generated_modules(
        monkeypatch,
        api_class=SyntheticApi,
        request_class=SyntheticRequest,
    )
    values = {"organization_id": object()}

    request = build_generated_request(_body_binding(), values)
    values.clear()

    assert isinstance(request, SyntheticRequest)
    assert tuple(seen[0]) == ("organization_id",)


def test_build_generated_request_redacts_all_validation_failures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class SyntheticApi:
        def synthetic_read_with_http_info(self, *, synthetic_request: object) -> None:
            del synthetic_request

    class SyntheticRequest:
        @classmethod
        def model_validate(cls, values: object) -> object:
            del values
            raise ValueError("supplied-live-value")

    _install_synthetic_generated_modules(
        monkeypatch,
        api_class=SyntheticApi,
        request_class=SyntheticRequest,
    )

    with pytest.raises(Exception) as raised:
        build_generated_request(
            _body_binding(),
            {"organization_id": "supplied-live-value"},
        )

    assert type(raised.value).__name__ == "SafetyError"
    assert str(raised.value) == "Generated read request validation failed"
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None
