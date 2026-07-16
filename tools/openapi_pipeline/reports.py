from __future__ import annotations

from pathlib import Path
from typing import Any

from .inventory import Inventory, InventoryDiff, collect_inventory, diff_inventory
from .io import write_bytes_atomic, write_json_atomic


def _empty_inventory(openapi: str = "") -> Inventory:
    return Inventory(openapi=openapi, paths=(), operations=(), schemas=())


def build_upstream_report(before: dict[str, Any] | None, after: dict[str, Any]) -> dict[str, Any]:
    before_inventory = collect_inventory(before) if before is not None else _empty_inventory()
    after_inventory = collect_inventory(after)
    difference = diff_inventory(before_inventory, after_inventory)
    return {
        "before": before_inventory.to_dict(),
        "after": after_inventory.to_dict(),
        "diff": difference.to_dict(),
    }


def _section(title: str, added: tuple[str, ...], removed: tuple[str, ...]) -> list[str]:
    lines = [f"## {title}", ""]
    lines.extend(f"- Added: `{value}`" for value in added)
    lines.extend(f"- Removed: `{value}`" for value in removed)
    if not added and not removed:
        lines.append("- No changes")
    lines.append("")
    return lines


def render_upstream_markdown(report: dict[str, Any]) -> str:
    raw = report["diff"]
    difference = InventoryDiff(
        added_paths=tuple(raw["added_paths"]),
        removed_paths=tuple(raw["removed_paths"]),
        added_operations=tuple(raw["added_operations"]),
        removed_operations=tuple(raw["removed_operations"]),
        added_schemas=tuple(raw["added_schemas"]),
        removed_schemas=tuple(raw["removed_schemas"]),
    )
    lines = ["# Upstream OpenAPI inventory diff", ""]
    lines.extend(_section("Paths", difference.added_paths, difference.removed_paths))
    lines.extend(
        _section("Operations", difference.added_operations, difference.removed_operations)
    )
    lines.extend(_section("Schemas", difference.added_schemas, difference.removed_schemas))
    return "\n".join(lines).rstrip() + "\n"


def write_upstream_reports(
    before: dict[str, Any] | None,
    after: dict[str, Any],
    reports: Path,
    *,
    include_json: bool = True,
) -> dict[str, Any]:
    report = build_upstream_report(before, after)
    reports.mkdir(parents=True, exist_ok=True)
    if include_json:
        write_json_atomic(reports / "upstream-diff.json", report)
    write_bytes_atomic(
        reports / "upstream-diff.md",
        render_upstream_markdown(report).encode("utf-8"),
    )
    return report
