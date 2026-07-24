from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.rates import RateCatalog
from tools.openapi_pipeline.live.safety import OperationSafetyCatalog
from tools.openapi_pipeline.live.session import load_operation_contract
from tools.openapi_pipeline.live.write_lifecycle import (
    WriteLifecycleRegistry,
    assert_lifecycle_consistency,
)


def _load(path: Path, value: object) -> WriteLifecycleRegistry:
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
    return WriteLifecycleRegistry.load(path)


def _valid() -> dict[str, object]:
    return {
        "version": 1,
        "scenarios": {
            "customer": {
                "enabled": True,
                "requires_profile_fields": [],
                "ownership_marker": {
                    "source": "literal",
                    "field": "phone",
                    "value": "+70000000042",
                },
                "steps": [
                    {"role": "prepare", "operation": "get_organizations"},
                    {"role": "create", "operation": "create_or_update_customer"},
                    {"role": "check", "operation": "get_customer_info"},
                    {
                        "role": "cleanup",
                        "operation": "delete_customers",
                        "compensates": "create_or_update_customer",
                    },
                ],
            },
        },
    }


def test_registry_loads_enabled_and_disabled_scenarios(tmp_path: Path) -> None:
    value = _valid()
    value["scenarios"]["draft"] = {  # type: ignore[index]
        "enabled": False,
        "disabled_reason": "Stand has no external menu.",
        "requires_profile_fields": ["terminal_group_id"],
        "ownership_marker": {
            "source": "literal",
            "field": "phone",
            "value": "+70000000042",
        },
        "steps": [
            {"role": "prepare", "operation": "get_organizations"},
            {"role": "create", "operation": "create_delivery_draft"},
            {
                "role": "cleanup",
                "operation": "delete_delivery_draft",
                "compensates": "create_delivery_draft",
            },
        ],
    }
    registry = _load(tmp_path / "lifecycles.yaml", value)

    customer = registry.scenarios["customer"]
    assert customer.enabled
    assert customer.ownership_marker.value == "+70000000042"
    assert customer.write_operation_ids == frozenset(
        {"create_or_update_customer", "delete_customers"}
    )
    assert not registry.scenarios["draft"].enabled
    assert registry.enabled_operation_ids() == customer.operation_ids


def test_registry_rejects_duplicate_and_missing_compensation(tmp_path: Path) -> None:
    value = _valid()
    steps = value["scenarios"]["customer"]["steps"]  # type: ignore[index]
    steps.append({"role": "create", "operation": "create_delivery_draft"})

    with pytest.raises(SafetyError, match="exactly one cleanup"):
        _load(tmp_path / "lifecycles.yaml", value)


def test_registry_rejects_cleanup_without_compensates(tmp_path: Path) -> None:
    value = _valid()
    steps = value["scenarios"]["customer"]["steps"]  # type: ignore[index]
    del steps[-1]["compensates"]

    with pytest.raises(SafetyError, match="compensated operation"):
        _load(tmp_path / "lifecycles.yaml", value)


def test_registry_rejects_compensation_of_later_step(tmp_path: Path) -> None:
    value = _valid()
    steps = value["scenarios"]["customer"]["steps"]  # type: ignore[index]
    steps[1], steps[-1] = steps[-1], steps[1]

    with pytest.raises(SafetyError, match="earlier create step"):
        _load(tmp_path / "lifecycles.yaml", value)


def test_registry_rejects_unknown_marker_source_and_bad_profile_field(
    tmp_path: Path,
) -> None:
    value = _valid()
    marker = value["scenarios"]["customer"]["ownership_marker"]  # type: ignore[index]
    marker["source"] = "guessed"

    with pytest.raises(SafetyError, match="source is invalid"):
        _load(tmp_path / "lifecycles.yaml", value)

    value = _valid()
    marker = value["scenarios"]["customer"]["ownership_marker"]  # type: ignore[index]
    marker["source"] = "profile_field"
    marker["field"] = "api_login"
    marker["value"] = None

    with pytest.raises(SafetyError, match="known profile field"):
        _load(tmp_path / "lifecycles.yaml", value)


def test_registry_rejects_disabled_without_reason_and_enabled_with_reason(
    tmp_path: Path,
) -> None:
    value = _valid()
    scenario = value["scenarios"]["customer"]  # type: ignore[index]
    scenario["enabled"] = False

    with pytest.raises(SafetyError, match="disabled_reason"):
        _load(tmp_path / "lifecycles.yaml", value)

    value = _valid()
    scenario = value["scenarios"]["customer"]  # type: ignore[index]
    scenario["disabled_reason"] = "stray"

    with pytest.raises(SafetyError, match="disabled reason"):
        _load(tmp_path / "lifecycles.yaml", value)


def _operation_id_registry() -> frozenset[str]:
    raw = yaml.safe_load(Path("openapi/operation-ids.yaml").read_text(encoding="utf-8"))
    return frozenset(raw["operations"].values())


def test_committed_write_lifecycles_are_consistent_with_live_contracts() -> None:
    registry = WriteLifecycleRegistry.load(Path("contracts/write-lifecycles.yaml"))
    safety = OperationSafetyCatalog.load(Path("contracts/operation-safety.yaml"))
    operations = load_operation_contract(Path("contracts/live-operations.yaml"))
    catalog = RateCatalog.load(Path("contracts/rate-limits.yaml"))

    assert_lifecycle_consistency(
        registry,
        operation_ids=_operation_id_registry(),
        safety_effects={key: entry.effect for key, entry in safety.operations.items()},
        live_operation_kinds={key: op.kind for key, op in operations.items()},
        rate_operation_ids=frozenset(catalog.operation_ids),
    )

    stop_list = registry.scenarios["stop_list_product"]
    assert stop_list.enabled
    assert stop_list.ownership_marker.source == "profile_field"
    assert registry.scenarios["customer"].enabled
    assert not registry.scenarios["delivery_draft"].enabled


def test_consistency_rejects_operation_outside_safety_catalog() -> None:
    registry = WriteLifecycleRegistry.from_mapping(_valid())

    with pytest.raises(SafetyError, match="missing from the safety catalog"):
        assert_lifecycle_consistency(
            registry,
            operation_ids=frozenset(registry.scenarios["customer"].operation_ids),
            safety_effects={},
            live_operation_kinds={},
            rate_operation_ids=frozenset(),
        )


def test_consistency_rejects_wrong_role_effect_and_allowlist_kind() -> None:
    registry = WriteLifecycleRegistry.from_mapping(_valid())
    operations = registry.scenarios["customer"].operation_ids
    safety = dict.fromkeys(operations, "read")
    kinds = {
        "get_organizations": "read",
        "get_customer_info": "read",
        "create_or_update_customer": "compensating",
        "delete_customers": "cleanup",
    }

    with pytest.raises(SafetyError, match="does not fit role"):
        assert_lifecycle_consistency(
            registry,
            operation_ids=operations,
            safety_effects=safety,
            live_operation_kinds=kinds,
            rate_operation_ids=operations,
        )

    safety = {
        "get_organizations": "read",
        "get_customer_info": "read",
        "create_or_update_customer": "create",
        "delete_customers": "delete",
    }
    with pytest.raises(SafetyError, match="allowlisted"):
        assert_lifecycle_consistency(
            registry,
            operation_ids=operations,
            safety_effects=safety,
            live_operation_kinds={"get_organizations": "read"},
            rate_operation_ids=operations,
        )
