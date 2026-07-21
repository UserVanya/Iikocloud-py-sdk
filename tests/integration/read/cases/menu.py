"""Guarded read cases for menu, combo, and stop-list operations."""

from __future__ import annotations

import importlib
from collections.abc import Callable, Mapping
from uuid import UUID, uuid4

from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    ContextView,
    GeneratedReadBinding,
    NoLiveTarget,
    NoLiveTargetCode,
    NoRequest,
    ReadAssertionFailure,
    ReadCase,
)

_PriceEntry = tuple[UUID, UUID | None, int | float]


def _binding(
    operation_id: str,
    *,
    request_module: str | None,
    request_class: str | None,
    request_keyword: str | None,
) -> GeneratedReadBinding:
    return GeneratedReadBinding(
        api_module="iikocloud_client.api.menu_api",
        api_class="MenuApi",
        method_name=f"{operation_id}_with_http_info",
        request_module=(
            f"iikocloud_client.models.{request_module}"
            if request_module is not None
            else None
        ),
        request_class=request_class,
        request_keyword=request_keyword,
    )


def _generated_class(module_name: str, class_name: str) -> type[object] | None:
    try:
        module = importlib.import_module(f"iikocloud_client.models.{module_name}")
        candidate = getattr(module, class_name, None)
    except Exception:
        return None
    if not isinstance(candidate, type):
        return None
    return candidate


def _is_exact_model(response: object, module_name: str, class_name: str) -> bool:
    model = _generated_class(module_name, class_name)
    return model is not None and type(response) is model


def _typed_validator(
    module_name: str,
    class_name: str,
) -> Callable[[object, ContextView], None]:
    def validate(response: object, _view: ContextView) -> None:
        if not _is_exact_model(response, module_name, class_name):
            raise ReadAssertionFailure()

    return validate


def _empty_extract(_response: object, _view: ContextView) -> Mapping[str, object]:
    return {}


def _build_nomenclature(view: ContextView) -> Mapping[str, object]:
    return {
        "organization_id": view["organization_id"],
        "start_revision": 0,
    }


def _is_product_order_item(value: object) -> bool:
    enum_class = _generated_class("order_item_type", "OrderItemType")
    if enum_class is None:
        return False
    product = getattr(enum_class, "PRODUCT", None)
    return type(value) is enum_class and value is product


def _product_price_entries(response: object) -> tuple[_PriceEntry, ...]:
    try:
        products = response.products  # type: ignore[attr-defined]
    except Exception:
        return ()
    if type(products) is not list:
        return ()

    candidates: list[_PriceEntry] = []
    for product in products:
        try:
            product_id = product.id
            is_deleted = product.is_deleted
            order_item_type = product.order_item_type
            size_prices = product.size_prices
        except Exception:
            continue
        if (
            type(product_id) is not UUID
            or is_deleted is not False
            or not _is_product_order_item(order_item_type)
            or type(size_prices) is not list
        ):
            continue
        for size_price in size_prices:
            try:
                size_id = size_price.size_id
                price = size_price.price
                included = price.is_included_in_menu
                current_price = price.current_price
            except Exception:
                continue
            if size_id is not None and type(size_id) is not UUID:
                continue
            if included is not True or type(current_price) not in (int, float):
                continue
            candidates.append((product_id, size_id, current_price))

    counts: dict[tuple[UUID, UUID | None], int] = {}
    for product_id, size_id, _price in candidates:
        key = (product_id, size_id)
        counts[key] = counts.get(key, 0) + 1
    return tuple(
        entry
        for entry in candidates
        if counts[(entry[0], entry[1])] == 1
    )


def _extract_nomenclature(
    response: object,
    _view: ContextView,
) -> Mapping[str, object]:
    prices = _product_price_entries(response)
    if not prices:
        return {}
    product_id, _size_id, product_price = prices[0]
    return {
        "product_id": product_id,
        "product_price": product_price,
        "nomenclature_prices": prices,
    }


