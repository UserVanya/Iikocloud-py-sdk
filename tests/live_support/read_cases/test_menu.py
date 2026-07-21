from __future__ import annotations

from importlib import import_module
from uuid import UUID

import pytest

from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.menu import MENU_CASES
from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    ContextView,
    NoLiveTarget,
    NoLiveTargetCode,
    ReadAssertionFailure,
    ReadCase,
    build_generated_request,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan

ORGANIZATION_ID = UUID("11111111-1111-4111-8111-111111111111")
TERMINAL_GROUP_ID = UUID("22222222-2222-4222-8222-222222222222")
PRODUCT_ID = UUID("33333333-3333-4333-8333-333333333333")
SECOND_PRODUCT_ID = UUID("44444444-4444-4444-8444-444444444444")
COMBO_SOURCE_ID = UUID("55555555-5555-4555-8555-555555555555")
COMBO_GROUP_ID = UUID("66666666-6666-4666-8666-666666666666")
SECOND_COMBO_GROUP_ID = UUID("77777777-7777-4777-8777-777777777777")
EXTERNAL_MENU_ID = "reviewed-menu"

MENU_IDS = {
    "calculate_combo_price",
    "check_products_in_stop_list",
    "get_combos_info",
    "get_external_menu_by_id",
    "get_external_menus",
    "get_nomenclature",
    "get_stop_lists",
}

RESPONSE_MODELS = {
    "calculate_combo_price": (
        "calculate_combo_price_response",
        "CalculateComboPriceResponse",
    ),
    "check_products_in_stop_list": (
        "check_stop_list_response",
        "CheckStopListResponse",
    ),
    "get_combos_info": ("get_combos_info_response", "GetCombosInfoResponse"),
    "get_external_menu_by_id": (
        "external_menu_response",
        "ExternalMenuResponse",
    ),
    "get_external_menus": ("menus_data_response", "MenusDataResponse"),
    "get_nomenclature": ("nomenclature_response", "NomenclatureResponse"),
    "get_stop_lists": ("stop_lists_response", "StopListsResponse"),
}


def _class(module_name: str, class_name: str) -> type[object]:
    module = import_module(f"iikocloud_client.models.{module_name}")
    return getattr(module, class_name)


def _model(module_name: str, class_name: str, **values: object) -> object:
    return _class(module_name, class_name).model_construct(**values)  # type: ignore[attr-defined]


def _jsonable(value: object) -> object:
    if type(value) is UUID:
        return str(value)
    if type(value) is list:
        return [_jsonable(item) for item in value]
    if type(value) is dict:
        return {key: _jsonable(item) for key, item in value.items()}
    return value


def _case(operation_id: str) -> ReadCase:
    return next(case for case in MENU_CASES if case.operation_id == operation_id)


def _view(case: ReadCase, **changes: object) -> ContextView:
    values: dict[str, object] = {
        "organization_id": ORGANIZATION_ID,
        "profile_external_menu_id": EXTERNAL_MENU_ID,
        "external_menu_id": EXTERNAL_MENU_ID,
        "terminal_group_id": TERMINAL_GROUP_ID,
        "product_id": PRODUCT_ID,
        "product_price": 199,
        "nomenclature_prices": ((PRODUCT_ID, None, 199),),
        "combo_items": (),
    }
    values.update(changes)
    return ContextView({key: values[key] for key in case.requires if key in values})


def _external_menus_response(*menu_ids: str) -> object:
    menus = [
        _model("external_menu", "ExternalMenu", id=menu_id, name="synthetic")
        for menu_id in menu_ids
    ]
    return _model(
        "menus_data_response",
        "MenusDataResponse",
        external_menus=menus,
    )


def _minimal_response(operation_id: str) -> object:
    if operation_id == "get_external_menus":
        return _external_menus_response(EXTERNAL_MENU_ID)
    module_name, class_name = RESPONSE_MODELS[operation_id]
    if operation_id == "get_nomenclature":
        return _model(module_name, class_name, products=[])
    if operation_id == "get_combos_info":
        return _model(module_name, class_name, combo_specifications=[])
    return _model(module_name, class_name)


