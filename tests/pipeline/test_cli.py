from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

import tools.openapi_pipeline.cli as cli_module
from tools.openapi_pipeline import pipeline
from tools.openapi_pipeline.cli import build_parser, main
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.fetch import FetchResult
from tools.openapi_pipeline.paths import RepoPaths

OPENAPI_FIXTURES = Path(__file__).resolve().parents[1] / "fixtures/openapi"


def test_cli_exposes_only_explicit_pipeline_commands() -> None:
    parser = build_parser()
    subparsers: Any = parser._subparsers
    choices = subparsers._group_actions[0].choices
    assert set(choices) == {
        "bootstrap",
        "sync",
        "verify",
        "upstream-check",
        "capture-evidence",
        "discover-read-targets",
        "promote-evidence",
        "cleanup-orphans",
        "reset-circuit",
        "verify-no-secrets",
        "publish",
    }


def test_cli_pipeline_arguments_are_exact() -> None:
    parser = build_parser()

    assert parser.parse_args(["bootstrap"]).accept_current_upstream is False
    assert parser.parse_args(["bootstrap", "--accept-current-upstream"]).accept_current_upstream
    assert parser.parse_args(["sync"]).offline is False
    assert parser.parse_args(["sync", "--offline"]).offline is True
    assert parser.parse_args(["verify"]).command == "verify"
    assert vars(parser.parse_args(["upstream-check"])) == {
        "command": "upstream-check",
        "fail_on_drift": False,
    }
    assert vars(parser.parse_args(["upstream-check", "--fail-on-drift"])) == {
        "command": "upstream-check",
        "fail_on_drift": True,
    }
    capture = parser.parse_args(
        [
            "capture-evidence",
            "--live-profile",
            "test-server",
            "--env-file",
            ".env",
            "--operation",
            "get_external_menu_by_id",
            "--menu-version",
            "4",
        ]
    )
    assert vars(capture) == {
        "command": "capture-evidence",
        "live_profile": "test-server",
        "env_file": ".env",
        "operation": "get_external_menu_by_id",
        "menu_version": 4,
    }
    discovery = parser.parse_args(
        [
            "discover-read-targets",
            "--live-profile",
            "test-server",
            "--env-file",
            ".env",
        ]
    )
    assert vars(discovery) == {
        "command": "discover-read-targets",
        "live_profile": "test-server",
        "env_file": ".env",
    }
    cleanup = parser.parse_args(
        [
            "cleanup-orphans",
            "--live-profile",
            "test-server",
        ]
    )
    assert vars(cleanup) == {
        "command": "cleanup-orphans",
        "live_profile": "test-server",
        "env_file": None,
    }
    cleanup_with_env = parser.parse_args(
        [
            "cleanup-orphans",
            "--live-profile",
            "test-server",
            "--env-file",
            ".env",
        ]
    )
    assert vars(cleanup_with_env) == {
        "command": "cleanup-orphans",
        "live_profile": "test-server",
        "env_file": ".env",
    }
    promote = parser.parse_args(["promote-evidence", "--operation", "get_external_menu_by_id"])
    assert vars(promote) == {
        "command": "promote-evidence",
        "operation": "get_external_menu_by_id",
        "accept": False,
    }
    accepted = parser.parse_args(
        [
            "promote-evidence",
            "--operation",
            "get_external_menu_by_id",
            "--accept",
        ]
    )
    assert vars(accepted) == {
        "command": "promote-evidence",
        "operation": "get_external_menu_by_id",
        "accept": True,
    }
    assert vars(parser.parse_args(["verify-no-secrets"])) == {
        "command": "verify-no-secrets",
        "create_baseline": False,
    }
    assert vars(parser.parse_args(["verify-no-secrets", "--create-baseline"])) == {
        "command": "verify-no-secrets",
        "create_baseline": True,
    }
    assert vars(parser.parse_args(["publish", "--version", "1.2.3"])) == {
        "command": "publish",
        "version": "1.2.3",
        "push": False,
    }
    assert vars(parser.parse_args(["publish", "--version", "1.2.3", "--push"])) == {
        "command": "publish",
        "version": "1.2.3",
        "push": True,
    }
    with pytest.raises(SystemExit):
        parser.parse_args(["verify", "--offline"])

    subparsers: Any = parser._subparsers
    choices = subparsers._group_actions[0].choices
    assert "--fail-on-drift" in choices["upstream-check"]._option_string_actions
    assert all(
        "--fail-on-drift" not in command_parser._option_string_actions
        for command, command_parser in choices.items()
        if command != "upstream-check"
    )


