from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.finance import FINANCE_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.inventory import (
    INVENTORY_CASES,
    INVENTORY_LIST_OPERATION_IDS,
    STORE_TARGET_KEYS,
)
from tests.integration.read.cases.menu import MENU_CASES
from tools.openapi_pipeline.live.read_case import (
    ContextView,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCapability,
    ReadCase,
    ReadContext,
    build_generated_request,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
PRODUCT_ID = UUID("22222222-2222-4222-8222-222222222222")
DOCUMENT_ID = "33333333-3333-4333-8333-333333333333"
OTHER_DOCUMENT_ID = "44444444-4444-4444-8444-444444444444"
FIELD_ID = "55555555-5555-4555-8555-555555555555"
FIRST_STORE_ID = "66666666-6666-4666-8666-666666666666"
LAST_STORE_ID = "77777777-7777-4777-8777-777777777777"
PERIOD_FROM = "2026-01-01"
PERIOD_TO = "2026-01-02"
DATE = "2026-01-01"
_UNSET = object()


@dataclass(frozen=True, slots=True)
class FamilySpec:
    family: str
    api_module: str
    api_class: str
    list_item_module: str
    list_item_class: str
    get_response_module: str
    get_response_class: str
    activity_attribute: str
    active_value: object
    inactive_value: object
    fields: tuple[tuple[str, str, bool], ...]

    @property
    def list_id(self) -> str:
        return f"list_inventory_{self.family}s"

    @property
    def get_id(self) -> str:
        return f"get_inventory_{self.family}"

    @property
    def document_key(self) -> str:
        suffix = "" if self.family.endswith("_document") else "_document"
        return f"inventory_{self.family}{suffix}_id"


FAMILY_SPECS = (
    FamilySpec(
        "disassemble_document",
        "public_api_invoice_processing_disassemble_document_api",
        "PublicApiInvoiceProcessingDisassembleDocumentApi",
        "disassemble_document_list_item",
        "DisassembleDocumentListItem",
        "disassemble_document_get_response",
        "DisassembleDocumentGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_disassemble_document_store_from_id",
                "store_from",
                False,
            ),
            (
                "inventory_disassemble_document_store_to_id",
                "store_to",
                False,
            ),
        ),
    ),
    FamilySpec(
        "incoming_invoice",
        "public_api_invoice_processing_incoming_invoices_api",
        "PublicApiInvoiceProcessingIncomingInvoicesApi",
        "incoming_invoice",
        "IncomingInvoice",
        "incoming_invoice",
        "IncomingInvoice",
        "status",
        "NEW",
        "DELETED",
        (
            (
                "inventory_incoming_invoice_default_store_id",
                "default_store",
                False,
            ),
        ),
    ),
    FamilySpec(
        "incoming_returned_invoice",
        "public_api_invoice_processing_incoming_returned_invoice_api",
        "PublicApiInvoiceProcessingIncomingReturnedInvoiceApi",
        "incoming_returned_invoice_list_item",
        "IncomingReturnedInvoiceListItem",
        "incoming_returned_invoice_get_response",
        "IncomingReturnedInvoiceGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_incoming_returned_invoice_expense_account_id",
                "expense_account",
                False,
            ),
            (
                "inventory_incoming_returned_invoice_revenue_account_id",
                "revenue_account",
                False,
            ),
            (
                "inventory_incoming_returned_invoice_assigned_store_id",
                "assigned_stores",
                True,
            ),
        ),
    ),
    FamilySpec(
        "internal_transfer",
        "public_api_invoice_processing_internal_transfer_api",
        "PublicApiInvoiceProcessingInternalTransferApi",
        "internal_transfer_list_item",
        "InternalTransferListItem",
        "internal_transfer_get_response",
        "InternalTransferGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_internal_transfer_store_from_id",
                "store_from",
                False,
            ),
            (
                "inventory_internal_transfer_store_to_id",
                "store_to",
                False,
            ),
        ),
    ),
    FamilySpec(
        "outgoing_invoice",
        "public_api_invoice_processing_outgoing_invoices_api",
        "PublicApiInvoiceProcessingOutgoingInvoicesApi",
        "outgoing_invoice",
        "OutgoingInvoice",
        "outgoing_invoice",
        "OutgoingInvoice",
        "status",
        "PROCESSED",
        "DELETED",
        (
            (
                "inventory_outgoing_invoice_expense_account_id",
                "expense_account",
                False,
            ),
            (
                "inventory_outgoing_invoice_revenue_account_id",
                "revenue_account",
                False,
            ),
            (
                "inventory_outgoing_invoice_default_store_id",
                "default_store",
                False,
            ),
        ),
    ),
    FamilySpec(
        "production_document",
        "public_api_invoice_processing_production_document_api",
        "PublicApiInvoiceProcessingProductionDocumentApi",
        "production_document_list_item",
        "ProductionDocumentListItem",
        "production_document_get_response",
        "ProductionDocumentGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_production_document_store_from_id",
                "store_from",
                False,
            ),
            (
                "inventory_production_document_store_to_id",
                "store_to",
                False,
            ),
        ),
    ),
    FamilySpec(
        "returned_invoice",
        "public_api_invoice_processing_returned_invoice_api",
        "PublicApiInvoiceProcessingReturnedInvoiceApi",
        "returned_invoice_list_item",
        "ReturnedInvoiceListItem",
        "returned_invoice_get_response",
        "ReturnedInvoiceGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_returned_invoice_expense_account_id",
                "expense_account",
                False,
            ),
            (
                "inventory_returned_invoice_assigned_store_id",
                "assigned_stores",
                True,
            ),
        ),
    ),
    FamilySpec(
        "sales_document",
        "public_api_invoice_processing_sales_document_api",
        "PublicApiInvoiceProcessingSalesDocumentApi",
        "sales_document_list_item",
        "SalesDocumentListItem",
        "sales_document_get_response",
        "SalesDocumentGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_sales_document_expense_account_id",
                "expense_account",
                False,
            ),
            (
                "inventory_sales_document_revenue_account_id",
                "revenue_account",
                False,
            ),
            (
                "inventory_sales_document_assigned_store_id",
                "assigned_stores",
                True,
            ),
        ),
    ),
    FamilySpec(
        "transformation_document",
        "public_api_invoice_processing_transformation_document_api",
        "PublicApiInvoiceProcessingTransformationDocumentApi",
        "transformation_document_list_item",
        "TransformationDocumentListItem",
        "transformation_document_get_response",
        "TransformationDocumentGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_transformation_document_store_from_id",
                "store_from",
                False,
            ),
            (
                "inventory_transformation_document_store_to_id",
                "store_to",
                False,
            ),
        ),
    ),
    FamilySpec(
        "writeoff_document",
        "public_api_invoice_processing_writeoff_document_api",
        "PublicApiInvoiceProcessingWriteoffDocumentApi",
        "writeoff_document_list_item",
        "WriteoffDocumentListItem",
        "writeoff_document_get_response",
        "WriteoffDocumentGetResponse",
        "deleted",
        False,
        True,
        (
            (
                "inventory_writeoff_document_expense_account_id",
                "expense_account",
                False,
            ),
            (
                "inventory_writeoff_document_store_from_id",
                "store_from",
                False,
            ),
        ),
    ),
)