def _size_price(price: int, *, size_id: UUID | None = None) -> object:
    price_model = _model(
        "price",
        "Price",
        current_price=price,
        is_included_in_menu=True,
    )
    return _model("size_price", "SizePrice", price=price_model, size_id=size_id)


def _product(
    product_id: UUID,
    price: int,
    *,
    size_id: UUID | None = None,
) -> object:
    order_item_type = _class("order_item_type", "OrderItemType")
    return _model(
        "product_info",
        "ProductInfo",
        id=product_id,
        is_deleted=False,
        order_item_type=order_item_type.PRODUCT,  # type: ignore[attr-defined]
        size_prices=[_size_price(price, size_id=size_id)],
    )


def _nomenclature_response(*products: object) -> object:
    return _model(
        "nomenclature_response",
        "NomenclatureResponse",
        products=list(products),
    )


def _combo_response(
    *products_by_group: tuple[UUID, UUID],
    active: bool = True,
) -> object:
    groups = []
    for group_id, product_id in products_by_group:
        combo_product = _model(
            "combo_product",
            "ComboProduct",
            product_id=product_id,
            size_id=None,
        )
        groups.append(
            _model(
                "combo_group",
                "ComboGroup",
                id=group_id,
                name="synthetic-group",
                products=[combo_product],
            )
        )
    specification = _model(
        "combo_specification",
        "ComboSpecification",
        groups=groups,
        is_active=active,
        source_action_id=COMBO_SOURCE_ID,
    )
    return _model(
        "get_combos_info_response",
        "GetCombosInfoResponse",
        combo_specifications=[specification],
    )


def test_menu_registry_is_exact_and_builds_with_foundation_cases() -> None:
    assert type(MENU_CASES) is tuple
    assert {case.operation_id for case in MENU_CASES} == MENU_IDS
    assert len(MENU_CASES) == len(MENU_IDS)

    plan = ReadPlan.build((*FOUNDATION_CASES, *MENU_CASES))
    assert set(plan.ordered_operation_ids) > MENU_IDS


def test_menu_dependencies_and_context_contracts_are_exact() -> None:
    nomenclature = _case("get_nomenclature")
    assert nomenclature.depends_on == ("get_organizations",)
    assert nomenclature.requires == ("organization_id",)
    assert nomenclature.provides == (
        "product_id",
        "product_price",
        "nomenclature_prices",
    )

    combos = _case("get_combos_info")
    assert combos.depends_on == ("get_nomenclature",)
    assert combos.requires == ("organization_id", "nomenclature_prices")
    assert combos.provides == ("combo_items",)

    calculation = _case("calculate_combo_price")
    assert calculation.depends_on == ("get_combos_info", "get_nomenclature")
    assert calculation.requires == ("organization_id", "combo_items")
    assert calculation.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.COMBO}
    )

    stop_lists = _case("get_stop_lists")
    assert stop_lists.depends_on == ("get_terminal_groups",)
    assert stop_lists.requires == ("organization_id", "terminal_group_id")

    check = _case("check_products_in_stop_list")
    assert check.depends_on == ("get_nomenclature", "get_terminal_groups")
    assert check.requires == (
        "organization_id",
        "product_id",
        "product_price",
        "nomenclature_prices",
        "terminal_group_id",
    )
    assert check.allowed_no_target_codes == frozenset(
        {NoLiveTargetCode.PRODUCT, NoLiveTargetCode.TERMINAL_GROUP}
    )

    external_menus = _case("get_external_menus")
    assert external_menus.depends_on == ()
    assert external_menus.requires == ("profile_external_menu_id",)
    assert external_menus.provides == ("external_menu_id",)

    external_menu = _case("get_external_menu_by_id")
    assert external_menu.depends_on == (
        "get_external_menus",
        "get_organizations",
    )
    assert external_menu.requires == ("organization_id", "external_menu_id")