def _build_organization_id(view: ContextView) -> Mapping[str, object]:
    return {"organization_id": view["organization_id"]}


def _price_lookup(value: object) -> Mapping[tuple[UUID, UUID | None], int | float]:
    if type(value) is not tuple:
        return {}
    lookup: dict[tuple[UUID, UUID | None], int | float] = {}
    ambiguous: set[tuple[UUID, UUID | None]] = set()
    for entry in value:
        if type(entry) is not tuple or len(entry) != 3:
            return {}
        product_id, size_id, price = entry
        if (
            type(product_id) is not UUID
            or (size_id is not None and type(size_id) is not UUID)
            or type(price) not in (int, float)
        ):
            return {}
        key = (product_id, size_id)
        if key in lookup:
            ambiguous.add(key)
        else:
            lookup[key] = price
    for key in ambiguous:
        lookup.pop(key, None)
    return lookup


def _combo_descriptors(
    response: object,
    prices: Mapping[tuple[UUID, UUID | None], int | float],
) -> tuple[
    UUID,
    tuple[tuple[UUID, str | None, UUID, UUID | None, int | float], ...],
] | None:
    try:
        specifications = response.combo_specifications  # type: ignore[attr-defined]
    except Exception:
        return None
    if type(specifications) is not list:
        return None

    for specification in specifications:
        try:
            active = specification.is_active
            source_id = specification.source_action_id
            groups = specification.groups
        except Exception:
            continue
        if active is not True or type(source_id) is not UUID or not groups:
            continue
        if type(groups) is not list:
            continue

        selected: list[tuple[UUID, str | None, UUID, UUID | None, int | float]] = []
        complete = True
        for group in groups:
            try:
                group_id = group.id
                group_name = group.name
                products = group.products
            except Exception:
                complete = False
                break
            if type(group_id) is not UUID or not products or type(products) is not list:
                complete = False
                break
            safe_group_name = group_name if type(group_name) is str else None
            selected_product = None
            for product in products:
                try:
                    product_id = product.product_id
                    size_id = product.size_id
                except Exception:
                    continue
                if type(product_id) is not UUID:
                    continue
                if size_id is not None and type(size_id) is not UUID:
                    continue
                price = prices.get((product_id, size_id))
                if type(price) not in (int, float):
                    continue
                assert price is not None
                selected_product = (
                    group_id,
                    safe_group_name,
                    product_id,
                    size_id,
                    price,
                )
                break
            if selected_product is None:
                complete = False
                break
            selected.append(selected_product)
        if complete and selected:
            return source_id, tuple(selected)
    return None


def _generated_combo_items(
    descriptors: tuple[
        tuple[UUID, str | None, UUID, UUID | None, int | float], ...
    ],
    source_id: UUID,
) -> tuple[object, ...] | None:
    combo_info_class = _generated_class(
        "delivery_order_create_combo_item_information",
        "DeliveryOrderCreateComboItemInformation",
    )
    product_item_class = _generated_class(
        "delivery_order_create_product_item",
        "DeliveryOrderCreateProductItem",
    )
    if combo_info_class is None or product_item_class is None:
        return None
    combo_id = uuid4()
    items: list[object] = []
    try:
        for group_id, group_name, product_id, size_id, price in descriptors:
            combo_values: dict[str, object] = {
                "combo_group_id": group_id,
                "combo_id": combo_id,
                "combo_source_id": source_id,
            }
            if group_name is not None:
                combo_values["combo_group_name"] = group_name
            combo_information = combo_info_class(**combo_values)
            item_values: dict[str, object] = {
                "amount": 1,
                "combo_information": combo_information,
                "price": price,
                "product_id": product_id,
                "type": "Product",
            }
            if size_id is not None:
                item_values["product_size_id"] = size_id
            items.append(product_item_class(**item_values))
    except Exception:
        return None
    return tuple(items)