INVENTORY_IDS = {
    "calculate_inventory_cost_prices",
    "get_inventory_counteragents",
    *(spec.get_id for spec in FAMILY_SPECS),
    *(spec.list_id for spec in FAMILY_SPECS),
}

EXPECTED_STORE_KEYS = (
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


def _class(module_name: str, class_name: str) -> type[object]:
    module = import_module(f"iikocloud_client.models.{module_name}")
    return getattr(module, class_name)


def _model(module_name: str, class_name: str, **values: object) -> object:
    model = _class(module_name, class_name)
    return model.model_construct(**values)  # type: ignore[attr-defined]


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
    return next(case for case in INVENTORY_CASES if case.operation_id == operation_id)


def _view(
    case: ReadCase,
    *,
    omit: frozenset[str] = frozenset(),
    **changes: object,
) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "product_id": PRODUCT_ID,
        "date_yyyy_mm_dd": DATE,
        "period_from_yyyy_mm_dd": PERIOD_FROM,
        "period_to_yyyy_mm_dd": PERIOD_TO,
        **{spec.document_key: DOCUMENT_ID for spec in FAMILY_SPECS},
        **{key: FIELD_ID for key in EXPECTED_STORE_KEYS},
    }
    values[EXPECTED_STORE_KEYS[0]] = FIRST_STORE_ID
    values[EXPECTED_STORE_KEYS[-1]] = LAST_STORE_ID
    values.update(changes)
    return ContextView(
        {key: values[key] for key in case.requires if key in values and key not in omit}
    )


def _provider_item(
    spec: FamilySpec,
    *,
    document_id: object = DOCUMENT_ID,
    activity: object = _UNSET,
    include_fields: bool = True,
) -> object:
    values: dict[str, object] = {
        "document_id": document_id,
        spec.activity_attribute: (spec.active_value if activity is _UNSET else activity),
    }
    for _context_key, attribute, is_list in spec.fields:
        if include_fields:
            values[attribute] = ["not-a-guid", FIELD_ID] if is_list else FIELD_ID
        else:
            values[attribute] = None
    return _model(spec.list_item_module, spec.list_item_class, **values)


