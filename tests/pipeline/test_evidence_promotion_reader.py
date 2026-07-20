from __future__ import annotations

import dataclasses
import gc
import hashlib
import json
import os
import warnings
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest

import tools.openapi_pipeline.evidence_promotion as promotion_module
import tools.openapi_pipeline.evidence_validation as validation_module
from tools.openapi_pipeline.capture import CaptureWriter
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence import build_versioned_evidence_redaction_hints
from tools.openapi_pipeline.evidence_promotion import (
    CaptureEvidenceReader,
    EvidencePair,
)
from tools.openapi_pipeline.evidence_validation import MenuEvidenceValidator
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.lock import LiveProcessLock

OPERATION = "get_external_menu_by_id"
CAPTURE_UUID_ALIAS = "00000000-0000-4000-8000-000000000001"
RAW_UUID_KEY = "11111111-1111-4111-8111-111111111111"


def _effective_schema() -> dict[str, Any]:
    def root_schema(version: int) -> dict[str, Any]:
        groups_name = "itemCategories" if version == 2 else "itemGroups"
        properties: dict[str, Any] = {
            "comboCategories": {"type": "array", "items": {"type": "object"}},
            "floatValue": {"format": "float", "type": "number"},
            "formatVersion": {"default": 2, "type": "integer"},
            "id": {"type": "string"},
            "int32Value": {"format": "int32", "type": "integer"},
            "int64Value": {"format": "int64", "type": "integer"},
            "mode": {"enum": [f"V{version}"], "type": "string"},
            groups_name: {"type": "array", "items": {"type": "object"}},
            "name": {"type": "string"},
        }
        if version in {3, 4}:
            item_component = {
                3: "OverrideTaxesDto",
                4: "OverrideTaxesDto2",
            }[version]
            properties["overrideTaxCategories"] = {
                "description": "Tax benefits",
                "items": {"$ref": f"#/components/schemas/{item_component}"},
                "type": "array",
            }
        if version == 4:
            properties["itemGroups"] = {
                "type": "array",
                "items": {"$ref": "#/components/schemas/ExternalMenuCategory3"},
            }
        return {
            "type": "object",
            "required": ["id", groups_name, "comboCategories", "mode"],
            "properties": properties,
        }

    return {
        "openapi": "3.1.0",
        "paths": {
            "/api/2/menu/by_id": {
                "post": {
                    "operationId": OPERATION,
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": (
                                        "#/components/schemas/"
                                        "iikoTransport.PublicApi.Contracts.Nomenclature.MenuRequest"
                                    )
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "oneOf": [
                                            {"$ref": "#/components/schemas/ExternalMenuV2"},
                                            {"$ref": "#/components/schemas/ExternalMenuV3"},
                                            {"$ref": "#/components/schemas/ExternalMenuV4"},
                                        ]
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "iikoTransport.PublicApi.Contracts.Nomenclature.MenuRequest": {
                    "additionalProperties": False,
                    "type": "object",
                    "required": ["externalMenuId", "organizationIds"],
                    "properties": {
                        "externalMenuId": {"type": "string"},
                        "organizationIds": {
                            "type": "array",
                            "items": {"format": "uuid", "type": "string"},
                        },
                        "version": {"nullable": True, "type": "integer"},
                    },
                },
                "ExternalMenuV2": root_schema(2),
                "ExternalMenuV3": root_schema(3),
                "ExternalMenuV4": root_schema(4),
                "OverrideTaxesDto": {"type": "object"},
                "OverrideTaxesDto2": {"type": "object"},
                "ExternalMenuCategory3": {
                    "type": "object",
                    "required": ["items"],
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {"$ref": "#/components/schemas/ExternalMenuItem3"},
                                    {"$ref": "#/components/schemas/ExternalMenuComboItem"},
                                ]
                            },
                        }
                    },
                },
                "ExternalMenuItem3": {
                    "type": "object",
                    "required": [
                        "itemSizes",
                        "modifierSchemaId",
                        "orderItemType",
                        "allergenGroupIds",
                        "id",
                        "splittable",
                    ],
                    "properties": {
                        "allergenGroupIds": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "id": {"type": "string"},
                        "itemSizes": {"type": "array", "items": {}},
                        "modifierSchemaId": {
                            "description": "Modifier schema ID",
                            "example": "00000000-0000-0000-0000-000000000000",
                            "nullable": True,
                            "type": "string",
                        },
                        "orderItemType": {
                            "description": "Product or compound",
                            "enum": ["Product", "Compound"],
                            "format": "enum",
                            "type": "string",
                        },
                        "splittable": {"type": "boolean"},
                        "type": {
                            "enum": ["DISH", "COMBO"],
                            "type": "string",
                            "description": "Item type",
                            "default": "DISH",
                        },
                        "name": {"type": "string"},
                    },
                },
                "ExternalMenuComboItem": {
                    "properties": {
                        "barcodes": {
                            "items": {"$ref": "#/components/schemas/BarcodeDto4"},
                            "nullable": True,
                            "type": "array",
                        },
                        "description": {
                            "default": "",
                            "description": "Product description",
                            "example": (
                                "Delicate taste, juicy chicken fillet, mushrooms, Cheddar "
                                "cheese and Mozzarella cheese, oregano, Parmegiano sauce"
                            ),
                            "type": "string",
                        },
                        "groups": {
                            "items": {"$ref": "#/components/schemas/ComboGroupDto4"},
                            "type": "array",
                        },
                        "id": {
                            "description": "Product ID",
                            "example": "00000000-0000-0000-0000-000000000000",
                            "type": "string",
                        },
                        "isMarked": {
                            "default": False,
                            "description": "Marking flag",
                            "type": "boolean",
                        },
                        "name": {
                            "default": "",
                            "description": "Product name",
                            "example": "Chicken Parmegiano",
                            "type": "string",
                        },
                        "priceStrategy": {
                            "default": "BY_COMPONENT",
                            "description": "Price strategy",
                            "enum": ["BY_COMPONENT"],
                            "type": "string",
                        },
                        "sizes": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/ExternalMenuComboItemSize"},
                        },
                        "sku": {
                            "default": "",
                            "description": "Product code",
                            "example": "002345-35cm",
                            "type": "string",
                        },
                        "type": {"type": "string"},
                    },
                    "required": [
                        "sizes",
                        "itemSizes",
                        "modifierSchemaId",
                        "type",
                        "orderItemType",
                        "allergenGroupIds",
                        "id",
                        "splittable",
                    ],
                    "type": "object",
                },
                "ExternalMenuComboItemSize": {
                    "type": "object",
                    "required": ["name", "sizeId"],
                    "properties": {
                        "name": {"type": "string"},
                        "sizeId": {"type": "string"},
                    },
                },
                "BarcodeDto4": {},
                "ComboGroupDto4": {},
            }
        },
    }


