"""Guarded finance document and transaction read cases."""

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

FieldSpec = tuple[str, str]

DOCUMENT_TARGET_KEYS = (
    "finance_incoming_service_document_id",
    "finance_outgoing_service_document_id",
    "inventory_disassemble_document_id",
    "inventory_incoming_invoice_document_id",
    "inventory_incoming_returned_invoice_document_id",
    "inventory_internal_transfer_document_id",
    "inventory_outgoing_invoice_document_id",
    "inventory_production_document_id",
    "inventory_returned_invoice_document_id",
    "inventory_sales_document_id",
    "inventory_transformation_document_id",
    "inventory_writeoff_document_id",
)

DOCUMENT_PROVIDER_OPERATION_IDS = (
    "list_finance_incoming_services",
    "list_finance_outgoing_services",
    "list_inventory_disassemble_documents",
    "list_inventory_incoming_invoices",
    "list_inventory_incoming_returned_invoices",
    "list_inventory_internal_transfers",
    "list_inventory_outgoing_invoices",
    "list_inventory_production_documents",
    "list_inventory_returned_invoices",
    "list_inventory_sales_documents",
    "list_inventory_transformation_documents",
    "list_inventory_writeoff_documents",
)

ACCOUNT_TARGET_KEYS = (
    "finance_incoming_service_revenue_account_id",
    "finance_outgoing_service_revenue_account_id",
    "inventory_incoming_returned_invoice_expense_account_id",
    "inventory_incoming_returned_invoice_revenue_account_id",
    "inventory_outgoing_invoice_expense_account_id",
    "inventory_outgoing_invoice_revenue_account_id",
    "inventory_returned_invoice_expense_account_id",
    "inventory_sales_document_expense_account_id",
    "inventory_sales_document_revenue_account_id",
    "inventory_writeoff_document_expense_account_id",
    "finance_document_transaction_from_account_id",
    "finance_document_transaction_to_account_id",
)

