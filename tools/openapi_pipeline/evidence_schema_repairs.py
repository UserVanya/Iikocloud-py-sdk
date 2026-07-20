from __future__ import annotations

import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, TypeAlias

from .errors import SafetyError
from .io import canonical_json_bytes, sha256_bytes

FrozenJson: TypeAlias = (
    None | bool | int | float | str | tuple["FrozenJson", ...] | Mapping[str, "FrozenJson"]
)


@dataclass(frozen=True)
class ReviewedSchemaPropertyRepair:
    path: tuple[str, ...]
    broken_sha256: str
    corrected: Mapping[str, FrozenJson]


@dataclass(frozen=True)
class ReviewedMissingPropertyRepair:
    parent_path: tuple[str, ...]
    property_name: str
    broken_parent_sha256: str
    corrected: Mapping[str, FrozenJson]


@dataclass(frozen=True)
class ReviewedNullOnlyPropertyException:
    component_name: str
    property_name_sha256: str


def _freeze(value: Any) -> FrozenJson:
    if type(value) is dict:
        return MappingProxyType({key: _freeze(child) for key, child in value.items()})
    if type(value) is list:
        return tuple(_freeze(child) for child in value)
    if value is None or type(value) in {bool, int, float, str}:
        return value
    raise TypeError("reviewed schema repair value must be strict JSON")


def _frozen_mapping(value: dict[str, Any]) -> Mapping[str, FrozenJson]:
    frozen = _freeze(value)
    assert isinstance(frozen, Mapping)
    return frozen


def _property_repair(
    component: str,
    property_name: str,
    broken_sha256: str,
    corrected: dict[str, Any],
) -> ReviewedSchemaPropertyRepair:
    return ReviewedSchemaPropertyRepair(
        path=("components", "schemas", component, "properties", property_name),
        broken_sha256=broken_sha256,
        corrected=_frozen_mapping(corrected),
    )


