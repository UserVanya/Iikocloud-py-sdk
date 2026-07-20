from __future__ import annotations

import json
import os
import stat
from dataclasses import fields
from pathlib import Path
from typing import Any, get_type_hints

import pytest
import yaml
from test_evidence_analysis import _pairs, _plain
from test_evidence_candidates import _retained_items, _reviewed_schema

import tools.openapi_pipeline.evidence_candidate_accept as accept_module
import tools.openapi_pipeline.promotion as promotion_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_analysis import analyze_menu_evidence
from tools.openapi_pipeline.evidence_candidate_accept import (
    EvidenceCandidateAcceptResult,
    accept_evidence_candidate,
)
from tools.openapi_pipeline.evidence_candidate_contract import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
)
from tools.openapi_pipeline.evidence_candidate_store import (
    EvidenceCandidateManifestResult,
    build_evidence_candidate_manifest,
)
from tools.openapi_pipeline.evidence_candidate_writer import (
    EvidenceCandidateProcessLock,
    write_evidence_candidate_tree,
)
from tools.openapi_pipeline.evidence_candidates import build_evidence_candidate_bundle
from tools.openapi_pipeline.evidence_promotion import CaptureEvidenceReader
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.normalization import build_types_overlay
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import compose_reviewed_evidence_base_candidate
from tools.openapi_pipeline.promotion import promote_transaction as real_promote_transaction


def _write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=True), encoding="utf-8")
    path.chmod(0o644)


def _repository(tmp_path: Path) -> RepoPaths:
    root = tmp_path / "repository"
    root.mkdir(mode=0o755)
    root.chmod(0o755)
    (root / "pyproject.toml").write_text(
        "[project]\nname='synthetic-evidence-accept'\n",
        encoding="utf-8",
    )
    (root / "pyproject.toml").chmod(0o644)

    schema = _reviewed_schema()
    candidate = root / "build/upstream/candidate.json"
    candidate.parent.mkdir(mode=0o755, parents=True)
    (root / "build").chmod(0o755)
    candidate.write_bytes(canonical_json_bytes(schema))
    candidate.chmod(0o644)

    contracts = {
        "overlay": "1.1.0",
        "info": {"title": "synthetic", "version": "1"},
        "actions": [
            {
                "target": "$",
                "update": {},
                "x-iiko-sdk-guard": {
                    "issue": "synthetic-noop-contract",
                    "expected-matches": 1,
                    "expected-sha256": sha256_bytes(canonical_json_bytes(schema)),
                },
            }
        ],
    }
    _write_yaml(root / "openapi/overlays/contracts.overlay.yaml", contracts)
    _write_yaml(root / "build/bootstrap/types.overlay.yaml", build_types_overlay(schema))
    _write_yaml(
        root / "build/bootstrap/operation-ids.yaml",
        {"operations": {"POST /api/2/menu/by_id": "get_external_menu_by_id"}},
    )
    _write_yaml(root / "build/bootstrap/model-collisions.yaml", {"collisions": {}})
    _write_yaml(root / "openapi/model-name-overrides.yaml", {"models": {}})
    fixtures = root / "tests/fixtures/contracts"
    fixtures.mkdir(mode=0o755, parents=True)
    for directory in (
        root / "openapi",
        root / "openapi/overlays",
        root / "tests",
        root / "tests/fixtures",
        fixtures,
    ):
        directory.chmod(0o755)
    return RepoPaths(root)


def _write_private_captures(paths: RepoPaths) -> None:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    capture_root = paths.root / "private/captures"
    capture_root.mkdir(mode=0o700, parents=True)
    for parent in (paths.root / "private", capture_root):
        parent.chmod(0o700)
    for version, pair in pairs.items():
        operation = capture_root / f"synthetic-v{version}/get_external_menu_by_id"
        operation.mkdir(mode=0o700, parents=True)
        for parent in (operation.parent, operation):
            parent.chmod(0o700)
        for name, value in (("request.json", pair.request), ("response.json", pair.response)):
            path = operation / name
            path.write_bytes(canonical_json_bytes(_plain(value)))
            path.chmod(0o600)


