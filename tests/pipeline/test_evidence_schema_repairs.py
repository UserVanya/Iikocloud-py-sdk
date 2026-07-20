from __future__ import annotations

import copy
from functools import lru_cache
from typing import Any

import pytest
from reviewed_baseline import compose_current_evidence_base

import tools.openapi_pipeline.evidence_schema_repairs as repair_module
from tools.openapi_pipeline.capture import ARRAY_ITEM, Sanitizer
from tools.openapi_pipeline.errors import SafetyError, StaleOverlayError
from tools.openapi_pipeline.evidence import build_versioned_evidence_redaction_hints
from tools.openapi_pipeline.evidence_schema_repairs import (
    build_reviewed_external_menu_validation_schema,
)
from tools.openapi_pipeline.evidence_validation import MenuEvidenceValidator
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.overlay import apply_overlay
from tools.openapi_pipeline.paths import RepoPaths


@lru_cache(maxsize=1)
def _public_schema() -> dict[str, Any]:
    schema, _mappings = compose_current_evidence_base(RepoPaths.discover())
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
    for component in ("ExternalMenuItem", "ExternalMenuItem2", "ExternalMenuItem3"):
        assert _property(corrected, component, "type")["enum"] == [
            "DISH",
            "COMBO",
            "SERVICE",
        ]
    assert _property(
        corrected,
        "ExternalMenuPriceByDepartmentsDto",
        "organizationId",
    ) == {"format": "uuid", "type": "string"}

    already_correct = build_reviewed_external_menu_validation_schema(corrected)
    assert canonical_json_bytes(already_correct) == canonical_json_bytes(corrected)


@pytest.mark.parametrize(
    ("version", "groups_name"),
    ((2, "itemCategories"), (3, "itemGroups"), (4, "itemGroups")),
)
def test_corrected_hints_preserve_historical_public_service_literal(
    version: int,
    groups_name: str,
) -> None:
    hints = build_versioned_evidence_redaction_hints(
        _schema(),
        "get_external_menu_by_id",
        version,
    )

    response_values = hints.response_values_for_status(200)
    assert response_values[(groups_name, ARRAY_ITEM, "items", ARRAY_ITEM, "type")] == frozenset(
        {"DISH", "COMBO", "SERVICE"}
    )
    sanitized = Sanitizer().sanitize(
        {
            groups_name: [
                {
                    "items": [
                        {"type": "SERVICE"},
                        {"type": "FUTURE_PUBLIC_ITEM_TYPE"},
                    ]
                }
            ]
        },
        path_values=response_values,
    )
    assert sanitized[groups_name][0]["items"] == [
        {"type": "SERVICE"},
        {"type": "<redacted:string>"},
    ]


def test_redacted_string_marker_is_rejected_for_all_reviewed_item_type_enums() -> None:
    validator = MenuEvidenceValidator(_schema())

    for component in ("ExternalMenuItem", "ExternalMenuItem2", "ExternalMenuItem3"):
        type_schema = validator._component(component)["properties"]["type"]  # noqa: SLF001
        for marker in ("<redacted:string>", "<redacted:other>"):
            with pytest.raises(SafetyError, match="reviewed schema enum"):
                validator._validate_instance(  # noqa: SLF001
                    marker,
                    type_schema,
                    path=f"components.schemas.{component}.properties.type",
                    schema_path=f"components.schemas.{component}.properties.type",
                    component_name=component,
                )


@pytest.mark.parametrize(
    "builder_name",
    [
        "build_reviewed_external_menu_validation_schema",
        "build_reviewed_external_menu_overlay_repairs",
    ],
)
@pytest.mark.parametrize("mutation", ["delete", "rename"])
def test_full_schema_entrypoints_require_every_reviewed_target(
    builder_name: str,
    mutation: str,
) -> None:
    schema = _schema()
    schemas = schema["components"]["schemas"]
    component = "ExternalMenuModifierItem3"
    if mutation == "delete":
        del schemas[component]
    else:
        schemas[f"Renamed{component}"] = schemas.pop(component)

    builder = getattr(repair_module, builder_name)
    with pytest.raises(
        SafetyError,
        match=(
            r"^Reviewed evidence schema repair drifted at components\.schemas\."
            r"ExternalMenuModifierItem3\.properties\.restrictions$"
        ),
    ):
        builder(schema)


