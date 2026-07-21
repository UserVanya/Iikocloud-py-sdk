from __future__ import annotations

import shutil
import subprocess
import traceback
from collections.abc import Iterable, Sequence
from datetime import date
from pathlib import Path
from typing import Any

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.receipt import LiveArtifactHashes, LiveReceipt
from tools.openapi_pipeline.publish import PublishDependencies


def _git(root: Path, *arguments: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *arguments],
        cwd=root,
        check=True,
        capture_output=True,
        shell=False,
    )


def _repository(tmp_path: Path, *, branch: str = "release/test") -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "-b", branch)
    _git(root, "config", "user.name", "Publish Test")
    _git(root, "config", "user.email", "publish@example.invalid")
    (root / ".gitignore").write_text("private/\n.state/\nbuild/\n", encoding="utf-8")
    (root / "pyproject.toml").write_text(
        '[project]\nname = "fixture"\nversion = "1.2.3"\n',
        encoding="utf-8",
    )
    _git(root, "add", "--", ".gitignore", "pyproject.toml")
    _git(root, "commit", "-m", "initial")
    return root


def _output(root: Path, *arguments: str) -> str:
    return _git(root, *arguments).stdout.decode("utf-8").strip()


class _RecordingRunner:
    def __init__(self, *, fail_command: str | None = None) -> None:
        self.calls: list[tuple[str, ...]] = []
        self.pushes: list[tuple[str, ...]] = []
        self.fail_command = fail_command

    def __call__(
        self,
        command: Sequence[str],
        **kwargs: Any,
    ) -> subprocess.CompletedProcess[bytes]:
        argv = tuple(command)
        self.calls.append(argv)
        assert argv[0] == "git"
        assert kwargs["check"] is True
        assert kwargs["shell"] is False
        if self.fail_command is not None and self.fail_command in argv:
            raise subprocess.CalledProcessError(1, argv, stderr=b"private-git-failure")
        if argv[1:2] == ("push",):
            self.pushes.append(argv)
            return subprocess.CompletedProcess(argv, 0, stdout=b"", stderr=b"")
        return subprocess.run(command, **kwargs)


def _dependencies(
    events: list[str],
    runner: _RecordingRunner,
    *,
    fail_gate: str | None = None,
    output: list[str] | None = None,
) -> PublishDependencies:

    scan_count = 0

    def gate(name: str) -> None:
        events.append(name)
        if fail_gate == name:
            raise RuntimeError("private-gate-failure")

    def receipt_gate(_root: Path) -> str:
        gate("receipt")
        return "a" * 64

    def circuit_gate(_root: Path, fingerprint: str) -> None:
        assert fingerprint == "a" * 64
        gate("circuit")

    def secret_scan(_root: Path, known_secrets: Iterable[str]) -> None:
        nonlocal scan_count
        scan_count += 1
        assert tuple(known_secrets) == ("private-known-secret",)
        gate(f"secret-{scan_count}")

    def wheel_smoke(root: Path) -> None:
        assert 'version = "1.2.3"' in (root / "pyproject.toml").read_text(encoding="utf-8")
        gate("wheel")

    def load_known_secrets(_root: Path) -> tuple[str, ...]:
        gate("known-secrets")
        return ("private-known-secret",)

    def emit(line: str) -> None:
        events.append("emit")
        if output is not None:
            output.append(line)

    return PublishDependencies(
        git_runner=runner,
        lock_check=lambda _root: gate("lock"),
        offline_verify=lambda _root: gate("verify"),
        runtime_version_gate=lambda _root, _version: gate("runtime-version"),
        receipt_gate=receipt_gate,
        circuit_gate=circuit_gate,
        mutation_gate=lambda _root: gate("mutations"),
        known_secrets_loader=load_known_secrets,
        secret_scan=secret_scan,
        wheel_smoke=wheel_smoke,
        emit=emit,
        today=lambda: date(2026, 7, 21),
    )


