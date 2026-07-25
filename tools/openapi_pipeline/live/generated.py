from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Awaitable, Callable, Mapping
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Generic, NoReturn, TypeVar, cast
from uuid import UUID

from pydantic import BaseModel

from iikocloud_client.api.banquets_reserves_api import BanquetsReservesApi
from iikocloud_client.api.customer_categories_api import CustomerCategoriesApi
from iikocloud_client.api.customers_api import CustomersApi
from iikocloud_client.api.deliveries_create_and_update_api import (
    DeliveriesCreateAndUpdateApi,
)
from iikocloud_client.api.drafts_api import DraftsApi
from iikocloud_client.api.employees_api import EmployeesApi
from iikocloud_client.api.menu_api import MenuApi
from iikocloud_client.api.orders_api import OrdersApi
from iikocloud_client.api.public_api_invoice_processing_nomenclature_api import (
    PublicApiInvoiceProcessingNomenclatureApi,
)
from iikocloud_client.api.terminal_groups_api import TerminalGroupsApi
from iikocloud_client.api.webhooks_api import WebhooksApi
from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException
from iikocloud_client.models.add_customer_to_table_order_request import (
    AddCustomerToTableOrderRequest,
)
from iikocloud_client.models.add_items_to_table_order_request import (
    AddItemsToTableOrderRequest,
)
from iikocloud_client.models.add_magnet_card_request import AddMagnetCardRequest
from iikocloud_client.models.add_order_items_request import AddOrderItemsRequest
from iikocloud_client.models.add_order_payments_request import AddOrderPaymentsRequest
from iikocloud_client.models.add_products_to_stop_list_request import (
    AddProductsToStopListRequest,
)
from iikocloud_client.models.awake_terminal_groups_request import AwakeTerminalGroupsRequest
from iikocloud_client.models.cancel_delivery_confirmation_request import (
    CancelDeliveryConfirmationRequest,
)
from iikocloud_client.models.cancel_order_request import CancelOrderRequest
from iikocloud_client.models.cancel_reserve_request import CancelReserveRequest
from iikocloud_client.models.cancel_table_order_request import CancelTableOrderRequest
from iikocloud_client.models.change_category_for_customer_request import (
    ChangeCategoryForCustomerRequest,
)
from iikocloud_client.models.change_complete_before_request import ChangeCompleteBeforeRequest
from iikocloud_client.models.change_delivery_comment_request import ChangeDeliveryCommentRequest
from iikocloud_client.models.change_delivery_operator_request import (
    ChangeDeliveryOperatorRequest,
)
from iikocloud_client.models.change_driver_info_request import ChangeDriverInfoRequest
from iikocloud_client.models.change_external_data_request import ChangeExternalDataRequest
from iikocloud_client.models.change_payments_request import ChangePaymentsRequest
from iikocloud_client.models.clear_stop_list_request import ClearStopListRequest
from iikocloud_client.models.close_delivery_order_request import CloseDeliveryOrderRequest
from iikocloud_client.models.close_personal_session_request import (
    ClosePersonalSessionRequest,
)
from iikocloud_client.models.close_table_order_request import CloseTableOrderRequest
from iikocloud_client.models.commit_draft_request import CommitDraftRequest
from iikocloud_client.models.confirm_delivery_request import ConfirmDeliveryRequest
from iikocloud_client.models.create_draft_request import CreateDraftRequest
from iikocloud_client.models.create_or_update_customer_request import (
    CreateOrUpdateCustomerRequest,
)
from iikocloud_client.models.create_order_request import CreateOrderRequest
from iikocloud_client.models.create_reserve_request import CreateReserveRequest
from iikocloud_client.models.create_table_order_request import CreateTableOrderRequest
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest
from iikocloud_client.models.delete_draft_request import DeleteDraftRequest
from iikocloud_client.models.delete_magnet_card_request import DeleteMagnetCardRequest
from iikocloud_client.models.delivery_order_create_compound_item import (
    DeliveryOrderCreateCompoundItem,
)
from iikocloud_client.models.delivery_order_create_product_item import (
    DeliveryOrderCreateProductItem,
)
from iikocloud_client.models.init_table_order_request import InitTableOrderRequest
from iikocloud_client.models.lock_or_unlock_draft_request import LockOrUnlockDraftRequest
from iikocloud_client.models.open_personal_session_request import OpenPersonalSessionRequest
from iikocloud_client.models.print_bill_request import PrintBillRequest
from iikocloud_client.models.print_delivery_bill_request import PrintDeliveryBillRequest
from iikocloud_client.models.remove_products_from_stop_list_request import (
    RemoveProductsFromStopListRequest,
)
from iikocloud_client.models.save_draft_request import SaveDraftRequest
from iikocloud_client.models.update_delivery_status_request import UpdateDeliveryStatusRequest
from iikocloud_client.models.update_order_courier_request import UpdateOrderCourierRequest
from iikocloud_client.models.update_order_problem_request import UpdateOrderProblemRequest
from iikocloud_client.models.update_product_barcodes_request import (
    UpdateProductBarcodesRequest,
)
from iikocloud_client.models.update_tracking_link_request import UpdateTrackingLinkRequest
from iikocloud_client.models.update_web_hook_settings_request import (
    UpdateWebHookSettingsRequest,
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
CUSTOMER_MARKER_CARD = "7999000000000042"
_PROFILE_BOUNDARY_ERROR = "Generated cleanup request is outside the selected write profile"
_NO_API_EXCEPTION = object()
_INVALID_API_EXCEPTION_STATUS = object()


@dataclass(frozen=True, slots=True)
class GeneratedCallResult(Generic[T]):
    data: T
    status_code: int
    duration_ms: int


class GeneratedCallFailure(SafetyError):
    # Only classification fields: free-text error messages can embed live
    # identifiers or credentials echoed by the server.
    _SAFE_ERROR_BODY_KEYS = frozenset(
        {
            "code",
            "description",
            "error",
            "errorCode",
            "httpStatusCode",
            "isIntegrationError",
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


def _repair_union_order_items(payload: object, items: list[Any]) -> None:
    """Replace base-parsed union items with discriminator-parsed subclass ones.

    The generated union base class silently drops subclass fields when parsing
    and dumping through the parent model, so every create payload carrying
    order items must be repaired from the raw payload before it is sent.
    """
    raw_items: object = None
    if isinstance(payload, dict):
        if isinstance(payload.get("items"), list):
            raw_items = payload["items"]
        elif isinstance(payload.get("order"), dict):
            raw_items = payload["order"].get("items")
    if not isinstance(raw_items, list) or len(raw_items) != 1:
        raise SafetyError("Generated compensating payload is invalid") from None
    repaired_items: list[object] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            raise SafetyError("Generated compensating payload is invalid") from None
        item_kind = raw_item.get("type")
        repaired: object | None = None
        with suppress(Exception):
            if item_kind == "Product":
                repaired = DeliveryOrderCreateProductItem.model_validate(raw_item)
            elif item_kind == "Compound":
                repaired = DeliveryOrderCreateCompoundItem.model_validate(raw_item)
        if repaired is None:
            raise SafetyError("Generated compensating payload is invalid") from None
        repaired_items.append(repaired)
    if any(type(item).__name__ == "DeliveryOrderCreateItem" for item in repaired_items):
        raise SafetyError("Generated compensating payload is invalid") from None
    items[:] = repaired_items


def validate_draft_create_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CreateDraftRequest:
    """Validate one owned delivery-draft create request against its write profile."""

    if type(operation_id) is not str or operation_id != "create_delivery_draft":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CreateDraftRequest | None = None
    with suppress(Exception):
        request = CreateDraftRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    order = request.order
    _repair_union_order_items(payload, order.items)
    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    external_menu_id = profile.external_menu_id
    if external_menu_id is None:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    items = order.items
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and (
                request.terminal_group_id is None
                or request.terminal_group_id == terminal_group_id
            )
            and order.menu_id == external_menu_id
            and order.phone == CUSTOMER_MARKER_PHONE
            and len(items) == 1
            and getattr(items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_draft_delete_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> DeleteDraftRequest:
    """Validate one owned delivery-draft delete request against its write profile."""

    if type(operation_id) is not str or operation_id != "delete_delivery_draft":
        raise SafetyError("Operation is not an approved cleanup operation") from None

    request: DeleteDraftRequest | None = None
    with suppress(Exception):
        request = DeleteDraftRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated cleanup payload is invalid") from None

    organization_id, allowed_organization_ids = _organization_boundary(profile)
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def _validate_single_target_write(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
    *,
    model: type[BaseModel],
    role: str,
) -> object:
    """Shared boundary validation for single-target writes on owned entities."""

    if type(operation_id) is not str:
        raise SafetyError(f"Operation is not an approved {role} operation") from None
    request: object | None = None
    with suppress(Exception):
        request = model.model_validate(payload)
    if request is None:
        raise SafetyError(f"Generated {role} payload is invalid") from None
    organization_id, allowed_organization_ids = _organization_boundary(profile)
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id  # type: ignore[attr-defined]
            and request.organization_id in allowed_organization_ids  # type: ignore[attr-defined]
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_category_add_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "add_customer_category":
        raise SafetyError("Operation is not an approved compensating operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=ChangeCategoryForCustomerRequest,
        role="compensating",
    )


def validate_category_remove_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "remove_customer_category":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=ChangeCategoryForCustomerRequest,
        role="cleanup",
    )


def validate_magnet_card_add_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "add_customer_magnet_card":
        raise SafetyError("Operation is not an approved compensating operation") from None
    request = _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=AddMagnetCardRequest,
        role="compensating",
    )
    if request.card_number != CUSTOMER_MARKER_CARD:  # type: ignore[attr-defined]
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_magnet_card_remove_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "remove_customer_magnet_card":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=DeleteMagnetCardRequest,
        role="cleanup",
    )


def validate_delivery_order_create_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CreateOrderRequest:
    """Validate one owned delivery-order create request against its write profile."""

    if type(operation_id) is not str or operation_id != "create_delivery_order":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CreateOrderRequest | None = None
    with suppress(Exception):
        request = CreateOrderRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    order = request.order
    _repair_union_order_items(payload, order.items)
    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and (
                request.terminal_group_id is None
                or request.terminal_group_id == terminal_group_id
            )
            and getattr(order, "phone", None) == CUSTOMER_MARKER_PHONE
            and getattr(order.items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_delivery_order_cancel_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CancelOrderRequest:
    """Validate one owned delivery-order cancel request against its write profile."""

    if type(operation_id) is not str or operation_id != "cancel_delivery_order":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=CancelOrderRequest,
        role="cleanup",
    )  # type: ignore[return-value]


def validate_draft_lock_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "lock_delivery_draft":
        raise SafetyError("Operation is not an approved compensating operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=LockOrUnlockDraftRequest,
        role="compensating",
    )


def validate_draft_unlock_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "unlock_delivery_draft":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=LockOrUnlockDraftRequest,
        role="cleanup",
    )


