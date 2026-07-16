from __future__ import annotations

import argparse
from collections.abc import Sequence

from .errors import PipelineError

COMMANDS = (
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
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m tools.openapi_pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in COMMANDS:
        subparsers.add_parser(command)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    raise PipelineError(f"Command is not implemented yet: {args.command}")
