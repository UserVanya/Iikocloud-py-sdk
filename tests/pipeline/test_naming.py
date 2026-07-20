import copy
import keyword
from pathlib import Path
from typing import Any, cast

import pytest
import yaml
from reviewed_baseline import compose_current_reviewed_source

import tools.openapi_pipeline.naming as naming_module
from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.inventory import HTTP_METHODS
from tools.openapi_pipeline.naming import (
    build_model_mappings,
    inject_operation_ids,
    normalize_model_name,
)
from tools.openapi_pipeline.paths import RepoPaths

_CLR_GENERIC_SCHEMA = (
    "Namespace.RmsItemsResponseWrapper`1[[Namespace.Item, "
    "Assembly, Version=1.0.0.0, Culture=neutral]]"
)


def _normalize_generator_schema_names(
    document: dict[str, Any], overrides: dict[str, str]
) -> tuple[dict[str, Any], dict[str, str]]:
    normalizer = getattr(naming_module, "normalize_generator_schema_names", None)
    assert callable(normalizer), "generator-invalid schema normalizer is missing"
    return normalizer(document, overrides)


def _all_refs(value: Any) -> list[str]:
    refs: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                refs.append(child)
            refs.extend(_all_refs(child))
    elif isinstance(value, list):
        for child in value:
            refs.extend(_all_refs(child))
    return refs


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
    assert result["paths"]["/api/1/organizations"]["post"]["operationId"] == "get_organizations"


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
    assert build_model_mappings({"Namespace.---": {}}, {"Namespace.---": "DashPlaceholder"}) == {
        "Namespace.---": "DashPlaceholder"
    }


@pytest.mark.parametrize(
    "raw",
    ["Namespace.None", "Namespace.True", "Namespace.False"],
)
def test_auto_normalized_python_keywords_require_explicit_override(raw: str) -> None:
    with pytest.raises(ValidationError, match="add an explicit override"):
        build_model_mappings({raw: {}}, {})


def test_explicit_override_can_replace_an_auto_normalized_python_keyword() -> None:
    assert build_model_mappings({"Namespace.None": {}}, {"Namespace.None": "NoneValue"}) == {
        "Namespace.None": "NoneValue"
    }


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


def test_generator_invalid_schema_key_is_physically_renamed_with_exact_refs() -> None:
    old_ref = f"#/components/schemas/{_CLR_GENERIC_SCHEMA}"
    document = {
        "openapi": "3.0.3",
        "paths": {
            "/items": {
                "get": {
                    "responses": {
                        "200": {"content": {"application/json": {"schema": {"$ref": old_ref}}}}
                    }
                }
            }
        },
        "components": {
            "schemas": {
                _CLR_GENERIC_SCHEMA: {
                    "type": "object",
                    "properties": {"next": {"$ref": old_ref}},
                },
                "Envelope": {
                    "type": "object",
                    "properties": {"payload": {"$ref": old_ref}},
                    "description": f"unrelated substring {old_ref} stays",
                },
                "Namespace.Valid": {"type": "object"},
            }
        },
        "x-unrelated": old_ref,
    }
    overrides = {
        _CLR_GENERIC_SCHEMA: "RmsItemResponse",
        "Namespace.Valid": "DomainValid",
    }
    original_document = copy.deepcopy(document)
    original_overrides = overrides.copy()

    corrected, mappings = _normalize_generator_schema_names(document, overrides)
    repeated, repeated_mappings = _normalize_generator_schema_names(document, overrides)

    schemas = corrected["components"]["schemas"]
    assert list(schemas) == sorted(schemas)
    assert _CLR_GENERIC_SCHEMA not in schemas
    assert "RmsItemResponse" in schemas
    assert "Namespace.Valid" in schemas
    assert "DomainValid" not in schemas
    assert _all_refs(corrected).count("#/components/schemas/RmsItemResponse") == 3
    assert old_ref not in _all_refs(corrected)
    assert corrected["x-unrelated"] == old_ref
    assert schemas["Envelope"]["description"] == f"unrelated substring {old_ref} stays"
    assert mappings == {
        "Envelope": "Envelope",
        "Namespace.Valid": "DomainValid",
        "RmsItemResponse": "RmsItemResponse",
    }
    assert corrected == repeated
    assert mappings == repeated_mappings
    assert document == original_document
    assert overrides == original_overrides