@pytest.mark.parametrize("operation_id", sorted(MENU_IDS))
def test_bindings_resolve_and_validators_use_only_fixed_failures(
    operation_id: str,
) -> None:
    case = _case(operation_id)
    resolved = case.binding.resolve()
    assert resolved.method.__name__ == f"{operation_id}_with_http_info"

    case.validate_response(_minimal_response(operation_id), _view(case))

    private_marker = "private-product-or-menu-value"
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response({"value": private_marker}, _view(case))
    assert str(raised.value) == "assertion_failed"
    assert private_marker not in repr(raised.value)
    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_simple_menu_requests_have_exact_generated_json_aliases() -> None:
    expected = {
        "get_nomenclature": {
            "organizationId": str(ORGANIZATION_ID),
            "startRevision": 0,
        },
        "get_combos_info": {"organizationId": str(ORGANIZATION_ID)},
        "get_external_menu_by_id": {
            "asyncMode": False,
            "externalMenuId": EXTERNAL_MENU_ID,
            "organizationIds": [str(ORGANIZATION_ID)],
        },
    }
    for operation_id, expected_json in expected.items():
        case = _case(operation_id)
        request = build_generated_request(case.binding, case.build_values(_view(case)))
        assert request is not None
        assert _jsonable(request.to_dict()) == expected_json  # type: ignore[attr-defined]


def test_external_menu_list_is_the_only_no_body_menu_operation() -> None:
    case = _case("get_external_menus")
    assert case.binding.request_module is None
    assert case.binding.request_class is None
    assert case.binding.request_keyword is None
    assert case.build_values(_view(case)) is NO_REQUEST


def test_nomenclature_extracts_first_product_and_immutable_price_lookup() -> None:
    case = _case("get_nomenclature")
    response = _nomenclature_response(
        _product(PRODUCT_ID, 199),
        _product(SECOND_PRODUCT_ID, 299),
    )

    extracted = case.extract(response, _view(case))

    assert extracted["product_id"] == PRODUCT_ID
    assert extracted["product_price"] == 199
    assert extracted["nomenclature_prices"] == (
        (PRODUCT_ID, None, 199),
        (SECOND_PRODUCT_ID, None, 299),
    )
    assert type(extracted["nomenclature_prices"]) is tuple

    empty = _nomenclature_response()
    assert case.extract(empty, _view(case)) == {}


def test_combo_items_require_every_group_and_exact_nomenclature_prices() -> None:
    nomenclature = _case("get_nomenclature")
    extracted_menu = nomenclature.extract(
        _nomenclature_response(
            _product(PRODUCT_ID, 199),
            _product(SECOND_PRODUCT_ID, 299),
        ),
        _view(nomenclature),
    )
    combos = _case("get_combos_info")
    combo_view = _view(
        combos,
        nomenclature_prices=extracted_menu["nomenclature_prices"],
    )
    response = _combo_response(
        (COMBO_GROUP_ID, PRODUCT_ID),
        (SECOND_COMBO_GROUP_ID, SECOND_PRODUCT_ID),
    )

    extracted = combos.extract(response, combo_view)
    items = extracted["combo_items"]

    assert type(items) is tuple
    assert len(items) == 2
    first, second = items
    assert type(first).__name__ == "DeliveryOrderCreateProductItem"
    assert type(second).__name__ == "DeliveryOrderCreateProductItem"
    assert first.price == 199
    assert second.price == 299
    assert first.combo_information.combo_id == second.combo_information.combo_id
    assert first.combo_information.combo_source_id == COMBO_SOURCE_ID

    incomplete = _combo_response(
        (COMBO_GROUP_ID, PRODUCT_ID),
        (SECOND_COMBO_GROUP_ID, UUID("88888888-8888-4888-8888-888888888888")),
    )
    assert combos.extract(incomplete, combo_view) == {}
    assert combos.extract(_minimal_response("get_combos_info"), combo_view) == {}