def test_publishable_paths_accept_only_exact_canonical_allowlist_members() -> None:
    from tools.openapi_pipeline.publish import assert_publishable_paths

    assert_publishable_paths(
        [
            "openapi/upstream/iikocloud.openapi.json",
            "src/iikocloud_client/api_client.py",
            "tests/generated/test_model.py",
            "docs/generation.md",
            "README.md",
            "pyproject.toml",
            "uv.lock",
        ]
    )

    rejected: Sequence[str] = (
        "private/captures/run/response.json",
        ".state/live-runs/receipt.json",
        "notes.txt",
        "./openapi/schema.json",
        "openapi/../notes.txt",
        "openapi//schema.json",
        "openapi\\schema.json",
        "/openapi/schema.json",
        "openapi",
    )
    for path in rejected:
        with pytest.raises(SafetyError):
            assert_publishable_paths([path])


def test_version_update_requires_strict_semver_and_one_exact_pep621_line(
    tmp_path: Path,
) -> None:
    from tools.openapi_pipeline.publish import update_project_version

    root = tmp_path / "project"
    root.mkdir()
    project = root / "pyproject.toml"
    project.write_text(
        '[project]\nname = "fixture"\nversion = "0.1.0"\n\n[tool.example]\nversion = "9"\n',
        encoding="utf-8",
    )

    original = update_project_version(root, "0.1.0")

    assert original.startswith(b"[project]\n")
    assert project.read_text(encoding="utf-8") == (
        '[project]\nname = "fixture"\nversion = "0.1.0"\n\n[tool.example]\nversion = "9"\n'
    )

    stable = project.read_bytes()
    for invalid in ("01.2.4", "1.2.3-01", "1.2.3+"):
        with pytest.raises(SafetyError, match="SemVer"):
            update_project_version(root, invalid)
        assert project.read_bytes() == stable

    with pytest.raises(SafetyError, match="before generation"):
        update_project_version(root, "1.2.3")
    assert project.read_bytes() == stable

    project.write_text('[project]\nversion="1.2.3"\n', encoding="utf-8")
    malformed = project.read_bytes()
    with pytest.raises(SafetyError, match="version line"):
        update_project_version(root, "1.2.4")
    assert project.read_bytes() == malformed