def validate_draft_save_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> SaveDraftRequest:
    """Validate one owned delivery-draft save request against its write profile."""

    if type(operation_id) is not str or operation_id != "save_delivery_draft":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: SaveDraftRequest | None = None
    with suppress(Exception):
        request = SaveDraftRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    order = request.order
    _repair_union_order_items(payload, order.items)
    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    external_menu_id = profile.external_menu_id
    if external_menu_id is None:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    items = order.items
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and (
                request.terminal_group_id is None
                or request.terminal_group_id == terminal_group_id
            )
            and order.menu_id == external_menu_id
            and order.phone == CUSTOMER_MARKER_PHONE
            and len(items) == 1
            and getattr(items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_draft_commit_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CommitDraftRequest:
    """Validate one owned delivery-draft commit request against its write profile."""

    if type(operation_id) is not str or operation_id != "commit_delivery_draft":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CommitDraftRequest | None = None
    with suppress(Exception):
        request = CommitDraftRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    organization_id, allowed_organization_ids, terminal_group_id, _product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and (
                request.terminal_group_id is None
                or request.terminal_group_id == terminal_group_id
            )
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_reserve_create_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CreateReserveRequest:
    """Validate one owned reserve create request against its write profile."""

    if type(operation_id) is not str or operation_id != "create_reserve":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CreateReserveRequest | None = None
    with suppress(Exception):
        request = CreateReserveRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    organization_id, allowed_organization_ids = _organization_boundary(profile)
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and request.phone == CUSTOMER_MARKER_PHONE
            and len(request.table_ids) >= 1
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_reserve_cancel_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "cancel_reserve":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=CancelReserveRequest,
        role="cleanup",
    )


