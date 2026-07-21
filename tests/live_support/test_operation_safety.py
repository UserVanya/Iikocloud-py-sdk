from __future__ import annotations

import copy
import json
from collections import Counter
from pathlib import Path
from typing import Any

import pytest
import yaml

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.live.safety import OperationSafetyCatalog

VALID: dict[str, Any] = {
    "version": 1,
    "operations": {
        "authenticate": {
            "effect": "auth",
            "live_policy": "automatic",
            "reason": "current single-session token endpoint",
        },
        "get_organizations": {
            "effect": "read",
            "live_policy": "automatic",
            "reason": "reviewed non-mutating organization query",
        },
        "create_delivery_order": {
            "effect": "create",
            "live_policy": "lifecycle_only",
            "reason": "requires an owned order and compensation",
        },
        "authenticate_v2": {
            "effect": "auth",
            "live_policy": "blocked",
            "reason": "requires a separate session contract migration",
        },
    },
}


def _write_catalog(path: Path, value: object) -> Path:
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
    return path


def _load_mapping(tmp_path: Path, value: object) -> OperationSafetyCatalog:
    return OperationSafetyCatalog.load(_write_catalog(tmp_path / "safety.yaml", value))


def _openapi_for(*operation_ids: str) -> dict[str, Any]:
    return {
        "paths": {
            f"/operation/{index}": {"post": {"operationId": operation_id}}
            for index, operation_id in enumerate(operation_ids)
        }
    }


def test_catalog_loads_valid_mapping_without_mutating_input(tmp_path: Path) -> None:
    value = copy.deepcopy(VALID)
    original = copy.deepcopy(value)

    catalog = _load_mapping(tmp_path, value)

    assert value == original
    assert catalog.version == 1
    assert tuple(catalog.operations) == tuple(sorted(VALID["operations"]))
    assert catalog.automatic_read_ids == frozenset({"get_organizations"})
    assert catalog.operations["create_delivery_order"].effect == "create"


def test_catalog_operations_and_entries_are_immutable(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)

    with pytest.raises(TypeError):
        catalog.operations["new_operation"] = catalog.operations["authenticate"]  # type: ignore[index]
    with pytest.raises(AttributeError):
        catalog.operations["authenticate"].effect = "read"  # type: ignore[misc]


def test_catalog_hash_uses_canonical_parsed_content_not_yaml_formatting(
    tmp_path: Path,
) -> None:
    first = _write_catalog(tmp_path / "first.yaml", VALID)
    reversed_operations = dict(reversed(tuple(VALID["operations"].items())))
    second = tmp_path / "second.yaml"
    second.write_text(
        yaml.safe_dump(
            {"operations": reversed_operations, "version": 1},
            sort_keys=False,
            default_flow_style=True,
        ),
        encoding="utf-8",
    )

    first_catalog = OperationSafetyCatalog.load(first)
    second_catalog = OperationSafetyCatalog.load(second)

    expected = {
        "version": 1,
        "operations": {
            operation_id: dict(VALID["operations"][operation_id])
            for operation_id in sorted(VALID["operations"])
        },
    }
    assert first_catalog.sha256 == sha256_bytes(canonical_json_bytes(expected))
    assert second_catalog.sha256 == first_catalog.sha256


def test_catalog_rejects_invalid_utf8(tmp_path: Path) -> None:
    path = tmp_path / "safety.yaml"
    path.write_bytes(b"version: 1\noperations: \xff\n")

    with pytest.raises(SafetyError, match="UTF-8"):
        OperationSafetyCatalog.load(path)


def test_catalog_rejects_file_larger_than_one_mibibyte(tmp_path: Path) -> None:
    path = tmp_path / "safety.yaml"
    path.write_bytes(b" " * (1024 * 1024 + 1))

    with pytest.raises(SafetyError, match="size limit|larger"):
        OperationSafetyCatalog.load(path)


