from __future__ import annotations

import json
import re
import shlex
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
OFFLINE_WORKFLOW = ROOT / ".github/workflows/python.yml"
UPSTREAM_WORKFLOW = ROOT / ".github/workflows/upstream-check.yml"
GENERATION_DOC = ROOT / "docs/generation.md"

PYTEST_PREFIX = ("uv", "run", "--frozen", "--offline", "pytest", "-q")
BUILDER_SMOKE = (
    "tests/pipeline/test_evidence_candidates.py::"
    "test_builder_smoke_uses_public_locally_composed_candidate_without_fetch"
)
ANALYZER_SMOKE = (
    "tests/pipeline/test_evidence_analysis.py::"
    "test_analyzer_smoke_uses_the_locally_composed_reviewed_schema_without_fetch"
)
ISOLATED_PIPELINE_FILES = (
    "tests/pipeline/test_evidence_candidate_writer.py",
    "tests/pipeline/test_evidence_candidate_contract.py",
    "tests/pipeline/test_evidence_candidate_store.py",
    "tests/pipeline/test_evidence_candidates.py",
    "tests/pipeline/test_evidence_analysis.py",
    "tests/pipeline/test_evidence_promotion_reader.py",
)

LIVE_WRITE_NODE = (
    "tests/integration/write/test_stop_list.py::"
    "test_stop_list_add_is_accepted_and_removed"
)

CHECKOUT_ACTION = "actions/checkout@11d5960a326750d5838078e36cf38b85af677262"
SETUP_UV_ACTION = "astral-sh/setup-uv@d0cc045d04ccac9d8b7881df0226f9e82c39688e"
SETUP_PYTHON_ACTION = "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065"
UPLOAD_ARTIFACT_ACTION = "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02"
OFFLINE_ACTIONS = (
    (CHECKOUT_ACTION, "v4.4.0"),
    (SETUP_UV_ACTION, "v6.8.0"),
    (SETUP_PYTHON_ACTION, "v5.6.0"),
)
UPSTREAM_ACTIONS = (*OFFLINE_ACTIONS, (UPLOAD_ARTIFACT_ACTION, "v4.6.2"))


def _load_workflow(path: Path) -> dict[str, Any]:
    assert path.is_file(), f"missing workflow: {path.relative_to(ROOT)}"
    loaded = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    assert isinstance(loaded, dict)
    return loaded


def _only_job(workflow: dict[str, Any]) -> dict[str, Any]:
    jobs = workflow.get("jobs")
    assert isinstance(jobs, dict)
    assert len(jobs) == 1
    job = next(iter(jobs.values()))
    assert isinstance(job, dict)
    return job


def _steps(job: dict[str, Any]) -> list[dict[str, Any]]:
    raw_steps = job.get("steps")
    assert isinstance(raw_steps, list)
    assert all(isinstance(step, dict) for step in raw_steps)
    return raw_steps


def _run_steps(steps: list[dict[str, Any]]) -> list[tuple[int, dict[str, Any], str]]:
    result: list[tuple[int, dict[str, Any], str]] = []
    for index, step in enumerate(steps):
        command = step.get("run")
        if command is not None:
            assert isinstance(command, str)
            result.append((index, step, " ".join(command.split())))
    return result


def _action_steps(steps: list[dict[str, Any]], action: str) -> list[dict[str, Any]]:
    return [
        step
        for step in steps
        if isinstance(step.get("uses"), str) and step["uses"] == action
    ]


def _assert_exact_action_allowlist(
    path: Path,
    steps: list[dict[str, Any]],
    expected: tuple[tuple[str, str], ...],
) -> None:
    refs = tuple(step["uses"] for step in steps if "uses" in step)
    assert refs == tuple(ref for ref, _version in expected)
    assert all(re.fullmatch(r"[^@]+@[0-9a-f]{40}", ref) for ref in refs)

    source_pins = tuple(
        re.findall(
            r"^\s*(?:-\s+)?uses:\s*(\S+)\s+#\s*(v\d+\.\d+\.\d+)\s*$",
            path.read_text(encoding="utf-8"),
            flags=re.MULTILINE,
        )
    )
    assert source_pins == expected


def _command_step(
    run_steps: list[tuple[int, dict[str, Any], str]], command: str
) -> tuple[int, dict[str, Any]]:
    matches = [(index, step) for index, step, run in run_steps if run == command]
    assert len(matches) == 1, f"expected one workflow step running: {command}"
    return matches[0]


def _assert_python_312_only(step: dict[str, Any]) -> None:
    condition = step.get("if")
    assert isinstance(condition, str)
    normalized = condition.strip()
    if normalized.startswith("${{") and normalized.endswith("}}"):
        normalized = normalized[3:-2].strip()
    assert re.fullmatch(r"matrix\.python-version\s*==\s*(['\"])3\.12\1", normalized)


