from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Awaitable, Callable, Mapping
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Generic, NoReturn, TypeVar, cast
from uuid import UUID

from iikocloud_client.api.customers_api import CustomersApi
from iikocloud_client.api.menu_api import MenuApi
from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException
from iikocloud_client.models.add_products_to_stop_list_request import (
    AddProductsToStopListRequest,
)
from iikocloud_client.models.create_or_update_customer_request import (
    CreateOrUpdateCustomerRequest,
)
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest
from iikocloud_client.models.remove_products_from_stop_list_request import (
    RemoveProductsFromStopListRequest,
)

from ..capture import LiveCapture
from ..errors import SafetyError
from .profile import ResolvedLiveProfile
from .rates import LiveRateGuard
from .read_case import GeneratedReadBinding, ReadFailureCode
from .receipt import LiveReceipt
from .session import LiveOperation
from .state import LiveStateStore

T = TypeVar("T")
_CLEANUP_OPERATION_ID = "remove_products_from_stop_list"
_COMPENSATING_OPERATION_ID = "add_products_to_stop_list"
CUSTOMER_MARKER_PHONE = "+70000000042"
_PROFILE_BOUNDARY_ERROR = "Generated cleanup request is outside the selected write profile"
_NO_API_EXCEPTION = object()
_INVALID_API_EXCEPTION_STATUS = object()


@dataclass(frozen=True, slots=True)
class GeneratedCallResult(Generic[T]):
    data: T
    status_code: int
    duration_ms: int


class GeneratedCallFailure(SafetyError):
    _SAFE_ERROR_BODY_KEYS = frozenset(
        {
            "code",
            "description",
            "error",
            "errorCode",
            "errorDescription",
            "httpStatusCode",
            "isIntegrationError",
            "message",
        }
    )

    def __init__(
        self,
        code: ReadFailureCode,
        status_code: int | None = None,
        error_details: Mapping[str, object] | None = None,
    ) -> None:
        if type(code) is not ReadFailureCode:
            raise TypeError("code must be a ReadFailureCode")
        if status_code is not None and (
            type(status_code) is not int or not 0 <= status_code <= 599
        ):
            raise ValueError("status_code must be a normalized HTTP status")
        if error_details is not None and (
            not isinstance(error_details, Mapping)
            or any(
                type(key) is not str
                or key not in GeneratedCallFailure._SAFE_ERROR_BODY_KEYS
                or type(error_details[key]) not in {str, int, bool, float, type(None)}
                for key in error_details
            )
        ):
            raise ValueError("error details must use reviewed error-body keys")
        self.code = code
        self.status_code = status_code
        self.error_details = (
            MappingProxyType(dict(error_details)) if error_details is not None else None
        )
        super().__init__(code.value)


def _safe_api_error_details(body: object) -> dict[str, object] | None:
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except ValueError:
            return None
    if not isinstance(body, dict):
        return None
    details = {
        key: value
        for key, value in body.items()
        if key in GeneratedCallFailure._SAFE_ERROR_BODY_KEYS
        and type(value) in {str, int, bool, float}
    }
    return details or None


def _profile_boundary_ids(
    profile: object,
) -> tuple[UUID, frozenset[UUID], UUID, UUID]:
    expected_ids: tuple[UUID, frozenset[UUID], UUID, UUID] | None = None
    allow_write = False
    if isinstance(profile, ResolvedLiveProfile):
        allow_write = profile.allow_write is True
        with suppress(Exception):
            if profile.terminal_group_id is not None and profile.write_product_id is not None:
                expected_ids = (
                    UUID(profile.organization_id),
                    frozenset(UUID(value) for value in profile.allowed_organization_ids),
                    UUID(profile.terminal_group_id),
                    UUID(profile.write_product_id),
                )
    if expected_ids is None or not allow_write:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return expected_ids


