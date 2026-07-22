from pathlib import Path

import pytest

from iikocloud_client.models.external_menu_response import ExternalMenuResponse


@pytest.mark.parametrize("version", [2, 3, 4])
def test_external_menu_union_selects_exactly_one_version(version: int) -> None:
    fixture = Path(__file__).parents[1] / "fixtures/contracts" / f"external-menu-v{version}.json"
    body = fixture.read_text()
    response = ExternalMenuResponse.from_json(body)
    assert response.actual_instance.format_version == version
