import json

from iikocloud_client.models.menu_v3 import MenuV3

MODIFIER = "00000000-0000-4000-8000-000000000011"
TAX = "00000000-0000-4000-8000-000000000012"


def _menu(modifier_item: dict[str, object]) -> str:
    return json.dumps(
        {
            "id": "1",
            "name": "menu",
            "itemsGroups": [
                {
                    "id": "2",
                    "name": "group",
                    "items": [
                        {
                            "name": "dish",
                            "modifierGroups": [{"name": "extras", "items": [modifier_item]}],
                        }
                    ],
                }
            ],
            "modifiers": [
                {"id": MODIFIER, "sku": "M-1", "name": "Cheese", "isHidden": False, "weight": 0.05}
            ],
        }
    )


def test_menu_v3_modifier_item_may_carry_only_its_id() -> None:
    # Upstream 9.8.6.3: every ModifierItem field except id is an optional override; a null
    # field means "take it from MenuV3.modifiers with the same id". A modifier item without a
    # name must decode instead of failing the whole menu.
    menu = MenuV3.from_json(_menu({"id": MODIFIER}))

    [option] = menu.items_groups[0].items[0].modifier_groups[0].items
    assert option.id == MODIFIER
    assert option.name is None
    assert option.is_hidden is None
    assert option.weight is None
    [reference] = menu.modifiers
    assert (reference.id, reference.name) == (MODIFIER, "Cheese")


def test_menu_v3_modifier_item_null_overrides_decode() -> None:
    menu = MenuV3.from_json(
        _menu(
            {
                "id": MODIFIER,
                "name": None,
                "isHidden": None,
                "measureUnitType": None,
                "weight": None,
            }
        )
    )

    [option] = menu.items_groups[0].items[0].modifier_groups[0].items
    assert option.name is None
    assert option.measure_unit_type is None


def test_menu_v3_override_tax_category_applies_to_all_order_types_when_null() -> None:
    # Upstream 9.8.6.3 describes overrideTaxCategories itself (TaxCategoryOverride, kept under
    # the public name MenuV3OverrideTaxCategory); a null orderTypeId means "all order types".
    body = json.loads(_menu({"id": MODIFIER}))
    body["overrideTaxCategories"] = [
        {"baseTaxCategoryId": TAX, "newTaxCategoryId": None, "orderTypeId": None}
    ]

    menu = MenuV3.from_json(json.dumps(body))

    [override] = menu.override_tax_categories
    assert str(override.base_tax_category_id) == TAX
    assert override.order_type_id is None