_DOCUMENT_TRANSACTION_ACCOUNT_KEYS = (
    "finance_document_transaction_from_account_id",
    "finance_document_transaction_to_account_id",
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


def _canonical_guid(value: object) -> str | None:
    if type(value) is not str or not value:
        return None
    try:
        parsed = UUID(value)
    except (AttributeError, TypeError, ValueError):
        return None
    return str(parsed)


def _organization_text(view: ContextView) -> str:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        raise ValueError("organization_id must be a UUID")
    return str(organization_id)


def _first_guid(
    view: ContextView,
    keys: tuple[str, ...],
    code: NoLiveTargetCode,
) -> str:
    for key in keys:
        candidate = _canonical_guid(view.get(key))
        if candidate is not None:
            return candidate
    raise NoLiveTarget(code)


def _exact_value(value: object, allowed: tuple[object, ...]) -> bool:
    return any(
        type(value) is type(candidate) and value == candidate
        for candidate in allowed
    )


def _attribute_guid(item: object, attribute: str) -> str | None:
    try:
        value = getattr(item, attribute)
    except Exception:
        return None
    if type(value) is list:
        for candidate in value:
            parsed = _canonical_guid(candidate)
            if parsed is not None:
                return parsed
        return None
    return _canonical_guid(value)


def _raw_list_validator(
    item_module: str,
    item_class: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        model = _generated_class(item_module, item_class)
        if (
            model is None
            or type(response) is not list
            or any(type(item) is not model for item in response)
        ):
            raise ReadAssertionFailure()

    return validate


def _list_extractor(
    *,
    item_module: str,
    item_class: str,
    document_key: str,
    account_keys: tuple[FieldSpec, ...],
    store_keys: tuple[FieldSpec, ...],
    active_attribute: str,
    active_values: tuple[object, ...],
) -> Callable[[object, ContextView], Mapping[str, object]]:
    def extract(response: object, _view: ContextView) -> Mapping[str, object]:
        model = _generated_class(item_module, item_class)
        if (
            model is None
            or type(response) is not list
            or any(type(item) is not model for item in response)
        ):
            return {}
        for item in response:
            generated_item = cast(Any, item)
            field_unavailable = False
            active: object = None
            try:
                active = getattr(generated_item, active_attribute)
            except Exception:
                field_unavailable = True
            document_id = _attribute_guid(generated_item, "document_id")
            if (
                field_unavailable
                or not _exact_value(active, active_values)
                or document_id is None
            ):
                continue
            extracted: dict[str, object] = {document_key: document_id}
            for context_key, attribute in (*account_keys, *store_keys):
                value = _attribute_guid(generated_item, attribute)
                if value is not None:
                    extracted[context_key] = value
            return extracted
        return {}

    return extract


def _build_period_list(view: ContextView) -> Mapping[str, object]:
    return {
        "var_from": view["period_from_yyyy_mm_dd"],
        "organization_id": _organization_text(view),
        "to": view["period_to_yyyy_mm_dd"],
    }


def make_period_list_case(
    operation_id: str,
    binding: GeneratedReadBinding,
    document_key: str,
    account_keys: tuple[FieldSpec, ...],
    store_keys: tuple[FieldSpec, ...],
    *,
    item_module: str,
    item_class: str,
    active_attribute: str = "deleted",
    active_values: tuple[object, ...] = (False,),
) -> ReadCase:
    """Create a bounded list case with same-item target extraction."""

    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=("get_organizations",),
        requires=(
            "organization_id",
            "period_from_yyyy_mm_dd",
            "period_to_yyyy_mm_dd",
        ),
        provides=(
            document_key,
            *(key for key, _attribute in account_keys),
            *(key for key, _attribute in store_keys),
        ),
        allowed_no_target_codes=frozenset(),
        binding=binding,
        build_values=_build_period_list,
        validate_response=_raw_list_validator(item_module, item_class),
        extract=_list_extractor(
            item_module=item_module,
            item_class=item_class,
            document_key=document_key,
            account_keys=account_keys,
            store_keys=store_keys,
            active_attribute=active_attribute,
            active_values=active_values,
        ),
    )


def _document_builder(document_key: str) -> Callable[[ContextView], Mapping[str, object]]:
    def build(view: ContextView) -> Mapping[str, object]:
        return {
            "document_id": _first_guid(
                view,
                (document_key,),
                NoLiveTargetCode.DOCUMENT,
            ),
            "organization_id": _organization_text(view),
        }

    return build


def _document_get_validator(
    response_module: str,
    response_class: str,
    document_key: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, view: ContextView) -> None:
        model = _generated_class(response_module, response_class)
        expected = _canonical_guid(view.get(document_key))
        field_unavailable = False
        response_document_id: object = None
        if model is not None and type(response) is model:
            try:
                response_document_id = response.document_id  # type: ignore[attr-defined]
            except Exception:
                field_unavailable = True
        else:
            field_unavailable = True
        if (
            field_unavailable
            or expected is None
            or type(response_document_id) is not str
            or response_document_id != expected
        ):
            raise ReadAssertionFailure()

    return validate


def _empty_extract(
    _response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    return {}


def make_document_get_case(
    operation_id: str,
    binding: GeneratedReadBinding,
    provider_operation_id: str,
    document_key: str,
    *,
    response_module: str,
    response_class: str,
) -> ReadCase:
    """Create a get case linked to one response-derived list document."""

    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=(provider_operation_id,),
        requires=("organization_id", document_key),
        provides=(),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.DOCUMENT}),
        binding=binding,
        build_values=_document_builder(document_key),
        validate_response=_document_get_validator(
            response_module,
            response_class,
            document_key,
        ),
        extract=_empty_extract,
    )