def _request_json(case: ReadCase, view: ContextView | None = None) -> object:
    request = build_generated_request(
        case.binding,
        case.build_values(_view(case) if view is None else view),
    )
    assert request is not None
    return _jsonable(request.to_dict())  # type: ignore[attr-defined]


def _minimal_response(case: ReadCase) -> object:
    if case.operation_id == "get_inventory_counteragents":
        return _model(
            "get_counteragents_response",
            "GetCounteragentsResponse",
            counteragents=[],
            total_count=0,
        )
    if case.operation_id == "calculate_inventory_cost_prices":
        return _model(
            "get_cost_prices_response",
            "GetCostPricesResponse",
            items=[],
            problem_items=[],
        )
    for spec in FAMILY_SPECS:
        if case.operation_id == spec.list_id:
            return []
        if case.operation_id == spec.get_id:
            return _model(
                spec.get_response_module,
                spec.get_response_class,
                document_id=DOCUMENT_ID,
            )
    raise AssertionError("unknown inventory case")


def test_inventory_registry_and_combined_plan_are_exact() -> None:
    assert type(INVENTORY_CASES) is tuple
    assert {case.operation_id for case in INVENTORY_CASES} == INVENTORY_IDS
    assert len(INVENTORY_CASES) == 22
    plan = ReadPlan.build((*FOUNDATION_CASES, *MENU_CASES, *FINANCE_CASES, *INVENTORY_CASES))
    assert set(plan.ordered_operation_ids) >= INVENTORY_IDS


def test_all_inventory_cases_declare_invoice_processing_capability() -> None:
    assert len(INVENTORY_CASES) == 22
    for case in INVENTORY_CASES:
        assert case.capability is ReadCapability.PUBLIC_API_INVOICE_PROCESSING
        assert NoLiveTargetCode.INVOICE_PROCESSING in case.allowed_no_target_codes


def test_inventory_list_and_store_orders_are_exact() -> None:
    assert tuple(spec.list_id for spec in FAMILY_SPECS) == (INVENTORY_LIST_OPERATION_IDS)
    assert STORE_TARGET_KEYS == EXPECTED_STORE_KEYS


@pytest.mark.parametrize("spec", FAMILY_SPECS, ids=lambda spec: spec.family)
def test_document_family_bindings_dependencies_and_keys_are_exact(
    spec: FamilySpec,
) -> None:
    list_case = _case(spec.list_id)
    assert list_case.binding.api_module == f"iikocloud_client.api.{spec.api_module}"
    assert list_case.binding.api_class == spec.api_class
    assert list_case.binding.request_module == "iikocloud_client.models.list_request"
    assert list_case.binding.request_class == "ListRequest"
    assert list_case.binding.request_keyword == "list_request"
    assert list_case.depends_on == ("get_organizations",)
    assert list_case.requires == (
        "organization_id",
        "period_from_yyyy_mm_dd",
        "period_to_yyyy_mm_dd",
    )
    assert list_case.provides == (
        spec.document_key,
        *(context_key for context_key, _attribute, _is_list in spec.fields),
    )

    get_case = _case(spec.get_id)
    assert get_case.binding.api_module == f"iikocloud_client.api.{spec.api_module}"
    assert get_case.binding.api_class == spec.api_class
    assert get_case.binding.request_module == ("iikocloud_client.models.get_by_id_request")
    assert get_case.binding.request_class == "GetByIDRequest"
    assert get_case.binding.request_keyword == "get_by_id_request"
    assert get_case.depends_on == (spec.list_id,)
    assert get_case.requires == ("organization_id", spec.document_key)
    assert get_case.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.DOCUMENT, NoLiveTargetCode.INVOICE_PROCESSING}
    )


@pytest.mark.parametrize("spec", FAMILY_SPECS, ids=lambda spec: spec.family)
def test_document_list_requests_and_exact_bare_response_shapes(
    spec: FamilySpec,
) -> None:
    case = _case(spec.list_id)
    assert _request_json(case) == {
        "from": PERIOD_FROM,
        "organizationId": str(ORGANIZATION_ID),
        "to": PERIOD_TO,
    }
    case.validate_response([], _view(case))
    case.validate_response([_provider_item(spec)], _view(case))
    with pytest.raises(ReadAssertionFailure):
        case.validate_response({}, _view(case))
    with pytest.raises(ReadAssertionFailure):
        case.validate_response([object()], _view(case))


@pytest.mark.parametrize("spec", FAMILY_SPECS, ids=lambda spec: spec.family)
def test_document_provider_activity_and_same_item_extraction(
    spec: FamilySpec,
) -> None:
    case = _case(spec.list_id)
    response = [
        _provider_item(spec, document_id="not-a-guid"),
        _provider_item(spec, activity=spec.inactive_value),
        _provider_item(spec, activity=None),
        _provider_item(spec),
    ]
    expected = {spec.document_key: DOCUMENT_ID}
    expected.update({context_key: FIELD_ID for context_key, _attribute, _is_list in spec.fields})
    assert case.extract(response, _view(case)) == expected
    assert case.extract([], _view(case)) == {}

    no_fields_first = [
        _provider_item(spec, include_fields=False),
        _provider_item(spec, document_id=OTHER_DOCUMENT_ID),
    ]
    assert case.extract(no_fields_first, _view(case)) == {spec.document_key: DOCUMENT_ID}


