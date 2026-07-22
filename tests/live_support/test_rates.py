from __future__ import annotations

import copy
import math
from dataclasses import FrozenInstanceError, is_dataclass
from pathlib import Path
from typing import Any

import pytest
import yaml

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.rates import (
    RateCatalog,
    RateLimit,
    RatePolicy,
    ServerLimit,
)
from tools.openapi_pipeline.live.rates import (
    TestBudget as RateTestBudget,
)
from tools.openapi_pipeline.live.safety import OperationSafetyCatalog

_REVIEWED_GLOBAL_TEST_BUDGET = {
    "min_interval_seconds": 30,
    "source": "user-approved-global-cadence-2026-07-22",
    "verified": True,
}

RATE_V2: dict[str, Any] = {
    "version": 2,
    "defaults": {
        "utilization": 0.20,
        "global_min_interval_seconds": 30,
        "max_calls_per_operation_per_run": 1,
    },
    "operations": {
        "get_nomenclature": {
            "test_budget": {
                "min_interval_seconds": 30,
                "source": "user-approved-global-read-cadence-2026-07-21",
                "verified": True,
            },
            "server_limit": None,
        },
        "get_external_menus": {
            "test_budget": {
                "min_interval_seconds": 30,
                "source": "user-approved-global-read-cadence-2026-07-21",
                "verified": True,
            },
            "server_limit": {
                "calls": 1,
                "per_seconds": 1800,
                "source": "existing-manager-configuration",
                "verified": True,
            },
        },
    },
}