def _build_document_transactions(view: ContextView) -> Mapping[str, object]:
    return {
        "document_id": _first_guid(
            view,
            DOCUMENT_TARGET_KEYS,
            NoLiveTargetCode.DOCUMENT,
        ),
        "organization_id": _organization_text(view),
    }


def _validate_document_transactions(
    response: object,
    view: ContextView,
) -> None:
    model = _generated_class(
        "document_transaction_item",
        "DocumentTransactionItem",
    )
    expected = None
    try:
        expected = _first_guid(
            view,
            DOCUMENT_TARGET_KEYS,
            NoLiveTargetCode.DOCUMENT,
        )
    except NoLiveTarget:
        expected = None
    invalid = (
        model is None
        or type(response) is not list
        or any(type(item) is not model for item in response)
        or expected is None
    )
    if not invalid:
        items = cast(list[object], response)
        for item in items:
            generated_item = cast(Any, item)
            field_unavailable = False
            document_id: object = None
            try:
                document_id = generated_item.document_id
            except Exception:
                field_unavailable = True
            if (
                field_unavailable
                or (
                    document_id is not None
                    and (type(document_id) is not str or document_id != expected)
                )
            ):
                invalid = True
                break
    if invalid:
        raise ReadAssertionFailure()


def _transaction_side_account(item: object, attribute: str) -> str | None:
    side_model = _generated_class("transaction_side", "TransactionSide")
    try:
        side = getattr(item, attribute)
    except Exception:
        return None
    if side_model is None or type(side) is not side_model:
        return None
    return _attribute_guid(side, "account")


