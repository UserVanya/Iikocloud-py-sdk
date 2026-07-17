from __future__ import annotations

import pytest

from tools.openapi_pipeline import pipeline
from tools.openapi_pipeline.cli import build_parser, main
from tools.openapi_pipeline.errors import PipelineError


def test_cli_exposes_only_explicit_pipeline_commands() -> None:
    parser = build_parser()
    choices = parser._subparsers._group_actions[0].choices  # type: ignore[attr-defined]
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


def test_main_lazy_dispatches_exact_sync_args(monkeypatch: pytest.MonkeyPatch) -> None:
    dependencies = object()
    calls: list[tuple[str, object]] = []
    monkeypatch.setattr(
        pipeline,
        "default_dependencies",
        lambda *, offline: calls.append(("dependencies", offline)) or dependencies,
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
