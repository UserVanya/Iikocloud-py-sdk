from __future__ import annotations

from collections.abc import Mapping
from enum import Enum
from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.finance import (
    ACCOUNT_TARGET_KEYS,
    DOCUMENT_PROVIDER_OPERATION_IDS,
    DOCUMENT_TARGET_KEYS,
    FINANCE_CASES,
)
from tools.openapi_pipeline.live.read_case import (
    ContextView,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
    ReadContext,
    build_generated_request,
)

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
INCOMING_DOCUMENT_ID = "22222222-2222-4222-8222-222222222222"
OUTGOING_DOCUMENT_ID = "33333333-3333-4333-8333-333333333333"
INVENTORY_DOCUMENT_ID = "44444444-4444-4444-8444-444444444444"
INCOMING_ACCOUNT_ID = "55555555-5555-4555-8555-555555555555"
OUTGOING_ACCOUNT_ID = "66666666-6666-4666-8666-666666666666"
FROM_ACCOUNT_ID = "77777777-7777-4777-8777-777777777777"
TO_ACCOUNT_ID = "88888888-8888-4888-8888-888888888888"
PERIOD_FROM = "2026-01-01"
PERIOD_TO = "2026-01-02"

FINANCE_IDS = {
    "get_finance_incoming_service",
    "get_finance_outgoing_service",
    "list_finance_account_transactions",
    "list_finance_document_transactions",
    "list_finance_incoming_services",
    "list_finance_outgoing_services",
}

EXPECTED_DOCUMENT_KEYS = (
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

EXPECTED_PROVIDER_OPERATIONS = (
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

EXPECTED_ACCOUNT_KEYS = (
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

PRIVATE_MARKERS = (
    str(ORGANIZATION_ID),
    INCOMING_DOCUMENT_ID,
    OUTGOING_DOCUMENT_ID,
    INVENTORY_DOCUMENT_ID,
    INCOMING_ACCOUNT_ID,
    OUTGOING_ACCOUNT_ID,
    FROM_ACCOUNT_ID,
    TO_ACCOUNT_ID,
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
    return next(case for case in FINANCE_CASES if case.operation_id == operation_id)


def _view(
    case: ReadCase,
    *,
    omit: frozenset[str] = frozenset(),
    **changes: object,
) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "period_from_yyyy_mm_dd": PERIOD_FROM,
        "period_to_yyyy_mm_dd": PERIOD_TO,
        "finance_incoming_service_document_id": INCOMING_DOCUMENT_ID,
        "finance_outgoing_service_document_id": OUTGOING_DOCUMENT_ID,
        "inventory_disassemble_document_id": INVENTORY_DOCUMENT_ID,
        "finance_incoming_service_revenue_account_id": INCOMING_ACCOUNT_ID,
        "finance_outgoing_service_revenue_account_id": OUTGOING_ACCOUNT_ID,
        "finance_document_transaction_from_account_id": FROM_ACCOUNT_ID,
        "finance_document_transaction_to_account_id": TO_ACCOUNT_ID,
    }
    values.update(changes)
    return ContextView(
        {
            key: values[key]
            for key in case.requires
            if key in values and key not in omit
        }
    )


def _list_item(
    family: str,
    *,
    document_id: object,
    revenue_account: object,
    deleted: object,
) -> object:
    return _model(
        f"{family}_service_list_item",
        f"{family.title()}ServiceListItem",
        deleted=deleted,
        document_id=document_id,
        revenue_account=revenue_account,
    )


def _minimal_response(operation_id: str, case: ReadCase) -> object:
    if operation_id in {
        "list_finance_incoming_services",
        "list_finance_outgoing_services",
        "list_finance_document_transactions",
    }:
        return []
    if operation_id == "list_finance_account_transactions":
        return _model(
            "account_transactions_response",
            "AccountTransactionsResponse",
            items=[],
        )
    if operation_id == "get_finance_incoming_service":
        values = case.build_values(_view(case))
        assert isinstance(values, Mapping)
        return _model(
            "incoming_service_get_response",
            "IncomingServiceGetResponse",
            document_id=values["document_id"],
        )
    values = case.build_values(_view(case))
    assert isinstance(values, Mapping)
    return _model(
        "outgoing_service_get_response",
        "OutgoingServiceGetResponse",
        document_id=values["document_id"],
    )


def _request_json(case: ReadCase, view: ContextView | None = None) -> object:
    request = build_generated_request(
        case.binding,
        case.build_values(_view(case) if view is None else view),
    )
    assert request is not None
    return _jsonable(request.to_dict())  # type: ignore[attr-defined]


def test_finance_registry_is_exact() -> None:
    assert type(FINANCE_CASES) is tuple
    assert {case.operation_id for case in FINANCE_CASES} == FINANCE_IDS
    assert len(FINANCE_CASES) == len(FINANCE_IDS)


def test_target_orders_and_transaction_contracts_are_exact() -> None:
    assert DOCUMENT_TARGET_KEYS == EXPECTED_DOCUMENT_KEYS
    assert DOCUMENT_PROVIDER_OPERATION_IDS == EXPECTED_PROVIDER_OPERATIONS
    assert ACCOUNT_TARGET_KEYS == EXPECTED_ACCOUNT_KEYS

    document = _case("list_finance_document_transactions")
    assert document.depends_on == EXPECTED_PROVIDER_OPERATIONS
    assert document.requires == ("organization_id", *EXPECTED_DOCUMENT_KEYS)
    assert document.provides == (
        "finance_document_transaction_from_account_id",
        "finance_document_transaction_to_account_id",
    )
    assert document.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.DOCUMENT}
    )

    account = _case("list_finance_account_transactions")
    assert account.depends_on == (
        *EXPECTED_PROVIDER_OPERATIONS,
        "list_finance_document_transactions",
    )
    assert account.requires == (
        "organization_id",
        "period_from_yyyy_mm_dd",
        "period_to_yyyy_mm_dd",
        *EXPECTED_ACCOUNT_KEYS,
    )
    assert account.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.ACCOUNT}
    )