def test_generator_invalid_schema_ref_rewrite_is_rfc6901_safe() -> None:
    raw = "Namespace/Bad~Name"
    old_ref = "#/components/schemas/Namespace~1Bad~0Name"
    document = {
        "components": {
            "schemas": {
                raw: {"type": "object"},
                "Holder": {"properties": {"item": {"$ref": old_ref}}},
            }
        }
    }

    corrected, mappings = _normalize_generator_schema_names(document, {raw: "SafeName"})

    assert _all_refs(corrected) == ["#/components/schemas/SafeName"]
    assert mappings == {"Holder": "Holder", "SafeName": "SafeName"}


def test_schema_ref_rewrite_requires_a_literal_local_fragment_marker() -> None:
    old_ref = f"#/components/schemas/{_CLR_GENERIC_SCHEMA}"
    encoded_fragment = old_ref.replace("#", "%23", 1)
    external_ref = f"https://example.invalid/openapi.json{old_ref}"
    relative_ref = f"other.json{old_ref}"
    document = {
        "components": {
            "schemas": {
                _CLR_GENERIC_SCHEMA: {"type": "object"},
                "Holder": {
                    "properties": {
                        "local": {"$ref": old_ref},
                        "encoded": {"$ref": encoded_fragment},
                        "external": {"$ref": external_ref},
                        "relative": {"$ref": relative_ref},
                    }
                },
            }
        }
    }

    corrected, _mappings = _normalize_generator_schema_names(
        document, {_CLR_GENERIC_SCHEMA: "SafeResponse"}
    )

    properties = corrected["components"]["schemas"]["Holder"]["properties"]
    assert properties["local"]["$ref"] == "#/components/schemas/SafeResponse"
    assert properties["encoded"]["$ref"] == encoded_fragment
    assert properties["external"]["$ref"] == external_ref
    assert properties["relative"]["$ref"] == relative_ref


def test_schema_ref_rewrite_skips_literal_data_but_keeps_semantic_map_keys() -> None:
    old_ref = f"#/components/schemas/{_CLR_GENERIC_SCHEMA}"
    literal_ref = {"$ref": old_ref}
    document = {
        "openapi": "3.0.3",
        "paths": {
            "/items": {
                "get": {
                    "responses": {
                        "default": {"content": {"application/json": {"schema": {"$ref": old_ref}}}}
                    }
                }
            }
        },
        "components": {
            "schemas": {
                _CLR_GENERIC_SCHEMA: {"type": "object"},
                "Payload": {
                    "type": "object",
                    "properties": {"example": {"$ref": old_ref}},
                    "example": copy.deepcopy(literal_ref),
                    "default": copy.deepcopy(literal_ref),
                    "enum": [copy.deepcopy(literal_ref)],
                    "const": copy.deepcopy(literal_ref),
                    "x-literal": copy.deepcopy(literal_ref),
                },
            }
        },
        "x-root-literal": copy.deepcopy(literal_ref),
    }
    original = copy.deepcopy(document)

    corrected, _mappings = _normalize_generator_schema_names(
        document, {_CLR_GENERIC_SCHEMA: "SafeResponse"}
    )

    payload = corrected["components"]["schemas"]["Payload"]
    assert payload["properties"]["example"]["$ref"] == ("#/components/schemas/SafeResponse")
    assert (
        corrected["paths"]["/items"]["get"]["responses"]["default"]["content"]["application/json"][
            "schema"
        ]["$ref"]
        == "#/components/schemas/SafeResponse"
    )
    assert payload["example"] == literal_ref
    assert payload["default"] == literal_ref
    assert payload["enum"] == [literal_ref]
    assert payload["const"] == literal_ref
    assert payload["x-literal"] == literal_ref
    assert corrected["x-root-literal"] == literal_ref
    assert document == original


