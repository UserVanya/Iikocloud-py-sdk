from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

from .errors import PipelineError
from .io import write_bytes_atomic
from .promotion import regular_tree_files

RUNTIME_DEPENDENCIES = (
    "httpx>=0.28,<1",
    "pydantic>=2.11,<3",
    "python-dateutil>=2.9,<3",
    "typing-extensions>=4.12,<5",
)

# The wheel smoke check is deliberately independent from dependency resolution.  This
# complete runtime closure is installed exactly as reviewed, with uv forced offline and
# dependency traversal disabled.  Keep these pins in sync when Task 11 replaces the
# temporary project metadata with the generated client's final dependency set.
LOCKED_RUNTIME_REQUIREMENTS = (
    "annotated-types==0.7.0",
    "anyio==4.11.0",
    "certifi==2026.6.17",
    "exceptiongroup==1.3.1",
    "h11==0.16.0",
    "httpcore==1.0.9",
    "httpx==0.28.1",
    "idna==3.11",
    "pydantic-core==2.41.5",
    "pydantic==2.12.5",
    "python-dateutil==2.9.0.post0",
    "six==1.17.0",
    "sniffio==1.3.1",
    "typing-extensions==4.15.0",
    "typing-inspection==0.4.2",
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

_INSTALLED_IMPORT_SCRIPT = f"""
from pathlib import Path
import site

{_IMPORT_SCRIPT}

package_file = Path(iikocloud_client.__file__).resolve(strict=True)
site_roots = [Path(value).resolve(strict=True) for value in site.getsitepackages()]
if not any(package_file.is_relative_to(root) for root in site_roots):
    raise RuntimeError(
        f"installed import escaped isolated site-packages: {{package_file}}"
    )
""".strip()

_UNSAFE_ENVIRONMENT_KEYS = {
    "PIP_CONFIG_FILE",
    "PIP_EXTRA_INDEX_URL",
    "PIP_INDEX_URL",
    "PYTHONHOME",
    "PYTHONPATH",
    "PYTHONUSERBASE",
    "UV_CONFIG_FILE",
    "UV_DEFAULT_INDEX",
    "UV_EXTRA_INDEX_URL",
    "UV_INDEX",
    "UV_INDEX_URL",
}


def _sanitized_environment() -> dict[str, str]:
    environment = {
        key: value
        for key, value in os.environ.items()
        if key.upper() not in _UNSAFE_ENVIRONMENT_KEYS
        and not key.upper().startswith("PIP_")
        and not (key.upper().startswith("UV_") and key.upper() != "UV_CACHE_DIR")
    }
    environment["PYTHONNOUSERSITE"] = "1"
    return environment


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
    regular_tree_files(package, label="Staged package")


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


def _install_and_verify_wheel(
    wheel: Path,
    *,
    environment: Path,
    workspace: Path,
    purpose_prefix: str,
    runner: Runner,
) -> None:
    clean_environment = _sanitized_environment()
    _run(
        [
            "uv",
            "venv",
            "--offline",
            "--no-config",
            "--no-python-downloads",
            "--python",
            sys.executable,
            str(environment),
        ],
        cwd=workspace,
        purpose=f"{purpose_prefix} environment creation",
        runner=runner,
        env=clean_environment,
    )
    isolated_python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    install_prefix = [
        "uv",
        "pip",
        "install",
        "--offline",
        "--no-config",
        "--no-python-downloads",
        "--no-deps",
        "--python",
        str(isolated_python),
    ]
    _run(
        [*install_prefix, *LOCKED_RUNTIME_REQUIREMENTS],
        cwd=workspace,
        purpose=f"{purpose_prefix} locked runtime installation",
        runner=runner,
        env=clean_environment,
    )
    _run(
        [*install_prefix, str(wheel)],
        cwd=workspace,
        purpose=f"{purpose_prefix} installation",
        runner=runner,
        env=clean_environment,
    )
    smoke_root = workspace / "smoke"
    smoke_root.mkdir()
    _run(
        [str(isolated_python), "-I", "-c", _INSTALLED_IMPORT_SCRIPT],
        cwd=smoke_root,
        purpose=f"{purpose_prefix} imports",
        runner=runner,
        env=clean_environment,
    )


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

    source_env = _sanitized_environment()
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
        env=_sanitized_environment(),
    )
    wheels = sorted((check_root / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise PipelineError("Staged wheel build did not produce exactly one wheel")
    environment = check_root / "venv"
    _install_and_verify_wheel(
        wheels[0],
        environment=environment,
        workspace=check_root,
        purpose_prefix="Isolated wheel",
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
        [
            "uv",
            "build",
            "--offline",
            "--no-config",
            "--wheel",
            "--out-dir",
            str(output / "dist"),
        ],
        cwd=resolved_root,
        purpose="Root wheel build",
        runner=command_runner,
        env=_sanitized_environment(),
    )
    wheels = sorted((output / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise PipelineError("Root wheel build did not produce exactly one wheel")
    environment = output / "venv"
    _install_and_verify_wheel(
        wheels[0],
        environment=environment,
        workspace=output,
        purpose_prefix="Root wheel",
        runner=command_runner,
    )


def verify_generated_contracts(
    root: Path,
    package: Path,
    *,
    runner: Runner | None = None,
) -> None:
    """Run only the hand-owned generated/fixture contract suites, when present."""

    resolved_root = root.resolve(strict=True)
    selected: list[str] = []
    for relative in (Path("tests/contracts"), Path("tests/generated")):
        candidate = resolved_root / relative
        if candidate.is_symlink():
            raise PipelineError(f"Generated contract test path must not be a symlink: {candidate}")
        if not candidate.exists():
            continue
        if not candidate.is_dir():
            raise PipelineError(f"Generated contract test path is not a directory: {candidate}")
        regular_tree_files(candidate, label="Generated contract test tree")
        selected.append(relative.as_posix())
    if not selected:
        return

    if package.is_symlink() or not package.is_dir():
        raise PipelineError("Generated contract package must be a regular directory")
    regular_tree_files(package, label="Generated contract package")
    environment = _sanitized_environment()
    environment["PYTHONPATH"] = str(package.parent.resolve(strict=True))
    _run(
        [sys.executable, "-m", "pytest", "-q", *selected],
        cwd=resolved_root,
        purpose="Generated contract tests",
        runner=runner or subprocess.run,
        env=environment,
    )