def _response_body(version: int) -> dict[str, Any]:
    result: dict[str, Any] = {
        "comboCategories": [],
        "formatVersion": version,
        "id": "33333333-3333-4333-8333-333333333333",
        "mode": f"V{version}",
    }
    if version == 2:
        result["itemCategories"] = []
    elif version == 3:
        result["itemGroups"] = []
    else:
        result["itemGroups"] = [
            {
                "items": [
                    {
                        "id": "44444444-4444-4444-8444-444444444444",
                        "sizes": [],
                        "type": "COMBO",
                    }
                ]
            }
        ]
    return result


def _capture_root(repository_root: Path) -> Path:
    return repository_root / "private/captures"


def _make_repository(repository_root: Path) -> None:
    repository_root.mkdir(mode=0o700, parents=True, exist_ok=True)
    marker = repository_root / "pyproject.toml"
    if not marker.exists():
        marker.write_text('[project]\nname = "synthetic-evidence-test"\n', encoding="utf-8")


def _write_menu_pair(
    repository_root: Path,
    version: int,
    *,
    run_id: str | None = None,
) -> tuple[Path, Path]:
    _make_repository(repository_root)
    schema = _effective_schema()
    hints = build_versioned_evidence_redaction_hints(schema, OPERATION, version)
    return CaptureWriter(_capture_root(repository_root)).write(
        run_id=run_id or f"run-v{version}",
        operation_id=OPERATION,
        kind="read",
        request_json={
            "externalMenuId": "11111111-1111-4111-8111-111111111111",
            "organizationIds": ["22222222-2222-4222-8222-222222222222"],
            "version": version,
        },
        response_json=_response_body(version),
        metadata={"method": "POST", "path": "/api/2/menu/by_id", "status": 200},
        approved_path="/api/2/menu/by_id",
        request_path_values=hints.request_values,
        response_path_values=hints.response_values_for_status(200),
    )


def _complete_tree(root: Path) -> dict[int, tuple[Path, Path]]:
    return {version: _write_menu_pair(root, version) for version in (4, 2, 3)}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert type(value) is dict
    return value


def _replace_json(path: Path, value: object) -> None:
    path.write_bytes(canonical_json_bytes(value))
    path.chmod(0o600)


def _lock_for(repository_root: Path) -> LiveProcessLock:
    return LiveProcessLock(repository_root / ".state/live.lock")


def _read(
    repository_root: Path,
    *,
    effective_schema: dict[str, Any] | None = None,
) -> Mapping[int, EvidencePair]:
    lock = _lock_for(repository_root)
    with lock:
        return CaptureEvidenceReader(
            repository_root,
            effective_schema or _effective_schema(),
            process_lock=lock,
        ).read_menu_pairs()