def validate_generated_cleanup_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> RemoveProductsFromStopListRequest:
    """Validate one generated cleanup request against its selected write profile."""

    if type(operation_id) is not str or operation_id != _CLEANUP_OPERATION_ID:
        raise SafetyError("Operation is not an approved cleanup operation") from None

    request: RemoveProductsFromStopListRequest | None = None
    with suppress(Exception):
        request = RemoveProductsFromStopListRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated cleanup payload is invalid") from None

    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and request.terminal_group_id == terminal_group_id
            and len(request.items) == 1
            and request.items[0].product_id == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_generated_compensating_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> AddProductsToStopListRequest:
    """Validate one generated compensating write request against its write profile."""

    if type(operation_id) is not str or operation_id != _COMPENSATING_OPERATION_ID:
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: AddProductsToStopListRequest | None = None
    with suppress(Exception):
        request = AddProductsToStopListRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and request.terminal_group_id == terminal_group_id
            and len(request.items) == 1
            and request.items[0].product_id == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def _organization_boundary(
    profile: object,
) -> tuple[UUID, frozenset[UUID]]:
    ids: tuple[UUID, frozenset[UUID]] | None = None
    allow_write = False
    if isinstance(profile, ResolvedLiveProfile):
        allow_write = profile.allow_write is True
        with suppress(Exception):
            ids = (
                UUID(profile.organization_id),
                frozenset(UUID(value) for value in profile.allowed_organization_ids),
            )
    if ids is None or not allow_write:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return ids


def validate_customer_create_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CreateOrUpdateCustomerRequest:
    """Validate one owned-customer create request against its write profile."""

    if type(operation_id) is not str or operation_id != "create_or_update_customer":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CreateOrUpdateCustomerRequest | None = None
    with suppress(Exception):
        request = CreateOrUpdateCustomerRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    organization_id, allowed_organization_ids = _organization_boundary(profile)
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and request.phone == CUSTOMER_MARKER_PHONE
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_customer_delete_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> DeleteCustomersRequest:
    """Validate one owned-customer delete request against its write profile."""

    if type(operation_id) is not str or operation_id != "delete_customers":
        raise SafetyError("Operation is not an approved cleanup operation") from None

    request: DeleteCustomersRequest | None = None
    with suppress(Exception):
        request = DeleteCustomersRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated cleanup payload is invalid") from None

    organization_id, allowed_organization_ids = _organization_boundary(profile)
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and len(request.customer_ids) == 1
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


@dataclass(frozen=True)
class _WriteExecutorSpec:
    api_class: type
    method_name: str
    request_keyword: str
    validator: Callable[[str, object, ResolvedLiveProfile], object]


_WRITE_EXECUTORS: Mapping[str, _WriteExecutorSpec] = MappingProxyType(
    {
        "add_products_to_stop_list": _WriteExecutorSpec(
            MenuApi,
            "add_products_to_stop_list_with_http_info",
            "add_products_to_stop_list_request",
            validate_generated_compensating_request,
        ),
        "remove_products_from_stop_list": _WriteExecutorSpec(
            MenuApi,
            "remove_products_from_stop_list_with_http_info",
            "remove_products_from_stop_list_request",
            validate_generated_cleanup_request,
        ),
        "create_or_update_customer": _WriteExecutorSpec(
            CustomersApi,
            "create_or_update_customer_with_http_info",
            "create_or_update_customer_request",
            validate_customer_create_request,
        ),
        "delete_customers": _WriteExecutorSpec(
            CustomersApi,
            "delete_customers_with_http_info",
            "delete_customers_request",
            validate_customer_delete_request,
        ),
    }
)


