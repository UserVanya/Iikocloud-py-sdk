import json
from pathlib import Path

import pytest

from iikocloud_client.models.external_menu_response import ExternalMenuResponse

FIXTURES = Path(__file__).parents[1] / "fixtures/contracts"

# iiko declares these product types for menu items (NomenclatureV3.ProductType, minus COMBO,
# which V4 routes to its own branch). A working menu sells semi-prepared items as PREPARED
# (production iiko, 25.09.2026), so each of them must decode instead of failing the menu.
PRODUCT_TYPES = ["DISH", "SERVICE", "GOODS", "PREPARED"]


def _menu_with_item_type(version: int, item_type: str) -> str:
    body = json.loads((FIXTURES / "external-menu-v4.json").read_text())
    body["formatVersion"] = version
    body["itemGroups"][0]["items"][0]["type"] = item_type
    return json.dumps(body)


@pytest.mark.parametrize("item_type", PRODUCT_TYPES)
def test_external_menu_v4_items_accept_every_iiko_product_type(item_type: str) -> None:
    menu = ExternalMenuResponse.from_json(_menu_with_item_type(4, item_type)).actual_instance

    assert menu.format_version == 4
    assert menu.item_groups[0].items[0].actual_instance.type == item_type


@pytest.mark.parametrize("item_type", PRODUCT_TYPES)
def test_external_menu_v3_items_accept_every_iiko_product_type(item_type: str) -> None:
    menu = ExternalMenuResponse.from_json(_menu_with_item_type(3, item_type)).actual_instance

    assert menu.format_version == 3
    assert menu.item_groups[0].items[0].type == item_type
