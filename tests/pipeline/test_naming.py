import copy
import keyword
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.naming import (
    build_model_mappings,
    inject_operation_ids,
    normalize_model_name,
)


def test_operation_registry_is_total_and_stable() -> None:
    document = {
        "paths": {
            "/api/1/access_token": {"post": {"responses": {}}},
            "/api/1/organizations": {"post": {"responses": {}}},
        }
    }
    registry = {
        "POST /api/1/access_token": "authenticate",
        "POST /api/1/organizations": "get_organizations",
    }

    result = inject_operation_ids(document, registry)

    assert result["paths"]["/api/1/access_token"]["post"]["operationId"] == "authenticate"
    assert (
        result["paths"]["/api/1/organizations"]["post"]["operationId"]
        == "get_organizations"
    )


def test_missing_operation_registry_entry_fails() -> None:
    document = {"paths": {"/api/1/new": {"post": {"responses": {}}}}}

    with pytest.raises(ValidationError, match="POST /api/1/new"):
        inject_operation_ids(document, {})


def test_operation_injection_ignores_path_metadata_and_does_not_mutate_inputs() -> None:
    document = {
        "paths": {
            "/api/1/z": {
                "parameters": [{"name": "organizationId"}],
                "summary": "Path metadata",
                "post": {"operationId": "unstable_upstream_name", "responses": {}},
            }
        }
    }
    registry = {"POST /api/1/z": "get_z"}
    original_document = copy.deepcopy(document)
    original_registry = registry.copy()

    result = inject_operation_ids(document, registry)

    assert result["paths"]["/api/1/z"]["post"]["operationId"] == "get_z"
    assert result["paths"]["/api/1/z"]["parameters"] == [{"name": "organizationId"}]
    assert result["paths"]["/api/1/z"]["summary"] == "Path metadata"
    assert document == original_document
    assert registry == original_registry


def test_stale_operation_registry_entry_fails() -> None:
    document = {"paths": {"/api/1/current": {"get": {"responses": {}}}}}
    registry = {
        "GET /api/1/current": "get_current",
        "POST /api/1/removed": "removed_operation",
    }

    with pytest.raises(ValidationError, match="POST /api/1/removed"):
        inject_operation_ids(document, registry)


def test_duplicate_operation_ids_fail() -> None:
    document = {
        "paths": {
            "/api/1/z": {"post": {"responses": {}}},
            "/api/1/a": {"get": {"responses": {}}},
        }
    }
    registry = {
        "POST /api/1/z": "duplicate_name",
        "GET /api/1/a": "duplicate_name",
    }

    with pytest.raises(ValidationError, match="Duplicate operationId duplicate_name"):
        inject_operation_ids(document, registry)


@pytest.mark.parametrize(
    "operation_id",
    [None, "", " ", "not-valid", "2invalid", "class", 7],
)
def test_invalid_operation_id_fails(operation_id: Any) -> None:
    document = {"paths": {"/api/1/current": {"get": {"responses": {}}}}}
    registry = cast(dict[str, str], {"GET /api/1/current": operation_id})

    with pytest.raises(ValidationError, match="Invalid operationId"):
        inject_operation_ids(document, registry)


def test_normalized_model_collision_requires_override() -> None:
    schemas = {
        "Namespace.One.Item": {},
        "Namespace.Two.Item": {},
    }

    with pytest.raises(ValidationError, match="Item"):
        build_model_mappings(schemas, {})

    assert build_model_mappings(schemas, {"Namespace.Two.Item": "SecondItem"}) == {
        "Namespace.One.Item": "Item",
        "Namespace.Two.Item": "SecondItem",
    }


def test_model_mapping_is_sorted_normalized_and_does_not_mutate_inputs() -> None:
    schemas = {
        "Namespace.Zed": {"type": "object"},
        "Namespace.alpha-item`2": {"type": "object"},
        "Namespace.2fa-token": {"type": "object"},
    }
    overrides = {"Namespace.Zed": "ZedOverride"}
    original_schemas = copy.deepcopy(schemas)
    original_overrides = overrides.copy()

    result = build_model_mappings(schemas, overrides)

    assert list(result) == sorted(schemas)
    assert result == {
        "Namespace.2fa-token": "Model2faToken",
        "Namespace.Zed": "ZedOverride",
        "Namespace.alpha-item`2": "AlphaItem",
    }
    assert schemas == original_schemas
    assert overrides == original_overrides


def test_explicit_override_can_name_an_otherwise_unnormalizable_schema() -> None:
    assert build_model_mappings(
        {"Namespace.---": {}}, {"Namespace.---": "DashPlaceholder"}
    ) == {"Namespace.---": "DashPlaceholder"}


def test_stale_model_overrides_fail_in_sorted_order() -> None:
    with pytest.raises(
        ValidationError,
        match="Stale model name overrides: Namespace.A, Namespace.Z",
    ):
        build_model_mappings({}, {"Namespace.Z": "Zed", "Namespace.A": "Alpha"})


@pytest.mark.parametrize(
    "model_name",
    [None, "", " ", "not-valid", "2Invalid", "class", 7],
)
def test_invalid_model_override_fails(model_name: Any) -> None:
    overrides = cast(dict[str, str], {"Namespace.Raw": model_name})

    with pytest.raises(ValidationError, match="Invalid model name override"):
        build_model_mappings({"Namespace.Raw": {}}, overrides)


def test_duplicate_override_targets_fail_deterministically() -> None:
    schemas = {"Namespace.Zed": {}, "Namespace.Alpha": {}}
    overrides = {
        "Namespace.Zed": "SharedModel",
        "Namespace.Alpha": "SharedModel",
    }

    with pytest.raises(
        ValidationError,
        match="SharedModel: Namespace.Alpha, Namespace.Zed",
    ):
        build_model_mappings(schemas, overrides)


def test_normalized_names_are_valid_python_identifiers() -> None:
    for raw in ("Namespace.Model", "Namespace.alpha-item`2", "Namespace.2fa-token"):
        name = normalize_model_name(raw)
        assert name.isascii()
        assert name.isidentifier()
        assert not keyword.iskeyword(name)


def test_registry_files_have_stable_empty_bootstrap_shapes() -> None:
    operation_ids = Path("openapi/operation-ids.yaml")
    model_overrides = Path("openapi/model-name-overrides.yaml")

    assert operation_ids.read_text(encoding="utf-8") == "operations: {}\n"
    assert model_overrides.read_text(encoding="utf-8") == "models: {}\n"
    assert yaml.safe_load(operation_ids.read_text(encoding="utf-8")) == {"operations": {}}
    assert yaml.safe_load(model_overrides.read_text(encoding="utf-8")) == {"models": {}}