def test_calculate_combo_price_uses_only_extracted_generated_items() -> None:
    nomenclature = _case("get_nomenclature")
    menu_values = nomenclature.extract(
        _nomenclature_response(_product(PRODUCT_ID, 199)),
        _view(nomenclature),
    )
    combos = _case("get_combos_info")
    combo_values = combos.extract(
        _combo_response((COMBO_GROUP_ID, PRODUCT_ID)),
        _view(combos, nomenclature_prices=menu_values["nomenclature_prices"]),
    )
    calculation = _case("calculate_combo_price")
    view = _view(calculation, combo_items=combo_values["combo_items"])

    values = calculation.build_values(view)
    request = build_generated_request(calculation.binding, values)
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "items": [
            _jsonable(combo_values["combo_items"][0].to_dict())  # type: ignore[index]
        ],
        "organizationId": str(ORGANIZATION_ID),
    }

    with pytest.raises(NoLiveTarget) as missing:
        calculation.build_values(
            ContextView({"organization_id": ORGANIZATION_ID})
        )
    assert missing.value.code is NoLiveTargetCode.COMBO


def test_stop_list_request_uses_at_most_one_validated_terminal_filter() -> None:
    case = _case("get_stop_lists")
    without_terminal = case.build_values(
        ContextView({"organization_id": ORGANIZATION_ID})
    )
    request = build_generated_request(case.binding, without_terminal)
    assert request is not None
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "organizationIds": [str(ORGANIZATION_ID)],
        "returnSize": True,
    }

    with_terminal = build_generated_request(
        case.binding,
        case.build_values(_view(case)),
    )
    assert with_terminal is not None
    assert _jsonable(with_terminal.to_dict()) == {  # type: ignore[attr-defined]
        "organizationIds": [str(ORGANIZATION_ID)],
        "returnSize": True,
        "terminalGroupsIds": [str(TERMINAL_GROUP_ID)],
    }


def test_check_stop_list_uses_one_concrete_generated_product_item() -> None:
    case = _case("check_products_in_stop_list")
    values = case.build_values(_view(case))
    request = build_generated_request(case.binding, values)
    assert request is not None

    assert len(request.items) == 1  # type: ignore[attr-defined]
    assert type(request.items[0]).__name__ == "DeliveryOrderCreateProductItem"  # type: ignore[attr-defined]
    assert _jsonable(request.to_dict()) == {  # type: ignore[attr-defined]
        "items": [
            {
                "amount": 1,
                "price": 199,
                "productId": str(PRODUCT_ID),
                "type": "Product",
            }
        ],
        "organizationId": str(ORGANIZATION_ID),
        "terminalGroupId": str(TERMINAL_GROUP_ID),
    }


def test_missing_product_and_terminal_fail_before_generated_item_construction() -> None:
    case = _case("check_products_in_stop_list")

    with pytest.raises(NoLiveTarget) as missing_product:
        case.build_values(
            ContextView(
                {
                    "organization_id": ORGANIZATION_ID,
                    "terminal_group_id": TERMINAL_GROUP_ID,
                }
            )
        )
    assert missing_product.value.code is NoLiveTargetCode.PRODUCT

    with pytest.raises(NoLiveTarget) as missing_terminal:
        case.build_values(
            ContextView(
                {
                    "organization_id": ORGANIZATION_ID,
                    "product_id": PRODUCT_ID,
                    "product_price": 199,
                    "nomenclature_prices": ((PRODUCT_ID, None, 199),),
                }
            )
        )
    assert missing_terminal.value.code is NoLiveTargetCode.TERMINAL_GROUP


def test_external_menu_target_is_validated_before_publication() -> None:
    case = _case("get_external_menus")
    view = _view(case)
    matching = _external_menus_response("other-menu", EXTERNAL_MENU_ID)

    case.validate_response(matching, view)
    assert case.extract(matching, view) == {"external_menu_id": EXTERNAL_MENU_ID}

    missing = _external_menus_response("other-menu")
    with pytest.raises(ReadAssertionFailure) as raised:
        case.validate_response(missing, view)
    assert str(raised.value) == "assertion_failed"
    assert EXTERNAL_MENU_ID not in repr(raised.value)
    assert case.extract(missing, view) == {}
