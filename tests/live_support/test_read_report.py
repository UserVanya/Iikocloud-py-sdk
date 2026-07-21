from __future__ import annotations

import json
import os
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.read_case import NoLiveTargetCode, ReadFailureCode
from tools.openapi_pipeline.live.read_report import (
    ReadOutcome,
    ReadReport,
    ReadReportWriter,
    ReadStatus,
)
from tools.openapi_pipeline.live.session import LiveOperation


def test_read_outcome_types_have_exact_status_values() -> None:
    assert [status.value for status in ReadStatus] == [
        "passed",
        "no_live_target",
        "failed",
        "aborted",
    ]
    outcome = ReadOutcome(
        operation_id="get_organizations",
        method="POST",
        path="/api/1/organizations",
        status=ReadStatus.PASSED,
        reason=None,
        http_status=200,
        duration_ms=1,
    )
    assert outcome.status is ReadStatus.PASSED


def _outcome(**overrides: object) -> ReadOutcome:
    values: dict[str, object] = {
        "operation_id": "get_organizations",
        "method": "POST",
        "path": "/api/1/organizations",
        "status": ReadStatus.PASSED,
        "reason": None,
        "http_status": 200,
        "duration_ms": 1,
    }
    values.update(overrides)
    return ReadOutcome(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("status", "reason"),
    [
        (ReadStatus.PASSED, None),
        (ReadStatus.NO_LIVE_TARGET, NoLiveTargetCode.CITY.value),
        (ReadStatus.FAILED, ReadFailureCode.ASSERTION_FAILED.value),
        (ReadStatus.FAILED, ReadFailureCode.EXTRACTOR_FAILED.value),
        (ReadStatus.ABORTED, ReadFailureCode.HTTP_ERROR.value),
    ],
)
def test_read_outcome_accepts_only_compatible_status_reasons(
    status: ReadStatus, reason: str | None
) -> None:
    assert _outcome(status=status, reason=reason).reason == reason


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"operation_id": "../unsafe"}, "operation"),
        ({"method": "get"}, "method"),
        ({"path": "https://example.invalid/api"}, "path"),
        ({"path": "/api?api_login=secret"}, "path"),
        ({"status": "passed"}, "status"),
        ({"reason": "raw exception"}, "reason"),
        (
            {
                "status": ReadStatus.NO_LIVE_TARGET,
                "reason": ReadFailureCode.HTTP_ERROR.value,
            },
            "reason",
        ),
        (
            {
                "status": ReadStatus.FAILED,
                "reason": ReadFailureCode.HTTP_ERROR.value,
            },
            "reason",
        ),
        (
            {
                "status": ReadStatus.ABORTED,
                "reason": ReadFailureCode.ASSERTION_FAILED.value,
            },
            "reason",
        ),
        ({"http_status": 99}, "HTTP"),
        ({"http_status": True}, "HTTP"),
        ({"duration_ms": -1}, "duration"),
        ({"duration_ms": 1.5}, "duration"),
    ],
)
def test_read_outcome_rejects_unsafe_or_incompatible_values(
    overrides: dict[str, object], message: str
) -> None:
    with pytest.raises(SafetyError, match=message):
        _outcome(**overrides)


@pytest.mark.parametrize("reason", [[], {}])
def test_read_outcome_rejects_non_scalar_reason_with_fixed_safety_error(
    reason: object,
) -> None:
    with pytest.raises(SafetyError, match="reason"):
        _outcome(
            status=ReadStatus.FAILED,
            reason=reason,
        )


def _report(**overrides: object) -> ReadReport:
    values: dict[str, object] = {
        "version": 1,
        "run_id": "20260721T120000Z-a1b2c3d4",
        "profile_fingerprint": "a" * 64,
        "effective_schema_sha256": "b" * 64,
        "generated_tree_sha256": "c" * 64,
        "live_contracts_sha256": "d" * 64,
        "registry_sha256": "e" * 64,
        "started_at": "2026-07-21T12:00:00Z",
        "finished_at": None,
        "completed": False,
        "outcomes": (),
        "counts": {
            "passed": 0,
            "no_live_target": 0,
            "failed": 0,
            "aborted": 0,
        },
    }
    values.update(overrides)
    return ReadReport(**values)  # type: ignore[arg-type]