def test_generator_invalid_schema_requires_explicit_reviewed_override() -> None:
    document = {"components": {"schemas": {_CLR_GENERIC_SCHEMA: {}}}}

    with pytest.raises(ValidationError, match="explicit reviewed model-name override"):
        _normalize_generator_schema_names(document, {})


@pytest.mark.parametrize("target", ["Bad Target", "bad-target", "class"])
def test_generator_invalid_schema_rejects_invalid_physical_target(target: str) -> None:
    document = {"components": {"schemas": {_CLR_GENERIC_SCHEMA: {}}}}

    with pytest.raises(ValidationError, match="physical schema target"):
        _normalize_generator_schema_names(document, {_CLR_GENERIC_SCHEMA: target})


def test_generator_invalid_schema_rejects_target_collision_with_untouched_key() -> None:
    document = {"components": {"schemas": {_CLR_GENERIC_SCHEMA: {}, "ExistingSchema": {}}}}

    with pytest.raises(ValidationError, match="physical schema target collision"):
        _normalize_generator_schema_names(document, {_CLR_GENERIC_SCHEMA: "ExistingSchema"})


def test_generator_invalid_schemas_reject_duplicate_physical_targets() -> None:
    other_invalid = "Namespace.Other`1[[Namespace.Item, Assembly]]"
    document = {"components": {"schemas": {_CLR_GENERIC_SCHEMA: {}, other_invalid: {}}}}

    with pytest.raises(ValidationError, match="duplicate physical schema target"):
        _normalize_generator_schema_names(
            document,
            {
                _CLR_GENERIC_SCHEMA: "SharedResponse",
                other_invalid: "SharedResponse",
            },
        )


def test_normalized_names_are_valid_python_identifiers() -> None:
    for raw in ("Namespace.Model", "Namespace.alpha-item`2", "Namespace.2fa-token"):
        name = normalize_model_name(raw)
        assert name.isascii()
        assert name.isidentifier()
        assert not keyword.iskeyword(name)


def test_registry_files_have_populated_canonical_shapes_and_cover_current_source() -> None:
    operation_ids = Path("openapi/operation-ids.yaml")
    model_overrides = Path("openapi/model-name-overrides.yaml")

    operations_value = yaml.safe_load(operation_ids.read_text(encoding="utf-8"))
    models_value = yaml.safe_load(model_overrides.read_text(encoding="utf-8"))
    assert isinstance(operations_value, dict) and set(operations_value) == {"operations"}
    assert isinstance(models_value, dict) and set(models_value) == {"models"}
    operations = operations_value["operations"]
    models = models_value["models"]
    assert isinstance(operations, dict) and operations
    assert isinstance(models, dict) and models
    assert all(
        isinstance(key, str)
        and key
        and isinstance(value, str)
        and value.isidentifier()
        and not keyword.iskeyword(value)
        for key, value in operations.items()
    )
    assert all(
        isinstance(key, str)
        and key
        and isinstance(value, str)
        and value.isidentifier()
        and not keyword.iskeyword(value)
        for key, value in models.items()
    )
    assert len(set(operations.values())) == len(operations)
    assert len(set(models.values())) == len(models)

    effective, mappings = compose_current_reviewed_source(RepoPaths.discover())
    paths = effective["paths"]
    assert isinstance(paths, dict)
    current_operations = {
        f"{method.upper()} {path}"
        for path, path_item in paths.items()
        if isinstance(path, str) and isinstance(path_item, dict)
        for method in path_item
        if method.lower() in HTTP_METHODS
    }
    assert set(operations) == current_operations
    schemas = effective["components"]
    assert isinstance(schemas, dict)
    schema_values = schemas["schemas"]
    assert isinstance(schema_values, dict)
    assert set(mappings) == set(schema_values)
    assert len(set(mappings.values())) == len(mappings)