def _extract_combo_items(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    prices = _price_lookup(view.get("nomenclature_prices"))
    if not prices:
        return {}
    selected = _combo_descriptors(response, prices)
    if selected is None:
        return {}
    source_id, descriptors = selected
    items = _generated_combo_items(descriptors, source_id)
    if not items:
        return {}
    return {"combo_items": items}


def _build_combo_price(view: ContextView) -> Mapping[str, object]:
    items = view.get("combo_items")
    product_item_class = _generated_class(
        "delivery_order_create_product_item",
        "DeliveryOrderCreateProductItem",
    )
    if (
        type(items) is not tuple
        or not items
        or product_item_class is None
        or any(type(item) is not product_item_class for item in items)
    ):
        raise NoLiveTarget(NoLiveTargetCode.COMBO)
    return {
        "items": list(items),
        "organization_id": view["organization_id"],
    }


def _build_stop_lists(view: ContextView) -> Mapping[str, object]:
    values: dict[str, object] = {
        "organization_ids": [view["organization_id"]],
        "return_size": True,
    }
    terminal_group_id = view.get("terminal_group_id")
    if terminal_group_id is not None:
        values["terminal_groups_ids"] = [terminal_group_id]
    return values


def _selected_product_size(view: ContextView) -> UUID | None | object:
    product_id = view.get("product_id")
    product_price = view.get("product_price")
    if type(product_id) is not UUID or type(product_price) not in (int, float):
        return _MISSING
    prices = _price_lookup(view.get("nomenclature_prices"))
    matches = [
        size_id
        for (candidate_id, size_id), price in prices.items()
        if candidate_id == product_id
        and type(price) is type(product_price)
        and price == product_price
    ]
    if len(matches) != 1:
        return _MISSING
    return matches[0]


_MISSING = object()


def _build_check_stop_list(view: ContextView) -> Mapping[str, object]:
    product_size_id = _selected_product_size(view)
    if product_size_id is _MISSING:
        raise NoLiveTarget(NoLiveTargetCode.PRODUCT)
    if "terminal_group_id" not in view:
        raise NoLiveTarget(NoLiveTargetCode.TERMINAL_GROUP)
    product_item_class = _generated_class(
        "delivery_order_create_product_item",
        "DeliveryOrderCreateProductItem",
    )
    if product_item_class is None:
        raise RuntimeError("generated product item unavailable")
    item_values: dict[str, object] = {
        "amount": 1,
        "price": view["product_price"],
        "product_id": view["product_id"],
        "type": "Product",
    }
    if product_size_id is not None:
        item_values["product_size_id"] = product_size_id
    item = product_item_class(**item_values)
    return {
        "items": [item],
        "organization_id": view["organization_id"],
        "terminal_group_id": view["terminal_group_id"],
    }


def _matching_external_menu_id(
    response: object,
    view: ContextView,
) -> str | None:
    target = view.get("profile_external_menu_id")
    if type(target) is not str:
        return None
    try:
        external_menus = response.external_menus  # type: ignore[attr-defined]
    except Exception:
        return None
    if type(external_menus) is not list:
        return None
    for menu in external_menus:
        try:
            menu_id = menu.id
        except Exception:
            continue
        if type(menu_id) is str and menu_id == target:
            return menu_id
    return None


def _validate_external_menus(response: object, view: ContextView) -> None:
    if not _is_exact_model(response, "menus_data_response", "MenusDataResponse"):
        raise ReadAssertionFailure()
    if _matching_external_menu_id(response, view) is None:
        raise ReadAssertionFailure()


def _extract_external_menu(
    response: object,
    view: ContextView,
) -> Mapping[str, object]:
    external_menu_id = _matching_external_menu_id(response, view)
    if external_menu_id is None:
        return {}
    return {"external_menu_id": external_menu_id}


def _build_external_menu(view: ContextView) -> Mapping[str, object]:
    return {
        "async_mode": False,
        "external_menu_id": view["external_menu_id"],
        "organization_ids": [view["organization_id"]],
    }


def _case(
    operation_id: str,
    response_module: str,
    response_class: str,
    *,
    request_module: str | None,
    request_class: str | None,
    request_keyword: str | None,
    depends_on: tuple[str, ...],
    requires: tuple[str, ...],
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
    build_values: Callable[[ContextView], Mapping[str, object] | NoRequest],
    validate_response: Callable[[object, ContextView], None] | None = None,
    extract: Callable[
        [object, ContextView], Mapping[str, object]
    ] = _empty_extract,
) -> ReadCase:
    return ReadCase(
        operation_id=operation_id,
        revision=1,
        depends_on=depends_on,
        requires=requires,
        provides=provides,
        allowed_no_target_codes=allowed_no_target_codes,
        binding=_binding(
            operation_id,
            request_module=request_module,
            request_class=request_class,
            request_keyword=request_keyword,
        ),
        build_values=build_values,
        validate_response=(
            validate_response
            or _typed_validator(response_module, response_class)
        ),
        extract=extract,
    )


MENU_CASES = (
    _case(
        "get_nomenclature",
        "nomenclature_response",
        "NomenclatureResponse",
        request_module="nomenclature_request",
        request_class="NomenclatureRequest",
        request_keyword="nomenclature_request",
        depends_on=("get_organizations",),
        requires=("organization_id",),
        provides=("product_id", "product_price", "nomenclature_prices"),
        build_values=_build_nomenclature,
        extract=_extract_nomenclature,
    ),
    _case(
        "get_combos_info",
        "get_combos_info_response",
        "GetCombosInfoResponse",
        request_module="get_combos_info_request",
        request_class="GetCombosInfoRequest",
        request_keyword="get_combos_info_request",
        depends_on=("get_nomenclature",),
        requires=("organization_id", "nomenclature_prices"),
        provides=("combo_items",),
        build_values=_build_organization_id,
        extract=_extract_combo_items,
    ),
    _case(
        "calculate_combo_price",
        "calculate_combo_price_response",
        "CalculateComboPriceResponse",
        request_module="calculate_combo_price_request",
        request_class="CalculateComboPriceRequest",
        request_keyword="calculate_combo_price_request",
        depends_on=("get_combos_info", "get_nomenclature"),
        requires=("organization_id", "combo_items"),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.COMBO}),
        build_values=_build_combo_price,
    ),
    _case(
        "get_stop_lists",
        "stop_lists_response",
        "StopListsResponse",
        request_module="stop_lists_request",
        request_class="StopListsRequest",
        request_keyword="stop_lists_request",
        depends_on=("get_terminal_groups",),
        requires=("organization_id", "terminal_group_id"),
        build_values=_build_stop_lists,
    ),
    _case(
        "check_products_in_stop_list",
        "check_stop_list_response",
        "CheckStopListResponse",
        request_module="check_stop_list_request",
        request_class="CheckStopListRequest",
        request_keyword="check_stop_list_request",
        depends_on=("get_nomenclature", "get_terminal_groups"),
        requires=(
            "organization_id",
            "product_id",
            "product_price",
            "nomenclature_prices",
            "terminal_group_id",
        ),
        allowed_no_target_codes=frozenset(
            {NoLiveTargetCode.PRODUCT, NoLiveTargetCode.TERMINAL_GROUP}
        ),
        build_values=_build_check_stop_list,
    ),
    _case(
        "get_external_menus",
        "menus_data_response",
        "MenusDataResponse",
        request_module=None,
        request_class=None,
        request_keyword=None,
        depends_on=(),
        requires=("profile_external_menu_id",),
        provides=("external_menu_id",),
        build_values=lambda _view: NO_REQUEST,
        validate_response=_validate_external_menus,
        extract=_extract_external_menu,
    ),
    _case(
        "get_external_menu_by_id",
        "external_menu_response",
        "ExternalMenuResponse",
        request_module="menu_request",
        request_class="MenuRequest",
        request_keyword="menu_request",
        depends_on=("get_external_menus", "get_organizations"),
        requires=("organization_id", "external_menu_id"),
        build_values=_build_external_menu,
    ),
)

__all__ = ["MENU_CASES"]
