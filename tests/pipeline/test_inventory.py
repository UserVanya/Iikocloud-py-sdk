import json
from pathlib import Path

from tools.openapi_pipeline.inventory import collect_inventory, diff_inventory


def test_inventory_diff_reports_added_paths_and_schemas() -> None:
    fixtures = Path("tests/fixtures/openapi")
    before = json.loads((fixtures / "minimal-v1.json").read_text())
    after = json.loads((fixtures / "minimal-v2.json").read_text())

    diff = diff_inventory(collect_inventory(before), collect_inventory(after))

    assert diff.added_paths == ("/api/1/status",)
    assert diff.added_schemas == ("Status",)
