from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

import tools.openapi_pipeline.cli as cli_module
from tools.openapi_pipeline import pipeline
from tools.openapi_pipeline.cli import build_parser, main
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.paths import RepoPaths


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
    assert parser.parse_args(["upstream-check"]).command == "upstream-check"
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
    promote = parser.parse_args(
        ["promote-evidence", "--operation", "get_external_menu_by_id"]
    )
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
    with pytest.raises(SystemExit):
        parser.parse_args(["verify", "--offline"])


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

    assert (
        main(["promote-evidence", "--operation", "get_external_menu_by_id"])
        == 0
    )
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
