from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

from .errors import PipelineError
from .io import write_bytes_atomic

RUNTIME_DEPENDENCIES = (
    "httpx>=0.28,<1",
    "pydantic>=2.11,<3",
    "python-dateutil>=2.9,<3",
    "typing-extensions>=4.12,<5",
)

Runner = Callable[..., subprocess.CompletedProcess[str]]

_IMPORT_SCRIPT = """
import importlib
import pkgutil
import iikocloud_client
from iikocloud_client import ApiClient, Configuration

for module in pkgutil.walk_packages(
    iikocloud_client.__path__, iikocloud_client.__name__ + "."
):
    importlib.import_module(module.name)
""".strip()


def _run(
    command: Sequence[str],
    *,
    cwd: Path,
    purpose: str,
    runner: Runner,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    argv = list(command)
    try:
        return runner(
            argv,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
    except FileNotFoundError as error:
        raise PipelineError(f"{purpose} could not start: executable not found") from error
    except subprocess.CalledProcessError as error:
        raise PipelineError(f"{purpose} failed with exit status {error.returncode}") from error
    except OSError as error:
        raise PipelineError(
            f"{purpose} could not start: {error.strerror or 'I/O error'}"
        ) from error


def _clean_directory(path: Path, *, controlled_root: Path) -> None:
    root = controlled_root.resolve(strict=False)
    resolved = path.resolve(strict=False)
    if path.is_symlink() or not resolved.is_relative_to(root) or resolved == root:
        raise PipelineError(f"Refusing to clean unsafe package-check path: {path}")
    if path.exists():
        if not path.is_dir():
            raise PipelineError(f"Package-check path is not a directory: {path}")
        shutil.rmtree(path)
    path.mkdir(parents=True)


def _assert_regular_tree(package: Path) -> None:
    for path in package.rglob("*"):
        if path.is_symlink():
            raise PipelineError(f"Staged package contains a symlink: {path}")
        if not (path.is_file() or path.is_dir()):
            raise PipelineError(f"Staged package contains a non-regular entry: {path}")


def _minimal_pyproject() -> bytes:
    dependencies = ",\n".join(f'  "{dependency}"' for dependency in RUNTIME_DEPENDENCIES)
    return (
        "[project]\n"
        'name = "iikocloud-client"\n'
        'version = "0.0.0"\n'
        'requires-python = ">=3.10"\n'
        "dependencies = [\n"
        f"{dependencies}\n"
        "]\n\n"
        "[build-system]\n"
        'requires = ["setuptools>=77,<82"]\n'
        'build-backend = "setuptools.build_meta"\n\n'
        "[tool.setuptools.packages.find]\n"
        'where = ["src"]\n'
    ).encode()


def verify_package(
    package: Path,
    *,
    build_root: Path | None = None,
    runner: Runner | None = None,
) -> None:
    if package.is_symlink() or not package.is_dir() or package.name != "iikocloud_client":
        raise PipelineError("Staged package must be a regular iikocloud_client directory")
    _assert_regular_tree(package)
    requested_build = build_root or package.parents[2]
    if requested_build.is_symlink():
        raise PipelineError(f"Package-check build root must not be a symlink: {requested_build}")
    controlled_build = requested_build.resolve(strict=False)
    command_runner = runner or subprocess.run
    check_root = controlled_build / "package-check"
    _clean_directory(check_root, controlled_root=controlled_build)
    source_root = check_root / "src"
    checked_package = source_root / "iikocloud_client"
    source_root.mkdir()
    shutil.copytree(package, checked_package)
    write_bytes_atomic(check_root / "pyproject.toml", _minimal_pyproject())

    source_env = dict(os.environ)
    source_env["PYTHONPATH"] = str(source_root)
    _run(
        [sys.executable, "-c", _IMPORT_SCRIPT],
        cwd=check_root,
        purpose="generated imports",
        runner=command_runner,
        env=source_env,
    )
    _run(
        [sys.executable, "-m", "build", "--no-isolation", "--wheel"],
        cwd=check_root,
        purpose="Staged wheel build",
        runner=command_runner,
    )
    wheels = sorted((check_root / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise PipelineError("Staged wheel build did not produce exactly one wheel")
    environment = check_root / "venv"
    _run(
        ["uv", "venv", "--python", sys.executable, str(environment)],
        cwd=check_root,
        purpose="Isolated wheel environment creation",
        runner=command_runner,
    )
    isolated_python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    _run(
        ["uv", "pip", "install", "--python", str(isolated_python), str(wheels[0])],
        cwd=check_root,
        purpose="Isolated wheel installation",
        runner=command_runner,
    )
    _run(
        [str(isolated_python), "-c", _IMPORT_SCRIPT],
        cwd=check_root,
        purpose="Installed wheel imports",
        runner=command_runner,
    )


def verify_root_wheel(root: Path, *, runner: Runner | None = None) -> None:
    resolved_root = root.resolve(strict=True)
    command_runner = runner or subprocess.run
    build_root = resolved_root / "build"
    if build_root.is_symlink():
        raise PipelineError(f"Root wheel build directory must not be a symlink: {build_root}")
    output = build_root / "root-wheel-check"
    _clean_directory(output, controlled_root=build_root)
    _run(
        ["uv", "build", "--wheel", "--out-dir", str(output / "dist")],
        cwd=resolved_root,
        purpose="Root wheel build",
        runner=command_runner,
    )
    wheels = sorted((output / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise PipelineError("Root wheel build did not produce exactly one wheel")
    environment = output / "venv"
    _run(
        ["uv", "venv", "--python", sys.executable, str(environment)],
        cwd=resolved_root,
        purpose="Root wheel environment creation",
        runner=command_runner,
    )
    isolated_python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    _run(
        ["uv", "pip", "install", "--python", str(isolated_python), str(wheels[0])],
        cwd=resolved_root,
        purpose="Root wheel installation",
        runner=command_runner,
    )
    _run(
        [str(isolated_python), "-c", _IMPORT_SCRIPT],
        cwd=resolved_root,
        purpose="Root installed wheel imports",
        runner=command_runner,
    )