def test_catalog_loader_does_not_use_unbounded_path_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = _write_catalog(tmp_path / "safety.yaml", VALID)

    def fail_unbounded_read(_: Path) -> bytes:
        raise AssertionError("Path.read_bytes performs an unbounded read")

    monkeypatch.setattr(Path, "read_bytes", fail_unbounded_read)

    OperationSafetyCatalog.load(path)


def test_catalog_rejects_duplicate_yaml_key(tmp_path: Path) -> None:
    path = tmp_path / "safety.yaml"
    path.write_text("version: 1\nversion: 1\noperations: {}\n", encoding="utf-8")

    with pytest.raises(SafetyError, match="duplicate key"):
        OperationSafetyCatalog.load(path)


def test_catalog_rejects_yaml_anchor_and_alias(tmp_path: Path) -> None:
    path = tmp_path / "safety.yaml"
    path.write_text(
        "version: 1\noperations:\n"
        "  first_read: &read_entry\n"
        "    effect: read\n"
        "    live_policy: automatic\n"
        "    reason: reviewed non-mutating first query\n"
        "  second_read: *read_entry\n",
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="anchor|alias"):
        OperationSafetyCatalog.load(path)


@pytest.mark.parametrize("field", ["version", "operations"])
def test_catalog_rejects_missing_root_key(tmp_path: Path, field: str) -> None:
    value = copy.deepcopy(VALID)
    del value[field]

    with pytest.raises(SafetyError, match="root keys must be exactly"):
        _load_mapping(tmp_path, value)


def test_catalog_rejects_extra_root_key(tmp_path: Path) -> None:
    value = copy.deepcopy(VALID)
    value["extra"] = True

    with pytest.raises(SafetyError, match="root keys must be exactly"):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize("field", ["effect", "live_policy", "reason"])
def test_catalog_rejects_missing_entry_key(tmp_path: Path, field: str) -> None:
    value = copy.deepcopy(VALID)
    del value["operations"]["get_organizations"][field]

    with pytest.raises(SafetyError, match="entry.*keys must be exactly"):
        _load_mapping(tmp_path, value)


def test_catalog_rejects_extra_entry_key(tmp_path: Path) -> None:
    value = copy.deepcopy(VALID)
    value["operations"]["get_organizations"]["extra"] = True

    with pytest.raises(SafetyError, match="entry.*keys must be exactly"):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize("operation_id", ["", "-unsafe", "has space", "x" * 129, 1])
def test_catalog_rejects_unsafe_operation_id(
    tmp_path: Path, operation_id: object
) -> None:
    value = copy.deepcopy(VALID)
    entry = value["operations"].pop("get_organizations")
    value["operations"][operation_id] = entry

    with pytest.raises(SafetyError, match="operation ID.*safe ASCII"):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize(
    ("field", "invalid"),
    [("effect", "lookup"), ("live_policy", "sometimes")],
)
def test_catalog_rejects_invalid_enum(
    tmp_path: Path, field: str, invalid: str
) -> None:
    value = copy.deepcopy(VALID)
    value["operations"]["get_organizations"][field] = invalid

    with pytest.raises(SafetyError, match=field):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize(
    "reason",
    [
        "",
        " leading whitespace",
        "trailing whitespace ",
        "line\nbreak",
        "control\x1fcharacter",
        "x" * 257,
        "customer 123e4567-e89b-12d3-a456-426614174000",
        "nil 00000000-0000-0000-0000-000000000000",
        "v7 01890f6c-7b5d-7cc0-98c4-dc0c0c07398f",
        "contact person@example.com",
        "Bearer secret-value",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.signature",
        "api_key=secret-value",
        "token: secret-value",
    ],
)
def test_catalog_rejects_unsafe_review_reason(tmp_path: Path, reason: str) -> None:
    value = copy.deepcopy(VALID)
    value["operations"]["get_organizations"]["reason"] = reason

    with pytest.raises(SafetyError, match="reason"):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize("live_policy", ["automatic", "lifecycle_only", "manual_only"])
