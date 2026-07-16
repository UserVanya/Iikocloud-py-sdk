from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any
from unittest.mock import Mock

import pytest

from tools.openapi_pipeline import package_checks as package_checks_module
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.package_checks import (
    RUNTIME_DEPENDENCIES,
    verify_package,
    verify_root_wheel,
)


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
    monkeypatch.setenv("PYTHONPATH", "/poisoned/source")
    monkeypatch.setenv("PYTHONHOME", "/poisoned/home")
    monkeypatch.setenv("PIP_INDEX_URL", "https://credentials.invalid/simple")
    monkeypatch.setenv("UV_INDEX_URL", "https://credentials.invalid/simple")
    monkeypatch.setenv("UV_CONFIG_FILE", "/poisoned/uv.toml")

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
        ["uv", "pip"],
        [str(build_root / "package-check/venv/bin/python"), "-I"],
    ]
    assert all(kwargs["check"] is True for _, kwargs in calls)
    assert all("shell" not in kwargs for _, kwargs in calls)

    uv_commands = [command for command, _ in calls if command[:2] == ["uv", "pip"]]
    assert len(uv_commands) == 2
    assert all("--offline" in command and "--no-deps" in command for command in uv_commands)
    runtime_install, wheel_install = uv_commands
    assert all(
        requirement.count("==") == 1 for requirement in runtime_install if "==" in requirement
    )
    assert any(requirement.startswith("httpx==") for requirement in runtime_install)
    assert any(requirement.startswith("pydantic==") for requirement in runtime_install)
    assert wheel_install[-1].endswith(".whl")

    installed_command, installed_kwargs = calls[-1]
    smoke_root = build_root / "package-check/smoke"
    assert installed_command[:2] == [
        str(build_root / "package-check/venv/bin/python"),
        "-I",
    ]
    assert installed_kwargs["cwd"] == smoke_root
    assert list(smoke_root.iterdir()) == []
    assert "site.getsitepackages" in installed_command[-1]
    assert "iikocloud_client.__file__" in installed_command[-1]
    installed_env = installed_kwargs["env"]
    for forbidden in (
        "PYTHONPATH",
        "PYTHONHOME",
        "PIP_INDEX_URL",
        "UV_INDEX_URL",
        "UV_CONFIG_FILE",
    ):
        assert forbidden not in installed_env
    assert installed_env["PYTHONNOUSERSITE"] == "1"


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


def test_installed_import_smoke_cannot_fall_back_to_healthy_checkout(
    tmp_path: Path,
) -> None:
    environment = tmp_path / "venv"
    subprocess.run(
        [sys.executable, "-m", "venv", "--without-pip", str(environment)],
        check=True,
        capture_output=True,
        text=True,
    )
    isolated_python = environment / (
        "Scripts/python.exe" if sys.platform == "win32" else "bin/python"
    )
    site_packages = subprocess.run(
        [
            str(isolated_python),
            "-I",
            "-c",
            "import site; print(site.getsitepackages()[0])",
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    broken = Path(site_packages) / "iikocloud_client"
    broken.mkdir()
    (broken / "__init__.py").write_text(
        'raise RuntimeError("broken installed wheel")\n', encoding="utf-8"
    )
    healthy = tmp_path / "healthy/iikocloud_client"
    healthy.mkdir(parents=True)
    (healthy / "__init__.py").write_text(
        "class ApiClient: pass\nclass Configuration: pass\n", encoding="utf-8"
    )

    with pytest.raises(PipelineError, match="Installed regression imports"):
        package_checks_module._run(
            [
                str(isolated_python),
                "-I",
                "-c",
                package_checks_module._INSTALLED_IMPORT_SCRIPT,
            ],
            cwd=healthy.parent,
            purpose="Installed regression imports",
            runner=subprocess.run,
            env=package_checks_module._sanitized_environment(),
        )


def test_root_wheel_smoke_uses_same_offline_isolated_install(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("PYTHONPATH", "/poisoned/source")
    monkeypatch.setenv("PIP_INDEX_URL", "https://credentials.invalid/simple")
    calls: list[tuple[list[str], dict[str, Any]]] = []

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        if command[:2] == ["uv", "build"]:
            output = Path(command[command.index("--out-dir") + 1])
            output.mkdir(parents=True)
            (output / "iikocloud_client-0.0.0-py3-none-any.whl").write_bytes(b"wheel")
        if command[:2] == ["uv", "venv"]:
            environment = Path(command[-1])
            (environment / "bin").mkdir(parents=True)
            (environment / "bin/python").write_text("", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    verify_root_wheel(tmp_path, runner=fake_run)

    assert [command[:2] for command, _ in calls] == [
        ["uv", "build"],
        ["uv", "venv"],
        ["uv", "pip"],
        ["uv", "pip"],
        [str(tmp_path / "build/root-wheel-check/venv/bin/python"), "-I"],
    ]
    for command, kwargs in calls:
        if command[:2] == ["uv", "pip"]:
            assert "--offline" in command
            assert "--no-deps" in command
        assert "PIP_INDEX_URL" not in kwargs["env"]
    assert calls[-1][1]["cwd"] == tmp_path / "build/root-wheel-check/smoke"
    assert list(calls[-1][1]["cwd"].iterdir()) == []


def test_generated_contract_gate_is_deterministic_noop_when_test_paths_are_absent(
    tmp_path: Path,
) -> None:
    package = tmp_path / "build/generated/iikocloud_client"
    package.mkdir(parents=True)
    runner = Mock()

    package_checks_module.verify_generated_contracts(tmp_path, package, runner=runner)

    runner.assert_not_called()


def test_generated_contract_gate_runs_present_offline_test_paths_against_staging(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = tmp_path / "build/generated/iikocloud_client"
    package.mkdir(parents=True)
    generated_tests = tmp_path / "tests/generated"
    contract_tests = tmp_path / "tests/contracts"
    generated_tests.mkdir(parents=True)
    contract_tests.mkdir(parents=True)
    (generated_tests / "test_generated.py").write_text("def test_ok(): pass\n", encoding="utf-8")
    (contract_tests / "test_contract.py").write_text("def test_ok(): pass\n", encoding="utf-8")
    monkeypatch.setenv("PYTHONPATH", "/poisoned/source")
    monkeypatch.setenv("PIP_INDEX_URL", "https://credentials.invalid/simple")
    runner = Mock(return_value=subprocess.CompletedProcess([], 0, stdout="", stderr=""))

    package_checks_module.verify_generated_contracts(tmp_path, package, runner=runner)

    command = runner.call_args.args[0]
    kwargs = runner.call_args.kwargs
    assert command == [
        command[0],
        "-m",
        "pytest",
        "-q",
        "tests/contracts",
        "tests/generated",
    ]
    assert kwargs["cwd"] == tmp_path
    assert kwargs["env"]["PYTHONPATH"] == str(package.parent)
    assert "PIP_INDEX_URL" not in kwargs["env"]


def test_generated_contract_gate_wraps_offline_test_failure(tmp_path: Path) -> None:
    package = tmp_path / "build/generated/iikocloud_client"
    package.mkdir(parents=True)
    tests = tmp_path / "tests/generated"
    tests.mkdir(parents=True)
    runner = Mock(side_effect=subprocess.CalledProcessError(1, ["pytest"]))

    with pytest.raises(PipelineError, match="Generated contract tests"):
        package_checks_module.verify_generated_contracts(tmp_path, package, runner=runner)
