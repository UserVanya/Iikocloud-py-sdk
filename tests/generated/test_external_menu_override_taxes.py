import json
from pathlib import Path

import pytest

from iikocloud_client.models.external_menu_response import ExternalMenuResponse

FIXTURES = Path(__file__).parents[1] / "fixtures/contracts"
ORGANIZATION = "00000000-0000-4000-8000-000000000001"


@pytest.mark.parametrize("version", [3, 4])
@pytest.mark.parametrize("overrides", [[], {ORGANIZATION: []}])
def test_override_tax_categories_accept_empty_list_and_map(
    version: int, overrides: object
) -> None:
    # iiko sends a UUID-keyed map when a point overrides taxes and an empty list when it
    # does not (write stand, 25.09.2026); both must decode instead of raising.
    body = json.loads((FIXTURES / f"external-menu-v{version}.json").read_text())
    body["overrideTaxCategories"] = overrides

    response = ExternalMenuResponse.from_json(json.dumps(body))

    menu = response.actual_instance
    assert menu.format_version == version
    assert menu.override_tax_categories.actual_instance == overrides
