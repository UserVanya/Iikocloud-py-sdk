from __future__ import annotations

import argparse
import asyncio
import sys
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
        command_parser = subparsers.add_parser(command)
        if command == "bootstrap":
            command_parser.add_argument("--accept-current-upstream", action="store_true")
        elif command == "sync":
            command_parser.add_argument("--offline", action="store_true")
        elif command == "capture-evidence":
            command_parser.add_argument("--live-profile", required=True)
            command_parser.add_argument("--env-file", required=True)
            command_parser.add_argument(
                "--operation",
                required=True,
                choices=("get_external_menu_by_id",),
            )
            command_parser.add_argument(
                "--menu-version",
                required=True,
                type=int,
                choices=(2, 3, 4),
            )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        from . import pipeline

        if args.command == "bootstrap":
            dependencies = pipeline.default_dependencies(
                offline=bool(args.accept_current_upstream)
            )
            pipeline.bootstrap(
                dependencies,
                accept_current_upstream=bool(args.accept_current_upstream),
            )
        elif args.command == "sync":
            dependencies = pipeline.default_dependencies(offline=bool(args.offline))
            pipeline.sync(dependencies)
        elif args.command == "verify":
            dependencies = pipeline.default_dependencies(offline=True)
            pipeline.verify(dependencies)
        elif args.command == "upstream-check":
            dependencies = pipeline.default_dependencies(offline=False)
            pipeline.upstream_check(dependencies)
        elif args.command == "capture-evidence":
            from . import evidence

            asyncio.run(
                evidence.capture_evidence(
                    live_profile=args.live_profile,
                    env_file=args.env_file,
                    operation=args.operation,
                    menu_version=args.menu_version,
                )
            )
        else:
            raise PipelineError(f"Command is not implemented yet: {args.command}")
    except PipelineError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0