REVIEWED_EXTERNAL_MENU_SCHEMA_REPAIRS: tuple[ReviewedSchemaPropertyRepair, ...] = (
    _property_repair(
        "ExternalMenuItem",
        "taxCategory",
        "a6c2ed498922acf7895d82d00d0c654959036c5dbd510d224180b01b5b154d84",
        {
            "description": "Tax category",
            "nullable": True,
            "oneOf": [{"$ref": "#/components/schemas/TaxCategoryDto3"}],
        },
    ),
    _property_repair(
        "ExternalMenuItemSize",
        "nutritionPerHundredGrams",
        "127599eab41f8f9cea4db687decc923f253a8901f25531564bcb2d489b50e71c",
        {"$ref": "#/components/schemas/NutritionInfoDto"},
    ),
    _property_repair(
        "ExternalMenuModifierItem",
        "nutritionPerHundredGrams",
        "cb491b6a629f6f615828841d17dc5dc8a00a888c0a3e4f4964424ce16f8e1032",
        {
            "description": "Nutrition per 100 g of modifier product",
            "nullable": True,
            "oneOf": [{"$ref": "#/components/schemas/NutritionInfoDto5"}],
        },
    ),
    _property_repair(
        "ExternalMenuModifierItem",
        "restrictions",
        "c22456d2dfe9478b27bd928468f8583642285cace822981365aaf73ddc29a4f5",
        {
            "nullable": True,
            "oneOf": [{"$ref": "#/components/schemas/ModifierRestrictionsDto5"}],
        },
    ),
    _property_repair(
        "ExternalMenuModifierItem2",
        "restrictions",
        "4ebef800bca89546db3b0a0ba07706c1909098df9310e6bc73f4b2c5b41c5a08",
        {
            "nullable": True,
            "oneOf": [{"$ref": "#/components/schemas/ModifierRestrictionsDto6"}],
        },
    ),
    _property_repair(
        "ExternalMenuModifierItem3",
        "restrictions",
        "901b2af4e7a66c3c15a6f1c4ccf397ff16bfa29314142385fcb9f8a0e21783c8",
        {
            "nullable": True,
            "oneOf": [{"$ref": "#/components/schemas/ModifierRestrictionsDto7"}],
        },
    ),
    _property_repair(
        "ExternalMenuV3",
        "overrideTaxCategories",
        "157d6ffeb89717a5ff9f6509bd9611c10998c06125dda0aa3d07ab0288a305b5",
        {
            "additionalProperties": {
                "items": {"$ref": "#/components/schemas/OverrideTaxesDto"},
                "type": "array",
            },
            "description": "Tax benefits",
            "type": "object",
        },
    ),
    _property_repair(
        "ExternalMenuV4",
        "overrideTaxCategories",
        "7dead4771c3fbade7c4ffac116217a1c407769872b9fc351197f691cb2379154",
        {
            "additionalProperties": {
                "items": {"$ref": "#/components/schemas/OverrideTaxesDto2"},
                "type": "array",
            },
            "description": "Tax benefits",
            "type": "object",
        },
    ),
    *(
        _property_repair(
            component,
            "modifierSchemaId",
            "8deb1e4116cacb97c6cc9a82e3c39fd9cdf7ff2a06c1827f1e055837d1c16741",
            {
                "description": "Modifier schema ID",
                "example": "00000000-0000-0000-0000-000000000000",
                "nullable": True,
                "type": "string",
            },
        )
        for component in ("ExternalMenuItem", "ExternalMenuItem2", "ExternalMenuItem3")
    ),
    _property_repair(
        "ExternalMenuItemSize",
        "sizeId",
        "4c1ebbf65069d8f4c1f76100167f9d8676ae1b67fd2272fee67267d2f2650f5f",
        {
            "description": (
                "ID size, can be empty if the default size is selected and it is the only "
                "size in the list"
            ),
            "example": "00000000-0000-0000-0000-000000000000",
            "nullable": True,
            "type": "string",
        },
    ),
    *(
        _property_repair(
            component,
            "id",
            "621b69149bce53f74bfbec26d12555f72d856a52cf1bf17c8599b152b42e309d",
            {
                "example": "00000000-0000-0000-0000-000000000000",
                "nullable": True,
                "type": "string",
            },
        )
        for component in ("ExternalMenuItemSize2", "ExternalMenuItemSize3")
    ),
    *(
        _property_repair(
            component,
            "price",
            "86897ffd706df644f6e31cd5d132c04c5b50111b22ce5c44254f142df9faa031",
            {
                "description": (
                    "Product size prices for the organization, if the value is null, then the "
                    "product/size is not for sale, the price always belongs to the price "
                    "category that was selected at the time of the request"
                ),
                "example": "0",
                "format": "float",
                "nullable": True,
                "type": "number",
            },
        )
        for component in (
            "ExternalMenuPriceByDepartmentsDto",
            "ExternalMenuPriceByDepartmentsDto2",
            "ExternalMenuPriceByDepartmentsDto3",
        )
    ),
)

REVIEWED_MISSING_EXTERNAL_MENU_PROPERTIES: tuple[ReviewedMissingPropertyRepair, ...] = (
    ReviewedMissingPropertyRepair(
        parent_path=(
            "components",
            "schemas",
            "ExternalMenuPriceByDepartmentsDto",
            "properties",
        ),
        property_name="organizationId",
        broken_parent_sha256=(
            "14dfe6ad05a1752370850fb33a977adfcbb7b690ee8764d18f68b55f8752c46e"
        ),
        corrected=_frozen_mapping({"format": "uuid", "type": "string"}),
    ),
)

REVIEWED_NULL_ONLY_PROPERTY_EXCEPTIONS: tuple[
    ReviewedNullOnlyPropertyException, ...
] = (
    ReviewedNullOnlyPropertyException(
        component_name="BarcodeDto",
        property_name_sha256="f00dac0f630fb4eb437debc2e71c866f7e0eac502c02ece2b753fc92e3ae8c64",
    ),
)