_READ_ENDPOINTS = {
    "calculate_combo_price": ("POST", "/api/1/combo/calculate"),
    "calculate_inventory_cost_prices": ("POST", "/api/inventory/v1/costings/calculate"),
    "calculate_loyalty_checkin": ("POST", "/api/1/loyalty/iiko/calculate"),
    "check_products_in_stop_list": ("POST", "/api/1/stop_lists/check"),
    "check_sms_sending_possibility": (
        "POST",
        "/api/1/loyalty/iiko/check_sms_sending_possibility",
    ),
    "check_sms_status": ("POST", "/api/1/loyalty/iiko/check_sms_status"),
    "check_terminal_groups_availability": ("POST", "/api/1/terminal_groups/is_alive"),
    "get_active_courier_locations": ("POST", "/api/1/employees/couriers/active_location"),
    "get_active_courier_locations_by_terminal": (
        "POST",
        "/api/1/employees/couriers/active_location/by_terminal",
    ),
    "get_allowed_delivery_restrictions": ("POST", "/api/1/delivery_restrictions/allowed"),
    "get_cancel_causes": ("POST", "/api/1/cancel_causes"),
    "get_cities": ("POST", "/api/1/cities"),
    "get_combos_info": ("POST", "/api/1/combo"),
    "get_command_status": ("POST", "/api/1/commands/status"),
    "get_coupon_info": ("POST", "/api/1/loyalty/iiko/coupons/info"),
    "get_coupon_series": ("POST", "/api/1/loyalty/iiko/coupons/series"),
    "get_courier_location_history": (
        "POST",
        "/api/1/employees/couriers/locations/by_time_offset",
    ),
    "get_couriers": ("POST", "/api/1/employees/couriers"),
    "get_couriers_by_role": ("POST", "/api/1/employees/couriers/by_role"),
    "get_customer_categories": ("POST", "/api/1/loyalty/iiko/customer_category"),
    "get_customer_info": ("POST", "/api/1/loyalty/iiko/customer/info"),
    "get_customer_transactions_by_date": (
        "POST",
        "/api/1/loyalty/iiko/customer/transactions/by_date",
    ),
    "get_customer_transactions_by_revision": (
        "POST",
        "/api/1/loyalty/iiko/customer/transactions/by_revision",
    ),
    "get_deliveries_by_delivery_date_and_phone": (
        "POST",
        "/api/1/deliveries/by_delivery_date_and_phone",
    ),
    "get_deliveries_by_delivery_date_and_status": (
        "POST",
        "/api/1/deliveries/by_delivery_date_and_status",
    ),
    "get_deliveries_by_id": ("POST", "/api/1/deliveries/by_id"),
    "get_deliveries_by_revision": ("POST", "/api/1/deliveries/by_revision"),
    "get_delivery_draft_by_id": ("POST", "/api/1/deliveries/drafts/by_id"),
    "get_delivery_drafts_by_filter": ("POST", "/api/1/deliveries/drafts/by_filter"),
    "get_delivery_history_by_delivery_date_and_phone": (
        "POST",
        "/api/1/deliveries/history/by_delivery_date_and_phone",
    ),
    "get_delivery_order_types": ("POST", "/api/1/deliveries/order_types"),
    "get_delivery_restrictions": ("POST", "/api/1/delivery_restrictions"),
    "get_discounts": ("POST", "/api/1/discounts"),
    "get_employee_info": ("POST", "/api/1/employees/info"),
    "get_external_menu_by_id": ("POST", "/api/2/menu/by_id"),
    "get_external_menus": ("POST", "/api/2/menu"),
    "get_finance_incoming_service": ("POST", "/api/finance/v1/incoming_service/get"),
    "get_finance_outgoing_service": ("POST", "/api/finance/v1/outgoing_service/get"),
    "get_inventory_counteragents": ("POST", "/api/inventory/v1/counteragents"),
    "get_inventory_disassemble_document": (
        "POST",
        "/api/inventory/v1/disassemble_document/get",
    ),
    "get_inventory_incoming_invoice": ("POST", "/api/inventory/v1/incoming_invoice/get"),
    "get_inventory_incoming_returned_invoice": (
        "POST",
        "/api/inventory/v1/incoming_returned_invoice/get",
    ),
    "get_inventory_internal_transfer": (
        "POST",
        "/api/inventory/v1/internal_transfer/get",
    ),
    "get_inventory_outgoing_invoice": ("POST", "/api/inventory/v1/outgoing_invoice/get"),
    "get_inventory_production_document": (
        "POST",
        "/api/inventory/v1/production_document/get",
    ),
    "get_inventory_returned_invoice": ("POST", "/api/inventory/v1/returned_invoice/get"),
    "get_inventory_sales_document": ("POST", "/api/inventory/v1/sales_document/get"),
    "get_inventory_transformation_document": (
        "POST",
        "/api/inventory/v1/transformation_document/get",
    ),
    "get_inventory_writeoff_document": (
        "POST",
        "/api/inventory/v1/writeoff_document/get",
    ),
    "get_loyalty_counters": ("POST", "/api/1/loyalty/iiko/get_counters"),
    "get_loyalty_manual_conditions": ("POST", "/api/1/loyalty/iiko/manual_condition"),
    "get_loyalty_programs": ("POST", "/api/1/loyalty/iiko/program"),
    "get_marketing_sources": ("POST", "/api/1/marketing_sources"),
    "get_nomenclature": ("POST", "/api/1/nomenclature"),
    "get_non_activated_coupons_by_series": (
        "POST",
        "/api/1/loyalty/iiko/coupons/by_series",
    ),
    "get_organization_settings": ("POST", "/api/1/organizations/settings"),
    "get_organizations": ("POST", "/api/1/organizations"),
    "get_payment_types": ("POST", "/api/1/payment_types"),
    "get_personal_session_info": ("POST", "/api/1/employees/shift/is_open"),
    "get_regions": ("POST", "/api/1/regions"),
    "get_removal_types": ("POST", "/api/1/removal_types"),
    "get_reserve_available_organizations": (
        "POST",
        "/api/1/reserve/available_organizations",
    ),
    "get_reserve_restaurant_sections": (
        "POST",
        "/api/1/reserve/available_restaurant_sections",
    ),
    "get_reserve_statuses_by_id": ("POST", "/api/1/reserve/status_by_id"),
    "get_reserve_terminal_groups": (
        "POST",
        "/api/1/reserve/available_terminal_groups",
    ),
    "get_restaurant_sections_workload": (
        "POST",
        "/api/1/reserve/restaurant_sections_workload",
    ),
    "get_stop_lists": ("POST", "/api/1/stop_lists"),
    "get_streets_by_city": ("POST", "/api/1/streets/by_city"),
    "get_streets_by_id": ("POST", "/api/1/streets/by_id"),
    "get_table_orders_by_id": ("POST", "/api/1/order/by_id"),
    "get_table_orders_by_table": ("POST", "/api/1/order/by_table"),
    "get_terminal_groups": ("POST", "/api/1/terminal_groups"),
    "get_terminal_groups_of_employee": ("POST", "/api/1/employees/shifts/by_courier"),
    "get_tips_types": ("POST", "/api/1/tips_types"),
    "get_webhook_settings": ("POST", "/api/1/webhooks/settings"),
    "list_finance_account_transactions": (
        "POST",
        "/api/finance/v1/account_transactions/list",
    ),
    "list_finance_document_transactions": (
        "POST",
        "/api/finance/v1/document_transactions/list",
    ),
    "list_finance_incoming_services": ("POST", "/api/finance/v1/incoming_service/list"),
    "list_finance_outgoing_services": ("POST", "/api/finance/v1/outgoing_service/list"),
    "list_inventory_disassemble_documents": (
        "POST",
        "/api/inventory/v1/disassemble_document/list",
    ),
    "list_inventory_incoming_invoices": (
        "POST",
        "/api/inventory/v1/incoming_invoice/list",
    ),
    "list_inventory_incoming_returned_invoices": (
        "POST",
        "/api/inventory/v1/incoming_returned_invoice/list",
    ),
    "list_inventory_internal_transfers": (
        "POST",
        "/api/inventory/v1/internal_transfer/list",
    ),
    "list_inventory_outgoing_invoices": (
        "POST",
        "/api/inventory/v1/outgoing_invoice/list",
    ),
    "list_inventory_production_documents": (
        "POST",
        "/api/inventory/v1/production_document/list",
    ),
    "list_inventory_returned_invoices": (
        "POST",
        "/api/inventory/v1/returned_invoice/list",
    ),
    "list_inventory_sales_documents": ("POST", "/api/inventory/v1/sales_document/list"),
    "list_inventory_transformation_documents": (
        "POST",
        "/api/inventory/v1/transformation_document/list",
    ),
    "list_inventory_writeoff_documents": (
        "POST",
        "/api/inventory/v1/writeoff_document/list",
    ),
    "list_organizations": ("GET", "/api/1/organizations"),
    "search_deliveries": (
        "POST",
        "/api/1/deliveries/by_delivery_date_and_source_key_and_filter",
    ),
}