def test_read_report_uses_exact_initial_canonical_shape() -> None:
    report = _report()
    expected = {
        "version": 1,
        "run_id": "20260721T120000Z-a1b2c3d4",
        "profile_fingerprint": "a" * 64,
        "effective_schema_sha256": "b" * 64,
        "generated_tree_sha256": "c" * 64,
        "live_contracts_sha256": "d" * 64,
        "registry_sha256": "e" * 64,
        "started_at": "2026-07-21T12:00:00Z",
        "finished_at": None,
        "completed": False,
        "outcomes": [],
        "counts": {
            "passed": 0,
            "no_live_target": 0,
            "failed": 0,
            "aborted": 0,
        },
    }

    assert report.to_json() == expected
    assert ReadReport.from_bytes(canonical_json_bytes(expected)) == report


@pytest.mark.parametrize("mutation", ["extra", "duplicate", "noncanonical", "large"])
def test_read_report_parser_rejects_non_strict_json(mutation: str) -> None:
    value = _report().to_json()
    if mutation == "extra":
        value["api_login"] = "must-not-be-allowed"
        body = canonical_json_bytes(value)
    elif mutation == "duplicate":
        body = canonical_json_bytes(value).replace(
            b'{"completed":false,', b'{"completed":false,"completed":false,', 1
        )
    elif mutation == "noncanonical":
        body = (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
    else:
        body = b" " * (1024 * 1024 + 1)

    with pytest.raises(SafetyError, match="fields|strict JSON|canonical|large"):
        ReadReport.from_bytes(body)


def test_read_report_rejects_duplicate_outcomes_count_drift_and_false_completion() -> None:
    outcome = _outcome()
    with pytest.raises(SafetyError, match="duplicate"):
        _report(
            outcomes=(outcome, outcome),
            counts={"passed": 2, "no_live_target": 0, "failed": 0, "aborted": 0},
        )
    with pytest.raises(SafetyError, match="counts"):
        _report(outcomes=(outcome,))
    with pytest.raises(SafetyError, match="finished"):
        _report(
            completed=True,
            outcomes=(outcome,),
            counts={"passed": 1, "no_live_target": 0, "failed": 0, "aborted": 0},
        )
    with pytest.raises(SafetyError, match="successful"):
        _report(
            completed=True,
            finished_at="2026-07-21T12:01:00Z",
            outcomes=(_outcome(status=ReadStatus.FAILED, reason="assertion_failed"),),
            counts={"passed": 0, "no_live_target": 0, "failed": 1, "aborted": 0},
        )


def _private_root(tmp_path: Path) -> Path:
    private = tmp_path / "private"
    private.mkdir(mode=0o700)
    private.chmod(0o700)
    return private


def _operation_contract() -> Mapping[str, LiveOperation]:
    return MappingProxyType(
        {
            "authenticate": LiveOperation(
                kind="auth",
                cleanup=None,
                method="POST",
                path="/api/1/access_token",
            ),
            "get_organizations": LiveOperation(
                kind="read",
                cleanup=None,
                method="POST",
                path="/api/1/organizations",
            ),
            "add_products_to_stop_list": LiveOperation(
                kind="compensating",
                cleanup="remove_products_from_stop_list",
                method="POST",
                path="/api/1/stop_lists/add",
            ),
            "remove_products_from_stop_list": LiveOperation(
                kind="cleanup",
                cleanup=None,
                method="POST",
                path="/api/1/stop_lists/remove",
            ),
        }
    )


def _writer(private: Path) -> ReadReportWriter:
    return ReadReportWriter.create(
        private,
        operation_contract=_operation_contract(),
        run_id="20260721T120000Z-a1b2c3d4",
        profile_fingerprint="a" * 64,
        effective_schema_sha256="b" * 64,
        generated_tree_sha256="c" * 64,
        live_contracts_sha256="d" * 64,
        registry_sha256="e" * 64,
        started_at="2026-07-21T12:00:00Z",
    )


@pytest.mark.parametrize(
    "sensitive_value",
    [
        "123e4567-e89b-12d3-a456-426614174000",
        "person@example.invalid",
        "+15551234567",
    ],
)
def test_writer_exact_contract_blocks_sensitive_values_in_outcome_path(
    tmp_path: Path,
    sensitive_value: str,
) -> None:
    writer = _writer(_private_root(tmp_path))
    before = writer.path.read_bytes()

    with pytest.raises(SafetyError, match="contract|path"):
        writer.append(
            _outcome(path=f"/api/1/organizations/{sensitive_value}")
        )

    assert writer.path.read_bytes() == before
    assert sensitive_value.encode() not in writer.path.read_bytes()


@pytest.mark.parametrize(
    "outcome",
    [
        pytest.param(_outcome(operation_id="unknown_read"), id="unknown"),
        pytest.param(_outcome(method="GET"), id="method"),
        pytest.param(_outcome(path="/api/1/other"), id="path"),
        pytest.param(
            _outcome(
                operation_id="add_products_to_stop_list",
                path="/api/1/stop_lists/add",
            ),
            id="non-read",
        ),
    ],
)
def test_writer_rejects_outcomes_not_bound_to_exact_read_operation(
    tmp_path: Path,
    outcome: ReadOutcome,
) -> None:
    writer = _writer(_private_root(tmp_path))
    before = writer.path.read_bytes()
    inode = writer.path.stat().st_ino

    with pytest.raises(SafetyError, match="contract|read|method|path|unknown"):
        writer.append(outcome)

    assert writer.path.read_bytes() == before
    assert writer.path.stat().st_ino == inode


def test_writer_requires_immutable_operation_contract(tmp_path: Path) -> None:
    private = _private_root(tmp_path)
    with pytest.raises(SafetyError, match="immutable"):
        ReadReportWriter.create(
            private,
            operation_contract=dict(_operation_contract()),
            run_id="20260721T120000Z-a1b2c3d4",
            profile_fingerprint="a" * 64,
            effective_schema_sha256="b" * 64,
            generated_tree_sha256="c" * 64,
            live_contracts_sha256="d" * 64,
            registry_sha256="e" * 64,
            started_at="2026-07-21T12:00:00Z",
        )


def test_writer_creates_private_report_appends_atomically_and_finishes(
    tmp_path: Path,
) -> None:
    private = _private_root(tmp_path)
    writer = _writer(private)

    assert writer.path == (
        private / "reports/live-read/20260721T120000Z-a1b2c3d4.json"
    )
    assert writer.path.stat().st_mode & 0o777 == 0o600
    assert (private / "reports").stat().st_mode & 0o777 == 0o700
    assert (private / "reports/live-read").stat().st_mode & 0o777 == 0o700
    assert writer.load_and_verify().outcomes == ()

    first_inode = writer.path.stat().st_ino
    writer.append(_outcome())
    assert writer.path.stat().st_ino != first_inode
    completed = writer.finish(True, finished_at="2026-07-21T12:01:00Z")

    assert completed.completed
    assert completed.counts == {
        "passed": 1,
        "no_live_target": 0,
        "failed": 0,
        "aborted": 0,
    }
    assert writer.load_and_verify() == completed
    assert writer.path.read_bytes() == canonical_json_bytes(completed.to_json())
    assert completed.matches(
        "20260721T120000Z-a1b2c3d4",
        "a" * 64,
        "b" * 64,
        "c" * 64,
        "d" * 64,
        "e" * 64,
    )
    assert not completed.matches(
        "20260721T120000Z-a1b2c3d4",
        "a" * 64,
        "b" * 64,
        "c" * 64,
        "d" * 64,
        "f" * 64,
    )


def test_writer_rejects_duplicate_outcome_and_unsuccessful_completion(
    tmp_path: Path,
) -> None:
    writer = _writer(_private_root(tmp_path))
    with pytest.raises(SafetyError, match="successful"):
        writer.finish(True, finished_at="2026-07-21T12:01:00Z")
    outcome = _outcome(status=ReadStatus.FAILED, reason="assertion_failed")
    writer.append(outcome)
    before = writer.path.read_bytes()
    with pytest.raises(SafetyError, match="duplicate"):
        writer.append(outcome)
    with pytest.raises(SafetyError, match="successful"):
        writer.finish(True, finished_at="2026-07-21T12:01:00Z")
    assert writer.path.read_bytes() == before


@pytest.mark.parametrize("attack", ["existing", "leaf-symlink", "ancestry-symlink", "escape"])
def test_writer_create_rejects_path_attacks_without_clobbering(
    tmp_path: Path, attack: str
) -> None:
    private = _private_root(tmp_path)
    leaf = private / "reports/live-read/20260721T120000Z-a1b2c3d4.json"
    if attack in {"existing", "leaf-symlink"}:
        leaf.parent.mkdir(parents=True, mode=0o700)
        (private / "reports").chmod(0o700)
        leaf.parent.chmod(0o700)
        target = tmp_path / "unrelated"
        target.write_bytes(b"do-not-clobber")
        if attack == "existing":
            leaf.write_bytes(b"do-not-clobber")
            leaf.chmod(0o600)
        else:
            leaf.symlink_to(target)
    elif attack == "ancestry-symlink":
        target = tmp_path / "elsewhere"
        target.mkdir(mode=0o700)
        (private / "reports").symlink_to(target, target_is_directory=True)
    else:
        private = private / ".." / "escaped-private"

    with pytest.raises(SafetyError, match="exists|symlink|canonical|unsafe"):
        _writer(private)

    if attack == "existing":
        assert leaf.read_bytes() == b"do-not-clobber"
    elif attack == "leaf-symlink":
        assert target.read_bytes() == b"do-not-clobber"


@pytest.mark.parametrize("attack", ["content", "mode", "hard-link", "parent-mode"])
def test_writer_rejects_changed_or_unsafe_current_report(
    tmp_path: Path, attack: str
) -> None:
    writer = _writer(_private_root(tmp_path))
    if attack == "content":
        writer.path.write_bytes(b"{}\n")
    elif attack == "mode":
        writer.path.chmod(0o644)
    elif attack == "hard-link":
        os.link(writer.path, tmp_path / "second-name")
    else:
        writer.path.parent.chmod(0o755)

    with pytest.raises(SafetyError, match="changed|0600|link|0700|private"):
        writer.append(_outcome())


def test_writer_preserves_concurrent_leaf_replacement_before_publication(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from tools.openapi_pipeline.live import read_report as report_module

    writer = _writer(_private_root(tmp_path))
    marker = b'{"unrelated":"marker"}\n'

    def replace_before_exchange(
        directory_fd: int,
        source: str,
        destination: str,
        *,
        renameat2: object,
    ) -> None:
        replacement = writer.path.with_name("unrelated-marker")
        replacement.write_bytes(marker)
        replacement.chmod(0o600)
        replacement.replace(writer.path)
        report_module._rename_exchange(
            directory_fd,
            source,
            destination,
            renameat2=renameat2,
        )

    monkeypatch.setattr(
        report_module,
        "_exchange_report_entries",
        replace_before_exchange,
        raising=False,
    )

    with pytest.raises(SafetyError, match="[Cc]oncurrent|changed|replaced"):
        writer.append(_outcome())

    assert writer.path.read_bytes() == marker
    assert not any(path.name.startswith(".") for path in writer.path.parent.iterdir())


def test_report_bytes_cannot_serialize_live_secrets_or_payloads(tmp_path: Path) -> None:
    writer = _writer(_private_root(tmp_path))
    writer.append(_outcome())
    writer.finish(True, finished_at="2026-07-21T12:01:00Z")
    body = writer.path.read_bytes()

    forbidden = (
        b"synthetic-api-login",
        b"Bearer synthetic-token",
        b"123e4567-e89b-12d3-a456-426614174000",
        b"person@example.invalid",
        b"+15551234567",
        b"Synthetic Customer",
        b"request_body",
        b"response_body",
        b"raw exception",
        b"Authorization",
        b"?api_login=",
    )
    assert all(value not in body for value in forbidden)