def test_reader_collects_one_immutable_canonical_pair_per_version_without_writes(
    tmp_path: Path,
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    before = {
        path: (path.stat().st_ino, path.stat().st_size, path.read_bytes())
        for pair in paths.values()
        for path in pair
    }

    pairs = _read(root)

    assert isinstance(pairs, MappingProxyType)
    assert tuple(pairs) == (2, 3, 4)
    for version, pair in pairs.items():
        request_path, response_path = paths[version]
        assert pair.version == version
        assert pair.request["body"]["version"] == version
        assert pair.response["body"]["formatVersion"] == version
        assert pair.request_sha256 == hashlib.sha256(request_path.read_bytes()).hexdigest()
        assert pair.response_sha256 == hashlib.sha256(response_path.read_bytes()).hexdigest()
        assert isinstance(pair.request, MappingProxyType)
        assert isinstance(pair.request["body"], MappingProxyType)
        assert isinstance(pair.request["body"]["organizationIds"], tuple)
        with pytest.raises(dataclasses.FrozenInstanceError):
            pair.version = 9
        with pytest.raises(TypeError):
            pair.request["body"] = {}  # type: ignore[index]

    assert {
        path: (path.stat().st_ino, path.stat().st_size, path.read_bytes()) for path in before
    } == before


def test_reader_accepts_an_injected_held_canonical_live_lock(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    _complete_tree(root)
    lock = _lock_for(root)

    with pytest.raises(SafetyError, match="held"):
        CaptureEvidenceReader(root, _effective_schema(), process_lock=lock).read_menu_pairs()

    with lock:
        assert tuple(
            CaptureEvidenceReader(
                root,
                _effective_schema(),
                process_lock=lock,
            ).read_menu_pairs()
        ) == (2, 3, 4)


@pytest.mark.parametrize("missing_version", [2, 3, 4])
def test_reader_rejects_a_missing_version(tmp_path: Path, missing_version: int) -> None:
    root = tmp_path / "captures"
    for version in {2, 3, 4} - {missing_version}:
        _write_menu_pair(root, version)

    with pytest.raises(SafetyError, match="exactly one.*2, 3, and 4"):
        _read(root)


def test_reader_rejects_duplicate_and_partial_pairs(tmp_path: Path) -> None:
    duplicate_root = tmp_path / "duplicates"
    _complete_tree(duplicate_root)
    _write_menu_pair(duplicate_root, 2, run_id="second-v2")
    with pytest.raises(SafetyError, match="duplicate.*version 2"):
        _read(duplicate_root)

    partial_root = tmp_path / "partial"
    paths = _complete_tree(partial_root)
    paths[3][1].unlink()
    with pytest.raises(SafetyError, match="exactly request.json and response.json"):
        _read(partial_root)


@pytest.mark.parametrize(
    ("target", "mutation", "message"),
    [
        ("request", lambda value: {**value, "extra": None}, "envelope"),
        (
            "request",
            lambda value: {**value, "metadata": {**value["metadata"], "status": 201}},
            "metadata",
        ),
        (
            "request",
            lambda value: {
                **value,
                "body": {**value["body"], "unexpected": "<redacted:string>"},
            },
            "payload",
        ),
        (
            "request",
            lambda value: {**value, "body": {**value["body"], "version": True}},
            "version",
        ),
        (
            "response",
            lambda value: {**value, "body": {**value["body"], "formatVersion": 3}},
            "formatVersion",
        ),
    ],
)
def test_reader_rejects_invalid_envelopes_metadata_and_version_contract(
    tmp_path: Path,
    target: str,
    mutation: Any,
    message: str,
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    path = paths[2][0 if target == "request" else 1]
    _replace_json(path, mutation(_load(path)))

    with pytest.raises(SafetyError, match=message):
        _read(root)


def test_reader_rejects_request_response_metadata_mismatch(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["metadata"]["headers"] = {"accept": "application/json"}
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="metadata.*identical"):
        _read(root)


@pytest.mark.parametrize("malformation", ["duplicate", "nan", "noncanonical", "utf8", "depth"])
def test_reader_rejects_non_strict_or_noncanonical_json(tmp_path: Path, malformation: str) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    request_path = paths[2][0]
    if malformation == "duplicate":
        body = request_path.read_bytes().replace(b'{"body":', b'{"body":null,"body":', 1)
    elif malformation == "nan":
        body = request_path.read_bytes().replace(b'"version":2', b'"version":NaN', 1)
    elif malformation == "noncanonical":
        body = json.dumps(_load(request_path), ensure_ascii=False).encode("utf-8")
    elif malformation == "utf8":
        body = b"\xff\n"
    else:
        nested: object = None
        for _index in range(66):
            nested = [nested]
        value = _load(request_path)
        value["body"]["nested"] = nested
        body = canonical_json_bytes(value)
    request_path.write_bytes(body)
    request_path.chmod(0o600)

    with pytest.raises(SafetyError, match="JSON|canonical|nesting"):
        _read(root)


@pytest.mark.parametrize("unsafe", ["extra", "symlink", "hardlink", "fifo", "directory"])
def test_reader_rejects_unsafe_or_extra_operation_entries(tmp_path: Path, unsafe: str) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    request_path, response_path = paths[2]
    operation = request_path.parent
    if unsafe == "extra":
        extra = operation / "extra.json"
        extra.write_bytes(b"{}\n")
        extra.chmod(0o600)
    elif unsafe == "symlink":
        request_path.unlink()
        request_path.symlink_to(response_path)
    elif unsafe == "hardlink":
        os.link(request_path, tmp_path / "request-alias.json")
    elif unsafe == "fifo":
        request_path.unlink()
        os.mkfifo(request_path, mode=0o600)
    else:
        request_path.unlink()
        request_path.mkdir(mode=0o700)

    with pytest.raises(SafetyError, match="exactly|private regular|symlink|hard link"):
        _read(root)


def test_reader_rejects_oversize_wide_or_wrong_owner_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    oversize_root = tmp_path / "oversize"
    paths = _complete_tree(oversize_root)
    with paths[2][0].open("r+b") as stream:
        stream.truncate(32 * 1024 * 1024 + 1)
    with pytest.raises(SafetyError, match="32 MiB"):
        _read(oversize_root)

    wide_root = tmp_path / "wide"
    wide_paths = _complete_tree(wide_root)
    wide_paths[2][1].chmod(0o644)
    with pytest.raises(SafetyError, match="0600"):
        _read(wide_root)

    owner_root = tmp_path / "owner"
    _complete_tree(owner_root)
    lock = _lock_for(owner_root)
    with lock:
        actual_uid = os.getuid()
        monkeypatch.setattr(promotion_module.os, "getuid", lambda: actual_uid + 1)
        with pytest.raises(SafetyError, match="owned"):
            CaptureEvidenceReader(
                owner_root,
                _effective_schema(),
                process_lock=lock,
            ).read_menu_pairs()


@pytest.mark.parametrize("component", ["root", "run", "operation"])
def test_reader_requires_mode_0700_on_every_private_directory(
    tmp_path: Path, component: str
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    target = {
        "root": _capture_root(root),
        "run": paths[2][0].parent.parent,
        "operation": paths[2][0].parent,
    }[component]
    target.chmod(0o755)

    with pytest.raises(SafetyError, match="0700"):
        _read(root)


def test_reader_rejects_symlinked_directory_and_unsafe_root_entries(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    operation = paths[2][0].parent
    moved = tmp_path / "moved-operation"
    operation.rename(moved)
    operation.symlink_to(moved, target_is_directory=True)
    with pytest.raises(SafetyError, match="directory|symlink"):
        _read(root)

    other_root = tmp_path / "other-captures"
    _complete_tree(other_root)
    extra = _capture_root(other_root) / "not-a-run"
    extra.write_bytes(b"unsafe\n")
    extra.chmod(0o600)
    with pytest.raises(SafetyError, match="run.*directory"):
        _read(other_root)


def test_reader_rejects_a_symlinked_capture_root_ancestor(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    private = repository_root / "private"
    moved_private = tmp_path / "moved-private"
    private.rename(moved_private)
    private.symlink_to(moved_private, target_is_directory=True)
    lock = LiveProcessLock(repository_root / ".state/live.lock")

    with lock, pytest.raises(SafetyError, match="symlink|ancestry"):
        CaptureEvidenceReader(
            repository_root,
            _effective_schema(),
            process_lock=lock,
        ).read_menu_pairs()


def test_reader_double_read_detects_a_concurrent_file_swap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    target = paths[2][0]
    original = promotion_module._read_private_file_once
    calls = 0

    def swap_after_first_read(directory_fd: int, name: str, expected: os.stat_result) -> bytes:
        nonlocal calls
        body = original(directory_fd, name, expected)
        if name == "request.json":
            calls += 1
            if calls == 1:
                replacement = target.with_name("replacement.json")
                replacement.write_bytes(target.read_bytes())
                replacement.chmod(0o600)
                replacement.replace(target)
        return body

    monkeypatch.setattr(promotion_module, "_read_private_file_once", swap_after_first_read)

    with pytest.raises(SafetyError, match="changed|concurrent"):
        _read(root)


def test_reader_revalidates_operation_entry_list_after_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    operation = paths[2][0].parent
    original = promotion_module._directory_entries
    target_calls = 0

    def add_entry_after_snapshot(directory_fd: int) -> tuple[str, ...]:
        nonlocal target_calls
        entries = original(directory_fd)
        if entries == ("request.json", "response.json"):
            target_calls += 1
            if target_calls == 1:
                extra = operation / "late.json"
                extra.write_bytes(b"{}\n")
                extra.chmod(0o600)
        return entries

    monkeypatch.setattr(promotion_module, "_directory_entries", add_entry_after_snapshot)

    with pytest.raises(SafetyError, match="changed|concurrent"):
        _read(root)


def test_reader_fails_if_the_injected_lock_is_released_mid_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    _complete_tree(root)
    lock = _lock_for(root)
    lock.acquire()
    original = promotion_module._directory_entries
    released = False

    def release_after_first_snapshot(directory_fd: int) -> tuple[str, ...]:
        nonlocal released
        entries = original(directory_fd)
        if not released:
            released = True
            lock.release()
        return entries

    monkeypatch.setattr(promotion_module, "_directory_entries", release_after_first_snapshot)
    try:
        with pytest.raises(SafetyError, match="released"):
            CaptureEvidenceReader(
                root,
                _effective_schema(),
                process_lock=lock,
            ).read_menu_pairs()
    finally:
        lock.release()


def test_reader_runs_generic_scan_and_concrete_schema_validator(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"]["leak"] = "person@example.com"
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="secret/PII"):
        _read(root)

    clean_root = tmp_path / "clean"
    _complete_tree(clean_root)
    pairs = _read(clean_root)
    assert tuple(pairs) == (2, 3, 4)


@pytest.mark.parametrize("version", [3, 4])
def test_pair_revalidator_allows_capture_alias_keys_only_in_reviewed_response_map(
    tmp_path: Path,
    version: int,
) -> None:
    root = tmp_path / "repository"
    request_path, response_path = _write_menu_pair(root, version)
    request = _load(request_path)
    response = _load(response_path)
    response["body"]["overrideTaxCategories"] = {CAPTURE_UUID_ALIAS: []}

    assert (
        promotion_module.revalidate_evidence_pair_contract(
            request,
            response,
            expected_run_id=f"run-v{version}",
        )
        == version
    )


@pytest.mark.parametrize(
    ("version", "mutation"),
    [
        (2, "reviewed-path"),
        (3, "other-response-path"),
        (3, "raw-uuid-at-reviewed-path"),
        (4, "list-item-alias-key"),
        (4, "nested-alias-key"),
    ],
)
def test_pair_revalidator_rejects_uuid_keys_outside_exact_reviewed_alias_scope(
    tmp_path: Path,
    version: int,
    mutation: str,
) -> None:
    root = tmp_path / "repository"
    request_path, response_path = _write_menu_pair(root, version)
    request = _load(request_path)
    response = _load(response_path)
    if mutation == "other-response-path":
        response["body"]["otherMap"] = {CAPTURE_UUID_ALIAS: []}
        sensitive_key = CAPTURE_UUID_ALIAS
    elif mutation == "raw-uuid-at-reviewed-path":
        response["body"]["overrideTaxCategories"] = {RAW_UUID_KEY: []}
        sensitive_key = RAW_UUID_KEY
    elif mutation == "nested-alias-key":
        response["body"]["overrideTaxCategories"] = {
            CAPTURE_UUID_ALIAS: [{CAPTURE_UUID_ALIAS: []}]
        }
        sensitive_key = CAPTURE_UUID_ALIAS
    elif mutation == "list-item-alias-key":
        response["body"]["overrideTaxCategories"] = [{CAPTURE_UUID_ALIAS: []}]
        sensitive_key = CAPTURE_UUID_ALIAS
    else:
        response["body"]["overrideTaxCategories"] = {CAPTURE_UUID_ALIAS: []}
        sensitive_key = CAPTURE_UUID_ALIAS

    with pytest.raises(SafetyError, match="secret/PII") as caught:
        promotion_module.revalidate_evidence_pair_contract(
            request,
            response,
            expected_run_id=f"run-v{version}",
        )

    assert sensitive_key not in str(caught.value)


def test_generic_scanner_does_not_allow_response_alias_exception_for_request_data() -> None:
    request_shaped_value: dict[str, Any] = {
        "body": {"overrideTaxCategories": {CAPTURE_UUID_ALIAS: []}}
    }

    with pytest.raises(SafetyError, match="secret/PII"):
        promotion_module._scan_for_secret_or_pii(  # noqa: SLF001 - exception-scope regression
            request_shaped_value
        )


@pytest.mark.parametrize("version", [3, 4])
def test_reader_preserves_reviewed_override_tax_map_and_validates_its_items(
    tmp_path: Path,
    version: int,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[version][1]
    response = _load(response_path)
    response["body"]["overrideTaxCategories"] = {CAPTURE_UUID_ALIAS: [{}]}
    _replace_json(response_path, response)
    before = response_path.read_bytes()

    pairs = _read(root)

    response_body = pairs[version].response["body"]
    assert isinstance(response_body, Mapping)
    override_tax_categories = response_body["overrideTaxCategories"]
    assert isinstance(override_tax_categories, Mapping)
    assert tuple(override_tax_categories) == (CAPTURE_UUID_ALIAS,)
    assert override_tax_categories[CAPTURE_UUID_ALIAS] == (MappingProxyType({}),)
    assert response_path.read_bytes() == before


@pytest.mark.parametrize(
    ("version", "valid_marker", "invalid_marker"),
    [
        (3, "v3Marker", "v4Marker"),
        (4, "v4Marker", "v3Marker"),
    ],
)
def test_validator_uses_the_version_specific_override_tax_item_component(
    tmp_path: Path,
    version: int,
    valid_marker: str,
    invalid_marker: str,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    request = _load(paths[version][0])
    response = _load(paths[version][1])
    schema = _effective_schema()
    components = schema["components"]["schemas"]
    components["OverrideTaxesDto"] = {
        "properties": {"v3Marker": {"type": "boolean"}},
        "required": ["v3Marker"],
        "type": "object",
    }
    components["OverrideTaxesDto2"] = {
        "properties": {"v4Marker": {"type": "boolean"}},
        "required": ["v4Marker"],
        "type": "object",
    }
    validator = MenuEvidenceValidator(schema)
    response["body"]["overrideTaxCategories"] = {
        CAPTURE_UUID_ALIAS: [{valid_marker: True}]
    }

    validator.validate(version, request, response)

    response["body"]["overrideTaxCategories"] = {
        CAPTURE_UUID_ALIAS: [{invalid_marker: True}]
    }
    with pytest.raises(SafetyError, match="required|undeclared|override"):
        validator.validate(version, request, response)


@pytest.mark.parametrize(
    ("version", "invalid_map"),
    [
        (2, {CAPTURE_UUID_ALIAS: []}),
        (3, {RAW_UUID_KEY: []}),
        (3, {CAPTURE_UUID_ALIAS: {}}),
        (4, {CAPTURE_UUID_ALIAS: ["not-an-object"]}),
    ],
)
def test_validator_rejects_override_tax_maps_outside_reviewed_shape(
    tmp_path: Path,
    version: int,
    invalid_map: object,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    request = _load(paths[version][0])
    response = _load(paths[version][1])
    response["body"]["overrideTaxCategories"] = invalid_map

    with pytest.raises(SafetyError, match="type|alias|list|undeclared|property"):
        MenuEvidenceValidator(_effective_schema()).validate(version, request, response)


def test_reader_requires_a_held_lock_before_filesystem_access(tmp_path: Path) -> None:
    root = tmp_path
    _make_repository(root)
    with pytest.raises(SafetyError, match="held.*lock"):
        CaptureEvidenceReader(root, _effective_schema()).read_menu_pairs()
    assert not _capture_root(root).exists()


def test_reader_rejects_an_unapproved_operation_before_filesystem_access(tmp_path: Path) -> None:
    root = tmp_path
    _make_repository(root)
    lock = _lock_for(root)
    with lock, pytest.raises(SafetyError, match="approved"):
        CaptureEvidenceReader(
            root,
            _effective_schema(),
            operation="authenticate",
            process_lock=lock,
        ).read_menu_pairs()

    assert not _capture_root(root).exists()


def test_reader_rejects_a_held_noncanonical_lock_before_capture_access(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    _complete_tree(root)
    wrong_lock = LiveProcessLock(tmp_path / "wrong-state/live.lock")
    opened = False
    real_open = promotion_module._open_absolute_private_root

    def track_open(path: Path) -> int:
        nonlocal opened
        opened = True
        return real_open(path)

    monkeypatch.setattr(promotion_module, "_open_absolute_private_root", track_open)
    with wrong_lock, pytest.raises(SafetyError, match="canonical.*lock"):
        CaptureEvidenceReader(
            root,
            _effective_schema(),
            process_lock=wrong_lock,
        ).read_menu_pairs()

    assert not opened


def test_reader_rejects_replaced_lock_inode_before_capture_access(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    path = repository_root / ".state/live.lock"
    displaced = repository_root / ".state/displaced.lock"
    first = LiveProcessLock(path)
    opened = False
    real_open = promotion_module._open_absolute_private_root

    def track_open(capture_root: Path) -> int:
        nonlocal opened
        opened = True
        return real_open(capture_root)

    first.acquire()
    try:
        path.rename(displaced)
        path.touch(mode=0o600)
        path.chmod(0o600)
        monkeypatch.setattr(promotion_module, "_open_absolute_private_root", track_open)
        with pytest.raises(SafetyError, match="binding|inode|changed"):
            CaptureEvidenceReader(
                repository_root,
                _effective_schema(),
                process_lock=first,
            ).read_menu_pairs()
    finally:
        if path.exists():
            path.unlink()
        if displaced.exists():
            displaced.rename(path)
        first.release()

    assert not opened


def test_reader_rechecks_lock_inode_after_validation_before_return(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    path = repository_root / ".state/live.lock"
    displaced = repository_root / ".state/displaced.lock"
    first = LiveProcessLock(path)
    original_validate = MenuEvidenceValidator.validate

    def replace_after_last_validation(
        validator: MenuEvidenceValidator,
        version: int,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> None:
        original_validate(validator, version, request, response)
        if version == 4:
            path.rename(displaced)
            path.touch(mode=0o600)
            path.chmod(0o600)

    monkeypatch.setattr(MenuEvidenceValidator, "validate", replace_after_last_validation)
    first.acquire()
    try:
        with pytest.raises(SafetyError, match="binding|inode|changed"):
            CaptureEvidenceReader(
                repository_root,
                _effective_schema(),
                process_lock=first,
            ).read_menu_pairs()
    finally:
        if path.exists():
            path.unlink()
        if displaced.exists():
            displaced.rename(path)
        first.release()


def test_reader_rejects_release_and_reacquire_of_same_lock_object(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    lock = _lock_for(repository_root)
    original_validate = MenuEvidenceValidator.validate

    def reacquire_after_last_validation(
        validator: MenuEvidenceValidator,
        version: int,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> None:
        original_validate(validator, version, request, response)
        if version == 4:
            lock.release()
            lock.acquire()

    monkeypatch.setattr(MenuEvidenceValidator, "validate", reacquire_after_last_validation)
    with lock, pytest.raises(SafetyError, match="binding|token|acquisition"):
        CaptureEvidenceReader(
            repository_root,
            _effective_schema(),
            process_lock=lock,
        ).read_menu_pairs()


def test_reader_continues_after_conforming_replacement_is_blocked_and_path_restored(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    path = repository_root / ".state/live.lock"
    displaced = repository_root / ".state/displaced.lock"
    first = LiveProcessLock(path)
    replacement = LiveProcessLock(path)
    original_validate = MenuEvidenceValidator.validate

    def restore_original_inode_after_last_validation(
        validator: MenuEvidenceValidator,
        version: int,
        request: Mapping[str, Any],
        response: Mapping[str, Any],
    ) -> None:
        original_validate(validator, version, request, response)
        if version == 4:
            path.rename(displaced)
            try:
                with pytest.raises(
                    SafetyError,
                    match="another live test process is active",
                ):
                    replacement.acquire()
            finally:
                replacement.release()
                if path.exists():
                    path.unlink()
                if displaced.exists():
                    displaced.rename(path)
            first.assert_current_binding()

    monkeypatch.setattr(
        MenuEvidenceValidator,
        "validate",
        restore_original_inode_after_last_validation,
    )
    first.acquire()
    try:
        pairs = CaptureEvidenceReader(
            repository_root,
            _effective_schema(),
            process_lock=first,
        ).read_menu_pairs()
    finally:
        replacement.release()
        first.release()

    assert tuple(pairs) == (2, 3, 4)


@pytest.mark.parametrize("alias_kind", ["relative", "dotdot", "symlink", "capture-root"])
def test_reader_rejects_noncanonical_repository_alias_before_capture_access(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    alias_kind: str,
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    if alias_kind == "relative":
        monkeypatch.chdir(tmp_path)
        supplied = Path("repository")
    elif alias_kind == "dotdot":
        (repository_root / "nested").mkdir(mode=0o700)
        supplied = repository_root / "nested/.."
    elif alias_kind == "symlink":
        supplied = tmp_path / "linked-repository"
        supplied.symlink_to(repository_root, target_is_directory=True)
    else:
        supplied = _capture_root(repository_root)

    opened = False

    def fail_if_opened(path: Path) -> int:
        nonlocal opened
        opened = True
        raise AssertionError("capture root was accessed")

    monkeypatch.setattr(promotion_module, "_open_absolute_private_root", fail_if_opened)
    with pytest.raises(SafetyError, match="repository|canonical|alias|marker|symlink"):
        CaptureEvidenceReader(supplied, _effective_schema())
    assert not opened


def test_reader_rejects_noncanonical_or_symlinked_lock_path_before_capture_access(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    lexical_lock = _lock_for(repository_root)
    opened = False

    def fail_if_opened(path: Path) -> int:
        nonlocal opened
        opened = True
        raise AssertionError("capture root was accessed")

    monkeypatch.setattr(promotion_module, "_open_absolute_private_root", fail_if_opened)
    lexical_lock.acquire()
    lexical_lock.path = repository_root / ".state/../.state/live.lock"
    try:
        with pytest.raises(SafetyError, match="canonical.*lock"):
            CaptureEvidenceReader(
                repository_root,
                _effective_schema(),
                process_lock=lexical_lock,
            ).read_menu_pairs()
    finally:
        lexical_lock.release()
    assert not opened

    canonical_lock = _lock_for(repository_root)
    canonical_lock.acquire()
    state = repository_root / ".state"
    moved_state = repository_root / "moved-state"
    state.rename(moved_state)
    state.symlink_to(moved_state, target_is_directory=True)
    try:
        with pytest.raises(SafetyError, match="symlink|canonical"):
            CaptureEvidenceReader(
                repository_root,
                _effective_schema(),
                process_lock=canonical_lock,
            ).read_menu_pairs()
    finally:
        canonical_lock.release()
    assert not opened


def test_reader_rejects_symlinked_repository_marker_before_capture_access(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository_root = tmp_path / "repository"
    _complete_tree(repository_root)
    marker = repository_root / "pyproject.toml"
    moved_marker = repository_root / "real-pyproject.toml"
    marker.rename(moved_marker)
    marker.symlink_to(moved_marker)
    monkeypatch.setattr(
        promotion_module,
        "_open_absolute_private_root",
        lambda path: (_ for _ in ()).throw(AssertionError("capture root was accessed")),
    )

    with pytest.raises(SafetyError, match="marker|symlink"):
        CaptureEvidenceReader(repository_root, _effective_schema())


def test_reader_rejects_non_fixed_point_opaque_schema_string(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    response = _load(paths[2][1])
    response["body"]["privateName"] = "opaque customer value"
    _replace_json(paths[2][1], response)

    with pytest.raises(SafetyError, match="fixed.point|schema-aware|undeclared"):
        _read(root)


def test_reader_compares_metadata_with_type_strict_identity(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    request = _load(paths[2][0])
    response = _load(paths[2][1])
    request["metadata"]["duration"] = 1
    response["metadata"]["duration"] = 1.0
    _replace_json(paths[2][0], request)
    _replace_json(paths[2][1], response)

    with pytest.raises(SafetyError, match="metadata.*identical"):
        _read(root)


def test_reviewed_combo_exception_hashes_are_computed_from_canonical_fragments() -> None:
    schema = _effective_schema()
    components = schema["components"]["schemas"]
    combo = components["ExternalMenuComboItem"]
    item_union = components["ExternalMenuCategory3"]["properties"]["items"]["items"]

    assert hashlib.sha256(canonical_json_bytes(combo)).hexdigest() == (
        validation_module._REVIEWED_COMBO_SHA256
    )
    assert hashlib.sha256(canonical_json_bytes(item_union)).hexdigest() == (
        validation_module._REVIEWED_ITEM_UNION_SHA256
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown-keyword",
        "unknown-format",
        "format-type-mismatch",
        "enum-format-without-enum",
        "properties-on-string",
        "required-on-string",
        "additional-properties-on-string",
        "items-on-string",
        "array-items-missing",
        "array-items-null",
        "length-on-integer",
        "nullable-without-type-or-one-of",
        "one-of-with-type",
        "open-additional-properties",
        "ref-sibling",
        "external-ref",
        "broken-ref",
        "reference-cycle",
        "combo-fragment",
        "item-union-fragment",
        "sixth-undefined-required",
    ],
)
def test_concrete_validator_fails_closed_on_reviewed_schema_drift(
    tmp_path: Path, mutation: str
) -> None:
    _make_repository(tmp_path)
    schema = _effective_schema()
    components = schema["components"]["schemas"]
    if mutation == "unknown-keyword":
        components["ExternalMenuV2"]["properties"]["name"]["pattern"] = ".*"
    elif mutation == "unknown-format":
        components["ExternalMenuV2"]["properties"]["name"]["format"] = "email"
    elif mutation == "format-type-mismatch":
        components["ExternalMenuV2"]["properties"]["name"]["format"] = "int32"
    elif mutation == "enum-format-without-enum":
        components["ExternalMenuV2"]["properties"]["name"]["format"] = "enum"
    elif mutation == "properties-on-string":
        components["ExternalMenuV2"]["properties"]["name"]["properties"] = {}
    elif mutation == "required-on-string":
        components["ExternalMenuV2"]["properties"]["name"]["required"] = []
    elif mutation == "additional-properties-on-string":
        components["ExternalMenuV2"]["properties"]["name"]["additionalProperties"] = False
    elif mutation == "items-on-string":
        components["ExternalMenuV2"]["properties"]["name"]["items"] = {}
    elif mutation == "array-items-missing":
        components["ExternalMenuV2"]["properties"]["comboCategories"].pop("items")
    elif mutation == "array-items-null":
        components["ExternalMenuV2"]["properties"]["comboCategories"]["items"] = None
    elif mutation == "length-on-integer":
        components["ExternalMenuV2"]["properties"]["formatVersion"]["minLength"] = 0
    elif mutation == "nullable-without-type-or-one-of":
        components["ExternalMenuV2"]["properties"]["name"] = {"nullable": True}
    elif mutation == "one-of-with-type":
        components["ExternalMenuV2"]["properties"]["name"]["oneOf"] = [{"type": "string"}]
    elif mutation == "open-additional-properties":
        components["ExternalMenuV2"]["additionalProperties"] = True
    elif mutation == "ref-sibling":
        schema["paths"]["/api/2/menu/by_id"]["post"]["requestBody"]["content"]["application/json"][
            "schema"
        ]["description"] = "drift"
    elif mutation == "external-ref":
        schema["paths"]["/api/2/menu/by_id"]["post"]["requestBody"]["content"]["application/json"][
            "schema"
        ] = {"$ref": "https://example.invalid/schema.json"}
    elif mutation == "broken-ref":
        components["ExternalMenuV2"]["properties"]["missing"] = {
            "$ref": "#/components/schemas/Missing"
        }
    elif mutation == "reference-cycle":
        components["ExternalMenuV2"]["properties"]["cycle"] = {
            "$ref": "#/components/schemas/ExternalMenuV2"
        }
    elif mutation == "combo-fragment":
        components["ExternalMenuComboItem"]["properties"]["description"]["default"] = None
    elif mutation == "item-union-fragment":
        components["ExternalMenuCategory3"]["properties"]["items"]["items"]["oneOf"].reverse()
    else:
        components["ExternalMenuComboItem"]["required"].append("sixthUnknown")

    with pytest.raises(SafetyError, match="schema|reference|fragment|defect|drift"):
        CaptureEvidenceReader(tmp_path, schema)


def test_combo_required_exception_applies_only_to_exact_reviewed_component() -> None:
    validator = MenuEvidenceValidator(_effective_schema())
    inline_child_schema = {
        "type": "object",
        "required": ["orderItemType"],
        "properties": {"orderItemType": {"type": "string"}},
    }

    with pytest.raises(SafetyError, match="required"):
        validator._validate_instance(  # noqa: SLF001 - exact exception-scope regression
            {},
            inline_child_schema,
            path="synthetic-inline-child",
            component_name="ExternalMenuComboItem",
        )


def test_concrete_preflight_rejects_non_object_array_items_contract() -> None:
    validator = MenuEvidenceValidator(_effective_schema())

    with pytest.raises(SafetyError, match="items"):
        validator._preflight_schema(  # noqa: SLF001 - placement regression
            {"type": "array", "items": None},
            path="synthetic-array",
            component_name=None,
            visited=set(),
            active=set(),
            depth=0,
        )


@pytest.mark.parametrize(
    ("target", "invalid_value"),
    [
        ("request-uuid", "<redacted:string>"),
        ("response-int32", 2**31),
        ("response-int64", 2**63),
    ],
)
def test_concrete_validator_enforces_supported_format_semantics(
    tmp_path: Path,
    target: str,
    invalid_value: object,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    if target == "request-uuid":
        path = paths[2][0]
        envelope = _load(path)
        envelope["body"]["organizationIds"] = [invalid_value]
    else:
        path = paths[2][1]
        envelope = _load(path)
        property_name = "int32Value" if target == "response-int32" else "int64Value"
        envelope["body"][property_name] = invalid_value
    _replace_json(path, envelope)

    with pytest.raises(SafetyError, match="format|uuid|range"):
        _read(root)


def test_concrete_validator_type_mismatch_reports_only_the_safe_schema_path(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    request = _load(paths[2][0])
    response = _load(paths[2][1])
    secret_like_value = "Bearer synthetic-secret-value"
    response["body"]["comboCategories"] = secret_like_value

    with pytest.raises(SafetyError) as caught:
        MenuEvidenceValidator(_effective_schema()).validate(2, request, response)

    assert str(caught.value) == (
        "Evidence value at response-v2.comboCategories "
        "does not match its reviewed schema type"
    )
    assert secret_like_value not in str(caught.value)


@pytest.mark.parametrize(
    "value",
    [
        0,
        1.25,
        float.fromhex("0x1.fffffep+127"),
        -float.fromhex("0x1.fffffep+127"),
    ],
)
def test_float_format_accepts_finite_binary32_values(tmp_path: Path, value: float) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"]["floatValue"] = value
    _replace_json(response_path, response)

    assert tuple(_read(root)) == (2, 3, 4)


@pytest.mark.parametrize("value", [1e100, -1e100, 1e-100, -1e-100])
def test_float_format_rejects_binary32_out_of_range(tmp_path: Path, value: float) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"]["floatValue"] = value
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="float|range|format"):
        _read(root)


@pytest.mark.parametrize("shape", ["dish-shape-combo-literal", "combo-shape-dish-literal"])
def test_category3_item_union_does_not_guess_branch_from_raw_discriminator(
    tmp_path: Path,
    shape: str,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[4][1]
    response = _load(response_path)
    item: dict[str, Any]
    if shape == "dish-shape-combo-literal":
        item = {
            "allergenGroupIds": [],
            "id": "00000000-0000-4000-8000-000000000099",
            "itemSizes": [],
            "modifierSchemaId": None,
            "orderItemType": "Product",
            "splittable": False,
            "type": "COMBO",
        }
    else:
        item = response["body"]["itemGroups"][0]["items"][0]
        item["type"] = "DISH"
    response["body"]["itemGroups"][0]["items"] = [item]
    _replace_json(response_path, response)

    assert tuple(_read(root)) == (2, 3, 4)


@pytest.mark.parametrize("shape", ["redacted-type", "no-reviewed-branch"])
def test_category3_item_union_rejects_unsafe_literal_or_zero_structural_branches(
    tmp_path: Path,
    shape: str,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[4][1]
    response = _load(response_path)
    if shape == "redacted-type":
        item = response["body"]["itemGroups"][0]["items"][0]
        item["type"] = "<redacted:string>"
    else:
        item = {"type": "DISH"}
    response["body"]["itemGroups"][0]["items"] = [item]
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="discriminator|DISH|COMBO|required|branch"):
        _read(root)


def test_ordinary_schema_object_rejects_fixed_point_unknown_key(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"]["unknown"] = "<redacted:string>"
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="undeclared|additional|property"):
        _read(root)


@pytest.mark.parametrize(
    "sensitive_key",
    [
        "11111111-1111-4111-8111-111111111111",
        "aaaaaaaa-aaaa-0000-0000-aaaaaaaaaaaa",
    ],
)
def test_reader_generic_scan_rejects_uuid_like_object_key(
    tmp_path: Path,
    sensitive_key: str,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"][sensitive_key] = "<redacted:string>"
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="secret/PII") as caught:
        _read(root)
    assert sensitive_key not in str(caught.value)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("missing-root-required", "required"),
        ("wrong-root-type", "type"),
        ("enum-sentinel", "enum"),
        ("missing-combo-sizes", "required|branch"),
        ("missing-combo-id", "required|branch"),
        ("missing-combo-type", "discriminator|DISH|COMBO"),
    ],
)
def test_concrete_validator_enforces_selected_root_and_defined_combo_contract(
    tmp_path: Path,
    mutation: str,
    message: str,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    version = (
        2
        if mutation
        in {
            "missing-root-required",
            "wrong-root-type",
            "enum-sentinel",
        }
        else 4
    )
    response_path = paths[version][1]
    response = _load(response_path)
    body = response["body"]
    if mutation == "missing-root-required":
        del body["id"]
    elif mutation == "wrong-root-type":
        body["comboCategories"] = {}
    elif mutation == "enum-sentinel":
        body["mode"] = "<redacted:string>"
    else:
        combo = body["itemGroups"][0]["items"][0]
        del combo[mutation.removeprefix("missing-combo-")]
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match=message):
        _read(root)


def test_exact_five_undefined_combo_fields_are_optional_but_validated_if_present(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repository"
    paths = _complete_tree(root)
    response_path = paths[4][1]
    response = _load(response_path)
    combo = response["body"]["itemGroups"][0]["items"][0]
    combo.update(
        {
            "allergenGroupIds": [],
            "itemSizes": [],
            "modifierSchemaId": "<redacted:string>",
            "orderItemType": "<redacted:string>",
            "splittable": False,
        }
    )
    _replace_json(response_path, response)
    assert tuple(_read(root)) == (2, 3, 4)

    combo["sixthUnknown"] = "<redacted:string>"
    _replace_json(response_path, response)
    with pytest.raises(SafetyError, match="undefined property|reviewed schema branch"):
        _read(root)


def test_reader_has_no_injectable_validator_escape_hatch(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    _complete_tree(root)
    lock = _lock_for(root)

    with pytest.raises(TypeError, match="validator"):
        CaptureEvidenceReader(
            root,
            _effective_schema(),
            process_lock=lock,
            validator=lambda version, request, response: None,  # type: ignore[call-arg]
        )


def test_reader_rejects_non_none_validator_result(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repository"
    _complete_tree(root)
    monkeypatch.setattr(MenuEvidenceValidator, "validate", lambda *args, **kwargs: True)

    with pytest.raises(SafetyError, match="return exactly None"):
        _read(root)


def test_reader_rejects_and_closes_awaitable_validator_result_without_warning(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repository"
    _complete_tree(root)

    async def asynchronous_result() -> None:
        return None

    monkeypatch.setattr(
        MenuEvidenceValidator,
        "validate",
        lambda *args, **kwargs: asynchronous_result(),
    )
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with pytest.raises(SafetyError, match="synchronous"):
            _read(root)
        gc.collect()

    assert not [warning for warning in caught if "never awaited" in str(warning.message)]