def _extract_document_transaction_accounts(
    response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    model = _generated_class(
        "document_transaction_item",
        "DocumentTransactionItem",
    )
    if (
        model is None
        or type(response) is not list
        or any(type(item) is not model for item in response)
    ):
        return {}
    extracted: dict[str, object] = {}
    for item in response:
        if "finance_document_transaction_from_account_id" not in extracted:
            account_from = _transaction_side_account(item, "var_from")
            if account_from is not None:
                extracted[
                    "finance_document_transaction_from_account_id"
                ] = account_from
        if "finance_document_transaction_to_account_id" not in extracted:
            account_to = _transaction_side_account(item, "to")
            if account_to is not None:
                extracted[
                    "finance_document_transaction_to_account_id"
                ] = account_to
        if len(extracted) == len(_DOCUMENT_TRANSACTION_ACCOUNT_KEYS):
            break
    return extracted


def _build_account_transactions(view: ContextView) -> Mapping[str, object]:
    return {
        "account_id": _first_guid(
            view,
            ACCOUNT_TARGET_KEYS,
            NoLiveTargetCode.ACCOUNT,
        ),
        "var_from": view["period_from_yyyy_mm_dd"],
        "organization_id": _organization_text(view),
        "to": view["period_to_yyyy_mm_dd"],
    }


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        model = _generated_class(module_name, class_name)
        if model is None or type(response) is not model:
            raise ReadAssertionFailure()

    return validate


_INCOMING_LIST_BINDING = _binding(
    "list_finance_incoming_services",
    "public_api_invoice_processing_incoming_service_api",
    "PublicApiInvoiceProcessingIncomingServiceApi",
    "list_request",
    "ListRequest",
    "list_request",
)
_OUTGOING_LIST_BINDING = _binding(
    "list_finance_outgoing_services",
    "public_api_invoice_processing_outgoing_service_api",
    "PublicApiInvoiceProcessingOutgoingServiceApi",
    "list_request",
    "ListRequest",
    "list_request",
)

_INCOMING_LIST = make_period_list_case(
    "list_finance_incoming_services",
    _INCOMING_LIST_BINDING,
    "finance_incoming_service_document_id",
    (("finance_incoming_service_revenue_account_id", "revenue_account"),),
    (),
    item_module="incoming_service_list_item",
    item_class="IncomingServiceListItem",
)
_OUTGOING_LIST = make_period_list_case(
    "list_finance_outgoing_services",
    _OUTGOING_LIST_BINDING,
    "finance_outgoing_service_document_id",
    (("finance_outgoing_service_revenue_account_id", "revenue_account"),),
    (),
    item_module="outgoing_service_list_item",
    item_class="OutgoingServiceListItem",
)

_INCOMING_GET = make_document_get_case(
    "get_finance_incoming_service",
    _binding(
        "get_finance_incoming_service",
        "public_api_invoice_processing_incoming_service_api",
        "PublicApiInvoiceProcessingIncomingServiceApi",
        "get_by_id_request",
        "GetByIDRequest",
        "get_by_id_request",
    ),
    "list_finance_incoming_services",
    "finance_incoming_service_document_id",
    response_module="incoming_service_get_response",
    response_class="IncomingServiceGetResponse",
)
_OUTGOING_GET = make_document_get_case(
    "get_finance_outgoing_service",
    _binding(
        "get_finance_outgoing_service",
        "public_api_invoice_processing_outgoing_service_api",
        "PublicApiInvoiceProcessingOutgoingServiceApi",
        "get_by_id_request",
        "GetByIDRequest",
        "get_by_id_request",
    ),
    "list_finance_outgoing_services",
    "finance_outgoing_service_document_id",
    response_module="outgoing_service_get_response",
    response_class="OutgoingServiceGetResponse",
)

_DOCUMENT_TRANSACTIONS = ReadCase(
    operation_id="list_finance_document_transactions",
    revision=1,
    depends_on=DOCUMENT_PROVIDER_OPERATION_IDS,
    requires=("organization_id", *DOCUMENT_TARGET_KEYS),
    provides=_DOCUMENT_TRANSACTION_ACCOUNT_KEYS,
    allowed_no_target_codes=frozenset({NoLiveTargetCode.DOCUMENT}),
    binding=_binding(
        "list_finance_document_transactions",
        "public_api_invoice_processing_document_transactions_api",
        "PublicApiInvoiceProcessingDocumentTransactionsApi",
        "document_transactions_list_request",
        "DocumentTransactionsListRequest",
        "document_transactions_list_request",
    ),
    build_values=_build_document_transactions,
    validate_response=_validate_document_transactions,
    extract=_extract_document_transaction_accounts,
)

_ACCOUNT_TRANSACTIONS = ReadCase(
    operation_id="list_finance_account_transactions",
    revision=1,
    depends_on=(
        *DOCUMENT_PROVIDER_OPERATION_IDS,
        "list_finance_document_transactions",
    ),
    requires=(
        "organization_id",
        "period_from_yyyy_mm_dd",
        "period_to_yyyy_mm_dd",
        *ACCOUNT_TARGET_KEYS,
    ),
    provides=(),
    allowed_no_target_codes=frozenset({NoLiveTargetCode.ACCOUNT}),
    binding=_binding(
        "list_finance_account_transactions",
        "public_api_invoice_processing_account_transactions_api",
        "PublicApiInvoiceProcessingAccountTransactionsApi",
        "account_transactions_list_request",
        "AccountTransactionsListRequest",
        "account_transactions_list_request",
    ),
    build_values=_build_account_transactions,
    validate_response=_typed_validator(
        "account_transactions_response",
        "AccountTransactionsResponse",
    ),
    extract=_empty_extract,
)

FINANCE_CASES = (
    _INCOMING_LIST,
    _OUTGOING_LIST,
    _INCOMING_GET,
    _OUTGOING_GET,
    _DOCUMENT_TRANSACTIONS,
    _ACCOUNT_TRANSACTIONS,
)

__all__ = [
    "ACCOUNT_TARGET_KEYS",
    "DOCUMENT_PROVIDER_OPERATION_IDS",
    "DOCUMENT_TARGET_KEYS",
    "FINANCE_CASES",
    "FieldSpec",
    "make_document_get_case",
    "make_period_list_case",
]