def _offline_upstream_dependencies(
    tmp_path: Path,
    *,
    committed_fixture: str,
    candidate_fixture: str,
) -> SimpleNamespace:
    paths = RepoPaths(tmp_path)
    paths.upstream.parent.mkdir(parents=True)
    paths.upstream.write_bytes((OPENAPI_FIXTURES / committed_fixture).read_bytes())
    candidate = OPENAPI_FIXTURES / candidate_fixture
    return SimpleNamespace(
        paths=paths,
        fetch=lambda: FetchResult("0" * 64, candidate, True),
    )


def test_upstream_check_manual_drift_writes_reports_without_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    dependencies = _offline_upstream_dependencies(
        tmp_path,
        committed_fixture="minimal-v1.json",
        candidate_fixture="minimal-v2.json",
    )
    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: dependencies,
    )

    assert main(["upstream-check"]) == 0

    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == ""
    assert (tmp_path / "build/reports/upstream-diff.json").is_file()
    assert (tmp_path / "build/reports/upstream-diff.md").is_file()


def test_upstream_check_fail_on_drift_writes_reports_before_sanitized_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    dependencies = _offline_upstream_dependencies(
        tmp_path,
        committed_fixture="minimal-v1.json",
        candidate_fixture="minimal-v2.json",
    )
    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: dependencies,
    )

    assert main(["upstream-check", "--fail-on-drift"]) == 2

    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == (
        "error: Upstream OpenAPI drift detected; review build/reports/upstream-diff.*\n"
    )
    assert (tmp_path / "build/reports/upstream-diff.json").is_file()
    assert (tmp_path / "build/reports/upstream-diff.md").is_file()


def test_upstream_check_fail_on_drift_succeeds_for_unchanged_fixture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    dependencies = _offline_upstream_dependencies(
        tmp_path,
        committed_fixture="minimal-v1.json",
        candidate_fixture="minimal-v1.json",
    )
    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: dependencies,
    )

    assert main(["upstream-check", "--fail-on-drift"]) == 0

    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == ""
    assert (tmp_path / "build/reports/upstream-diff.json").is_file()
    markdown = (tmp_path / "build/reports/upstream-diff.md").read_text(encoding="utf-8")
    assert markdown.count("- No changes") == 3


@pytest.mark.parametrize(
    "arguments",
    [
        ("verify-no-secrets", "--force"),
        ("publish",),
        ("publish", "--push"),
        ("publish", "--version", "1.2.3", "--force"),
        ("publish", "--version", "1.2.3", "--allow-protected-branch"),
    ],
)
def test_security_and_publish_commands_reject_unapproved_arguments(
    arguments: tuple[str, ...],
) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(arguments)


@pytest.mark.parametrize(
    "arguments",
    [
        (),
        ("--live-profile", "test-server"),
        (
            "--live-profile",
            "test-server",
            "--env-file",
            ".env",
            "--operation",
            "get_organizations",
            "--menu-version",
            "2",
        ),
        (
            "--live-profile",
            "test-server",
            "--env-file",
            ".env",
            "--operation",
            "get_external_menu_by_id",
            "--menu-version",
            "1",
        ),
    ],
)
def test_capture_evidence_rejects_missing_or_unapproved_arguments(
    arguments: tuple[str, ...],
) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(("capture-evidence", *arguments))


@pytest.mark.parametrize(
    "arguments",
    [
        (),
        ("--live-profile", "test-server"),
        ("--env-file", ".env"),
        ("--live-profile", "test-server", "--env-file", ".env", "--extra"),
    ],
)
def test_discover_read_targets_requires_exact_arguments(
    arguments: tuple[str, ...],
) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(("discover-read-targets", *arguments))


@pytest.mark.parametrize(
    "arguments",
    [
        (),
        ("--env-file", ".env"),
        ("--live-profile", "test-server", "--env-file"),
        ("--live-profile", "test-server", "--extra"),
    ],
)
def test_cleanup_orphans_requires_exact_arguments(
    arguments: tuple[str, ...],
) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(("cleanup-orphans", *arguments))


@pytest.mark.parametrize(
    "arguments",
    [
        (),
        ("--operation", "get_organizations"),
        (
            "--operation",
            "get_external_menu_by_id",
            "--live-profile",
            "test-server",
        ),
        (
            "--operation",
            "get_external_menu_by_id",
            "--menu-version",
            "4",
        ),
        ("--operation", "get_external_menu_by_id", "--force"),
    ],
)
def test_promote_evidence_rejects_missing_or_unapproved_arguments(
    arguments: tuple[str, ...],
) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(("promote-evidence", *arguments))