def test_protected_branch_requires_strict_ignored_private_opt_in(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import assert_publish_branch

    root = _repository(tmp_path, branch="main")

    with pytest.raises(SafetyError, match="protected"):
        assert_publish_branch(root)

    private = root / "private"
    private.mkdir()
    opt_in = private / "publish.toml"
    opt_in.write_text("allow_protected_branch = true\n", encoding="utf-8")

    assert_publish_branch(root)

    opt_in.write_text(
        "allow_protected_branch = true\nunexpected = true\n",
        encoding="utf-8",
    )
    with pytest.raises(SafetyError, match="protected"):
        assert_publish_branch(root)


def test_private_opt_in_must_be_ignored(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import assert_publish_branch

    root = _repository(tmp_path, branch="main")
    (root / ".gitignore").write_text(".state/\nbuild/\n", encoding="utf-8")
    private = root / "private"
    private.mkdir()
    (private / "publish.toml").write_text(
        "allow_protected_branch = true\n",
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="protected"):
        assert_publish_branch(root)


def test_publish_blocks_unrelated_and_forced_private_paths_before_gates_or_mutations(
    tmp_path: Path,
) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("VALUE = 1\n", encoding="utf-8")
    unrelated = root / "notes.txt"
    unrelated.write_text("not releasable\n", encoding="utf-8")
    events: list[str] = []
    runner = _RecordingRunner()
    dependencies = _dependencies(events, runner)
    initial_head = _output(root, "rev-parse", "HEAD")
    initial_project = (root / "pyproject.toml").read_bytes()

    with pytest.raises(SafetyError, match="notes.txt"):
        publish(root, version="1.2.3", dependencies=dependencies)

    assert events == []
    assert _output(root, "rev-parse", "HEAD") == initial_head
    assert _output(root, "tag", "--list") == ""
    assert (root / "pyproject.toml").read_bytes() == initial_project

    unrelated.unlink()
    private = root / "private/captures/response.json"
    private.parent.mkdir(parents=True)
    private.write_text("{}\n", encoding="utf-8")
    _git(root, "add", "-f", "--", "private/captures/response.json")

    with pytest.raises(SafetyError, match="private/captures"):
        publish(root, version="1.2.3", dependencies=dependencies)

    assert events == []
    assert _output(root, "rev-parse", "HEAD") == initial_head
    assert _output(root, "tag", "--list") == ""
    assert (root / "pyproject.toml").read_bytes() == initial_project


def test_publish_rejects_nonempty_index_without_changing_staged_blob(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("STAGED = 1\n", encoding="utf-8")
    _git(root, "add", "--", "src/iikocloud_client/generated.py")
    staged_before = _git(
        root,
        "show",
        ":src/iikocloud_client/generated.py",
    ).stdout
    generated.write_text("WORKTREE = 2\n", encoding="utf-8")
    events: list[str] = []

    with pytest.raises(SafetyError, match="index"):
        publish(
            root,
            version="1.2.3",
            dependencies=_dependencies(events, _RecordingRunner()),
        )

    assert events == []
    assert _git(root, "show", ":src/iikocloud_client/generated.py").stdout == staged_before


@pytest.mark.parametrize(
    "fail_gate",
    [
        "lock",
        "verify",
        "runtime-version",
        "receipt",
        "circuit",
        "mutations",
        "known-secrets",
        "secret-1",
        "wheel",
    ],
)
def test_precommit_gate_failure_is_sanitized_and_restores_version(
    tmp_path: Path,
    fail_gate: str,
) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("VALUE = 1\n", encoding="utf-8")
    events: list[str] = []
    dependencies = _dependencies(events, _RecordingRunner(), fail_gate=fail_gate)
    initial_head = _output(root, "rev-parse", "HEAD")
    initial_project = (root / "pyproject.toml").read_bytes()

    with pytest.raises(SafetyError) as caught:
        publish(root, version="1.2.3", dependencies=dependencies)

    rendered = "".join(traceback.format_exception(caught.value))
    assert "private-gate-failure" not in rendered
    assert _output(root, "rev-parse", "HEAD") == initial_head
    assert _output(root, "tag", "--list") == ""
    assert (root / "pyproject.toml").read_bytes() == initial_project
    assert _output(root, "diff", "--cached", "--name-only") == ""


def test_post_stage_scan_failure_unstages_and_restores_release_version(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("VALUE = 1\n", encoding="utf-8")
    events: list[str] = []
    dependencies = _dependencies(events, _RecordingRunner(), fail_gate="secret-2")
    initial_head = _output(root, "rev-parse", "HEAD")
    initial_project = (root / "pyproject.toml").read_bytes()

    with pytest.raises(SafetyError):
        publish(root, version="1.2.3", dependencies=dependencies)

    assert "secret-2" in events
    assert _output(root, "rev-parse", "HEAD") == initial_head
    assert _output(root, "tag", "--list") == ""
    assert (root / "pyproject.toml").read_bytes() == initial_project
    assert _output(root, "diff", "--cached", "--name-only") == ""


def test_publish_creates_one_commit_annotated_tag_and_only_two_stubbed_pushes(
    tmp_path: Path,
) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("VALUE = 1\n", encoding="utf-8")
    events: list[str] = []
    output: list[str] = []
    runner = _RecordingRunner()
    dependencies = _dependencies(events, runner, output=output)
    initial_count = int(_output(root, "rev-list", "--count", "HEAD"))

    publish(root, version="1.2.3", push=True, dependencies=dependencies)

    assert int(_output(root, "rev-list", "--count", "HEAD")) == initial_count + 1
    assert _output(root, "log", "-1", "--pretty=%s") == (
        "chore(sdk): sync iiko OpenAPI 2026-07-21"
    )
    assert _output(root, "tag", "--list") == "v1.2.3"
    assert _output(root, "cat-file", "-t", "v1.2.3") == "tag"
    assert runner.pushes == [
        ("git", "push", "origin", "HEAD"),
        ("git", "push", "origin", "v1.2.3"),
    ]
    assert _output(root, "status", "--porcelain") == ""
    assert events.count("secret-1") == 1
    assert events.count("secret-2") == 1
    assert events.index("lock") < events.index("verify") < events.index("runtime-version")
    assert events.index("runtime-version") < events.index("receipt") < events.index("circuit")
    assert events.index("circuit") < events.index("mutations") < events.index("secret-1")
    assert events.index("secret-1") < events.index("wheel") < events.index("secret-2")
    rendered = "\n".join(output)
    assert "src/iikocloud_client/generated.py" in rendered
    assert "private-known-secret" not in rendered
    assert not any("--force" in argument for call in runner.calls for argument in call)


def test_git_commit_failure_is_sanitized_and_creates_no_commit_or_tag(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import publish

    root = _repository(tmp_path)
    generated = root / "src/iikocloud_client/generated.py"
    generated.parent.mkdir(parents=True)
    generated.write_text("VALUE = 1\n", encoding="utf-8")
    runner = _RecordingRunner(fail_command="commit")
    dependencies = _dependencies([], runner)
    initial_head = _output(root, "rev-parse", "HEAD")
    initial_project = (root / "pyproject.toml").read_bytes()

    with pytest.raises(SafetyError) as caught:
        publish(root, version="1.2.3", dependencies=dependencies)

    assert "private-git-failure" not in "".join(traceback.format_exception(caught.value))
    assert _output(root, "rev-parse", "HEAD") == initial_head
    assert _output(root, "tag", "--list") == ""
    assert (root / "pyproject.toml").read_bytes() == initial_project
    assert _output(root, "diff", "--cached", "--name-only") == ""


def _receipt(
    run_id: str,
    artifacts: LiveArtifactHashes,
    *,
    completed: bool,
) -> LiveReceipt:
    return LiveReceipt(
        run_id=run_id,
        profile_fingerprint="a" * 64,
        effective_schema_sha256=artifacts.effective_schema_sha256,
        generated_tree_sha256=artifacts.generated_tree_sha256,
        live_contracts_sha256=artifacts.live_contracts_sha256,
        operations=("authenticate", "get_organizations") if completed else (),
        had_429=False,
        completed=completed,
    )


def test_matching_receipt_gate_strictly_loads_all_residue_and_selects_latest(
    tmp_path: Path,
) -> None:
    from tools.openapi_pipeline.publish import select_matching_live_receipt

    artifacts = LiveArtifactHashes("b" * 64, "c" * 64, "d" * 64)
    runs = tmp_path / ".state/live-runs"
    older = _receipt("20260720T100000Z-a1b2c3d4", artifacts, completed=True)
    newer = _receipt("20260721T100000Z-a1b2c3d4", artifacts, completed=True)
    incomplete = _receipt("20260722T100000Z-a1b2c3d4", artifacts, completed=False)
    stale_contract = _receipt(
        "20260723T100000Z-a1b2c3d4",
        LiveArtifactHashes("b" * 64, "c" * 64, "e" * 64),
        completed=True,
    )
    older.write(runs / f"{older.run_id}.json")
    newer.write(runs / f"{newer.run_id}.json")
    incomplete.write(runs / f"{incomplete.run_id}.json")
    stale_contract.write(runs / f"{stale_contract.run_id}.json")

    selected = select_matching_live_receipt(tmp_path, artifacts)

    assert selected == newer

    invalid = runs / "invalid.json"
    invalid.write_text("{}\n", encoding="utf-8")
    invalid.chmod(0o600)
    with pytest.raises(SafetyError, match="receipt"):
        select_matching_live_receipt(tmp_path, artifacts)


def test_default_lock_gate_rejects_project_version_drift(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import _default_lock_check

    repository = Path(__file__).resolve().parents[2]
    root = tmp_path / "project"
    root.mkdir()
    for name in ("pyproject.toml", "uv.lock", "README.md"):
        shutil.copy2(repository / name, root / name)

    _default_lock_check(root)
    project = root / "pyproject.toml"
    project.write_text(
        project.read_text(encoding="utf-8").replace(
            'version = "0.1.0"',
            'version = "9.9.9"',
            1,
        ),
        encoding="utf-8",
    )

    with pytest.raises(SafetyError, match="lock"):
        _default_lock_check(root)


def test_generated_runtime_version_gate_checks_all_embedded_locations(tmp_path: Path) -> None:
    from tools.openapi_pipeline.publish import assert_generated_runtime_version

    package = tmp_path / "src/iikocloud_client"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
    (package / "api_client.py").write_text(
        "self.user_agent = 'OpenAPI-Generator/1.2.3/python'\n",
        encoding="utf-8",
    )
    (package / "configuration.py").write_text(
        'report = "SDK Package Version: 1.2.3"\n',
        encoding="utf-8",
    )

    assert_generated_runtime_version(tmp_path, "1.2.3")
    with pytest.raises(SafetyError, match="runtime version"):
        assert_generated_runtime_version(tmp_path, "1.2.4")
