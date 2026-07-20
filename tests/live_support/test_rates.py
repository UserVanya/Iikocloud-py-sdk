from __future__ import annotations

import copy
import math
from pathlib import Path

import pytest
import yaml

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.rates import RateCatalog, RateLimit, RatePolicy


def test_safe_interval_uses_twenty_percent_and_global_floor() -> None:
    policy = RatePolicy(utilization=0.20, global_min_interval_seconds=30)
    assert policy.safe_interval(RateLimit(calls=1, per_seconds=60)) == 300
    assert policy.safe_interval(RateLimit(calls=100, per_seconds=60)) == 30


def test_unverified_operation_is_disabled() -> None:
    policy = RatePolicy(utilization=0.20, global_min_interval_seconds=30)
    with pytest.raises(SafetyError, match="not verified"):
        policy.operation_budget(
            "unsafe_operation",
            {"verified": False, "server_limit": {"calls": 1, "per_seconds": 60}},
        )


def _catalog_data(*, verified: bool = True) -> dict[str, object]:
    return {
        "version": 1,
        "defaults": {
            "utilization": 0.20,
            "global_min_interval_seconds": 30,
            "max_calls_per_operation_per_run": 1,
        },
        "operations": {
            "get_organizations": {
                "server_limit": {"calls": 1, "per_seconds": 60},
                "source": "test-fixture",
                "verified": verified,
            }
        },
    }


def test_catalog_returns_only_explicit_verified_budget_without_mutation() -> None:
    data = _catalog_data()
    original = copy.deepcopy(data)
    catalog = RateCatalog.from_mapping(data)

    budget = catalog.operation_budget("get_organizations")

    assert budget.safe_interval_seconds == 300
    assert budget.max_calls_per_run == 1
    assert data == original
    with pytest.raises(SafetyError, match="Unknown live operation"):
        catalog.operation_budget("missing")


def test_catalog_rejects_unverified_operation() -> None:
    catalog = RateCatalog.from_mapping(_catalog_data(verified=False))
    with pytest.raises(SafetyError, match="not verified"):
        catalog.operation_budget("get_organizations")


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
        (("operations", "get_organizations", "server_limit", "calls"), True, "calls"),
        (("operations", "get_organizations", "server_limit", "calls"), 0, "calls"),
        (
            ("operations", "get_organizations", "server_limit", "per_seconds"),
            math.nan,
            "per_seconds",
        ),
        (
            ("operations", "get_organizations", "server_limit", "per_seconds"),
            -1,
            "per_seconds",
        ),
        (("operations", "get_organizations", "verified"), 1, "verified"),
    ],
)
def test_catalog_rejects_unsafe_scalar_types_and_values(
    path: tuple[str, ...], value: object, message: str
) -> None:
    data = _catalog_data()
    target: dict[str, object] = data
    for segment in path[:-1]:
        child = target[segment]
        assert isinstance(child, dict)
        target = child
    target[path[-1]] = value

    with pytest.raises(SafetyError, match=message):
        RateCatalog.from_mapping(data)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda data: data.update(extra=True),
        lambda data: data["defaults"].update(extra=True),
        lambda data: data["operations"]["get_organizations"].update(extra=True),
        lambda data: data["operations"]["get_organizations"]["server_limit"].update(extra=True),
    ],
)
def test_catalog_rejects_unknown_fields(mutate) -> None:
    data = _catalog_data()
    mutate(data)
    with pytest.raises(SafetyError, match="exactly"):
        RateCatalog.from_mapping(data)


@pytest.mark.parametrize("root", [None, [], "catalog", 1, True])
def test_catalog_requires_object_root(root: object) -> None:
    with pytest.raises(SafetyError, match="root must be an object"):
        RateCatalog.from_mapping(root)


def test_catalog_load_rejects_duplicate_yaml_keys(tmp_path: Path) -> None:
    path = tmp_path / "rates.yaml"
    path.write_text(
        "version: 1\nversion: 1\ndefaults: {}\noperations: {}\n",
        encoding="utf-8",
    )
    with pytest.raises(SafetyError, match="duplicate key"):
        RateCatalog.load(path)


def test_committed_rate_catalog_is_exact_and_disabled_by_default() -> None:
    path = Path("contracts/rate-limits.yaml")
    packaged_path = Path("src/iikocloud_client/_contracts/rate-limits.yaml")
    assert path.read_bytes() == packaged_path.read_bytes()
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    expected_operations = {
        "authenticate": {
            "server_limit": {"calls": 1, "per_seconds": 5},
            "source": "existing-manager-configuration",
            "verified": False,
        },
        "get_organizations": {
            "server_limit": {"calls": 1, "per_seconds": 10},
            "source": "existing-manager-configuration",
            "verified": False,
        },
        "get_external_menus": {
            "server_limit": {"calls": 1, "per_seconds": 1800},
            "source": "existing-manager-configuration",
            "verified": False,
        },
        "get_external_menu_by_id": {
            "server_limit": {"calls": 5, "per_seconds": 60},
            "source": "existing-manager-configuration",
            "verified": False,
        },
        "get_stop_lists": {
            "server_limit": {"calls": 10, "per_seconds": 60},
            "source": "existing-manager-configuration",
            "verified": False,
        },
        "add_products_to_stop_list": {
            "server_limit": {"calls": 1, "per_seconds": 60},
            "source": "conservative-unverified",
            "verified": False,
        },
        "remove_products_from_stop_list": {
            "server_limit": {"calls": 1, "per_seconds": 60},
            "source": "conservative-unverified",
            "verified": False,
        },
    }
    assert value == {
        "version": 1,
        "defaults": {
            "utilization": 0.20,
            "global_min_interval_seconds": 30,
            "max_calls_per_operation_per_run": 1,
        },
        "operations": expected_operations,
    }

    catalog = RateCatalog.load(path)
    for operation_id in expected_operations:
        with pytest.raises(SafetyError, match="not verified"):
            catalog.operation_budget(operation_id)


def test_committed_live_operation_contract_is_exact() -> None:
    value = yaml.safe_load(Path("contracts/live-operations.yaml").read_text(encoding="utf-8"))
    assert value == {
        "version": 1,
        "operations": {
            "authenticate": {
                "kind": "auth",
                "cleanup": None,
                "method": "POST",
                "path": "/api/1/access_token",
            },
            "get_organizations": {
                "kind": "read",
                "cleanup": None,
                "method": "POST",
                "path": "/api/1/organizations",
            },
            "get_external_menus": {
                "kind": "read",
                "cleanup": None,
                "method": "POST",
                "path": "/api/2/menu",
            },
            "get_external_menu_by_id": {
                "kind": "read",
                "cleanup": None,
                "method": "POST",
                "path": "/api/2/menu/by_id",
            },
            "get_stop_lists": {
                "kind": "read",
                "cleanup": None,
                "method": "POST",
                "path": "/api/1/stop_lists",
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
        },
    }
    rate_value = yaml.safe_load(Path("contracts/rate-limits.yaml").read_text(encoding="utf-8"))
    assert set(value["operations"]) == set(rate_value["operations"])


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