def test_main_lazy_dispatches_exact_sync_args(monkeypatch: pytest.MonkeyPatch) -> None:
    dependencies = object()
    calls: list[tuple[str, object]] = []

    def build_dependencies(*, offline: bool) -> object:
        calls.append(("dependencies", offline))
        return dependencies

    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        build_dependencies,
    )
    monkeypatch.setattr(
        pipeline,
        "sync",
        lambda value: calls.append(("sync", value)),
    )

    assert main(["sync", "--offline"]) == 0
    assert calls == [("dependencies", True), ("sync", dependencies)]


def test_main_catches_only_pipeline_errors(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: (_ for _ in ()).throw(PipelineError(f"offline={offline}")),
    )

    assert main(["verify"]) == 2
    assert capsys.readouterr().err == "error: offline=True\n"

    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: (_ for _ in ()).throw(ValueError(f"offline={offline}")),
    )
    with pytest.raises(ValueError, match="offline=True"):
        main(["verify"])


def test_main_dispatches_capture_evidence_and_handles_pipeline_error(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from tools.openapi_pipeline import evidence

    calls: list[dict[str, object]] = []

    async def capture(**kwargs: object) -> None:
        calls.append(kwargs)

    monkeypatch.setattr(evidence, "capture_evidence", capture)
    arguments = [
        "capture-evidence",
        "--live-profile",
        "test-server",
        "--env-file",
        ".env",
        "--operation",
        "get_external_menu_by_id",
        "--menu-version",
        "3",
    ]

    assert main(arguments) == 0
    assert calls == [
        {
            "live_profile": "test-server",
            "env_file": ".env",
            "operation": "get_external_menu_by_id",
            "menu_version": 3,
        }
    ]

    async def fail(**kwargs: object) -> None:
        raise PipelineError("evidence is disabled")

    monkeypatch.setattr(evidence, "capture_evidence", fail)
    assert main(arguments) == 2
    assert capsys.readouterr().err == "error: evidence is disabled\n"


def test_main_dispatches_discovery_and_renders_only_fixed_json(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from tools.openapi_pipeline import discovery

    result = discovery.DiscoveryResult(
        organizations=(
            discovery.DiscoveredOrganization(
                id="org-1",
                name="Организация",
                terminal_groups=(
                    discovery.DiscoveredTerminalGroup(
                        id="terminal-1",
                        name="Касса",
                        is_sleeping=False,
                    ),
                ),
            ),
        ),
        external_menus=(discovery.DiscoveredNamedTarget(id="menu-1", name="Меню"),),
    )
    calls: list[dict[str, object]] = []

    async def discover(**kwargs: object) -> discovery.DiscoveryResult:
        calls.append(kwargs)
        return result

    monkeypatch.setattr(discovery, "discover_read_targets", discover)

    assert (
        main(
            [
                "discover-read-targets",
                "--live-profile",
                "test-server",
                "--env-file",
                ".env",
            ]
        )
        == 0
    )
    assert calls == [{"live_profile": "test-server", "env_file": ".env"}]
    assert capsys.readouterr().out == discovery.render_discovery_result(result) + "\n"


def test_main_dispatches_cleanup_orphans_without_rendering_private_state(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from tools.openapi_pipeline import orphan_cleanup

    calls: list[dict[str, object]] = []

    async def cleanup(**kwargs: object) -> int:
        calls.append(kwargs)
        return 2

    monkeypatch.setattr(orphan_cleanup, "cleanup_orphans_command", cleanup)
    arguments = [
        "cleanup-orphans",
        "--live-profile",
        "test-server",
        "--env-file",
        ".env",
    ]

    assert main(arguments) == 0
    assert calls == [{"live_profile": "test-server", "env_file": ".env"}]
    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == ""

    async def fail(**_kwargs: object) -> int:
        raise PipelineError("orphan cleanup unavailable")

    monkeypatch.setattr(orphan_cleanup, "cleanup_orphans_command", fail)
    assert main(arguments) == 2
    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == "error: orphan cleanup unavailable\n"


def test_main_builds_only_a_detached_evidence_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from tools.openapi_pipeline import evidence, evidence_candidate_accept

    paths = RepoPaths(tmp_path)
    calls: list[tuple[str, object]] = []
    monkeypatch.setattr(cli_module.RepoPaths, "discover", lambda: paths)
    monkeypatch.setattr(
        evidence,
        "build_evidence_candidate",
        lambda received, *, operation: calls.append((operation, received)),
        raising=False,
    )
    monkeypatch.setattr(
        evidence_candidate_accept,
        "accept_evidence_candidate",
        lambda _paths: (_ for _ in ()).throw(AssertionError("accept must not run")),
    )

    assert main(["promote-evidence", "--operation", "get_external_menu_by_id"]) == 0
    output = capsys.readouterr()
    assert calls == [("get_external_menu_by_id", paths)]
    assert output.out == (
        "evidence candidate ready for review at build/evidence-candidates; "
        "tracked files unchanged\n"
    )
    assert output.err == ""


def test_main_accepts_only_an_already_reviewed_evidence_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from tools.openapi_pipeline import evidence, evidence_candidate_accept

    paths = RepoPaths(tmp_path)
    calls: list[RepoPaths] = []
    monkeypatch.setattr(cli_module.RepoPaths, "discover", lambda: paths)
    monkeypatch.setattr(
        evidence,
        "build_evidence_candidate",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("candidate rebuild must not run")
        ),
        raising=False,
    )
    monkeypatch.setattr(
        evidence_candidate_accept,
        "accept_evidence_candidate",
        lambda received: calls.append(received),
    )

    assert (
        main(
            [
                "promote-evidence",
                "--operation",
                "get_external_menu_by_id",
                "--accept",
            ]
        )
        == 0
    )
    output = capsys.readouterr()
    assert calls == [paths]
    assert output.out == "reviewed evidence accepted into tracked overlays and fixtures\n"
    assert output.err == ""


@pytest.mark.parametrize("accept", [False, True])
def test_main_sanitizes_promote_evidence_pipeline_errors(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    accept: bool,
) -> None:
    from tools.openapi_pipeline import evidence, evidence_candidate_accept

    paths = RepoPaths(tmp_path)
    monkeypatch.setattr(cli_module.RepoPaths, "discover", lambda: paths)

    def fail(*_args: object, **_kwargs: object) -> None:
        raise PipelineError("reviewed evidence is unavailable")

    monkeypatch.setattr(evidence, "build_evidence_candidate", fail, raising=False)
    monkeypatch.setattr(evidence_candidate_accept, "accept_evidence_candidate", fail)
    arguments = ["promote-evidence", "--operation", "get_external_menu_by_id"]
    if accept:
        arguments.append("--accept")

    assert main(arguments) == 2
    output = capsys.readouterr()
    assert output.out == ""
    assert output.err == "error: reviewed evidence is unavailable\n"


def test_main_dispatches_secret_verification_and_baseline_creation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from tools.openapi_pipeline import secrets

    paths = RepoPaths(tmp_path)
    calls: list[tuple[str, object]] = []
    known_secrets = ("known-secret",)

    def load_known_secrets(root: Path) -> tuple[str, ...]:
        calls.append(("load", root))
        return known_secrets

    monkeypatch.setattr(cli_module.RepoPaths, "discover", lambda: paths)
    monkeypatch.setattr(
        secrets,
        "load_known_secrets",
        load_known_secrets,
    )
    monkeypatch.setattr(
        secrets,
        "verify_no_secrets",
        lambda root, values: calls.append(("verify", (root, values))),
    )
    monkeypatch.setattr(
        secrets,
        "create_secrets_baseline",
        lambda root: calls.append(("baseline", root)),
    )

    assert main(["verify-no-secrets"]) == 0
    assert calls == [
        ("load", tmp_path),
        ("verify", (tmp_path, known_secrets)),
    ]
    assert capsys.readouterr().out == "secret verification passed\n"

    calls.clear()
    assert main(["verify-no-secrets", "--create-baseline"]) == 0
    assert calls == [("baseline", tmp_path)]
    assert capsys.readouterr().out == "secret baseline created; audit it before use\n"


def test_main_dispatches_publish_with_only_version_and_push(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from tools.openapi_pipeline import publish as publish_module

    paths = RepoPaths(tmp_path)
    calls: list[tuple[Path, str, bool]] = []
    monkeypatch.setattr(cli_module.RepoPaths, "discover", lambda: paths)
    monkeypatch.setattr(
        publish_module,
        "publish",
        lambda root, *, version, push=False: calls.append((root, version, push)),
    )

    assert main(["publish", "--version", "1.2.3", "--push"]) == 0
    assert calls == [(tmp_path, "1.2.3", True)]
