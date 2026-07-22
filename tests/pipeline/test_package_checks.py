from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any
from unittest.mock import Mock

import pytest
from packaging.markers import default_environment

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - exercised in the Python 3.10 CI matrix
    import tomli as tomllib

from tools.openapi_pipeline import package_checks as package_checks_module
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.package_checks import (
    LOCKED_RUNTIME_REQUIREMENTS,
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
    (package / "py.typed").write_bytes(b"")


def test_runtime_dependencies_are_exact_task_11_dependencies() -> None:
    assert RUNTIME_DEPENDENCIES == (
        "httpx>=0.28,<1",
        "pydantic>=2.11,<3",
        "python-dateutil>=2.9,<3",
        "typing-extensions>=4.12,<5",
    )


def test_root_project_uses_exact_task_11_src_packaging_metadata() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert project["project"] == {
        "name": "iikocloud-client",
        "version": "0.1.0",
        "description": "Generated async Python SDK for iiko Cloud API",
        "readme": "README.md",
        "requires-python": ">=3.10",
        "dependencies": [
            "httpx>=0.28,<1",
            "pydantic>=2.11,<3",
            "python-dateutil>=2.9,<3",
            "typing-extensions>=4.12,<5",
        ],
        "urls": {"Repository": "https://github.com/UserVanya/Iikocloud-py-sdk"},
    }
    assert project["build-system"] == {
        "requires": ["setuptools>=77,<82"],
        "build-backend": "setuptools.build_meta",
    }
    assert project["tool"]["setuptools"] == {
        "packages": {"find": {"where": ["src"]}},
        "package-data": {
            "iikocloud_client": ["py.typed", "_contracts/*.yaml"],
        },
    }
    assert project["tool"]["mypy"]["files"] == ["tools/openapi_pipeline"]
    assert project["tool"]["pytest"]["ini_options"]["pythonpath"] == ["."]
    assert "poetry" not in project["tool"]
    assert "pylint" not in project["tool"]


def test_package_check_group_and_recursive_lock_match_runtime_closure() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert tuple(project["dependency-groups"]["package-check"]) == (
        "httpx==0.28.1",
        "pydantic==2.12.5",
        "python-dateutil==2.9.0.post0",
        "typing-extensions==4.15.0",
    )
    assert project["tool"]["uv"]["default-groups"] == ["dev", "package-check"]
    assert "packaging==26.2" in project["dependency-groups"]["dev"]
    assert package_checks_module.locked_runtime_requirements(Path.cwd()) == (
        LOCKED_RUNTIME_REQUIREMENTS
    )
    assert ("exceptiongroup==1.3.1" in LOCKED_RUNTIME_REQUIREMENTS) is (
        sys.version_info < (3, 11)
    )


def test_recursive_lock_closure_evaluates_markers_for_simulated_python_310() -> None:
    environment: dict[str, str] = {
        key: value for key, value in default_environment().items() if isinstance(value, str)
    }
    environment.update(python_version="3.10", python_full_version="3.10.0")

    closure = package_checks_module.locked_runtime_requirements(
        Path.cwd(), marker_environment=environment
    )

    assert "exceptiongroup==1.3.1" in closure


def _write_synthetic_lock(root: Path, dependency: str) -> None:
    (root / "uv.lock").write_text(
        "version = 1\n"
        'requires-python = ">=3.10"\n\n'
        "[[package]]\n"
        'name = "fixture"\n'
        'source = { editable = "." }\n'
        "[package.dev-dependencies]\n"
        'package-check = [{ name = "root" }]\n\n'
        "[[package]]\n"
        'name = "root"\n'
        'version = "1.0"\n'
        f"dependencies = [{dependency}]\n\n"
        "[[package]]\n"
        'name = "conditional"\n'
        'version = "2.0"\n',
        encoding="utf-8",
    )


def test_recursive_lock_closure_rejects_malformed_marker_actionably(tmp_path: Path) -> None:
    _write_synthetic_lock(
        tmp_path,
        '{ name = "conditional", marker = "python_version << \'3.11\'" }',
    )

    with pytest.raises(PipelineError, match="Invalid marker.*root.*conditional"):
        package_checks_module.locked_runtime_requirements(tmp_path)


def test_recursive_lock_closure_rejects_dependency_cycles_actionably(tmp_path: Path) -> None:
    _write_synthetic_lock(tmp_path, '{ name = "conditional" }')
    with (tmp_path / "uv.lock").open("a", encoding="utf-8") as lock:
        lock.write('dependencies = [{ name = "root" }]\n')

    with pytest.raises(PipelineError, match=r"cycle.*root.*conditional.*root"):
        package_checks_module.locked_runtime_requirements(tmp_path)


def test_package_check_cache_prime_compiles_exact_locked_runtime_requirements(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "uv.lock").write_bytes(Path("uv.lock").read_bytes())
    calls: list[tuple[list[str], dict[str, Any]]] = []
    monkeypatch.setenv("PIP_INDEX_URL", "https://credentials.invalid/simple")
    monkeypatch.setenv("UV_INDEX_URL", "https://credentials.invalid/simple")
    monkeypatch.setenv("UV_CONFIG_FILE", "/poisoned/uv.toml")
    monkeypatch.setenv("UV_CACHE_DIR", str(tmp_path / "cache"))

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        output = Path(command[command.index("--output-file") + 1])
        source = Path(command[-1])
        output.write_bytes(source.read_bytes())
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    package_checks_module.prime_package_check_cache(tmp_path, runner=fake_run)

    assert len(calls) == 1
    command, kwargs = calls[0]
    assert command[:3] == ["uv", "pip", "compile"]
    assert command[3:-2] == [
        "--refresh",
        "--no-config",
        "--no-deps",
        "--no-annotate",
        "--no-header",
        "--output-file",
    ]
    output = Path(command[-2])
    source = Path(command[-1])
    expected = "\n".join(LOCKED_RUNTIME_REQUIREMENTS) + "\n"
    assert source.read_text(encoding="utf-8") == expected
    assert output.read_text(encoding="utf-8") == expected
    assert kwargs["cwd"] == tmp_path
    assert kwargs["check"] is True
    assert kwargs["capture_output"] is True
    assert kwargs["text"] is True
    assert "--offline" not in command
    assert "PIP_INDEX_URL" not in kwargs["env"]
    assert "UV_INDEX_URL" not in kwargs["env"]
    assert "UV_CONFIG_FILE" not in kwargs["env"]
    assert kwargs["env"]["UV_CACHE_DIR"] == str(tmp_path / "cache")
    assert kwargs["env"]["PYTHONNOUSERSITE"] == "1"


def test_package_check_cache_prime_rejects_changed_compiler_output(tmp_path: Path) -> None:
    (tmp_path / "uv.lock").write_bytes(Path("uv.lock").read_bytes())

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        del kwargs
        output = Path(command[command.index("--output-file") + 1])
        output.write_text("httpx==0.0.0\n", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    with pytest.raises(PipelineError, match="compiled runtime pins differ"):
        package_checks_module.prime_package_check_cache(tmp_path, runner=fake_run)


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
    assert 'iikocloud_client = ["py.typed", "_contracts/*.yaml"]' in pyproject
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


def test_installed_import_smoke_ignores_missing_reported_site_root(
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
    site_packages = Path(
        subprocess.run(
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
    )
    installed = site_packages / "iikocloud_client"
    installed.mkdir()
    (installed / "__init__.py").write_text(
        "class ApiClient: pass\nclass Configuration: pass\n",
        encoding="utf-8",
    )
    (installed / "py.typed").write_bytes(b"")
    missing_site_root = tmp_path / "guaranteed-missing-site-root"
    smoke = tmp_path / "smoke"
    smoke.mkdir()
    script = (
        "import site\n"
        f"site.getsitepackages = lambda: [{str(site_packages)!r}, "
        f"{str(missing_site_root)!r}]\n"
        f"{package_checks_module._INSTALLED_IMPORT_SCRIPT}"
    )

    package_checks_module._run(
        [str(isolated_python), "-I", "-c", script],
        cwd=smoke,
        purpose="Installed missing-root regression imports",
        runner=subprocess.run,
        env=package_checks_module._sanitized_environment(),
    )


def test_installed_import_smoke_requires_empty_py_typed_marker(tmp_path: Path) -> None:
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
    site_packages = Path(
        subprocess.run(
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
    )
    installed = site_packages / "iikocloud_client"
    installed.mkdir()
    (installed / "__init__.py").write_text(
        "class ApiClient: pass\nclass Configuration: pass\n",
        encoding="utf-8",
    )
    smoke = tmp_path / "smoke"
    smoke.mkdir()

    with pytest.raises(PipelineError, match="Installed marker regression imports"):
        package_checks_module._run(
            [str(isolated_python), "-I", "-c", package_checks_module._INSTALLED_IMPORT_SCRIPT],
            cwd=smoke,
            purpose="Installed marker regression imports",
            runner=subprocess.run,
            env=package_checks_module._sanitized_environment(),
        )

    (installed / "py.typed").write_bytes(b"")
    package_checks_module._run(
        [str(isolated_python), "-I", "-c", package_checks_module._INSTALLED_IMPORT_SCRIPT],
        cwd=smoke,
        purpose="Installed marker regression imports",
        runner=subprocess.run,
        env=package_checks_module._sanitized_environment(),
    )


def test_root_wheel_smoke_uses_same_offline_isolated_install(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "uv.lock").write_bytes(Path("uv.lock").read_bytes())
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
    assert command[:3] == [sys.executable, "-I", "-c"]
    wrapper = command[3]
    assert "sys.path.insert(0" in wrapper
    assert "import iikocloud_client" in wrapper
    assert "iikocloud_client.__file__" in wrapper
    assert "--import-mode=importlib" in wrapper
    assert command[4:] == [
        str(package.parent.resolve()),
        str(package.resolve()),
        str(contract_tests.resolve()),
        str(generated_tests.resolve()),
    ]
    assert kwargs["cwd"] == tmp_path / "build/contract-check/run"
    assert list(kwargs["cwd"].iterdir()) == []
    assert "PYTHONPATH" not in kwargs["env"]
    assert kwargs["env"]["PYTHONDONTWRITEBYTECODE"] == "1"
    assert "PIP_INDEX_URL" not in kwargs["env"]


def test_generated_contract_gate_resolves_repo_fixtures_from_test_file(tmp_path: Path) -> None:
    package = tmp_path / "build/generated/iikocloud_client"
    models = package / "models"
    models.mkdir(parents=True)
    (package / "__init__.py").write_text("", encoding="utf-8")
    (models / "__init__.py").write_text("", encoding="utf-8")
    (models / "external_menu_response.py").write_text(
        "import json\n"
        "from types import SimpleNamespace\n\n"
        "class ExternalMenuResponse:\n"
        "    @classmethod\n"
        "    def from_json(cls, body):\n"
        "        data = json.loads(body)\n"
        "        instance = SimpleNamespace(format_version=data['formatVersion'])\n"
        "        return SimpleNamespace(actual_instance=instance)\n",
        encoding="utf-8",
    )
    generated_tests = tmp_path / "tests/generated"
    generated_tests.mkdir(parents=True)
    union_test = Path(__file__).parents[1] / "generated/test_external_menu_response.py"
    (generated_tests / union_test.name).write_bytes(union_test.read_bytes())
    fixtures = tmp_path / "tests/fixtures/contracts"
    fixtures.mkdir(parents=True)
    for version in (2, 3, 4):
        (fixtures / f"external-menu-v{version}.json").write_text(
            f'{{"formatVersion": {version}}}\n',
            encoding="utf-8",
        )

    package_checks_module.verify_generated_contracts(tmp_path, package)


def test_generated_contract_gate_wraps_offline_test_failure(tmp_path: Path) -> None:
    package = tmp_path / "build/generated/iikocloud_client"
    package.mkdir(parents=True)
    tests = tmp_path / "tests/generated"
    tests.mkdir(parents=True)
    runner = Mock(side_effect=subprocess.CalledProcessError(1, ["pytest"]))

    with pytest.raises(PipelineError, match="Generated contract tests"):
        package_checks_module.verify_generated_contracts(tmp_path, package, runner=runner)


def test_generated_contract_gate_cannot_import_healthy_legacy_checkout(
    tmp_path: Path,
) -> None:
    legacy = tmp_path / "iikocloud_client"
    legacy.mkdir()
    (legacy / "__init__.py").write_text("HEALTHY = True\n", encoding="utf-8")
    checked = tmp_path / "build/contract-check/src/iikocloud_client"
    checked.mkdir(parents=True)
    (checked / "__init__.py").write_text(
        'raise RuntimeError("broken checked package")\n', encoding="utf-8"
    )
    tests = tmp_path / "tests/generated"
    tests.mkdir(parents=True)
    (tests / "test_import.py").write_text(
        "import iikocloud_client\n\ndef test_import():\n    assert iikocloud_client.HEALTHY\n",
        encoding="utf-8",
    )

    with pytest.raises(PipelineError, match="Generated contract tests"):
        package_checks_module.verify_generated_contracts(tmp_path, checked)

    assert not list(checked.rglob("__pycache__"))
