"""Typed, fail-closed descriptors for guarded live read operations."""

from __future__ import annotations

import importlib
import inspect
import re
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType
from typing import Final

from tools.openapi_pipeline.errors import SafetyError


class ReadCapability(str, Enum):
    PUBLIC_API_INVOICE_PROCESSING = "public_api_invoice_processing"


class NoLiveTargetCode(str, Enum):
    ENDPOINT = "endpoint_unavailable"
    CITY = "city_unavailable"
    STREET = "street_unavailable"
    TERMINAL_GROUP = "terminal_group_unavailable"
    PRODUCT = "product_unavailable"
    COMBO = "combo_unavailable"
    DELIVERY = "delivery_unavailable"
    DELIVERY_PHONE = "delivery_phone_unavailable"
    DELIVERY_REVISION = "delivery_revision_unavailable"
    DRAFT = "draft_unavailable"
    RESERVE = "reserve_unavailable"
    RESTAURANT_SECTION = "restaurant_section_unavailable"
    TABLE = "table_unavailable"
    TABLE_ORDER = "table_order_unavailable"
    EMPLOYEE = "employee_unavailable"
    EMPLOYEE_ROLE = "employee_role_unavailable"
    SMS = "sms_unavailable"
    COMMAND = "command_unavailable"
    COUPON_SERIES = "coupon_series_unavailable"
    COUPON = "coupon_unavailable"
    CUSTOMER = "customer_unavailable"
    DOCUMENT = "document_unavailable"
    ACCOUNT = "account_unavailable"
    STORE = "store_unavailable"
    INVOICE_PROCESSING = "invoice_processing_unavailable"


_CAPABILITY_NO_TARGET_CODES: Final[Mapping[ReadCapability, NoLiveTargetCode]] = (
    MappingProxyType(
        {
            ReadCapability.PUBLIC_API_INVOICE_PROCESSING: (
                NoLiveTargetCode.INVOICE_PROCESSING
            ),
        }
    )
)


def no_target_code_for_read_capability(
    capability: ReadCapability,
) -> NoLiveTargetCode:
    if type(capability) is not ReadCapability:
        raise TypeError("capability must be a ReadCapability")
    return _CAPABILITY_NO_TARGET_CODES[capability]


class ReadFailureCode(str, Enum):
    DEPENDENCY_FAILED = "dependency_failed"
    ASSERTION_FAILED = "assertion_failed"
    EXTRACTOR_FAILED = "extractor_failed"
    INVOCATION_FAILED = "invocation_failed"
    HTTP_ERROR = "http_error"
    TRANSPORT_ERROR = "transport_error"
    RATE_GUARD_FAILED = "rate_guard_failed"
    RECEIPT_FAILED = "receipt_failed"
    REPORT_FAILED = "report_failed"
    CAPTURE_FAILED = "capture_failed"
    CANCELLED = "cancelled"
    SAFETY_INVARIANT = "safety_invariant"