def _fresh_manifest(paths: RepoPaths) -> EvidenceCandidateManifestResult:
    base, _mappings = compose_reviewed_evidence_base_candidate(paths)
    with LiveProcessLock(paths.state / "live.lock") as live_lock:
        pairs = CaptureEvidenceReader(
            paths.root,
            base,
            process_lock=live_lock,
        ).read_menu_pairs()
    analysis = analyze_menu_evidence(pairs, base)
    return build_evidence_candidate_manifest(
        build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=base,
        )
    )


def _prepared_repository(tmp_path: Path) -> tuple[RepoPaths, EvidenceCandidateManifestResult]:
    paths = _repository(tmp_path)
    _write_private_captures(paths)
    expected = _fresh_manifest(paths)
    write_evidence_candidate_tree(expected, paths)
    return paths, expected


def _candidate_snapshot(root: Path) -> dict[str, tuple[int, ...] | bytes]:
    result: dict[str, tuple[int, ...] | bytes] = {}
    for path in (root, *sorted(root.rglob("*"))):
        relative = path.relative_to(root).as_posix() if path != root else "."
        metadata = path.lstat()
        result[f"metadata:{relative}"] = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_uid,
            metadata.st_nlink,
            metadata.st_size,
        )
        if stat.S_ISREG(metadata.st_mode):
            result[f"body:{relative}"] = path.read_bytes()
    return result


@pytest.fixture(scope="module")
def detached_result(tmp_path_factory: pytest.TempPathFactory) -> EvidenceCandidateManifestResult:
    paths = _repository(tmp_path_factory.mktemp("accept-authority"))
    _write_private_captures(paths)
    return _fresh_manifest(paths)


def _write_candidate_direct(
    paths: RepoPaths,
    result: EvidenceCandidateManifestResult,
) -> Path:
    candidate_root = paths.build / "evidence-candidates"
    files = {
        "candidate-manifest.json": result.canonical_json_bytes,
        **dict(result.canonical_payloads),
    }
    for relative in files:
        parent = (candidate_root / relative).parent
        parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    for directory in (candidate_root, *candidate_root.rglob("*")):
        if directory.is_dir():
            directory.chmod(0o755)
    for relative, body in files.items():
        target = candidate_root / relative
        target.write_bytes(body)
        target.chmod(0o644)
    return candidate_root


def _stub_authority(
    monkeypatch: pytest.MonkeyPatch,
    result: EvidenceCandidateManifestResult,
    *,
    compose: Any | None = None,
) -> None:
    base = _reviewed_schema()

    class Reader:
        def __init__(
            self,
            repository_root: Path,
            effective_schema: dict[str, Any],
            *,
            process_lock: LiveProcessLock,
        ) -> None:
            assert repository_root.is_absolute()
            assert type(effective_schema) is dict
            assert process_lock.held

        def read_menu_pairs(self) -> object:
            return object()

    monkeypatch.setattr(
        accept_module,
        "compose_reviewed_evidence_base_candidate",
        compose or (lambda _paths: (base, {})),
    )
    monkeypatch.setattr(accept_module, "CaptureEvidenceReader", Reader)
    monkeypatch.setattr(accept_module, "analyze_menu_evidence", lambda _pairs, _base: object())
    monkeypatch.setattr(
        accept_module,
        "build_evidence_candidate_bundle",
        lambda **_kwargs: object(),
    )
    monkeypatch.setattr(
        accept_module,
        "build_evidence_candidate_manifest",
        lambda _bundle: result,
    )


def _write_targets(
    paths: RepoPaths,
    result: EvidenceCandidateManifestResult,
    *,
    body: bytes | None = None,
) -> dict[Path, bytes]:
    before: dict[Path, bytes] = {}
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        target = paths.root / relative
        target.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
        target.write_bytes(body if body is not None else result.canonical_payloads[relative])
        target.chmod(0o644)
        before[target] = target.read_bytes()
    return before


def _make_entry(path: Path, kind: str) -> None:
    if kind == "file":
        path.write_bytes(b"residue\n")
    elif kind == "directory":
        path.mkdir()
    elif kind == "symlink":
        path.symlink_to("missing-residue-target")
    elif kind == "fifo":
        os.mkfifo(path)
    else:  # pragma: no cover - test helper contract
        raise AssertionError(kind)