def validate_table_order_create_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> CreateTableOrderRequest:
    """Validate one owned table-order create request against its write profile."""

    if type(operation_id) is not str or operation_id != "create_table_order":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: CreateTableOrderRequest | None = None
    with suppress(Exception):
        request = CreateTableOrderRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    order = request.order
    if order is None:
        raise SafetyError("Generated compensating payload is invalid") from None
    _repair_union_order_items(payload, order.items)
    organization_id, allowed_organization_ids, terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and request.terminal_group_id == terminal_group_id
            and getattr(order, "phone", None) == CUSTOMER_MARKER_PHONE
            and len(order.items) == 1
            and getattr(order.items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_table_order_cancel_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> object:
    if operation_id != "cancel_table_order":
        raise SafetyError("Operation is not an approved cleanup operation") from None
    return _validate_single_target_write(
        operation_id,
        payload,
        profile,
        model=CancelTableOrderRequest,
        role="cleanup",
    )


def _single_target_validator(
    operation_id: str,
    *,
    model: type[BaseModel],
    role: str,
) -> Callable[[str, object, ResolvedLiveProfile], object]:
    """Build a boundary validator for single-target writes on owned entities."""

    def validate(
        requested_operation_id: str,
        payload: object,
        profile: ResolvedLiveProfile,
    ) -> object:
        if requested_operation_id != operation_id:
            raise SafetyError(f"Operation is not an approved {role} operation") from None
        return _validate_single_target_write(
            requested_operation_id,
            payload,
            profile,
            model=model,
            role=role,
        )

    return validate


def validate_table_order_add_items_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> AddItemsToTableOrderRequest:
    """Validate one table-order add-items write against its write profile."""

    if type(operation_id) is not str or operation_id != "add_items_to_table_order":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: AddItemsToTableOrderRequest | None = None
    with suppress(Exception):
        request = AddItemsToTableOrderRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    _repair_union_order_items(payload, request.items)
    organization_id, allowed_organization_ids, _terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and len(request.items) == 1
            and getattr(request.items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_order_add_items_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> AddOrderItemsRequest:
    """Validate one add-items write against its write profile (dedicated product only)."""

    if type(operation_id) is not str or operation_id != "add_delivery_order_items":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: AddOrderItemsRequest | None = None
    with suppress(Exception):
        request = AddOrderItemsRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    _repair_union_order_items(payload, request.items)
    organization_id, allowed_organization_ids, _terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == organization_id
            and request.organization_id in allowed_organization_ids
            and len(request.items) == 1
            and getattr(request.items[0], "product_id", None) == product_id
        )
    if not within_profile:
        raise SafetyError(_PROFILE_BOUNDARY_ERROR) from None
    return request


def validate_product_barcodes_request(
    operation_id: str,
    payload: object,
    profile: ResolvedLiveProfile,
) -> UpdateProductBarcodesRequest:
    """Validate one barcode update against its write profile (dedicated product only)."""

    if type(operation_id) is not str or operation_id != "update_inventory_product_barcodes":
        raise SafetyError("Operation is not an approved compensating operation") from None

    request: UpdateProductBarcodesRequest | None = None
    with suppress(Exception):
        request = UpdateProductBarcodesRequest.model_validate(payload)
    if request is None:
        raise SafetyError("Generated compensating payload is invalid") from None

    organization_id, allowed_organization_ids, _terminal_group_id, product_id = (
        _profile_boundary_ids(profile)
    )
    within_profile = False
    with suppress(Exception):
        within_profile = (
            request.organization_id == str(organization_id)
            and request.organization_id in {str(value) for value in allowed_organization_ids}
            and request.product_id == str(product_id)
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
        "create_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "create_delivery_draft_with_http_info",
            "create_draft_request",
            validate_draft_create_request,
        ),
        "delete_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "delete_delivery_draft_with_http_info",
            "delete_draft_request",
            validate_draft_delete_request,
        ),
        "add_customer_category": _WriteExecutorSpec(
            CustomerCategoriesApi,
            "add_customer_category_with_http_info",
            "change_category_for_customer_request",
            validate_category_add_request,
        ),
        "remove_customer_category": _WriteExecutorSpec(
            CustomerCategoriesApi,
            "remove_customer_category_with_http_info",
            "change_category_for_customer_request",
            validate_category_remove_request,
        ),
        "add_customer_magnet_card": _WriteExecutorSpec(
            CustomersApi,
            "add_customer_magnet_card_with_http_info",
            "add_magnet_card_request",
            validate_magnet_card_add_request,
        ),
        "remove_customer_magnet_card": _WriteExecutorSpec(
            CustomersApi,
            "remove_customer_magnet_card_with_http_info",
            "delete_magnet_card_request",
            validate_magnet_card_remove_request,
        ),
        "create_delivery_order": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "create_delivery_order_with_http_info",
            "create_order_request",
            validate_delivery_order_create_request,
        ),
        "cancel_delivery_order": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "cancel_delivery_order_with_http_info",
            "cancel_order_request",
            validate_delivery_order_cancel_request,
        ),
        "lock_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "lock_delivery_draft_with_http_info",
            "lock_or_unlock_draft_request",
            validate_draft_lock_request,
        ),
        "unlock_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "unlock_delivery_draft_with_http_info",
            "lock_or_unlock_draft_request",
            validate_draft_unlock_request,
        ),
        "save_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "save_delivery_draft_with_http_info",
            "save_draft_request",
            validate_draft_save_request,
        ),
        "commit_delivery_draft": _WriteExecutorSpec(
            DraftsApi,
            "commit_delivery_draft_with_http_info",
            "commit_draft_request",
            validate_draft_commit_request,
        ),
        "create_reserve": _WriteExecutorSpec(
            BanquetsReservesApi,
            "create_reserve_with_http_info",
            "create_reserve_request",
            validate_reserve_create_request,
        ),
        "cancel_reserve": _WriteExecutorSpec(
            BanquetsReservesApi,
            "cancel_reserve_with_http_info",
            "cancel_reserve_request",
            validate_reserve_cancel_request,
        ),
        "create_table_order": _WriteExecutorSpec(
            OrdersApi,
            "create_table_order_with_http_info",
            "create_table_order_request",
            validate_table_order_create_request,
        ),
        "cancel_table_order": _WriteExecutorSpec(
            OrdersApi,
            "cancel_table_order_with_http_info",
            "cancel_table_order_request",
            validate_table_order_cancel_request,
        ),
        "add_delivery_order_items": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "add_delivery_order_items_with_http_info",
            "add_order_items_request",
            validate_order_add_items_request,
        ),
        "add_delivery_order_payments": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "add_delivery_order_payments_with_http_info",
            "add_order_payments_request",
            _single_target_validator(
                "add_delivery_order_payments",
                model=AddOrderPaymentsRequest,
                role="compensating",
            ),
        ),
        "change_delivery_comment": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "change_delivery_comment_with_http_info",
            "change_delivery_comment_request",
            _single_target_validator(
                "change_delivery_comment",
                model=ChangeDeliveryCommentRequest,
                role="compensating",
            ),
        ),
        "change_delivery_complete_before": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "change_delivery_complete_before_with_http_info",
            "change_complete_before_request",
            _single_target_validator(
                "change_delivery_complete_before",
                model=ChangeCompleteBeforeRequest,
                role="compensating",
            ),
        ),
        "change_delivery_driver_info": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "change_delivery_driver_info_with_http_info",
            "change_driver_info_request",
            _single_target_validator(
                "change_delivery_driver_info",
                model=ChangeDriverInfoRequest,
                role="compensating",
            ),
        ),
        "change_delivery_external_data": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "change_delivery_external_data_with_http_info",
            "change_external_data_request",
            _single_target_validator(
                "change_delivery_external_data",
                model=ChangeExternalDataRequest,
                role="compensating",
            ),
        ),
        "change_delivery_operator": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "change_delivery_operator_with_http_info",
            "change_delivery_operator_request",
            _single_target_validator(
                "change_delivery_operator",
                model=ChangeDeliveryOperatorRequest,
                role="compensating",
            ),
        ),
        "close_delivery_order": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "close_delivery_order_with_http_info",
            "close_delivery_order_request",
            _single_target_validator(
                "close_delivery_order", model=CloseDeliveryOrderRequest, role="compensating"
            ),
        ),
        "confirm_delivery": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "confirm_delivery_with_http_info",
            "confirm_delivery_request",
            _single_target_validator(
                "confirm_delivery", model=ConfirmDeliveryRequest, role="compensating"
            ),
        ),
        "cancel_delivery_confirmation": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "cancel_delivery_confirmation_with_http_info",
            "cancel_delivery_confirmation_request",
            _single_target_validator(
                "cancel_delivery_confirmation",
                model=CancelDeliveryConfirmationRequest,
                role="cleanup",
            ),
        ),
        "print_delivery_bill": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "print_delivery_bill_with_http_info",
            "print_delivery_bill_request",
            _single_target_validator(
                "print_delivery_bill", model=PrintDeliveryBillRequest, role="compensating"
            ),
        ),
        "update_delivery_order_courier": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "update_delivery_order_courier_with_http_info",
            "update_order_courier_request",
            _single_target_validator(
                "update_delivery_order_courier",
                model=UpdateOrderCourierRequest,
                role="compensating",
            ),
        ),
        "update_delivery_order_problem": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "update_delivery_order_problem_with_http_info",
            "update_order_problem_request",
            _single_target_validator(
                "update_delivery_order_problem",
                model=UpdateOrderProblemRequest,
                role="compensating",
            ),
        ),
        "update_delivery_order_status": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "update_delivery_order_status_with_http_info",
            "update_delivery_status_request",
            _single_target_validator(
                "update_delivery_order_status",
                model=UpdateDeliveryStatusRequest,
                role="compensating",
            ),
        ),
        "update_delivery_tracking_link": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "update_delivery_tracking_link_with_http_info",
            "update_tracking_link_request",
            _single_target_validator(
                "update_delivery_tracking_link",
                model=UpdateTrackingLinkRequest,
                role="compensating",
            ),
        ),
        "update_inventory_product_barcodes": _WriteExecutorSpec(
            PublicApiInvoiceProcessingNomenclatureApi,
            "update_inventory_product_barcodes_with_http_info",
            "update_product_barcodes_request",
            validate_product_barcodes_request,
        ),
        "awake_terminal_groups": _WriteExecutorSpec(
            TerminalGroupsApi,
            "awake_terminal_groups_with_http_info",
            "awake_terminal_groups_request",
            _single_target_validator(
                "awake_terminal_groups",
                model=AwakeTerminalGroupsRequest,
                role="compensating",
            ),
        ),
        "clear_stop_list": _WriteExecutorSpec(
            MenuApi,
            "clear_stop_list_with_http_info",
            "clear_stop_list_request",
            _single_target_validator(
                "clear_stop_list", model=ClearStopListRequest, role="cleanup"
            ),
        ),
        "update_webhook_settings": _WriteExecutorSpec(
            WebhooksApi,
            "update_webhook_settings_with_http_info",
            "update_web_hook_settings_request",
            _single_target_validator(
                "update_webhook_settings",
                model=UpdateWebHookSettingsRequest,
                role="compensating",
            ),
        ),
        "add_items_to_table_order": _WriteExecutorSpec(
            OrdersApi,
            "add_items_to_table_order_with_http_info",
            "add_items_to_table_order_request",
            validate_table_order_add_items_request,
        ),
        "add_customer_to_table_order": _WriteExecutorSpec(
            OrdersApi,
            "add_customer_to_table_order_with_http_info",
            "add_customer_to_table_order_request",
            _single_target_validator(
                "add_customer_to_table_order",
                model=AddCustomerToTableOrderRequest,
                role="compensating",
            ),
        ),
        "add_table_order_payments": _WriteExecutorSpec(
            OrdersApi,
            "add_table_order_payments_with_http_info",
            "add_order_payments_request",
            _single_target_validator(
                "add_table_order_payments",
                model=AddOrderPaymentsRequest,
                role="compensating",
            ),
        ),
        "change_table_order_external_data": _WriteExecutorSpec(
            OrdersApi,
            "change_table_order_external_data_with_http_info",
            "change_external_data_request",
            _single_target_validator(
                "change_table_order_external_data",
                model=ChangeExternalDataRequest,
                role="compensating",
            ),
        ),
        "change_table_order_payments": _WriteExecutorSpec(
            OrdersApi,
            "change_table_order_payments_with_http_info",
            "change_payments_request",
            _single_target_validator(
                "change_table_order_payments",
                model=ChangePaymentsRequest,
                role="compensating",
            ),
        ),
        "print_table_order_bill": _WriteExecutorSpec(
            DeliveriesCreateAndUpdateApi,
            "print_table_order_bill_with_http_info",
            "print_bill_request",
            _single_target_validator(
                "print_table_order_bill", model=PrintBillRequest, role="compensating"
            ),
        ),
        "close_table_order": _WriteExecutorSpec(
            OrdersApi,
            "close_table_order_with_http_info",
            "close_table_order_request",
            _single_target_validator(
                "close_table_order", model=CloseTableOrderRequest, role="compensating"
            ),
        ),
        "initialize_table_orders_by_tables": _WriteExecutorSpec(
            OrdersApi,
            "initialize_table_orders_by_tables_with_http_info",
            "init_table_order_request",
            _single_target_validator(
                "initialize_table_orders_by_tables",
                model=InitTableOrderRequest,
                role="compensating",
            ),
        ),
        "open_personal_session": _WriteExecutorSpec(
            EmployeesApi,
            "open_personal_session_with_http_info",
            "open_personal_session_request",
            _single_target_validator(
                "open_personal_session",
                model=OpenPersonalSessionRequest,
                role="compensating",
            ),
        ),
        "close_personal_session": _WriteExecutorSpec(
            EmployeesApi,
            "close_personal_session_with_http_info",
            "close_personal_session_request",
            _single_target_validator(
                "close_personal_session",
                model=ClosePersonalSessionRequest,
                role="cleanup",
            ),
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
