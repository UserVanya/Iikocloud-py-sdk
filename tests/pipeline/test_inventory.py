import json
from pathlib import Path

from tools.openapi_pipeline.inventory import collect_inventory, diff_inventory


def test_inventory_diff_reports_added_paths_and_schemas() -> None:
    fixtures = Path("tests/fixtures/openapi")
    before = json.loads((fixtures / "minimal-v1.json").read_text())
    after = json.loads((fixtures / "minimal-v2.json").read_text())

    diff = diff_inventory(collect_inventory(before), collect_inventory(after))

    assert diff.added_paths == ("/api/1/status",)
    assert diff.added_operations == ("POST /api/1/status",)
    assert diff.added_schemas == ("Status",)


def test_collect_inventory_sorts_paths_operations_and_schemas() -> None:
    document = {
        "openapi": "3.0.1",
        "paths": {
            "/z": {"post": {}, "parameters": []},
            "/a": {"trace": {}, "get": {}},
        },
        "components": {"schemas": {"Zulu": {}, "Alpha": {}}},
    }

    inventory = collect_inventory(document)

    assert inventory.paths == ("/a", "/z")
    assert inventory.operations == ("GET /a", "POST /z", "TRACE /a")
    assert inventory.schemas == ("Alpha", "Zulu")


def test_inventory_diff_reports_sorted_removals() -> None:
    before = collect_inventory(
        {
            "openapi": "3.0.1",
            "paths": {
                "/z": {"post": {}},
                "/a": {"get": {}},
                "/m": {"delete": {}},
            },
            "components": {"schemas": {"Zulu": {}, "Alpha": {}, "Middle": {}}},
        }
    )
    after = collect_inventory(
        {
            "openapi": "3.0.1",
            "paths": {"/m": {"delete": {}}},
            "components": {"schemas": {"Middle": {}}},
        }
    )

    diff = diff_inventory(before, after)

    assert diff.removed_paths == ("/a", "/z")
    assert diff.removed_operations == ("GET /a", "POST /z")
    assert diff.removed_schemas == ("Alpha", "Zulu")