def _catalog_data() -> dict[str, Any]:
    return copy.deepcopy(RATE_V2)


def _set_nested(data: dict[str, Any], path: tuple[str, ...], value: object) -> None:
    target = data
    for segment in path[:-1]:
        target = target[segment]
    target[path[-1]] = value


def test_safe_interval_uses_twenty_percent_and_global_floor() -> None:
    policy = RatePolicy(utilization=0.20, global_min_interval_seconds=30)
    assert policy.safe_interval(RateLimit(calls=1, per_seconds=60)) == 300
    assert policy.safe_interval(RateLimit(calls=100, per_seconds=60)) == 30


def test_version_two_catalog_separates_test_budget_from_optional_server_limit() -> None:
    data = _catalog_data()
    original = copy.deepcopy(data)

    catalog = RateCatalog.from_mapping(data)

    assert catalog.operation_budget("get_nomenclature").safe_interval_seconds == 30
    assert catalog.operation_budget("get_external_menus").safe_interval_seconds == 9000
    assert catalog.operation_ids == ("get_external_menus", "get_nomenclature")
    assert data == original


def test_version_two_budget_types_are_frozen_slotted_data() -> None:
    assert is_dataclass(RateTestBudget)
    assert is_dataclass(ServerLimit)

    test_budget = RateTestBudget(30, "reviewed", True)
    server_limit = ServerLimit(1, 60, "documented", True)
    assert hasattr(RateTestBudget, "__slots__")
    assert hasattr(ServerLimit, "__slots__")
    with pytest.raises(FrozenInstanceError):
        test_budget.verified = False  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        server_limit.verified = False  # type: ignore[misc]


def test_catalog_rejects_version_one() -> None:
    data = _catalog_data()
    data["version"] = 1

    with pytest.raises(SafetyError, match="version.*integer 2"):
        RateCatalog.from_mapping(data)


def test_catalog_rejects_missing_or_non_object_test_budget() -> None:
    data = _catalog_data()
    del data["operations"]["get_nomenclature"]["test_budget"]
    with pytest.raises(SafetyError, match="test_budget"):
        RateCatalog.from_mapping(data)

    data = _catalog_data()
    data["operations"]["get_nomenclature"]["test_budget"] = None
    with pytest.raises(SafetyError, match="test_budget.*object"):
        RateCatalog.from_mapping(data)