READ_SEED_KEYS: Final[frozenset[str]] = frozenset(
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

_SAFE_VALUE_NAME = re.compile(r"[a-z][a-z0-9_]*\Z")
_SAFE_CLASS_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z")
_API_MODULE_PREFIX = "iikocloud_client.api."
_REQUEST_MODULE_PREFIX = "iikocloud_client.models."


def _require_safe_value_name(value: object, *, field_name: str) -> str:
    if type(value) is not str:
        raise TypeError(f"{field_name} must be a string")
    if _SAFE_VALUE_NAME.fullmatch(value) is None:
        raise ValueError(f"{field_name} is unsafe")
    return value


def _require_safe_class_name(value: object, *, field_name: str) -> str:
    if type(value) is not str:
        raise TypeError(f"{field_name} must be a string")
    if _SAFE_CLASS_NAME.fullmatch(value) is None:
        raise ValueError(f"{field_name} is unsafe")
    return value


def _require_safe_module(value: object, *, prefix: str, field_name: str) -> str:
    if type(value) is not str:
        raise TypeError(f"{field_name} must be a string")
    if not value.startswith(prefix):
        raise ValueError(f"{field_name} has an unsafe prefix")
    suffix = value.removeprefix(prefix)
    if not suffix or any(
        _SAFE_VALUE_NAME.fullmatch(component) is None
        for component in suffix.split(".")
    ):
        raise ValueError(f"{field_name} is unsafe")
    return value


def _require_unique_names(values: object, *, field_name: str) -> tuple[str, ...]:
    if type(values) is not tuple:
        raise TypeError(f"{field_name} must be a tuple")
    checked = tuple(
        _require_safe_value_name(value, field_name=field_name) for value in values
    )
    if len(set(checked)) != len(checked):
        raise ValueError(f"{field_name} contains duplicates")
    return checked


@dataclass(frozen=True, slots=True)
class _ResolvedGeneratedReadBinding:
    api_class: type[object]
    request_class: type[object] | None
    method: Callable[..., object]


@dataclass(frozen=True, slots=True)
class GeneratedReadBinding:
    api_module: str
    api_class: str
    method_name: str
    request_module: str | None
    request_class: str | None
    request_keyword: str | None

    def __post_init__(self) -> None:
        _require_safe_module(
            self.api_module,
            prefix=_API_MODULE_PREFIX,
            field_name="api_module",
        )
        _require_safe_class_name(self.api_class, field_name="api_class")
        method_name = _require_safe_value_name(
            self.method_name,
            field_name="method_name",
        )
        if not method_name.endswith("_with_http_info"):
            raise ValueError("method_name must end with _with_http_info")

        request_fields = (
            self.request_module,
            self.request_class,
            self.request_keyword,
        )
        populated_count = sum(value is not None for value in request_fields)
        if populated_count not in (0, 3):
            raise ValueError("request binding fields must be all null or all present")
        if populated_count == 3:
            _require_safe_module(
                self.request_module,
                prefix=_REQUEST_MODULE_PREFIX,
                field_name="request_module",
            )
            _require_safe_class_name(self.request_class, field_name="request_class")
            _require_safe_value_name(
                self.request_keyword,
                field_name="request_keyword",
            )

    def resolve(self) -> _ResolvedGeneratedReadBinding:
        """Resolve and validate generated types without importing them eagerly."""

        # Revalidate before any import so even a forged instance fails closed.
        self.__post_init__()
        try:
            api_module = importlib.import_module(self.api_module)
        except Exception:
            raise SafetyError("generated read api module resolution failed") from None

        api_class = getattr(api_module, self.api_class, None)
        if not inspect.isclass(api_class):
            raise SafetyError("generated read api class resolution failed")
        method = getattr(api_class, self.method_name, None)
        if method is None or not callable(method):
            raise SafetyError("generated read binding method missing")

        try:
            parameters = inspect.signature(method).parameters
        except (TypeError, ValueError):
            raise SafetyError("generated read method signature unavailable") from None

        request_class: type[object] | None = None
        if self.request_module is not None:
            # __post_init__ proved that the complete request triple is present.
            assert self.request_class is not None
            assert self.request_keyword is not None
            if self.request_keyword not in parameters:
                raise SafetyError("generated read request keyword missing")
            try:
                request_module = importlib.import_module(self.request_module)
            except Exception:
                raise SafetyError(
                    "generated read request module resolution failed"
                ) from None
            candidate = getattr(request_module, self.request_class, None)
            if not inspect.isclass(candidate):
                raise SafetyError("generated read request class resolution failed")
            if not callable(getattr(candidate, "model_validate", None)):
                raise SafetyError("generated read request validator missing")
            request_class = candidate

        return _ResolvedGeneratedReadBinding(
            api_class=api_class,
            request_class=request_class,
            method=method,
        )


@dataclass(frozen=True, slots=True)
class NoRequest:
    pass


NO_REQUEST: Final[NoRequest] = NoRequest()


class ContextView(Mapping[str, object]):
    __slots__ = ("_values",)

    _values: Mapping[str, object]

    def __init__(self, values: Mapping[str, object]) -> None:
        if not isinstance(values, Mapping):
            raise TypeError("context view values must be a mapping")
        copied: dict[str, object] = {}
        for key, value in values.items():
            safe_key = _require_safe_value_name(key, field_name="context view key")
            copied[safe_key] = value
        object.__setattr__(self, "_values", MappingProxyType(copied))

    def __setattr__(self, name: str, value: object) -> None:
        del name, value
        raise AttributeError("ContextView is immutable")

    def __delattr__(self, name: str) -> None:
        del name
        raise AttributeError("ContextView is immutable")

    def __repr__(self) -> str:
        return "ContextView()"

    def __getitem__(self, key: str) -> object:
        return self._values[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)


@dataclass(frozen=True, slots=True)
class ReadCase:
    operation_id: str
    revision: int
    depends_on: tuple[str, ...]
    requires: tuple[str, ...]
    provides: tuple[str, ...]
    allowed_no_target_codes: frozenset[NoLiveTargetCode]
    binding: GeneratedReadBinding
    build_values: Callable[[ContextView], Mapping[str, object] | NoRequest]
    validate_response: Callable[[object, ContextView], None]
    extract: Callable[[object, ContextView], Mapping[str, object]]
    capability: ReadCapability | None = None

    def __post_init__(self) -> None:
        operation_id = _require_safe_value_name(
            self.operation_id,
            field_name="operation_id",
        )
        if type(self.revision) is not int:
            raise TypeError("revision must be an integer")
        if self.revision <= 0:
            raise ValueError("revision must be positive")
        _require_unique_names(self.depends_on, field_name="depends_on")
        _require_unique_names(self.requires, field_name="requires")
        _require_unique_names(self.provides, field_name="provides")
        if type(self.allowed_no_target_codes) is not frozenset:
            raise TypeError("allowed_no_target_codes must be a frozenset")
        if any(
            type(code) is not NoLiveTargetCode
            for code in self.allowed_no_target_codes
        ):
            raise TypeError("allowed_no_target_codes contains an invalid code")
        if self.capability is not None:
            if type(self.capability) is not ReadCapability:
                raise TypeError("capability must be a ReadCapability or None")
            capability_code = no_target_code_for_read_capability(self.capability)
            if capability_code not in self.allowed_no_target_codes:
                raise ValueError(
                    "capability requires its matching allowed no-target code"
                )
        if type(self.binding) is not GeneratedReadBinding:
            raise TypeError("binding must be a GeneratedReadBinding")
        expected_method_name = f"{operation_id}_with_http_info"
        if self.binding.method_name != expected_method_name:
            raise ValueError("binding method_name does not match operation_id")
        if not callable(self.build_values):
            raise TypeError("build_values must be callable")
        if not callable(self.validate_response):
            raise TypeError("validate_response must be callable")
        if not callable(self.extract):
            raise TypeError("extract must be callable")


class ReadContext:
    __slots__ = ("_values",)

    _values: dict[str, object]

    def __init__(self, values: Mapping[str, object]) -> None:
        if not isinstance(values, Mapping):
            raise TypeError("read context values must be a mapping")
        copied: dict[str, object] = {}
        for key, value in values.items():
            safe_key = _require_safe_value_name(key, field_name="context key")
            copied[safe_key] = value
        object.__setattr__(self, "_values", copied)

    def __setattr__(self, name: str, value: object) -> None:
        del name, value
        raise AttributeError("ReadContext is immutable")

    def __delattr__(self, name: str) -> None:
        del name
        raise AttributeError("ReadContext is immutable")

    def __repr__(self) -> str:
        return "ReadContext()"

    @classmethod
    def seed(cls, values: Mapping[str, object]) -> ReadContext:
        return cls(values)

    def view(self, keys: tuple[str, ...]) -> ContextView:
        declared = _require_unique_names(keys, field_name="context view keys")
        visible = {key: self._values[key] for key in declared if key in self._values}
        return ContextView(MappingProxyType(visible))

    def apply(self, case: ReadCase, extracted: Mapping[str, object]) -> None:
        if type(case) is not ReadCase:
            raise TypeError("case must be a ReadCase")
        if not isinstance(extracted, Mapping):
            raise TypeError("extracted values must be a mapping")

        pending: dict[str, object] = {}
        declared = frozenset(case.provides)
        for key, value in extracted.items():
            safe_key = _require_safe_value_name(key, field_name="extracted key")
            if safe_key not in declared:
                raise ValueError("extractor returned an undeclared key")
            if safe_key in self._values and not _values_are_equal(
                self._values[safe_key],
                value,
            ):
                raise ValueError("read context overwrite rejected")
            if safe_key not in self._values:
                pending[safe_key] = value

        self._values.update(pending)


def _values_are_equal(existing: object, candidate: object) -> bool:
    if existing is candidate:
        return True
    if type(existing) is not type(candidate):
        return False
    try:
        comparison = existing == candidate
    except Exception:
        return False
    return comparison is True


class NoLiveTarget(Exception):
    def __init__(self, code: NoLiveTargetCode) -> None:
        if type(code) is not NoLiveTargetCode:
            raise TypeError("code must be a NoLiveTargetCode")
        self.code = code
        super().__init__(code.value)


class ReadAssertionFailure(Exception):
    def __init__(self) -> None:
        super().__init__(ReadFailureCode.ASSERTION_FAILED.value)


class ReadExtractorFailure(Exception):
    def __init__(self) -> None:
        super().__init__(ReadFailureCode.EXTRACTOR_FAILED.value)


def build_generated_request(
    binding: GeneratedReadBinding,
    values: Mapping[str, object] | NoRequest,
) -> object | None:
    """Build one generated request model without exposing validation details."""

    if type(binding) is not GeneratedReadBinding:
        raise TypeError("binding must be a GeneratedReadBinding")
    has_request = binding.request_module is not None
    if values is NO_REQUEST:
        if has_request:
            raise ValueError("body binding requires request values")
        return None
    if isinstance(values, NoRequest):
        raise ValueError("only NO_REQUEST represents an absent request")
    if not has_request:
        raise ValueError("no-body binding requires NO_REQUEST")
    if not isinstance(values, Mapping):
        raise TypeError("request values must be a mapping")

    resolved = binding.resolve()
    request_class = resolved.request_class
    if request_class is None:
        raise SafetyError("generated read request class resolution failed")
    try:
        return request_class.model_validate(dict(values))  # type: ignore[attr-defined]
    except Exception:
        pass
    raise SafetyError("Generated read request validation failed") from None


__all__ = [
    "NO_REQUEST",
    "READ_SEED_KEYS",
    "ContextView",
    "GeneratedReadBinding",
    "NoLiveTarget",
    "NoLiveTargetCode",
    "NoRequest",
    "ReadAssertionFailure",
    "ReadCapability",
    "ReadCase",
    "ReadContext",
    "ReadExtractorFailure",
    "ReadFailureCode",
    "build_generated_request",
    "no_target_code_for_read_capability",
]
