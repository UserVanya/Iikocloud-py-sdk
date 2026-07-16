from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any
from unittest.mock import Mock

import pytest

from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.package_checks import RUNTIME_DEPENDENCIES, verify_package


def _write_generated_fixture(package: Path, *, broken: bool = False) -> None:
    (package / "api").mkdir(parents=True)
    (package / "models").mkdir()
    (package / "__init__.py").write_text(
        "from .api_client import ApiClient\nfrom .configuration import Configuration\n",
        encoding="utf-8",
    )
    (package / "api_client.py").write_text("class ApiClient: pass\n", encoding="utf-8")
    (package / "configuration.py").write_text("class Configuration: pass\n", encoding="utf-8")
    (package / "api/__init__.py").write_text("", encoding="utf-8")
    (package / "models/__init__.py").write_text("", encoding="utf-8")
    (package / "api/ping_api.py").write_text(
        "from missing_generated_module import Broken\n" if broken else "class PingApi: pass\n",
        encoding="utf-8",
    )
    (package / "models/ping.py").write_text("class Ping: pass\n", encoding="utf-8")


def test_runtime_dependencies_are_exact_task_11_dependencies() -> None:
    assert RUNTIME_DEPENDENCIES == (
        "httpx>=0.28,<1",
        "pydantic>=2.11,<3",
        "python-dateutil>=2.9,<3",
        "typing-extensions>=4.12,<5",
    )


def test_broken_generated_import_fails_before_wheel_build(
    tmp_path: Path,
) -> None:
    package = tmp_path / "generated/iikocloud_client"
    _write_generated_fixture(package, broken=True)
    calls: list[tuple[list[str], dict[str, Any]]] = []
    real_run = subprocess.run

    def recording_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        return real_run(command, **kwargs)

    with pytest.raises(PipelineError, match="generated imports"):
        verify_package(
            package,
            build_root=tmp_path / "build",
            runner=recording_run,
        )

    assert len(calls) == 1
    assert calls[0][0][1] == "-c"
    assert all(isinstance(command, list) for command, _ in calls)
    assert all("cwd" in kwargs for _, kwargs in calls)
    assert not any("-m" in command and "build" in command for command, _ in calls)


def test_package_check_uses_clean_tree_argv_and_isolated_wheel_install(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = tmp_path / "generated/iikocloud_client"
    _write_generated_fixture(package)
    build_root = tmp_path / "build"
    stale = build_root / "package-check/stale.txt"
    stale.parent.mkdir(parents=True)
    stale.write_text("stale", encoding="utf-8")
    calls: list[tuple[list[str], dict[str, Any]]] = []

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        cwd = Path(kwargs["cwd"])
        if command[1:5] == ["-m", "build", "--no-isolation", "--wheel"]:
            (cwd / "dist").mkdir()
            (cwd / "dist/iikocloud_client-0.0.0-py3-none-any.whl").write_bytes(b"wheel")
        if command[:2] == ["uv", "venv"]:
            environment = Path(command[-1])
            (environment / "bin").mkdir(parents=True)
            (environment / "bin/python").write_text("", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr("tools.openapi_pipeline.package_checks.subprocess.run", fake_run)

    verify_package(package, build_root=build_root)

    assert not stale.exists()
    pyproject = (build_root / "package-check/pyproject.toml").read_text(encoding="utf-8")
    assert all(dependency in pyproject for dependency in RUNTIME_DEPENDENCIES)
    assert [command[:2] for command, _ in calls] == [
        [command_python := calls[0][0][0], "-c"],
        [command_python, "-m"],
        ["uv", "venv"],
        ["uv", "pip"],
        [str(build_root / "package-check/venv/bin/python"), "-c"],
    ]
    assert all(kwargs["check"] is True for _, kwargs in calls)
    assert all(kwargs["cwd"] == build_root / "package-check" for _, kwargs in calls)
    assert all("shell" not in kwargs for _, kwargs in calls)


def test_package_check_rejects_symlink_before_copy_or_subprocess(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = tmp_path / "generated/iikocloud_client"
    _write_generated_fixture(package)
    outside = tmp_path / "outside.py"
    outside.write_text("private", encoding="utf-8")
    (package / "models/escaped.py").symlink_to(outside)
    runner = Mock()
    monkeypatch.setattr("tools.openapi_pipeline.package_checks.subprocess.run", runner)

    with pytest.raises(PipelineError, match="symlink"):
        verify_package(package, build_root=tmp_path / "build")

    runner.assert_not_called()


def test_package_check_rejects_symlinked_build_root_without_outside_mutation(
    tmp_path: Path,
) -> None:
    package = tmp_path / "generated/iikocloud_client"
    _write_generated_fixture(package)
    outside = tmp_path / "outside-build"
    outside.mkdir()
    build_link = tmp_path / "build"
    build_link.symlink_to(outside, target_is_directory=True)
    runner = Mock()

    with pytest.raises(PipelineError, match="symlink"):
        verify_package(package, build_root=build_link, runner=runner)

    assert list(outside.iterdir()) == []
    runner.assert_not_called()