def build_reviewed_external_menu_validation_schema(
    effective_schema: dict[str, Any],
) -> dict[str, Any]:
    """Return a corrected, caller-independent view of exact reviewed menu defects."""

    document = _strict_document_copy(effective_schema)
    for missing_repair in REVIEWED_MISSING_EXTERNAL_MENU_PROPERTIES:
        if not _has_component(document, missing_repair.parent_path[2]):
            continue
        parent = _at(document, missing_repair.parent_path)
        if type(parent) is not dict:
            _raise_drift((*missing_repair.parent_path, missing_repair.property_name))
        corrected = _thaw(missing_repair.corrected)
        if missing_repair.property_name in parent:
            if not _canonical_equal(parent[missing_repair.property_name], corrected):
                _raise_drift((*missing_repair.parent_path, missing_repair.property_name))
            continue
        if (
            sha256_bytes(canonical_json_bytes(parent))
            != missing_repair.broken_parent_sha256
        ):
            _raise_drift((*missing_repair.parent_path, missing_repair.property_name))
        parent[missing_repair.property_name] = corrected

    for property_repair in REVIEWED_EXTERNAL_MENU_SCHEMA_REPAIRS:
        if not _has_component(document, property_repair.path[2]):
            continue
        actual = _at(document, property_repair.path)
        corrected = _thaw(property_repair.corrected)
        if _canonical_equal(actual, corrected):
            continue
        try:
            actual_sha256 = sha256_bytes(canonical_json_bytes(actual))
        except (TypeError, ValueError):
            _raise_drift(property_repair.path)
        if actual_sha256 != property_repair.broken_sha256:
            _raise_drift(property_repair.path)
        parent = _at(document, property_repair.path[:-1])
        if type(parent) is not dict:
            _raise_drift(property_repair.path)
        parent[property_repair.path[-1]] = corrected
    return document


def is_reviewed_dynamic_map_schema(schema: object) -> bool:
    if not isinstance(schema, Mapping):
        return False
    try:
        digest = sha256_bytes(canonical_json_bytes(schema))
    except (TypeError, ValueError):
        return False
    return digest in _REVIEWED_DYNAMIC_MAP_HASHES


def is_reviewed_null_only_property_hash(
    *,
    component_name: str,
    property_name_sha256: str,
    value: object,
) -> bool:
    return value is None and any(
        exception.component_name == component_name
        and exception.property_name_sha256 == property_name_sha256
        for exception in REVIEWED_NULL_ONLY_PROPERTY_EXCEPTIONS
    )


def _strict_document_copy(value: object) -> dict[str, Any]:
    try:
        copied = json.loads(canonical_json_bytes(value))
    except (TypeError, ValueError, json.JSONDecodeError, RecursionError) as error:
        raise SafetyError("Evidence repair input is not strict canonical JSON") from error
    if type(copied) is not dict:
        raise SafetyError("Evidence repair input must be a strict JSON object")
    return copied


def _at(document: dict[str, Any], path: tuple[str, ...]) -> Any:
    value: Any = document
    try:
        for part in path:
            if type(value) is not dict:
                raise KeyError(part)
            value = value[part]
    except (KeyError, TypeError):
        _raise_drift(path)
    return value


def _has_component(document: dict[str, Any], component_name: str) -> bool:
    components = document.get("components")
    schemas = components.get("schemas") if type(components) is dict else None
    return type(schemas) is dict and component_name in schemas


def _raise_drift(path: tuple[str, ...]) -> None:
    raise SafetyError(f"Reviewed evidence schema repair drifted at {'.'.join(path)}")


def _canonical_equal(left: object, right: object) -> bool:
    try:
        return canonical_json_bytes(left) == canonical_json_bytes(right)
    except (TypeError, ValueError):
        return False


def _thaw(value: FrozenJson) -> Any:
    if isinstance(value, Mapping):
        return {key: _thaw(child) for key, child in value.items()}
    if type(value) is tuple:
        return [_thaw(child) for child in value]
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Reviewed evidence schema repair contains invalid JSON")


_REVIEWED_DYNAMIC_MAP_HASHES = frozenset(
    sha256_bytes(canonical_json_bytes(_thaw(repair.corrected)))
    for repair in REVIEWED_EXTERNAL_MENU_SCHEMA_REPAIRS
    if repair.path[-1] == "overrideTaxCategories"
)
