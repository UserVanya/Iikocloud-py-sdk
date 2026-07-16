from tools.openapi_pipeline.cli import build_parser


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
