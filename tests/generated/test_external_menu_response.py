from pathlib import Path

import pytest
from iikocloud_client.models.external_menu_response import ExternalMenuResponse


@pytest.mark.parametrize("version", [2, 3, 4])
def test_external_menu_union_selects_exactly_one_version(version: int) -> None:
    body = Path(f"tests/fixtures/contracts/external-menu-v{version}.json").read_text()
    response = ExternalMenuResponse.from_json(body)
    assert response.actual_instance.format_version == version