def test_public_accept_api_is_fixed_and_path_only(tmp_path: Path) -> None:
    assert [field.name for field in fields(EvidenceCandidateAcceptResult)] == [
        "candidate_root",
        "accepted_paths",
        "manifest_sha256",
        "changed",
    ]
    hints = get_type_hints(accept_evidence_candidate)
    assert hints == {
        "paths": RepoPaths,
        "return": EvidenceCandidateAcceptResult,
    }


def test_accept_full_real_pipeline_promotes_exact_five_and_reruns_as_noop(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths, expected = _prepared_repository(tmp_path)
    candidate_root = paths.build / "evidence-candidates"
    before = _candidate_snapshot(candidate_root)
    unrelated = paths.root / "unrelated.txt"
    unrelated.write_bytes(b"keep me\n")
    unrelated.chmod(0o644)

    accepted = accept_evidence_candidate(paths)

    exact_targets = tuple(paths.root / path for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS)
    assert accepted == EvidenceCandidateAcceptResult(
        candidate_root=candidate_root,
        accepted_paths=exact_targets,
        manifest_sha256=expected.sha256,
        changed=True,
    )
    assert tuple(path.read_bytes() for path in exact_targets) == tuple(
        expected.canonical_payloads[path] for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
    )
    assert all(stat.S_IMODE(path.lstat().st_mode) == 0o644 for path in exact_targets)
    assert not (paths.root / "candidate-manifest.json").exists()
    assert unrelated.read_bytes() == b"keep me\n"
    assert _candidate_snapshot(candidate_root) == before
    assert not list(paths.build.glob(".evidence-accept.tmp-*"))

    def unexpected_promotion(*_args: Any, **_kwargs: Any) -> None:
        raise AssertionError("no-op acceptance must not invoke promotion")

    monkeypatch.setattr(accept_module, "promote_transaction", unexpected_promotion)
    repeated = accept_evidence_candidate(paths)
    assert repeated.changed is False
    assert repeated.accepted_paths == exact_targets
    assert repeated.manifest_sha256 == expected.sha256
    assert _candidate_snapshot(candidate_root) == before


@pytest.mark.parametrize("mask", (0o077, 0o000))
def test_first_accept_creates_missing_contract_parent_as_owned_mode_0755(
    tmp_path: Path,
    mask: int,
) -> None:
    paths, expected = _prepared_repository(tmp_path)
    candidate_root = paths.build / "evidence-candidates"
    candidate_before = _candidate_snapshot(candidate_root)
    contracts = paths.root / "tests/fixtures/contracts"
    contracts.rmdir()

    previous = os.umask(mask)
    try:
        accepted = accept_evidence_candidate(paths)
    finally:
        os.umask(previous)

    metadata = contracts.lstat()
    assert accepted.changed is True
    assert stat.S_ISDIR(metadata.st_mode)
    assert not stat.S_ISLNK(metadata.st_mode)
    assert stat.S_IMODE(metadata.st_mode) == 0o755
    assert metadata.st_uid == os.getuid()
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        assert (paths.root / relative).read_bytes() == expected.canonical_payloads[relative]
    assert _candidate_snapshot(candidate_root) == candidate_before
    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_candidate_lock_contention_happens_before_live_state_creation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    assert not paths.state.exists()

    with (
        EvidenceCandidateProcessLock(paths),
        pytest.raises(SafetyError, match="candidate writer lock is already held"),
    ):
        accept_evidence_candidate(paths)

    assert not paths.state.exists()
    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_live_lock_contention_releases_candidate_without_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)

    with (
        LiveProcessLock(paths.state / "live.lock"),
        pytest.raises(SafetyError, match="another live test process is active"),
    ):
        accept_evidence_candidate(paths)

    assert not list(paths.build.glob(".evidence-accept.tmp-*"))
    with EvidenceCandidateProcessLock(paths):
        pass