def test_operation_budget_rejects_unverified_test_budget() -> None:
    data = _catalog_data()
    data["operations"]["get_nomenclature"]["test_budget"]["verified"] = False

    catalog = RateCatalog.from_mapping(data)

    with pytest.raises(SafetyError, match="test budget.*not verified"):
        catalog.operation_budget("get_nomenclature")


def test_null_server_limit_uses_only_the_reviewed_test_cadence() -> None:
    catalog = RateCatalog.from_mapping(_catalog_data())

    assert catalog.operation_budget("get_nomenclature").safe_interval_seconds == 30


def test_operation_budget_rejects_present_unverified_server_limit() -> None:
    data = _catalog_data()
    data["operations"]["get_external_menus"]["server_limit"]["verified"] = False

    catalog = RateCatalog.from_mapping(data)

    with pytest.raises(SafetyError, match="server limit.*not verified"):
        catalog.operation_budget("get_external_menus")


@pytest.mark.parametrize("value", [False, "unknown", [], 1])
def test_catalog_rejects_non_object_non_null_server_limit(value: object) -> None:
    data = _catalog_data()
    data["operations"]["get_nomenclature"]["server_limit"] = value

    with pytest.raises(SafetyError, match="server_limit.*object or null"):
        RateCatalog.from_mapping(data)


def test_catalog_rejects_unknown_operation_id_when_budget_is_requested() -> None:
    catalog = RateCatalog.from_mapping(_catalog_data())

    with pytest.raises(SafetyError, match="Unknown live operation"):
        catalog.operation_budget("missing")


@pytest.mark.parametrize(
    ("path", "value", "message"),
    [
        (("version",), True, "version"),
        (("defaults", "utilization"), True, "utilization"),
        (("defaults", "utilization"), 0.0, "utilization"),
        (("defaults", "utilization"), 0.200001, "utilization"),
        (("defaults", "utilization"), math.inf, "utilization"),
        (("defaults", "global_min_interval_seconds"), 29.99, "global"),
        (("defaults", "global_min_interval_seconds"), True, "global"),
        (("defaults", "max_calls_per_operation_per_run"), 2, "exactly 1"),
        (("defaults", "max_calls_per_operation_per_run"), True, "exactly 1"),
        (
            (
                "operations",
                "get_nomenclature",
                "test_budget",
                "min_interval_seconds",
            ),
            29.99,
            "test budget.*at least 30",
        ),
        (
            (
                "operations",
                "get_nomenclature",
                "test_budget",
                "min_interval_seconds",
            ),
            True,
            "min_interval_seconds",
        ),
        (
            (
                "operations",
                "get_nomenclature",
                "test_budget",
                "min_interval_seconds",
            ),
            math.nan,
            "min_interval_seconds",
        ),
        (
            ("operations", "get_nomenclature", "test_budget", "verified"),
            1,
            "verified",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "calls"),
            True,
            "calls",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "calls"),
            0,
            "calls",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "per_seconds"),
            math.inf,
            "per_seconds",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "per_seconds"),
            -1,
            "per_seconds",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "verified"),
            1,
            "verified",
        ),
    ],
)
def test_catalog_rejects_unsafe_scalar_types_and_values(
    path: tuple[str, ...], value: object, message: str
) -> None:
    data = _catalog_data()
    _set_nested(data, path, value)

    with pytest.raises(SafetyError, match=message):
        RateCatalog.from_mapping(data)


@pytest.mark.parametrize(
    "path",
    [
        (),
        ("defaults",),
        ("operations", "get_nomenclature"),
        ("operations", "get_nomenclature", "test_budget"),
        ("operations", "get_external_menus", "server_limit"),
    ],
)
def test_catalog_rejects_unknown_fields(path: tuple[str, ...]) -> None:
    data = _catalog_data()
    target = data
    for segment in path:
        target = target[segment]
    target["extra"] = True

    with pytest.raises(SafetyError, match="keys must be exactly"):
        RateCatalog.from_mapping(data)


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (
            ("operations", "get_nomenclature", "test_budget", "source"),
            " leading",
        ),
        (
            ("operations", "get_external_menus", "server_limit", "source"),
            "trailing ",
        ),
    ],
)
def test_catalog_uses_the_shared_bounded_safe_source_validator(
    path: tuple[str, ...], value: object
) -> None:
    data = _catalog_data()
    _set_nested(data, path, value)

    with pytest.raises(SafetyError, match="source.*trimmed printable"):
        RateCatalog.from_mapping(data)