@pytest.mark.parametrize("spec", FAMILY_SPECS, ids=lambda spec: spec.family)
def test_document_get_request_and_response_are_linked(spec: FamilySpec) -> None:
    case = _case(spec.get_id)
    assert _request_json(case) == {
        "documentId": DOCUMENT_ID,
        "organizationId": str(ORGANIZATION_ID),
    }
    response = _model(
        spec.get_response_module,
        spec.get_response_class,
        document_id=DOCUMENT_ID,
    )
    case.validate_response(response, _view(case))
    mismatched = _model(
        spec.get_response_module,
        spec.get_response_class,
        document_id=OTHER_DOCUMENT_ID,
    )
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(mismatched, _view(case))
    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(_view(case, omit=frozenset({spec.document_key})))
    assert missing.value.code is NoLiveTargetCode.DOCUMENT


def test_counteragent_live_read_is_temporarily_skipped_before_request_construction() -> None:
    case = _case("get_inventory_counteragents")
    assert case.depends_on == ("get_organizations",)
    assert case.requires == ("organization_id",)
    assert case.provides == ()

    with pytest.raises(NoLiveTarget) as unavailable:
        case.build_values(_view(case))

    assert unavailable.value.code.value == "endpoint_unavailable"
    assert case.allowed_no_target_codes == frozenset(
        {unavailable.value.code, NoLiveTargetCode.INVOICE_PROCESSING}
    )
    assert case.revision == 2


def test_cost_price_request_is_one_product_store_at_utc_midnight() -> None:
    case = _case("calculate_inventory_cost_prices")
    assert case.depends_on == ("get_nomenclature", *INVENTORY_LIST_OPERATION_IDS)
    assert case.requires == (
        "organization_id",
        "date_yyyy_mm_dd",
        "product_id",
        *STORE_TARGET_KEYS,
    )
    assert case.allowed_no_target_codes == frozenset(
        {
            NoLiveTargetCode.PRODUCT,
            NoLiveTargetCode.STORE,
            NoLiveTargetCode.INVOICE_PROCESSING,
        }
    )
    assert _request_json(case) == {
        "dateIncoming": "2026-01-01T00:00:00.000+00:00",
        "items": [
            {
                "amountFactor": 1,
                "productId": str(PRODUCT_ID),
                "storeId": FIRST_STORE_ID,
            }
        ],
        "organizationId": str(ORGANIZATION_ID),
    }
    request = build_generated_request(case.binding, case.build_values(_view(case)))
    assert request is not None
    assert type(request.items[0]).__name__ == "PriceItem"  # type: ignore[attr-defined]


def test_cost_price_store_priority_and_missing_targets_are_fixed() -> None:
    case = _case("calculate_inventory_cost_prices")
    last_only = _view(
        case,
        omit=frozenset(STORE_TARGET_KEYS[:-1]),
    )
    assert _request_json(case, last_only)["items"][0]["storeId"] == (  # type: ignore[index]
        LAST_STORE_ID
    )

    with pytest.raises(NoLiveTarget) as no_product:
        case.build_values(_view(case, omit=frozenset({"product_id"})))
    assert no_product.value.code is NoLiveTargetCode.PRODUCT

    with pytest.raises(NoLiveTarget) as no_store:
        case.build_values(_view(case, omit=frozenset(STORE_TARGET_KEYS)))
    assert no_store.value.code is NoLiveTargetCode.STORE


@pytest.mark.parametrize("operation_id", sorted(INVENTORY_IDS))
def test_bindings_resolve_and_validators_fail_with_fixed_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(case), _view(case))
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": "payload-marker"}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_inventory_targets_remain_hidden_in_context_renderings() -> None:
    list_case = _case("list_inventory_disassemble_documents")
    context = ReadContext.seed({"organization_id": ORGANIZATION_ID})
    context.apply(
        list_case,
        {
            "inventory_disassemble_document_id": DOCUMENT_ID,
            "inventory_disassemble_document_store_from_id": FIRST_STORE_ID,
        },
    )
    rendered = repr(
        (
            context,
            context.view(list_case.provides),
            INVENTORY_CASES,
        )
    )
    for marker in (
        str(ORGANIZATION_ID),
        str(PRODUCT_ID),
        DOCUMENT_ID,
        FIRST_STORE_ID,
    ):
        assert marker not in rendered