def test_list_and_get_dependencies_and_provider_keys_are_exact() -> None:
    expected = {
        "incoming": (
            "list_finance_incoming_services",
            "get_finance_incoming_service",
            "finance_incoming_service_document_id",
            "finance_incoming_service_revenue_account_id",
        ),
        "outgoing": (
            "list_finance_outgoing_services",
            "get_finance_outgoing_service",
            "finance_outgoing_service_document_id",
            "finance_outgoing_service_revenue_account_id",
        ),
    }
    for list_id, get_id, document_key, account_key in expected.values():
        list_case = _case(list_id)
        assert list_case.depends_on == ("get_organizations",)
        assert list_case.requires == (
            "organization_id",
            "period_from_yyyy_mm_dd",
            "period_to_yyyy_mm_dd",
        )
        assert list_case.provides == (document_key, account_key)

        get_case = _case(get_id)
        assert get_case.depends_on == (list_id,)
        assert get_case.requires == ("organization_id", document_key)
        assert get_case.provides == ()
        assert get_case.allowed_no_target_codes == frozenset(
            {NoLiveTargetCode.DOCUMENT}
        )


@pytest.mark.parametrize("operation_id", sorted(FINANCE_IDS))
def test_bindings_resolve_and_validators_fail_with_fixed_redacted_errors(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"
    case.validate_response(_minimal_response(operation_id, case), _view(case))

    private_marker = "private-finance-payload-marker"
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"private": private_marker}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert private_marker not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_period_list_requests_use_strict_string_guids_and_from_alias() -> None:
    for operation_id in (
        "list_finance_incoming_services",
        "list_finance_outgoing_services",
    ):
        case = _case(operation_id)
        assert _request_json(case) == {
            "from": PERIOD_FROM,
            "organizationId": str(ORGANIZATION_ID),
            "to": PERIOD_TO,
        }


@pytest.mark.parametrize("family", ["incoming", "outgoing"])
def test_service_list_selects_one_active_item_and_keeps_fields_together(
    family: str,
) -> None:
    case = _case(f"list_finance_{family}_services")
    expected_document = (
        INCOMING_DOCUMENT_ID if family == "incoming" else OUTGOING_DOCUMENT_ID
    )
    expected_account = (
        INCOMING_ACCOUNT_ID if family == "incoming" else OUTGOING_ACCOUNT_ID
    )
    prefix = f"finance_{family}_service"
    response = [
        _list_item(
            family,
            document_id="not-a-guid",
            revenue_account=FROM_ACCOUNT_ID,
            deleted=False,
        ),
        _list_item(
            family,
            document_id=INVENTORY_DOCUMENT_ID,
            revenue_account=TO_ACCOUNT_ID,
            deleted=None,
        ),
        _list_item(
            family,
            document_id=INVENTORY_DOCUMENT_ID,
            revenue_account=TO_ACCOUNT_ID,
            deleted=True,
        ),
        _list_item(
            family,
            document_id=expected_document,
            revenue_account=expected_account,
            deleted=False,
        ),
    ]

    case.validate_response(response, _view(case))
    assert case.extract(response, _view(case)) == {
        f"{prefix}_document_id": expected_document,
        f"{prefix}_revenue_account_id": expected_account,
    }
    assert case.extract([], _view(case)) == {}


def test_service_list_does_not_mix_account_from_another_item() -> None:
    case = _case("list_finance_incoming_services")
    response = [
        _list_item(
            "incoming",
            document_id=INCOMING_DOCUMENT_ID,
            revenue_account=None,
            deleted=False,
        ),
        _list_item(
            "incoming",
            document_id=OUTGOING_DOCUMENT_ID,
            revenue_account=OUTGOING_ACCOUNT_ID,
            deleted=False,
        ),
    ]
    assert case.extract(response, _view(case)) == {
        "finance_incoming_service_document_id": INCOMING_DOCUMENT_ID
    }