def _assert_read_only_permissions(workflow: dict[str, Any]) -> None:
    assert workflow.get("permissions") == {"contents": "read"}


def _assert_no_live_or_mutating_configuration(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    forbidden_literals = (
        "IIKO_API_KEY",
        "IIKO_API_KEY_2",
        "--env-file",
        ".env",
        "--live-profile",
        "--allow-live-write",
        "--allow-audit-residue",
        "--target-organization",
        "--capture-http",
        "--capture-operation",
        "live_read_smoke",
        "live_read_full",
        "live_read_selected",
        "live_write",
        "audit_residue",
    )
    for literal in forbidden_literals:
        assert literal not in text

    assert "secrets." not in text
    assert not re.search(r"\bgit\s+(?:add|commit|push|tag|merge|reset|checkout|switch)\b", text)


def _pipeline_commands(path: Path) -> list[str]:
    return re.findall(
        r"python\s+-m\s+tools\.openapi_pipeline\s+([a-z][a-z-]*)\b",
        path.read_text(encoding="utf-8"),
    )


def test_generation_doc_forbidden_live_write_template_has_every_gate() -> None:
    text = GENERATION_DOC.read_text(encoding="utf-8")
    match = re.search(
        r"### Точная команда write-прогона\n.*?```bash\n(?P<command>.*?)\n```",
        text,
        flags=re.DOTALL,
    )
    assert match is not None
    command = match.group("command").replace("\\\n", " ")
    tokens = tuple(shlex.split(command))

    assert tokens == (
        "PYTHONDONTWRITEBYTECODE=1",
        "uv",
        "run",
        "--frozen",
        "--offline",
        "pytest",
        "-m",
        "live_write",
        "-n0",
        LIVE_WRITE_NODE,
        "--live-profile",
        "write-server",
        "--env-file",
        ".env",
        "--target-organization",
        "${IIKO_WRITE_ORGANIZATION_ID:?required}",
        "--allow-live-write",
        "--allow-audit-residue",
    )
    assert "--collect-only" not in tokens


def test_offline_workflow_has_read_only_two_version_matrix() -> None:
    workflow = _load_workflow(OFFLINE_WORKFLOW)
    triggers = workflow.get("on")
    assert isinstance(triggers, dict)
    assert set(triggers) == {"push", "pull_request"}
    _assert_read_only_permissions(workflow)

    job = _only_job(workflow)
    strategy = job.get("strategy")
    assert isinstance(strategy, dict)
    assert strategy.get("fail-fast") == "false"
    matrix = strategy.get("matrix")
    assert isinstance(matrix, dict)
    assert matrix.get("python-version") == ["3.10", "3.12"]


def test_offline_workflow_runs_required_checks_and_pinned_generator() -> None:
    workflow = _load_workflow(OFFLINE_WORKFLOW)
    steps = _steps(_only_job(workflow))
    run_steps = _run_steps(steps)

    install_index, _ = _command_step(run_steps, "uv sync --frozen --group dev")
    prime_index, _ = _command_step(
        run_steps,
        "uv run --frozen --no-sync python -m tools.openapi_pipeline "
        "prime-package-check-cache",
    )
    lint_index, _ = _command_step(
        run_steps,
        "uv run --frozen --offline ruff check --no-cache tools tests",
    )
    assert install_index < prime_index < lint_index
    _command_step(
        run_steps,
        "uv run --frozen --offline python -m tools.openapi_pipeline verify-no-secrets",
    )
    _command_step(run_steps, "uv build --offline")

    _, mypy_step = _command_step(
        run_steps, "uv run --frozen --offline mypy tools/openapi_pipeline"
    )
    _assert_python_312_only(mypy_step)
    verify_index, verify_step = _command_step(
        run_steps,
        "uv run --frozen --offline python -m tools.openapi_pipeline verify",
    )
    _assert_python_312_only(verify_step)

    lock = json.loads((ROOT / "generator/toolchain.lock").read_text(encoding="utf-8"))
    pinned_image = f"{lock['image']}@{lock['digest']}"
    pull_index, pull_step = _command_step(run_steps, f"docker pull {pinned_image}")
    _assert_python_312_only(pull_step)
    assert pull_index < verify_index

    pytest_commands = {run for _, _, run in run_steps if "pytest" in shlex.split(run)}
    non_pytest_commands = {run for _, _, run in run_steps} - pytest_commands
    assert non_pytest_commands == {
        "uv sync --frozen --group dev",
        "uv run --frozen --no-sync python -m tools.openapi_pipeline "
        "prime-package-check-cache",
        "uv run --frozen --offline ruff check --no-cache tools tests",
        "uv run --frozen --offline python -m tools.openapi_pipeline verify-no-secrets",
        "uv build --offline",
        "uv run --frozen --offline mypy tools/openapi_pipeline",
        f"docker pull {pinned_image}",
        "uv run --frozen --offline python -m tools.openapi_pipeline verify",
    }

    checkout = _action_steps(steps, CHECKOUT_ACTION)
    assert len(checkout) == 1
    assert checkout[0].get("with") == {"persist-credentials": "false"}
    assert len(_action_steps(steps, SETUP_UV_ACTION)) == 1
    setup_python = _action_steps(steps, SETUP_PYTHON_ACTION)
    assert len(setup_python) == 1
    assert setup_python[0].get("with") == {"python-version": "${{ matrix.python-version }}"}
    _assert_exact_action_allowlist(OFFLINE_WORKFLOW, steps, OFFLINE_ACTIONS)


def test_offline_workflow_uses_exact_fresh_process_pytest_partition() -> None:
    workflow = _load_workflow(OFFLINE_WORKFLOW)
    run_steps = _run_steps(_steps(_only_job(workflow)))
    pytest_commands = [run for _, _, run in run_steps if "pytest" in shlex.split(run)]

    expected = (
        PYTEST_PREFIX + (ISOLATED_PIPELINE_FILES[0],),
        PYTEST_PREFIX
        + ISOLATED_PIPELINE_FILES[1:4]
        + ("-k", "not locally_composed"),
        PYTEST_PREFIX
        + ISOLATED_PIPELINE_FILES[4:]
        + ("-k", "not locally_composed"),
        PYTEST_PREFIX + (BUILDER_SMOKE,),
        PYTEST_PREFIX + (ANALYZER_SMOKE,),
        PYTEST_PREFIX + ("tests/capture",),
        PYTEST_PREFIX + ("tests/live_support",),
        PYTEST_PREFIX
        + (
            "tests",
            "--ignore=tests/capture",
            "--ignore=tests/live_support",
        )
        + tuple(f"--ignore={path}" for path in ISOLATED_PIPELINE_FILES),
    )

    assert len(pytest_commands) == 8
    assert {tuple(shlex.split(command)) for command in pytest_commands} == set(expected)
    assert all(tuple(shlex.split(command)) != PYTEST_PREFIX for command in pytest_commands)


def test_offline_workflow_never_uses_live_or_mutating_pipeline_commands() -> None:
    _assert_no_live_or_mutating_configuration(OFFLINE_WORKFLOW)
    assert _pipeline_commands(OFFLINE_WORKFLOW) == [
        "prime-package-check-cache",
        "verify-no-secrets",
        "verify",
    ]


def test_scheduled_workflow_only_reports_public_upstream_drift() -> None:
    workflow = _load_workflow(UPSTREAM_WORKFLOW)
    triggers = workflow.get("on")
    assert isinstance(triggers, dict)
    assert set(triggers) == {"schedule", "workflow_dispatch"}
    schedule = triggers.get("schedule")
    assert isinstance(schedule, list) and schedule
    _assert_read_only_permissions(workflow)

    steps = _steps(_only_job(workflow))
    run_steps = _run_steps(steps)
    _command_step(run_steps, "uv sync --frozen --group dev")
    _command_step(
        run_steps,
        "uv run --frozen python -m tools.openapi_pipeline upstream-check --fail-on-drift",
    )
    assert [run for _, _, run in run_steps] == [
        "uv sync --frozen --group dev",
        "uv run --frozen python -m tools.openapi_pipeline upstream-check --fail-on-drift",
    ]

    checkout = _action_steps(steps, CHECKOUT_ACTION)
    assert len(checkout) == 1
    assert checkout[0].get("with") == {"persist-credentials": "false"}
    assert len(_action_steps(steps, SETUP_UV_ACTION)) == 1
    setup_python = _action_steps(steps, SETUP_PYTHON_ACTION)
    assert len(setup_python) == 1
    assert setup_python[0].get("with") == {"python-version": "3.12"}

    upload_steps = _action_steps(steps, UPLOAD_ARTIFACT_ACTION)
    assert len(upload_steps) == 1
    upload = upload_steps[0]
    assert upload.get("if") == "always()"
    assert upload.get("with") == {
        "name": "upstream-diff",
        "path": "build/reports/upstream-diff.*",
        "if-no-files-found": "error",
    }
    _assert_exact_action_allowlist(UPSTREAM_WORKFLOW, steps, UPSTREAM_ACTIONS)

    _assert_no_live_or_mutating_configuration(UPSTREAM_WORKFLOW)
    assert _pipeline_commands(UPSTREAM_WORKFLOW) == ["upstream-check"]
