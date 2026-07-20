from __future__ import annotations

import copy
from functools import lru_cache
from typing import Any

import pytest

import tools.openapi_pipeline.evidence_schema_repairs as repair_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_schema_repairs import (
    build_reviewed_external_menu_validation_schema,
)
from tools.openapi_pipeline.evidence_validation import MenuEvidenceValidator
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_reviewed_evidence_base_candidate


@lru_cache(maxsize=1)
def _public_schema() -> dict[str, Any]:
    schema, _mappings = compose_reviewed_evidence_base_candidate(RepoPaths.discover())
    return schema


def _schema() -> dict[str, Any]:
    return copy.deepcopy(_public_schema())


def _property(schema: dict[str, Any], component: str, name: str) -> dict[str, Any]:
    return schema["components"]["schemas"][component]["properties"][name]


def _minimal_schema_value(schema: dict[str, Any], node: dict[str, Any]) -> Any:
    reference = node.get("$ref")
    if isinstance(reference, str):
        name = reference.removeprefix("#/components/schemas/")
        return _minimal_schema_value(schema, schema["components"]["schemas"][name])
    enum = node.get("enum")
    if isinstance(enum, list) and enum:
        return copy.deepcopy(enum[0])
    if node.get("nullable") is True:
        return None
    node_type = node.get("type")
    if node_type == "object":
        properties = node.get("properties", {})
        return {
            name: _minimal_schema_value(schema, properties[name])
            for name in node.get("required", [])
        }
    if node_type == "array":
        return []
    if node_type == "boolean":
        return False
    if node_type == "integer":
        return 0
    if node_type == "number":
        return 0.0
    return "00000000-0000-4000-8000-000000000000"


def test_registry_builds_complete_corrected_view_without_mutating_caller() -> None:
    schema = _schema()
    before = canonical_json_bytes(schema)

    corrected = build_reviewed_external_menu_validation_schema(schema)

    assert canonical_json_bytes(schema) == before
    assert corrected is not schema
    assert _property(corrected, "ExternalMenuItem", "taxCategory") == {
        "description": "Tax category",
        "nullable": True,
        "oneOf": [{"$ref": "#/components/schemas/TaxCategoryDto3"}],
    }
    assert _property(corrected, "ExternalMenuItemSize", "nutritionPerHundredGrams") == {
        "$ref": "#/components/schemas/NutritionInfoDto"
    }
    for component, target in (
        ("ExternalMenuV3", "OverrideTaxesDto"),
        ("ExternalMenuV4", "OverrideTaxesDto2"),
    ):
        assert _property(corrected, component, "overrideTaxCategories") == {
            "additionalProperties": {
                "items": {"$ref": f"#/components/schemas/{target}"},
                "type": "array",
            },
            "description": "Tax benefits",
            "type": "object",
        }
    for component, name in (
        ("ExternalMenuItem", "modifierSchemaId"),
        ("ExternalMenuItem2", "modifierSchemaId"),
        ("ExternalMenuItem3", "modifierSchemaId"),
        ("ExternalMenuItemSize", "sizeId"),
        ("ExternalMenuItemSize2", "id"),
        ("ExternalMenuItemSize3", "id"),
        ("ExternalMenuPriceByDepartmentsDto", "price"),
        ("ExternalMenuPriceByDepartmentsDto2", "price"),
        ("ExternalMenuPriceByDepartmentsDto3", "price"),
    ):
        assert _property(corrected, component, name)["nullable"] is True
    assert _property(
        corrected,
        "ExternalMenuPriceByDepartmentsDto",
        "organizationId",
    ) == {"format": "uuid", "type": "string"}

    already_correct = build_reviewed_external_menu_validation_schema(corrected)
    assert canonical_json_bytes(already_correct) == canonical_json_bytes(corrected)


def test_registry_rejects_stale_third_shape_with_only_static_schema_path() -> None:
    schema = _schema()
    marker = "captured-sensitive-marker"
    _property(schema, "ExternalMenuItem", "taxCategory")[marker] = marker

    with pytest.raises(SafetyError) as caught:
        build_reviewed_external_menu_validation_schema(schema)

    message = str(caught.value)
    assert message == (
        "Reviewed evidence schema repair drifted at "
        "components.schemas.ExternalMenuItem.properties.taxCategory"
    )
    assert marker not in message
    assert marker not in repr(caught.value)


def test_corrected_additional_properties_map_is_preflighted_and_validated() -> None:
    validator = MenuEvidenceValidator(_schema())
    map_schema = validator._component("ExternalMenuV3")["properties"][  # noqa: SLF001
        "overrideTaxCategories"
    ]
    item = validator._component("OverrideTaxesDto")  # noqa: SLF001
    value = _minimal_schema_value(validator._schema, item)  # noqa: SLF001

    validator._validate_instance(  # noqa: SLF001
        {"00000000-0000-4000-8000-000000000001": [value]},
        map_schema,
        path="components.schemas.ExternalMenuV3.properties.overrideTaxCategories",
        component_name="ExternalMenuV3",
    )
    with pytest.raises(SafetyError, match="reviewed schema type") as caught:
        validator._validate_instance(  # noqa: SLF001
            {"00000000-0000-4000-8000-000000000001": [None]},
            map_schema,
            path="components.schemas.ExternalMenuV3.properties.overrideTaxCategories",
            component_name="ExternalMenuV3",
        )
    assert "00000000-0000-4000-8000-000000000001" not in str(caught.value)


def test_barcode_null_only_exception_is_exact_and_component_scoped() -> None:
    reviewed_hash = repair_module.REVIEWED_NULL_ONLY_PROPERTY_EXCEPTIONS[
        0
    ].property_name_sha256

    assert repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto",
        property_name_sha256=reviewed_hash,
        value=None,
    )
    assert not repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto",
        property_name_sha256=reviewed_hash,
        value="non-null",
    )
    assert not repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto2",
        property_name_sha256=reviewed_hash,
        value=None,
    )
    assert not repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto",
        property_name_sha256="0" * 64,
        value=None,
    )
