"""Guarded inventory document, counteragent, and cost-price read cases."""

from __future__ import annotations

import importlib
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import date
from uuid import UUID

from tests.integration.read.cases.finance import (
    FieldSpec,
    make_document_get_case,
    make_period_list_case,
)
from tools.openapi_pipeline.live.read_case import (
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
)

INVENTORY_LIST_OPERATION_IDS = (
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

STORE_TARGET_KEYS = (
    "inventory_disassemble_document_store_from_id",
    "inventory_disassemble_document_store_to_id",
    "inventory_incoming_invoice_default_store_id",
    "inventory_incoming_returned_invoice_assigned_store_id",
    "inventory_internal_transfer_store_from_id",
    "inventory_internal_transfer_store_to_id",
    "inventory_outgoing_invoice_default_store_id",
    "inventory_production_document_store_from_id",
    "inventory_production_document_store_to_id",
    "inventory_returned_invoice_assigned_store_id",
    "inventory_sales_document_assigned_store_id",
    "inventory_transformation_document_store_from_id",
    "inventory_transformation_document_store_to_id",
    "inventory_writeoff_document_store_from_id",
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


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        model = _generated_class(module_name, class_name)
        if model is None or type(response) is not model:
            raise ReadAssertionFailure()

    return validate


def _empty_extract(
    _response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    return {}


def _organization_text(view: ContextView) -> str:
    organization_id = view.get("organization_id")
    if type(organization_id) is not UUID:
        raise ValueError("organization_id must be a UUID")
    return str(organization_id)


def _canonical_guid(value: object) -> str | None:
    if type(value) is not str or not value:
        return None
    try:
        parsed = UUID(value)
    except (AttributeError, TypeError, ValueError):
        return None
    return str(parsed)


def _first_store(view: ContextView) -> str:
    for key in STORE_TARGET_KEYS:
        candidate = _canonical_guid(view.get(key))
        if candidate is not None:
            return candidate
    raise NoLiveTarget(NoLiveTargetCode.STORE)


def _product_text(view: ContextView) -> str:
    product_id = view.get("product_id")
    if type(product_id) is not UUID:
        raise NoLiveTarget(NoLiveTargetCode.PRODUCT)
    return str(product_id)


def _incoming_timestamp(view: ContextView) -> str:
    raw_date = view.get("date_yyyy_mm_dd")
    parsed: date | None = None
    if type(raw_date) is str:
        try:
            parsed = date.fromisoformat(raw_date)
        except ValueError:
            parsed = None
    if parsed is None or parsed.isoformat() != raw_date:
        raise ValueError("date_yyyy_mm_dd must be an ISO date")
    return f"{raw_date}T00:00:00.000+00:00"


def _counteragents_unavailable(_view: ContextView) -> Mapping[str, object]:
    raise NoLiveTarget(NoLiveTargetCode.ENDPOINT)


def _build_cost_prices(view: ContextView) -> Mapping[str, object]:
    product_id = _product_text(view)
    store_id = _first_store(view)
    return {
        "date_incoming": _incoming_timestamp(view),
        "items": [
            {
                "amount_factor": 1,
                "product_id": product_id,
                "store_id": store_id,
            }
        ],
        "organization_id": _organization_text(view),
    }


@dataclass(frozen=True, slots=True)
class _DocumentFamily:
    list_operation_id: str
    get_operation_id: str
    list_binding: GeneratedReadBinding
    get_binding: GeneratedReadBinding
    item_module: str
    item_class: str
    get_response_module: str
    get_response_class: str
    document_key: str
    account_keys: tuple[FieldSpec, ...] = ()
    store_keys: tuple[FieldSpec, ...] = ()
    active_attribute: str = "deleted"
    active_values: tuple[object, ...] = (False,)

    def cases(self) -> tuple[ReadCase, ReadCase]:
        list_case = make_period_list_case(
            self.list_operation_id,
            self.list_binding,
            self.document_key,
            self.account_keys,
            self.store_keys,
            item_module=self.item_module,
            item_class=self.item_class,
            active_attribute=self.active_attribute,
            active_values=self.active_values,
        )
        get_case = make_document_get_case(
            self.get_operation_id,
            self.get_binding,
            self.list_operation_id,
            self.document_key,
            response_module=self.get_response_module,
            response_class=self.get_response_class,
        )
        return list_case, get_case


_DOCUMENT_FAMILIES = (
    _DocumentFamily(
        "list_inventory_disassemble_documents",
        "get_inventory_disassemble_document",
        _binding(
            "list_inventory_disassemble_documents",
            "public_api_invoice_processing_disassemble_document_api",
            "PublicApiInvoiceProcessingDisassembleDocumentApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_disassemble_document",
            "public_api_invoice_processing_disassemble_document_api",
            "PublicApiInvoiceProcessingDisassembleDocumentApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "disassemble_document_list_item",
        "DisassembleDocumentListItem",
        "disassemble_document_get_response",
        "DisassembleDocumentGetResponse",
        "inventory_disassemble_document_id",
        store_keys=(
            (
                "inventory_disassemble_document_store_from_id",
                "store_from",
            ),
            ("inventory_disassemble_document_store_to_id", "store_to"),
        ),
    ),
    _DocumentFamily(
        "list_inventory_incoming_invoices",
        "get_inventory_incoming_invoice",
        _binding(
            "list_inventory_incoming_invoices",
            "public_api_invoice_processing_incoming_invoices_api",
            "PublicApiInvoiceProcessingIncomingInvoicesApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_incoming_invoice",
            "public_api_invoice_processing_incoming_invoices_api",
            "PublicApiInvoiceProcessingIncomingInvoicesApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "incoming_invoice",
        "IncomingInvoice",
        "incoming_invoice",
        "IncomingInvoice",
        "inventory_incoming_invoice_document_id",
        store_keys=(("inventory_incoming_invoice_default_store_id", "default_store"),),
        active_attribute="status",
        active_values=("NEW", "PROCESSED"),
    ),
    _DocumentFamily(
        "list_inventory_incoming_returned_invoices",
        "get_inventory_incoming_returned_invoice",
        _binding(
            "list_inventory_incoming_returned_invoices",
            "public_api_invoice_processing_incoming_returned_invoice_api",
            "PublicApiInvoiceProcessingIncomingReturnedInvoiceApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_incoming_returned_invoice",
            "public_api_invoice_processing_incoming_returned_invoice_api",
            "PublicApiInvoiceProcessingIncomingReturnedInvoiceApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "incoming_returned_invoice_list_item",
        "IncomingReturnedInvoiceListItem",
        "incoming_returned_invoice_get_response",
        "IncomingReturnedInvoiceGetResponse",
        "inventory_incoming_returned_invoice_document_id",
        account_keys=(
            (
                "inventory_incoming_returned_invoice_expense_account_id",
                "expense_account",
            ),
            (
                "inventory_incoming_returned_invoice_revenue_account_id",
                "revenue_account",
            ),
        ),
        store_keys=(
            (
                "inventory_incoming_returned_invoice_assigned_store_id",
                "assigned_stores",
            ),
        ),
    ),
    _DocumentFamily(
        "list_inventory_internal_transfers",
        "get_inventory_internal_transfer",
        _binding(
            "list_inventory_internal_transfers",
            "public_api_invoice_processing_internal_transfer_api",
            "PublicApiInvoiceProcessingInternalTransferApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_internal_transfer",
            "public_api_invoice_processing_internal_transfer_api",
            "PublicApiInvoiceProcessingInternalTransferApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "internal_transfer_list_item",
        "InternalTransferListItem",
        "internal_transfer_get_response",
        "InternalTransferGetResponse",
        "inventory_internal_transfer_document_id",
        store_keys=(
            ("inventory_internal_transfer_store_from_id", "store_from"),
            ("inventory_internal_transfer_store_to_id", "store_to"),
        ),
    ),
    _DocumentFamily(
        "list_inventory_outgoing_invoices",
        "get_inventory_outgoing_invoice",
        _binding(
            "list_inventory_outgoing_invoices",
            "public_api_invoice_processing_outgoing_invoices_api",
            "PublicApiInvoiceProcessingOutgoingInvoicesApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_outgoing_invoice",
            "public_api_invoice_processing_outgoing_invoices_api",
            "PublicApiInvoiceProcessingOutgoingInvoicesApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "outgoing_invoice",
        "OutgoingInvoice",
        "outgoing_invoice",
        "OutgoingInvoice",
        "inventory_outgoing_invoice_document_id",
        account_keys=(
            (
                "inventory_outgoing_invoice_expense_account_id",
                "expense_account",
            ),
            (
                "inventory_outgoing_invoice_revenue_account_id",
                "revenue_account",
            ),
        ),
        store_keys=(("inventory_outgoing_invoice_default_store_id", "default_store"),),
        active_attribute="status",
        active_values=("NEW", "PROCESSED"),
    ),
    _DocumentFamily(
        "list_inventory_production_documents",
        "get_inventory_production_document",
        _binding(
            "list_inventory_production_documents",
            "public_api_invoice_processing_production_document_api",
            "PublicApiInvoiceProcessingProductionDocumentApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_production_document",
            "public_api_invoice_processing_production_document_api",
            "PublicApiInvoiceProcessingProductionDocumentApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "production_document_list_item",
        "ProductionDocumentListItem",
        "production_document_get_response",
        "ProductionDocumentGetResponse",
        "inventory_production_document_id",
        store_keys=(
            ("inventory_production_document_store_from_id", "store_from"),
            ("inventory_production_document_store_to_id", "store_to"),
        ),
    ),
    _DocumentFamily(
        "list_inventory_returned_invoices",
        "get_inventory_returned_invoice",
        _binding(
            "list_inventory_returned_invoices",
            "public_api_invoice_processing_returned_invoice_api",
            "PublicApiInvoiceProcessingReturnedInvoiceApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_returned_invoice",
            "public_api_invoice_processing_returned_invoice_api",
            "PublicApiInvoiceProcessingReturnedInvoiceApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "returned_invoice_list_item",
        "ReturnedInvoiceListItem",
        "returned_invoice_get_response",
        "ReturnedInvoiceGetResponse",
        "inventory_returned_invoice_document_id",
        account_keys=(
            (
                "inventory_returned_invoice_expense_account_id",
                "expense_account",
            ),
        ),
        store_keys=(
            (
                "inventory_returned_invoice_assigned_store_id",
                "assigned_stores",
            ),
        ),
    ),
    _DocumentFamily(
        "list_inventory_sales_documents",
        "get_inventory_sales_document",
        _binding(
            "list_inventory_sales_documents",
            "public_api_invoice_processing_sales_document_api",
            "PublicApiInvoiceProcessingSalesDocumentApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_sales_document",
            "public_api_invoice_processing_sales_document_api",
            "PublicApiInvoiceProcessingSalesDocumentApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "sales_document_list_item",
        "SalesDocumentListItem",
        "sales_document_get_response",
        "SalesDocumentGetResponse",
        "inventory_sales_document_id",
        account_keys=(
            (
                "inventory_sales_document_expense_account_id",
                "expense_account",
            ),
            (
                "inventory_sales_document_revenue_account_id",
                "revenue_account",
            ),
        ),
        store_keys=(
            (
                "inventory_sales_document_assigned_store_id",
                "assigned_stores",
            ),
        ),
    ),
    _DocumentFamily(
        "list_inventory_transformation_documents",
        "get_inventory_transformation_document",
        _binding(
            "list_inventory_transformation_documents",
            "public_api_invoice_processing_transformation_document_api",
            "PublicApiInvoiceProcessingTransformationDocumentApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_transformation_document",
            "public_api_invoice_processing_transformation_document_api",
            "PublicApiInvoiceProcessingTransformationDocumentApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "transformation_document_list_item",
        "TransformationDocumentListItem",
        "transformation_document_get_response",
        "TransformationDocumentGetResponse",
        "inventory_transformation_document_id",
        store_keys=(
            (
                "inventory_transformation_document_store_from_id",
                "store_from",
            ),
            (
                "inventory_transformation_document_store_to_id",
                "store_to",
            ),
        ),
    ),
    _DocumentFamily(
        "list_inventory_writeoff_documents",
        "get_inventory_writeoff_document",
        _binding(
            "list_inventory_writeoff_documents",
            "public_api_invoice_processing_writeoff_document_api",
            "PublicApiInvoiceProcessingWriteoffDocumentApi",
            "list_request",
            "ListRequest",
            "list_request",
        ),
        _binding(
            "get_inventory_writeoff_document",
            "public_api_invoice_processing_writeoff_document_api",
            "PublicApiInvoiceProcessingWriteoffDocumentApi",
            "get_by_id_request",
            "GetByIDRequest",
            "get_by_id_request",
        ),
        "writeoff_document_list_item",
        "WriteoffDocumentListItem",
        "writeoff_document_get_response",
        "WriteoffDocumentGetResponse",
        "inventory_writeoff_document_id",
        account_keys=(
            (
                "inventory_writeoff_document_expense_account_id",
                "expense_account",
            ),
        ),
        store_keys=(("inventory_writeoff_document_store_from_id", "store_from"),),
    ),
)

_DOCUMENT_CASES = tuple(case for family in _DOCUMENT_FAMILIES for case in family.cases())

_COUNTERAGENTS = ReadCase(
    operation_id="get_inventory_counteragents",
    revision=2,
    depends_on=("get_organizations",),
    requires=("organization_id",),
    provides=(),
    allowed_no_target_codes=frozenset({NoLiveTargetCode.ENDPOINT}),
    binding=_binding(
        "get_inventory_counteragents",
        "public_api_invoice_processing_counteragents_api",
        "PublicApiInvoiceProcessingCounteragentsApi",
        "get_counteragents_request",
        "GetCounteragentsRequest",
        "get_counteragents_request",
    ),
    build_values=_counteragents_unavailable,
    validate_response=_typed_validator(
        "get_counteragents_response",
        "GetCounteragentsResponse",
    ),
    extract=_empty_extract,
)

_COST_PRICES = ReadCase(
    operation_id="calculate_inventory_cost_prices",
    revision=1,
    depends_on=("get_nomenclature", *INVENTORY_LIST_OPERATION_IDS),
    requires=(
        "organization_id",
        "date_yyyy_mm_dd",
        "product_id",
        *STORE_TARGET_KEYS,
    ),
    provides=(),
    allowed_no_target_codes=frozenset({NoLiveTargetCode.PRODUCT, NoLiveTargetCode.STORE}),
    binding=_binding(
        "calculate_inventory_cost_prices",
        "public_api_invoice_processing_outgoing_invoices_api",
        "PublicApiInvoiceProcessingOutgoingInvoicesApi",
        "get_cost_prices_request",
        "GetCostPricesRequest",
        "get_cost_prices_request",
    ),
    build_values=_build_cost_prices,
    validate_response=_typed_validator(
        "get_cost_prices_response",
        "GetCostPricesResponse",
    ),
    extract=_empty_extract,
)

INVENTORY_CASES = (*_DOCUMENT_CASES, _COUNTERAGENTS, _COST_PRICES)

__all__ = [
    "INVENTORY_CASES",
    "INVENTORY_LIST_OPERATION_IDS",
    "STORE_TARGET_KEYS",
]
