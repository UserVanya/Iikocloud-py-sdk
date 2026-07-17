from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.receipt import LiveReceipt


def test_receipt_matches_only_exact_profile_and_artifact_hashes(tmp_path: Path) -> None:
    receipt = LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="a" * 64,
        effective_schema_sha256="b" * 64,
        generated_tree_sha256="c" * 64,
        operations=("authenticate", "get_organizations"),
        had_429=False,
        completed=True,
    )
    path = tmp_path / "receipt.json"

    receipt.write(path)
    loaded = LiveReceipt.load(path)

    assert loaded.matches("a" * 64, "b" * 64, "c" * 64)
    assert not loaded.matches("a" * 64, "d" * 64, "c" * 64)
    assert path.stat().st_mode & 0o777 == 0o600


def _receipt(*, completed: bool = False, had_429: bool = False) -> LiveReceipt:
    return LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="a" * 64,
        effective_schema_sha256="b" * 64,
        generated_tree_sha256="c" * 64,
        operations=("authenticate", "get_organizations") if completed else (),
        had_429=had_429,
        completed=completed,
    )


def test_receipt_records_operation_before_completion_and_429_is_terminal(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    receipt = _receipt().with_operation("authenticate")
    receipt.write(path)
    assert LiveReceipt.load(path).operations == ("authenticate",)

    with pytest.raises(SafetyError, match="get_organizations"):
        receipt.as_completed()

    receipt = receipt.with_operation("get_organizations")
    completed = receipt.as_completed()
    assert completed.matches("a" * 64, "b" * 64, "c" * 64)

    blocked = receipt.with_429()
    with pytest.raises(SafetyError, match="429"):
        blocked.as_completed()


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("run_id", "run-1", "run_id"),
        ("profile_fingerprint", "A" * 64, "fingerprint"),
        ("effective_schema_sha256", "x" * 64, "schema hash"),
        ("generated_tree_sha256", "0" * 63, "tree hash"),
        ("operations", ["authenticate"], "operations"),
        ("had_429", 0, "flags"),
        ("completed", 1, "flags"),
    ],
)
def test_receipt_rejects_wrong_types_and_identifiers(
    field: str, value: object, message: str
) -> None:
    values = {
        "run_id": "20260716T180000Z-a1b2c3d4",
        "profile_fingerprint": "a" * 64,
        "effective_schema_sha256": "b" * 64,
        "generated_tree_sha256": "c" * 64,
        "operations": (),
        "had_429": False,
        "completed": False,
    }
    values[field] = value
    with pytest.raises(SafetyError, match=message):
        LiveReceipt(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize("mutation", ["extra", "duplicate", "noncanonical"])
def test_receipt_load_rejects_unknown_duplicate_and_noncanonical_json(
    tmp_path: Path, mutation: str
) -> None:
    path = tmp_path / "receipt.json"
    value = _receipt().to_json()
    if mutation == "extra":
        value["api_login"] = "must-not-be-allowed"
        body = canonical_json_bytes(value)
    elif mutation == "duplicate":
        body = canonical_json_bytes(value).replace(
            b'{"completed":false,', b'{"completed":false,"completed":false,', 1
        )
    else:
        body = (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
    path.write_bytes(body)
    path.chmod(0o600)

    with pytest.raises(SafetyError, match="fields|strict JSON|canonical"):
        LiveReceipt.load(path)


def test_receipt_rejects_unsafe_storage(tmp_path: Path) -> None:
    target = tmp_path / "target.json"
    _receipt().write(target)
    link = tmp_path / "link.json"
    link.symlink_to(target)
    with pytest.raises(SafetyError, match="symlink"):
        LiveReceipt.load(link)

    target.chmod(0o644)
    with pytest.raises(SafetyError, match="0600"):
        LiveReceipt.load(target)

    wide_parent = tmp_path / "wide"
    wide_parent.mkdir(mode=0o755)
    with pytest.raises(SafetyError, match="0700"):
        _receipt().write(wide_parent / "receipt.json")