def test_dynamic_map_approval_is_bound_to_its_exact_reviewed_property_path() -> None:
    schema = _schema()
    corrected = build_reviewed_external_menu_validation_schema(schema)
    copied_map = copy.deepcopy(_property(corrected, "ExternalMenuV3", "overrideTaxCategories"))
    schema["components"]["schemas"]["ExternalMenuV2"]["properties"]["unrelatedDynamicMap"] = (
        copied_map
    )

    with pytest.raises(SafetyError, match="additionalProperties contract"):
        MenuEvidenceValidator(schema)

    validator = MenuEvidenceValidator(_schema())
    with pytest.raises(SafetyError, match="undeclared property"):
        validator._validate_instance(  # noqa: SLF001 - runtime path binding regression
            {"00000000-0000-4000-8000-000000000001": []},
            copied_map,
            path="response-v2.unrelatedDynamicMap",
            schema_path="components.schemas.ExternalMenuV2.properties.unrelatedDynamicMap",
            component_name="ExternalMenuV2",
        )


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
        schema_path="components.schemas.ExternalMenuV3.properties.overrideTaxCategories",
        component_name="ExternalMenuV3",
    )
    with pytest.raises(SafetyError, match="reviewed schema type") as caught:
        validator._validate_instance(  # noqa: SLF001
            {"00000000-0000-4000-8000-000000000001": [None]},
            map_schema,
            path="components.schemas.ExternalMenuV3.properties.overrideTaxCategories",
            schema_path="components.schemas.ExternalMenuV3.properties.overrideTaxCategories",
            component_name="ExternalMenuV3",
        )
    assert "00000000-0000-4000-8000-000000000001" not in str(caught.value)


def test_barcode_null_only_exception_is_exact_and_component_scoped() -> None:
    reviewed_hash = repair_module.REVIEWED_NULL_ONLY_PROPERTY_EXCEPTIONS[0].property_name_sha256

    assert {
        exception.component_name
        for exception in repair_module.REVIEWED_NULL_ONLY_PROPERTY_EXCEPTIONS
    } == {"BarcodeDto", "BarcodeDto2", "BarcodeDto3"}
    for component in ("BarcodeDto", "BarcodeDto2", "BarcodeDto3"):
        assert repair_module.is_reviewed_null_only_property_hash(
            component_name=component,
            property_name_sha256=reviewed_hash,
            value=None,
        )
        assert not repair_module.is_reviewed_null_only_property_hash(
            component_name=component,
            property_name_sha256=reviewed_hash,
            value="non-null",
        )
    assert not repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto4",
        property_name_sha256=reviewed_hash,
        value=None,
    )
    assert not repair_module.is_reviewed_null_only_property_hash(
        component_name="BarcodeDto",
        property_name_sha256="0" * 64,
        value=None,
    )


def test_registry_emits_guarded_reproducible_overlay_actions() -> None:
    builder = getattr(
        repair_module,
        "build_reviewed_external_menu_overlay_repairs",
        None,
    )
    assert callable(builder)
    schema = _schema()

    corrected, actions = builder(schema)

    assert actions
    assert all(action["x-iiko-sdk-guard"]["expected-matches"] == 1 for action in actions)
    overlay = {
        "overlay": "1.1.0",
        "info": {"title": "reviewed repairs", "version": "1.0.0"},
        "actions": copy.deepcopy(list(actions)),
    }
    assert apply_overlay(schema, overlay) == corrected
    assert corrected == build_reviewed_external_menu_validation_schema(schema)

    already_correct, no_op_actions = builder(corrected)
    assert already_correct == corrected
    assert no_op_actions == ()
    with pytest.raises(StaleOverlayError):
        apply_overlay(corrected, overlay)