@pytest.mark.parametrize("root", [None, [], "catalog", 1, True])
def test_catalog_requires_object_root(root: object) -> None:
    with pytest.raises(SafetyError, match="root must be an object"):
        RateCatalog.from_mapping(root)


def test_catalog_load_rejects_duplicate_yaml_keys(tmp_path: Path) -> None:
    path = tmp_path / "rates.yaml"
    path.write_text(
        "version: 2\nversion: 2\ndefaults: {}\noperations: {}\n",
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="duplicate key"):
        RateCatalog.load(path)


def test_catalog_load_rejects_yaml_anchors_and_aliases(tmp_path: Path) -> None:
    path = tmp_path / "rates.yaml"
    path.write_text(
        "version: 2\n"
        "defaults: {}\n"
        "operations:\n"
        "  first: &entry {}\n"
        "  second: *entry\n",
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="anchors or aliases"):
        RateCatalog.load(path)


def _expected_committed_rate_operations() -> dict[str, Any]:
    return {
        operation_id: {
            "test_budget": copy.deepcopy(_REVIEWED_GLOBAL_TEST_BUDGET),
            "server_limit": None,
        }
        for operation_id in (
            "authenticate",
            *_READ_ENDPOINTS,
            "add_products_to_stop_list",
            "remove_products_from_stop_list",
        )
    }


def test_committed_rate_catalog_is_exact_and_budgets_every_guarded_operation() -> None:
    path = Path("contracts/rate-limits.yaml")
    packaged_path = Path("src/iikocloud_client/_contracts/rate-limits.yaml")
    assert path.read_bytes() == packaged_path.read_bytes()
    expected_operations = _expected_committed_rate_operations()
    assert len(expected_operations) == 94
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert value == {
        "version": 2,
        "defaults": {
            "utilization": 0.20,
            "global_min_interval_seconds": 30,
            "max_calls_per_operation_per_run": 1,
        },
        "operations": expected_operations,
    }

    catalog = RateCatalog.load(path)
    assert catalog.operation_ids == tuple(sorted(expected_operations))
    for operation_id in expected_operations:
        assert catalog.operation_budget(operation_id).safe_interval_seconds == 30.0


def test_committed_live_operation_contract_is_the_exact_reviewed_read_allowlist() -> None:
    value = yaml.safe_load(Path("contracts/live-operations.yaml").read_text(encoding="utf-8"))
    expected_operations = {
        "authenticate": {
            "kind": "auth",
            "cleanup": None,
            "method": "POST",
            "path": "/api/1/access_token",
        },
        **{
            operation_id: {
                "kind": "read",
                "cleanup": None,
                "method": method,
                "path": path,
            }
            for operation_id, (method, path) in _READ_ENDPOINTS.items()
        },
        "add_products_to_stop_list": {
            "kind": "compensating",
            "cleanup": "remove_products_from_stop_list",
            "method": "POST",
            "path": "/api/1/stop_lists/add",
        },
        "remove_products_from_stop_list": {
            "kind": "cleanup",
            "cleanup": None,
            "method": "POST",
            "path": "/api/1/stop_lists/remove",
        },
    }
    assert value == {"version": 1, "operations": expected_operations}
    assert len(expected_operations) == 94
    assert "authenticate_v2" not in expected_operations

    safety = OperationSafetyCatalog.load(Path("contracts/operation-safety.yaml"))
    assert safety.automatic_read_ids == frozenset(_READ_ENDPOINTS)
    rate_catalog = RateCatalog.load(Path("contracts/rate-limits.yaml"))
    assert rate_catalog.operation_ids == tuple(sorted(expected_operations))


@pytest.mark.parametrize(
    "limit",
    [
        RateLimit(calls=True, per_seconds=1),
        RateLimit(calls=1, per_seconds=True),
        RateLimit(calls=0, per_seconds=1),
        RateLimit(calls=1, per_seconds=math.inf),
    ],
)
def test_rate_limit_rejects_bool_nonpositive_and_nonfinite(limit: RateLimit) -> None:
    policy = RatePolicy(utilization=0.2, global_min_interval_seconds=30)
    with pytest.raises(SafetyError, match="server limit"):
        policy.safe_interval(limit)