def test_unknown_effect_must_be_blocked(tmp_path: Path, live_policy: str) -> None:
    value = copy.deepcopy(VALID)
    entry = value["operations"]["get_organizations"]
    entry["effect"] = "unknown"
    entry["live_policy"] = live_policy

    with pytest.raises(SafetyError, match="unknown.*blocked"):
        _load_mapping(tmp_path, value)


@pytest.mark.parametrize("effect", ["create", "update", "delete", "action", "irreversible"])
def test_automatic_policy_rejects_mutating_effects(tmp_path: Path, effect: str) -> None:
    value = copy.deepcopy(VALID)
    entry = value["operations"]["get_organizations"]
    entry["effect"] = effect
    entry["live_policy"] = "automatic"

    with pytest.raises(SafetyError, match="automatic.*read|read.*automatic"):
        _load_mapping(tmp_path, value)


def test_auth_automatic_is_reserved_for_authenticate(tmp_path: Path) -> None:
    value = copy.deepcopy(VALID)
    value["operations"]["authenticate_v2"]["live_policy"] = "automatic"

    with pytest.raises(SafetyError, match="authenticate"):
        _load_mapping(tmp_path, value)


def test_openapi_parity_uses_only_the_eight_inventory_http_methods(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*VALID["operations"])
    document["paths"]["/ignored"] = {
        "parameters": [{"name": "fixture"}],
        "connect": {"operationId": "not_an_openapi_operation"},
    }

    catalog.assert_matches_openapi(document)


def test_openapi_parity_rejects_duplicate_operation_id(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*VALID["operations"])
    document["paths"]["/duplicate"] = {"get": {"operationId": "authenticate"}}

    with pytest.raises(SafetyError, match="duplicate.*authenticate"):
        catalog.assert_matches_openapi(document)


def test_openapi_parity_rejects_operation_without_id(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*VALID["operations"])
    document["paths"]["/missing-id"] = {"trace": {}}

    with pytest.raises(SafetyError, match="missing.*operationId"):
        catalog.assert_matches_openapi(document)


def test_openapi_parity_rejects_path_item_reference(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*VALID["operations"])
    document["paths"]["/hidden"] = {"$ref": "#/x-hidden-path-item"}
    document["x-hidden-path-item"] = {"get": {"operationId": "hidden_operation"}}

    with pytest.raises(SafetyError, match=r"path item.*\$ref"):
        catalog.assert_matches_openapi(document)


def test_openapi_parity_rejects_missing_catalog_operation(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*tuple(VALID["operations"])[1:])

    with pytest.raises(SafetyError, match="missing from OpenAPI.*authenticate"):
        catalog.assert_matches_openapi(document)


def test_openapi_parity_rejects_extra_openapi_operation(tmp_path: Path) -> None:
    catalog = _load_mapping(tmp_path, VALID)
    document = _openapi_for(*VALID["operations"], "new_upstream_operation")

    with pytest.raises(SafetyError, match="extra in OpenAPI.*new_upstream_operation"):
        catalog.assert_matches_openapi(document)


def test_committed_catalog_is_exhaustive_and_matches_effective_openapi() -> None:
    document = json.loads(
        Path("build/openapi/effective.json").read_text(encoding="utf-8")
    )
    catalog = OperationSafetyCatalog.load(Path("contracts/operation-safety.yaml"))

    catalog.assert_matches_openapi(document)

    assert len(catalog.operations) == 225
    assert len(catalog.automatic_read_ids) == 91
    assert Counter(
        (entry.effect, entry.live_policy) for entry in catalog.operations.values()
    ) == Counter(
        {
            ("auth", "automatic"): 1,
            ("auth", "blocked"): 1,
            ("read", "automatic"): 91,
            ("create", "lifecycle_only"): 17,
            ("update", "lifecycle_only"): 43,
            ("update", "manual_only"): 1,
            ("update", "blocked"): 2,
            ("delete", "lifecycle_only"): 20,
            ("action", "lifecycle_only"): 32,
            ("action", "manual_only"): 3,
            ("irreversible", "manual_only"): 13,
            ("irreversible", "blocked"): 1,
        }
    )
