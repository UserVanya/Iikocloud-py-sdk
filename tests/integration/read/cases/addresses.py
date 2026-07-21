"""Guarded read cases for regions, cities, and streets."""

from __future__ import annotations

import importlib
from collections.abc import Callable, Mapping
from uuid import UUID

from tools.openapi_pipeline.live.read_case import (
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
)


def _binding(
    operation_id: str,
    request_module: str,
    request_class: str,
    request_keyword: str,
) -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module="iikocloud_client.api.addresses_api",
        api_class="AddressesApi",
        method_name=f"{operation_id}_with_http_info",
        request_module=f"iikocloud_client.models.{request_module}",
        request_class=request_class,
        request_keyword=request_keyword,
    )


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        try:
            module = importlib.import_module(
                f"iikocloud_client.models.{module_name}"
            )
            model = getattr(module, class_name, None)
            valid = isinstance(model, type) and type(response) is model
        except Exception:
            valid = False
        if not valid:
            raise ReadAssertionFailure()

    return validate


def _uuid(value: object) -> UUID | None:
    if type(value) is UUID:
        return value
    return None


def _build_organization_ids(view: ContextView) -> Mapping[str, object]:
    return {"organization_ids": [view["organization_id"]]}


def _build_cities(view: ContextView) -> Mapping[str, object]:
    return {
        "include_deleted": False,
        "organization_ids": [view["organization_id"]],
    }


def _extract_city(response: object, view: ContextView) -> Mapping[str, object]:
    organization_id = _uuid(view.get("organization_id"))
    if organization_id is None:
        return {}
    try:
        groups = response.cities  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(groups) is not list:
        return {}
    for group in groups:
        try:
            group_organization_id = group.organization_id
            cities = group.items
        except Exception:
            continue
        if group_organization_id != organization_id or type(cities) is not list:
            continue
        for city in cities:
            try:
                city_id = city.id
            except Exception:
                continue
            if type(city_id) is UUID:
                return {"city_id": city_id}
    return {}


def _build_streets_by_city(view: ContextView) -> Mapping[str, object]:
    if "city_id" not in view:
        raise NoLiveTarget(NoLiveTargetCode.CITY)
    return {
        "city_id": view["city_id"],
        "include_deleted": False,
        "organization_id": view["organization_id"],
    }


def _extract_street(response: object, _view: ContextView) -> Mapping[str, object]:
    try:
        streets = response.streets  # type: ignore[attr-defined]
    except Exception:
        return {}
    if type(streets) is not list:
        return {}
    for street in streets:
        try:
            street_id = street.id
        except Exception:
            continue
        if type(street_id) is UUID:
            return {"street_id": street_id}
    return {}


def _build_streets_by_id(view: ContextView) -> Mapping[str, object]:
    if "street_id" not in view:
        raise NoLiveTarget(NoLiveTargetCode.STREET)
    return {
        "ids": [view["street_id"]],
        "organization_id": view["organization_id"],
    }


def _empty_extract(_response: object, _view: ContextView) -> Mapping[str, object]:
    return {}


ADDRESS_CASES = (
    ReadCase(
        operation_id="get_cities",
        revision=1,
        depends_on=("get_organizations",),
        requires=("organization_id",),
        provides=("city_id",),
        allowed_no_target_codes=frozenset(),
        binding=_binding(
            "get_cities",
            "cities_request",
            "CitiesRequest",
            "cities_request",
        ),
        build_values=_build_cities,
        validate_response=_typed_validator("cities_response", "CitiesResponse"),
        extract=_extract_city,
    ),
    ReadCase(
        operation_id="get_regions",
        revision=1,
        depends_on=("get_organizations",),
        requires=("organization_id",),
        provides=(),
        allowed_no_target_codes=frozenset(),
        binding=_binding(
            "get_regions",
            "regions_request",
            "RegionsRequest",
            "regions_request",
        ),
        build_values=_build_organization_ids,
        validate_response=_typed_validator("regions_response", "RegionsResponse"),
        extract=_empty_extract,
    ),
    ReadCase(
        operation_id="get_streets_by_city",
        revision=1,
        depends_on=("get_cities",),
        requires=("organization_id", "city_id"),
        provides=("street_id",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.CITY}),
        binding=_binding(
            "get_streets_by_city",
            "streets_by_city_request",
            "StreetsByCityRequest",
            "streets_by_city_request",
        ),
        build_values=_build_streets_by_city,
        validate_response=_typed_validator("streets_response", "StreetsResponse"),
        extract=_extract_street,
    ),
    ReadCase(
        operation_id="get_streets_by_id",
        revision=1,
        depends_on=("get_streets_by_city",),
        requires=("organization_id", "street_id"),
        provides=(),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.STREET}),
        binding=_binding(
            "get_streets_by_id",
            "streets_by_id_request",
            "StreetsByIdRequest",
            "streets_by_id_request",
        ),
        build_values=_build_streets_by_id,
        validate_response=_typed_validator(
            "streets_by_id_response",
            "StreetsByIdResponse",
        ),
        extract=_empty_extract,
    ),
)

__all__ = ["ADDRESS_CASES"]