class GeneratedLiveSdk:
    """Apply live safety controls around one generated SDK invocation."""

    def __init__(
        self,
        api_client: ApiClient,
        profile: ResolvedLiveProfile,
        guard: LiveRateGuard,
        state: LiveStateStore,
        operation_contract: Mapping[str, LiveOperation],
        capture: LiveCapture | None = None,
        receipt: LiveReceipt | None = None,
        receipt_path: Path | None = None,
    ) -> None:
        if getattr(guard, "state", state) is not state:
            raise SafetyError("Generated live guard must use the same live state")
        if (receipt is None) != (receipt_path is None):
            raise SafetyError("Generated live receipt and path must be supplied together")
        if receipt is not None and receipt.profile_fingerprint != profile.fingerprint:
            raise SafetyError("Generated live receipt must belong to the selected profile")
        if not isinstance(operation_contract, Mapping) or any(
            type(operation_id) is not str or type(operation) is not LiveOperation
            for operation_id, operation in operation_contract.items()
        ):
            raise SafetyError("Generated live operation contract is invalid")
        self.api_client = api_client
        self.profile = profile
        self.guard = guard
        self.state = state
        self.operation_contract = MappingProxyType(dict(operation_contract))
        self.capture = capture
        self._receipt = receipt
        self._receipt_path = receipt_path
        self._unusable = False

    @property
    def receipt(self) -> LiveReceipt | None:
        return self._receipt

    def _assert_usable(self) -> None:
        if self._unusable:
            raise SafetyError("Generated live SDK is unusable after a failed live call")

    def _record_status(self, operation_id: str, status: int) -> None:
        failed = False
        try:
            self.guard.record_status(operation_id, status)
        except Exception:
            failed = True
        if failed:
            self._unusable = True
            raise SafetyError(
                "Generated SDK status recording failed without a retry"
            ) from None

    def _record_operation(self, operation_id: str) -> None:
        if self._receipt is None or self._receipt_path is None:
            return
        failed = False
        updated: LiveReceipt | None = None
        try:
            updated = self._receipt.with_operation(operation_id)
            updated.write(self._receipt_path)
        except Exception:
            failed = True
        if failed or updated is None:
            self._unusable = True
            raise SafetyError(
                "Generated SDK receipt recording failed without a retry"
            ) from None
        self._receipt = updated

    def _record_429(self) -> None:
        if self._receipt is None or self._receipt_path is None:
            return
        failed = False
        updated: LiveReceipt | None = None
        try:
            updated = self._receipt.with_429()
            updated.write(self._receipt_path)
        except Exception:
            failed = True
        if failed or updated is None:
            self._unusable = True
            raise SafetyError("Generated SDK 429 receipt recording failed") from None
        self._receipt = updated

    def _normalize_api_exception_status(self, status: object) -> int:
        if status is None:
            return 0
        if type(status) is int and 0 <= status <= 599:
            return status
        if type(status) is str and len(status) == 3 and status.isascii() and status.isdecimal():
            normalized = int(status)
            if 100 <= normalized <= 599:
                return normalized
        self._unusable = True
        raise SafetyError("Generated SDK exception has an invalid HTTP status") from None

    async def execute_cleanup(self, operation_id: str, payload: object) -> None:
        self._assert_usable()
        request = validate_generated_cleanup_request(operation_id, payload, self.profile)
        operation = self.operation_contract.get(operation_id)
        if operation is None or operation.kind not in {"cleanup", "compensating"}:
            raise SafetyError("Operation is not an approved cleanup operation")
        api = MenuApi(self.api_client)
        method = MenuApi.remove_products_from_stop_list_with_http_info

        async def invoke() -> ApiResponse[object]:
            pending = method(
                api,
                remove_products_from_stop_list_request=request,
                _request_timeout=(10.0, 30.0),
            )
            return cast(ApiResponse[object], await pending)

        await self._call_generated(
            operation_id,
            operation,
            request,
            invoke,
        )

    async def execute_compensating(self, operation_id: str, payload: object) -> None:
        self._assert_usable()
        request = validate_generated_compensating_request(
            operation_id, payload, self.profile
        )
        operation = self.operation_contract.get(operation_id)
        if operation is None or operation.kind != "compensating":
            raise SafetyError("Operation is not an approved compensating operation")
        api = MenuApi(self.api_client)
        method = MenuApi.add_products_to_stop_list_with_http_info

        async def invoke() -> ApiResponse[object]:
            pending = method(
                api,
                add_products_to_stop_list_request=request,
                _request_timeout=(10.0, 30.0),
            )
            return cast(ApiResponse[object], await pending)

        await self._call_generated(
            operation_id,
            operation,
            request,
            invoke,
        )

    async def execute_write(self, operation_id: str, payload: object) -> object:
        """Execute one reviewed write operation through its validated executor."""

        self._assert_usable()
        spec = _WRITE_EXECUTORS.get(operation_id)
        if spec is None:
            raise SafetyError("Operation is not an approved write operation")
        request = spec.validator(operation_id, payload, self.profile)
        operation = self.operation_contract.get(operation_id)
        if operation is None or operation.kind not in {"compensating", "cleanup"}:
            raise SafetyError("Operation is not an approved write operation")
        api_type = spec.api_class
        method = api_type.__dict__.get(spec.method_name)
        if method is None:
            raise SafetyError("Generated write API class does not own the bound method")
        api = api_type(self.api_client)

        async def invoke() -> ApiResponse[object]:
            pending = method(
                api,
                **{spec.request_keyword: request, "_request_timeout": (10.0, 30.0)},
            )
            return cast(ApiResponse[object], await pending)

        return await self._call_generated(
            operation_id,
            operation,
            request,
            invoke,
        )

    async def call_bound_read(
        self,
        operation_id: str,
        binding: GeneratedReadBinding,
        request_model: object | None,
    ) -> GeneratedCallResult[object]:
        self._assert_usable()
        if type(operation_id) is not str:
            raise SafetyError("Generated read operation is not allowlisted")
        operation = self.operation_contract.get(operation_id)
        if operation is None or operation.kind != "read":
            raise SafetyError("Generated read operation is not allowlisted")
        if type(binding) is not GeneratedReadBinding or (
            binding.method_name != f"{operation_id}_with_http_info"
        ):
            raise SafetyError("Generated read binding does not match operation ID")

        resolution_failed = False
        resolved = None
        try:
            resolved = binding.resolve()
        except Exception:
            resolution_failed = True
        if resolution_failed or resolved is None:
            raise SafetyError("Generated read binding resolution failed") from None

        api_type = resolved.api_class
        request_type = resolved.request_class
        method = resolved.method
        if api_type.__dict__.get(binding.method_name) is not method:
            raise SafetyError("Generated read API class does not own bound method")
        if request_type is None:
            if request_model is not None or binding.request_keyword is not None:
                raise SafetyError("Generated read request model does not match binding")
        elif (
            type(request_model) is not request_type
            or binding.request_keyword is None
        ):
            raise SafetyError("Generated read request model does not match binding")

        construction_failed = False
        api: object | None = None
        try:
            constructor = cast(Callable[[ApiClient], object], api_type)
            api = constructor(self.api_client)
        except Exception:
            construction_failed = True
        if construction_failed or api is None:
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.INVOCATION_FAILED)

        kwargs: dict[str, object] = {"_request_timeout": (10.0, 30.0)}
        if binding.request_keyword is not None:
            kwargs[binding.request_keyword] = request_model

        async def invoke() -> ApiResponse[object]:
            pending = cast(Awaitable[ApiResponse[object]], method(api, **kwargs))
            return await pending

        return await self._call_generated(
            operation_id,
            operation,
            request_model,
            invoke,
        )

    def _raise_call_failure(
        self,
        code: ReadFailureCode,
        status_code: int | None = None,
    ) -> NoReturn:
        raise GeneratedCallFailure(code, status_code) from None

    async def _call_generated(
        self,
        operation_id: str,
        operation: LiveOperation,
        request_model: object | None,
        invoke: Callable[[], Awaitable[ApiResponse[object]]],
    ) -> GeneratedCallResult[object]:
        self._assert_usable()
        await self.guard.acquire(operation_id)
        self._record_operation(operation_id)
        started_ns = time.monotonic_ns()
        response: ApiResponse[object] | None = None
        cancelled: asyncio.CancelledError | None = None
        api_exception_status: object = _NO_API_EXCEPTION
        api_error_details: dict[str, object] | None = None
        transport_failed = False
        try:
            response = await invoke()
        except asyncio.CancelledError as error:
            cancelled = error
        except ApiException as error:
            try:
                api_exception_status = error.status
            except Exception:
                api_exception_status = _INVALID_API_EXCEPTION_STATUS
            api_error_details = _safe_api_error_details(getattr(error, "body", None))
        except Exception:
            transport_failed = True
        duration_ms = max(0, (time.monotonic_ns() - started_ns) // 1_000_000)

        if cancelled is not None:
            self._unusable = True
            raise cancelled
        if api_exception_status is not _NO_API_EXCEPTION:
            status = self._normalize_api_exception_status(api_exception_status)
            self._record_status(operation_id, status)
            if status == 429:
                self._record_429()
            self._unusable = True
            raise GeneratedCallFailure(
                ReadFailureCode.HTTP_ERROR, status, api_error_details
            ) from None
        if transport_failed:
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.TRANSPORT_ERROR)

        if not isinstance(response, ApiResponse):
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.INVOCATION_FAILED)
        status_code = response.status_code
        if type(status_code) is not int or not 100 <= status_code <= 599:
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.INVOCATION_FAILED)
        self._record_status(operation_id, status_code)
        if not 200 <= status_code <= 299:
            if status_code == 429:
                self._record_429()
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.HTTP_ERROR, status_code)

        data_failed = False
        data: object | None = None
        try:
            data = response.data
        except Exception:
            data_failed = True
        if data_failed:
            self._unusable = True
            self._raise_call_failure(ReadFailureCode.INVOCATION_FAILED)

        if self.capture is not None and self.capture.selected_operation == operation_id:
            capture_failed = False
            try:
                self.capture.write_model_pair(
                    operation_id,
                    request_model,
                    data,
                    metadata={
                        "method": operation.method,
                        "path": operation.path,
                        "status": status_code,
                        "duration": duration_ms / 1000,
                    },
                )
            except Exception:
                capture_failed = True
            if capture_failed:
                self._unusable = True
                self._raise_call_failure(ReadFailureCode.CAPTURE_FAILED, status_code)
        return GeneratedCallResult(
            data=data,
            status_code=status_code,
            duration_ms=duration_ms,
        )