def test_both_canonical_locks_are_held_during_the_single_promotion_call(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    calls = 0

    def checked_promotion(items: Any, *, root: Path) -> None:
        nonlocal calls
        calls += 1
        assert root == paths.root
        assert tuple(item.target for item in items) == tuple(
            paths.root / relative for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
        )
        assert tuple(item.staged.read_bytes() for item in items) == tuple(
            detached_result.canonical_payloads[relative]
            for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
        )
        assert all(stat.S_IMODE(item.staged.lstat().st_mode) == 0o644 for item in items)
        assert (
            len(
                {
                    next(path for path in item.staged.parents if path.parent == paths.build)
                    for item in items
                }
            )
            == 1
        )
        with pytest.raises(SafetyError, match="candidate writer lock is already held"):
            EvidenceCandidateProcessLock(paths).acquire()
        with pytest.raises(SafetyError, match="another live test process is active"):
            LiveProcessLock(paths.state / "competitor.lock").acquire()
        real_promote_transaction(items, root=root)

    monkeypatch.setattr(accept_module, "promote_transaction", checked_promotion)

    result = accept_evidence_candidate(paths)

    assert result.changed is True
    assert calls == 1


@pytest.mark.parametrize(
    "relative",
    ("candidate-manifest.json", EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]),
)
def test_candidate_manifest_or_payload_tamper_is_rejected_before_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
    relative: str,
) -> None:
    paths = _repository(tmp_path)
    candidate_root = _write_candidate_direct(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    target = candidate_root / relative
    target.write_bytes(target.read_bytes() + b"\n")
    target.chmod(0o644)

    with pytest.raises(SafetyError, match="candidate") as raised:
        accept_evidence_candidate(paths)

    assert "caller-private" not in str(raised.value)
    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_second_reviewed_base_composition_drift_is_rejected_sanitized(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    first = _reviewed_schema()
    second = _reviewed_schema()
    second["x-second-composition-drift"] = "caller-private-sensitive-marker"
    calls = 0

    def drifting_compose(_paths: RepoPaths) -> tuple[dict[str, Any], dict[str, str]]:
        nonlocal calls
        calls += 1
        return (first if calls == 1 else second), {}

    _stub_authority(monkeypatch, detached_result, compose=drifting_compose)

    with pytest.raises(
        SafetyError,
        match="^Reviewed evidence base changed during candidate acceptance$",
    ) as raised:
        accept_evidence_candidate(paths)

    assert calls == 2
    assert "caller-private-sensitive-marker" not in str(raised.value)
    assert raised.value.__cause__ is None
    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_changed_capture_provenance_builds_fresh_authority_and_rejects_stale_candidate(
    tmp_path: Path,
) -> None:
    paths, _expected = _prepared_repository(tmp_path)
    response = paths.root / "private/captures/synthetic-v2/get_external_menu_by_id/response.json"
    value = json.loads(response.read_text(encoding="utf-8"))
    value["body"]["floatValue"] = 7.5
    response.write_bytes(canonical_json_bytes(value))
    response.chmod(0o600)

    with pytest.raises(SafetyError, match="candidate"):
        accept_evidence_candidate(paths)

    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_changed_reviewed_raw_input_builds_fresh_authority_and_rejects_stale_candidate(
    tmp_path: Path,
) -> None:
    paths, _expected = _prepared_repository(tmp_path)
    raw = _reviewed_schema()
    raw["info"] = {"title": "changed reviewed base", "version": "1"}
    paths.candidate.write_bytes(canonical_json_bytes(raw))
    paths.candidate.chmod(0o644)
    contracts = {
        "overlay": "1.1.0",
        "info": {"title": "synthetic", "version": "1"},
        "actions": [
            {
                "target": "$",
                "update": {},
                "x-iiko-sdk-guard": {
                    "issue": "synthetic-noop-contract",
                    "expected-matches": 1,
                    "expected-sha256": sha256_bytes(canonical_json_bytes(raw)),
                },
            }
        ],
    }
    _write_yaml(paths.root / "openapi/overlays/contracts.overlay.yaml", contracts)
    _write_yaml(paths.root / "build/bootstrap/types.overlay.yaml", build_types_overlay(raw))

    with pytest.raises(SafetyError, match="candidate"):
        accept_evidence_candidate(paths)

    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


@pytest.mark.parametrize("kind", ("file", "directory", "symlink", "fifo"))
def test_accept_staging_residue_of_any_kind_blocks_even_exact_noop_before_authority(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
    kind: str,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _write_targets(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    residue = paths.build / f".evidence-accept.tmp-{kind}"
    _make_entry(residue, kind)
    monkeypatch.setattr(
        accept_module,
        "compose_reviewed_evidence_base_candidate",
        lambda _paths: (_ for _ in ()).throw(AssertionError("authority must not run")),
    )

    with pytest.raises(
        SafetyError,
        match="^Evidence acceptance residue requires operator resolution$",
    ):
        accept_evidence_candidate(paths)


@pytest.mark.parametrize("family", ("backup", "orphaned-backup"))
@pytest.mark.parametrize("kind", ("file", "directory", "symlink", "fifo"))
def test_promotion_backup_residue_of_any_kind_blocks_exact_noop_before_authority(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
    family: str,
    kind: str,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _write_targets(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    first = paths.root / EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    residue = first.with_name(f".{first.name}.{family}-{kind}")
    _make_entry(residue, kind)
    monkeypatch.setattr(
        accept_module,
        "compose_reviewed_evidence_base_candidate",
        lambda _paths: (_ for _ in ()).throw(AssertionError("authority must not run")),
    )

    with pytest.raises(
        SafetyError,
        match="^Evidence acceptance residue requires operator resolution$",
    ):
        accept_evidence_candidate(paths)


@pytest.mark.parametrize("kind", ("symlink", "directory", "fifo", "hardlink", "mode"))
def test_unsafe_existing_target_is_rejected_without_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
    kind: str,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _write_targets(paths, detached_result)
    _stub_authority(monkeypatch, detached_result)
    target = paths.root / EVIDENCE_CANDIDATE_PAYLOAD_PATHS[-1]
    if kind == "mode":
        target.chmod(0o600)
    else:
        target.unlink()
        if kind == "symlink":
            target.symlink_to(paths.root / "unrelated-target")
        elif kind == "directory":
            target.mkdir()
        elif kind == "fifo":
            os.mkfifo(target)
        else:
            source = paths.root / "hardlink-source"
            source.write_bytes(b"hardlinked\n")
            source.chmod(0o644)
            os.link(source, target)

    with pytest.raises(SafetyError, match="^Evidence acceptance target is unsafe$"):
        accept_evidence_candidate(paths)

    assert not list(paths.build.glob(".evidence-accept.tmp-*"))


def test_injected_mid_promotion_failure_rolls_back_and_preserves_blocking_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    candidate_root = _write_candidate_direct(paths, detached_result)
    candidate_before = _candidate_snapshot(candidate_root)
    before = _write_targets(paths, detached_result, body=b"reviewed old target\n")
    _stub_authority(monkeypatch, detached_result)
    original_replace = promotion_module.os.replace
    calls = 0

    def fail_once(source: Any, target: Any) -> None:
        nonlocal calls
        calls += 1
        if calls == 5:
            raise OSError("injected promotion boundary")
        original_replace(source, target)

    monkeypatch.setattr(promotion_module.os, "replace", fail_once)

    with pytest.raises(OSError, match="injected promotion boundary"):
        accept_evidence_candidate(paths)

    assert {path: path.read_bytes() for path in before} == before
    assert _candidate_snapshot(candidate_root) == candidate_before
    residues = list(paths.build.glob(".evidence-accept.tmp-*"))
    assert len(residues) == 1
    assert any(path.is_file() for path in residues[0].rglob("*"))
    with pytest.raises(
        SafetyError,
        match="^Evidence acceptance residue requires operator resolution$",
    ):
        accept_evidence_candidate(paths)


def test_keyboard_interrupt_from_real_transaction_is_rolled_back_and_not_masked(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    before = _write_targets(paths, detached_result, body=b"reviewed old target\n")
    _stub_authority(monkeypatch, detached_result)
    original_replace = promotion_module.os.replace
    calls = 0

    def interrupt_once(source: Any, target: Any) -> None:
        nonlocal calls
        calls += 1
        if calls == 5:
            raise KeyboardInterrupt
        original_replace(source, target)

    monkeypatch.setattr(promotion_module.os, "replace", interrupt_once)

    with pytest.raises(KeyboardInterrupt):
        accept_evidence_candidate(paths)

    assert {path: path.read_bytes() for path in before} == before
    assert len(list(paths.build.glob(".evidence-accept.tmp-*"))) == 1


def test_postcommit_orphan_is_reported_as_committed_with_residue(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    _write_candidate_direct(paths, detached_result)
    _write_targets(paths, detached_result, body=b"reviewed old target\n")
    _stub_authority(monkeypatch, detached_result)

    def fail_backup_removal(_path: Path) -> None:
        raise OSError("injected postcommit cleanup")

    monkeypatch.setattr(promotion_module, "_remove", fail_backup_removal)

    with pytest.raises(
        SafetyError,
        match=("^Evidence acceptance committed with residue; operator resolution is required$"),
    ) as raised:
        accept_evidence_candidate(paths)

    assert raised.value.__cause__ is None
    assert "injected" not in str(raised.value)
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        assert (paths.root / relative).read_bytes() == detached_result.canonical_payloads[relative]
    orphaned = [
        path
        for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
        for path in (paths.root / relative).parent.glob(
            f".{Path(relative).name}.orphaned-backup-*"
        )
    ]
    assert len(orphaned) == len(EVIDENCE_CANDIDATE_PAYLOAD_PATHS)
    assert len(list(paths.build.glob(".evidence-accept.tmp-*"))) == 1


def test_interrupt_after_backup_removal_commit_is_sanitized_and_blocks_retry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    candidate_root = _write_candidate_direct(paths, detached_result)
    candidate_before = _candidate_snapshot(candidate_root)
    _write_targets(paths, detached_result, body=b"reviewed old target\n")
    _stub_authority(monkeypatch, detached_result)
    real_remove = promotion_module._remove
    interrupted = False

    def interrupt_after_remove(path: Path) -> None:
        nonlocal interrupted
        real_remove(path)
        if not interrupted and ".backup-" in path.name:
            interrupted = True
            raise KeyboardInterrupt

    monkeypatch.setattr(promotion_module, "_remove", interrupt_after_remove)

    with pytest.raises(
        SafetyError,
        match=("^Evidence acceptance committed with residue; operator resolution is required$"),
    ) as raised:
        accept_evidence_candidate(paths)

    assert interrupted is True
    assert raised.value.__cause__ is None
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        assert (paths.root / relative).read_bytes() == detached_result.canonical_payloads[relative]
    assert _candidate_snapshot(candidate_root) == candidate_before
    assert len(list(paths.build.glob(".evidence-accept.tmp-*"))) == 1
    with pytest.raises(
        SafetyError,
        match="^Evidence acceptance residue requires operator resolution$",
    ):
        accept_evidence_candidate(paths)


def test_interrupt_after_orphan_rename_commit_is_sanitized_and_blocks_retry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    detached_result: EvidenceCandidateManifestResult,
) -> None:
    paths = _repository(tmp_path)
    candidate_root = _write_candidate_direct(paths, detached_result)
    candidate_before = _candidate_snapshot(candidate_root)
    _write_targets(paths, detached_result, body=b"reviewed old target\n")
    _stub_authority(monkeypatch, detached_result)
    real_remove = promotion_module._remove
    real_replace = promotion_module.os.replace
    interrupted = False

    def force_orphan(path: Path) -> None:
        if ".backup-" in path.name:
            raise OSError("injected cleanup failure")
        real_remove(path)

    def interrupt_after_orphan(source: Any, target: Any) -> None:
        nonlocal interrupted
        real_replace(source, target)
        if (
            not interrupted
            and ".backup-" in Path(source).name
            and ".orphaned-backup-" in Path(target).name
        ):
            interrupted = True
            raise KeyboardInterrupt

    monkeypatch.setattr(promotion_module, "_remove", force_orphan)
    monkeypatch.setattr(promotion_module.os, "replace", interrupt_after_orphan)

    with pytest.raises(
        SafetyError,
        match=("^Evidence acceptance committed with residue; operator resolution is required$"),
    ) as raised:
        accept_evidence_candidate(paths)

    assert interrupted is True
    assert raised.value.__cause__ is None
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        assert (paths.root / relative).read_bytes() == detached_result.canonical_payloads[relative]
    assert _candidate_snapshot(candidate_root) == candidate_before
    assert list(paths.root.rglob("*.orphaned-backup-*"))
    assert len(list(paths.build.glob(".evidence-accept.tmp-*"))) == 1
    with pytest.raises(
        SafetyError,
        match="^Evidence acceptance residue requires operator resolution$",
    ):
        accept_evidence_candidate(paths)