@pytest.mark.parametrize("family", ["incoming", "outgoing"])
def test_get_request_and_response_are_linked_to_list_document(family: str) -> None:
    case = _case(f"get_finance_{family}_service")
    document_id = (
        INCOMING_DOCUMENT_ID if family == "incoming" else OUTGOING_DOCUMENT_ID
    )
    assert _request_json(case) == {
        "documentId": document_id,
        "organizationId": str(ORGANIZATION_ID),
    }

    response = _model(
        f"{family}_service_get_response",
        f"{family.title()}ServiceGetResponse",
        document_id=document_id,
    )
    case.validate_response(response, _view(case))
    mismatched = _model(
        f"{family}_service_get_response",
        f"{family.title()}ServiceGetResponse",
        document_id=INVENTORY_DOCUMENT_ID,
    )
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(mismatched, _view(case))

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(
            _view(
                case,
                omit=frozenset({f"finance_{family}_service_document_id"}),
            )
        )
    assert missing.value.code is NoLiveTargetCode.DOCUMENT


def test_document_transaction_uses_fixed_document_priority_without_dates() -> None:
    case = _case("list_finance_document_transactions")
    assert _request_json(case) == {
        "documentId": INCOMING_DOCUMENT_ID,
        "organizationId": str(ORGANIZATION_ID),
    }

    inventory_only = _view(
        case,
        omit=frozenset(
            {
                "finance_incoming_service_document_id",
                "finance_outgoing_service_document_id",
            }
        ),
    )
    assert _request_json(case, inventory_only)["documentId"] == (  # type: ignore[index]
        INVENTORY_DOCUMENT_ID
    )

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(
            _view(case, omit=frozenset(EXPECTED_DOCUMENT_KEYS))
        )
    assert missing.value.code is NoLiveTargetCode.DOCUMENT


def test_document_transaction_validates_linkage_and_extracts_side_accounts() -> None:
    case = _case("list_finance_document_transactions")
    side_from = _model(
        "transaction_side",
        "TransactionSide",
        account=FROM_ACCOUNT_ID,
    )
    side_to = _model(
        "transaction_side",
        "TransactionSide",
        account=TO_ACCOUNT_ID,
    )
    response = [
        _model(
            "document_transaction_item",
            "DocumentTransactionItem",
            document_id=INCOMING_DOCUMENT_ID,
            var_from=side_from,
            to=side_to,
        )
    ]
    case.validate_response(response, _view(case))
    assert case.extract(response, _view(case)) == {
        "finance_document_transaction_from_account_id": FROM_ACCOUNT_ID,
        "finance_document_transaction_to_account_id": TO_ACCOUNT_ID,
    }

    mismatched = [
        _model(
            "document_transaction_item",
            "DocumentTransactionItem",
            document_id=OUTGOING_DOCUMENT_ID,
        )
    ]
    with pytest.raises(ReadAssertionFailure):
        case.validate_response(mismatched, _view(case))


def test_account_transaction_uses_fixed_priority_and_bounded_period() -> None:
    case = _case("list_finance_account_transactions")
    assert _request_json(case) == {
        "accountId": INCOMING_ACCOUNT_ID,
        "from": PERIOD_FROM,
        "organizationId": str(ORGANIZATION_ID),
        "to": PERIOD_TO,
    }

    outgoing_only = _view(
        case,
        omit=frozenset({"finance_incoming_service_revenue_account_id"}),
    )
    assert _request_json(case, outgoing_only)["accountId"] == (  # type: ignore[index]
        OUTGOING_ACCOUNT_ID
    )

    side_only = _view(
        case,
        omit=frozenset(EXPECTED_ACCOUNT_KEYS[:-2]),
    )
    assert _request_json(case, side_only)["accountId"] == FROM_ACCOUNT_ID  # type: ignore[index]

    with pytest.raises(NoLiveTarget) as missing:
        case.build_values(_view(case, omit=frozenset(EXPECTED_ACCOUNT_KEYS)))
    assert missing.value.code is NoLiveTargetCode.ACCOUNT


def test_finance_targets_remain_hidden_in_context_renderings() -> None:
    context = ReadContext.seed({"organization_id": ORGANIZATION_ID})
    context.apply(
        _case("list_finance_incoming_services"),
        {
            "finance_incoming_service_document_id": INCOMING_DOCUMENT_ID,
            "finance_incoming_service_revenue_account_id": INCOMING_ACCOUNT_ID,
        },
    )
    context.apply(
        _case("list_finance_document_transactions"),
        {
            "finance_document_transaction_from_account_id": FROM_ACCOUNT_ID,
            "finance_document_transaction_to_account_id": TO_ACCOUNT_ID,
        },
    )
    rendered = repr(
        (
            context,
            context.view(
                (
                    "finance_incoming_service_document_id",
                    "finance_document_transaction_from_account_id",
                )
            ),
            FINANCE_CASES,
        )
    )
    for marker in PRIVATE_MARKERS:
        assert marker not in rendered
