import json

import pytest

from iikocloud_client.models.menu_v3 import MenuV3

BASE_TAX = "00000000-0000-4000-8000-000000000001"
NEW_TAX = "00000000-0000-4000-8000-000000000002"
ORDER_TYPE = "00000000-0000-4000-8000-000000000003"


def _menu(overrides: object) -> str:
    return json.dumps({"id": "1", "name": "menu", "overrideTaxCategories": overrides})


def test_menu_v3_keeps_override_tax_categories() -> None:
    # iiko's MenuV3 schema omits overrideTaxCategories and forbids extra properties, yet
    # production /api/menu/v3/by_id sends it (25.09.2026); the model must not drop it.
    menu = MenuV3.from_json(
        _menu(
            [
                {
                    "baseTaxCategoryId": BASE_TAX,
                    "newTaxCategoryId": NEW_TAX,
                    "orderTypeId": ORDER_TYPE,
                }
            ]
        )
    )

    [override] = menu.override_tax_categories
    assert str(override.base_tax_category_id) == BASE_TAX
    assert str(override.new_tax_category_id) == NEW_TAX
    assert str(override.order_type_id) == ORDER_TYPE
    assert json.loads(menu.to_json())["overrideTaxCategories"] == [
        {"baseTaxCategoryId": BASE_TAX, "newTaxCategoryId": NEW_TAX, "orderTypeId": ORDER_TYPE}
    ]


@pytest.mark.parametrize("overrides", [[], None])
def test_menu_v3_accepts_empty_override_tax_categories(overrides: object) -> None:
    menu = MenuV3.from_json(_menu(overrides))

    assert menu.override_tax_categories in ([], None)
