from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path

from packaging.markers import (
    InvalidMarker,
    Marker,
    UndefinedComparison,
    UndefinedEnvironmentName,
    default_environment,
)

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - exercised on supported Python 3.10
    import tomli as tomllib

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
_LOCKED_RUNTIME_PINS = {
    "annotated-types": "0.7.0",
    "anyio": "4.14.2",
    "certifi": "2026.6.17",
    "exceptiongroup": "1.3.1",
    "h11": "0.16.0",
    "httpcore": "1.0.9",
    "httpx": "0.28.1",
    "idna": "3.11",
    "pydantic": "2.12.5",
    "pydantic-core": "2.41.5",
    "python-dateutil": "2.9.0.post0",
    "six": "1.17.0",
    "typing-extensions": "4.15.0",
    "typing-inspection": "0.4.2",
}
_EXCEPTIONGROUP_MARKER = Marker("python_full_version < '3.11'")
LOCKED_RUNTIME_REQUIREMENTS = tuple(
    f"{name}=={version}"
    for name, version in sorted(_LOCKED_RUNTIME_PINS.items())
    if name != "exceptiongroup" or _EXCEPTIONGROUP_MARKER.evaluate()
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
site_roots = []
for value in site.getsitepackages():
    try:
        site_root = Path(value).resolve(strict=True)
    except FileNotFoundError:
        continue
    site_roots.append(site_root)
if not any(package_file.is_relative_to(root) for root in site_roots):
    raise RuntimeError(
        f"installed import escaped isolated site-packages: {{package_file}}"
    )
""".strip()

_CONTRACT_TEST_SCRIPT = """
from pathlib import Path
import sys

package_parent = Path(sys.argv[1]).resolve(strict=True)
checked_package = Path(sys.argv[2]).resolve(strict=True)
sys.dont_write_bytecode = True
sys.path.insert(0, str(package_parent))

import iikocloud_client

package_file = Path(iikocloud_client.__file__).resolve(strict=True)
if not package_file.is_relative_to(checked_package):
    raise RuntimeError(
        f"contract import escaped checked package: {package_file}"
    )

import pytest

raise SystemExit(
    pytest.main([
        "-q",
        "--import-mode=importlib",
        "-p",
        "no:cacheprovider",
        *sys.argv[3:],
    ])
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


def locked_runtime_requirements(
    root: Path,
    *,
    marker_environment: Mapping[str, str] | None = None,
) -> tuple[str, ...]:
    try:
        lock = tomllib.loads((root / "uv.lock").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise PipelineError(f"Cannot read package-check lock: {root / 'uv.lock'}") from error
    raw_packages = lock.get("package")
    if not isinstance(raw_packages, list):
        raise PipelineError("uv.lock has no package table")
    packages: dict[str, list[dict[str, object]]] = {}
    project_package: dict[str, object] | None = None
    for raw in raw_packages:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str):
            raise PipelineError("uv.lock contains an invalid package entry")
        name = raw["name"]
        packages.setdefault(name, []).append(raw)
        source = raw.get("source")
        if isinstance(source, dict) and source.get("editable") == ".":
            project_package = raw
    if project_package is None:
        raise PipelineError("uv.lock has no editable project package")
    groups = project_package.get("dev-dependencies")
    package_check = groups.get("package-check") if isinstance(groups, dict) else None
    if not isinstance(package_check, list):
        raise PipelineError("uv.lock has no package-check dependency group")
    if not package_check:
        raise PipelineError("uv.lock package-check group is invalid")

    environment: dict[str, str] = {
        key: value for key, value in default_environment().items() if isinstance(value, str)
    }
    if marker_environment is not None:
        if not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in marker_environment.items()
        ):
            raise PipelineError("Package-check marker environment is invalid")
        environment.update(marker_environment)

    closure: dict[str, str] = {}
    visiting: list[str] = []

    def active_edge(dependency: object, *, parent: str) -> tuple[str, str | None] | None:
        if not isinstance(dependency, dict) or not isinstance(dependency.get("name"), str):
            raise PipelineError(f"uv.lock dependency is invalid for {parent}")
        name = dependency["name"]
        assert isinstance(name, str)
        raw_marker = dependency.get("marker")
        if raw_marker is not None:
            if not isinstance(raw_marker, str):
                raise PipelineError(f"Invalid marker on dependency {parent} -> {name}")
            try:
                applies = Marker(raw_marker).evaluate(environment=environment)
            except (InvalidMarker, UndefinedComparison, UndefinedEnvironmentName) as error:
                raise PipelineError(
                    f"Invalid marker on dependency {parent} -> {name}: {raw_marker!r}"
                ) from error
            if not applies:
                return None
        raw_version = dependency.get("version")
        if raw_version is not None and not isinstance(raw_version, str):
            raise PipelineError(f"uv.lock dependency version is invalid for {parent} -> {name}")
        return name, raw_version

    def select_package(name: str, requested_version: str | None) -> tuple[str, dict[str, object]]:
        entries = packages.get(name, [])
        if not entries:
            raise PipelineError(f"uv.lock has no package-check artifact for {name}")
        versions: list[str] = []
        for entry in entries:
            version = entry.get("version")
            if not isinstance(version, str):
                raise PipelineError(f"uv.lock package-check version is invalid for {name}")
            versions.append(version)
        selected_versions = sorted(set(versions))
        if requested_version is None:
            if len(selected_versions) != 1:
                raise PipelineError(
                    f"uv.lock has conflicting versions for package-check dependency {name}: "
                    + ", ".join(selected_versions)
                )
            selected_version = selected_versions[0]
        else:
            selected_version = requested_version
            if selected_version not in selected_versions:
                raise PipelineError(
                    f"uv.lock has no package-check artifact for {name}=={selected_version}"
                )
        selected = [entry for entry in entries if entry.get("version") == selected_version]
        if len(selected) != 1:
            raise PipelineError(
                f"uv.lock selects multiple package-check artifacts for {name}=={selected_version}"
            )
        return selected_version, selected[0]

    def visit(name: str, requested_version: str | None) -> None:
        if name in visiting:
            cycle_start = visiting.index(name)
            cycle = (*visiting[cycle_start:], name)
            raise PipelineError("Package-check dependency cycle: " + " -> ".join(cycle))
        version, entry = select_package(name, requested_version)
        selected_version = closure.get(name)
        if selected_version is not None:
            if selected_version != version:
                raise PipelineError(
                    f"uv.lock has conflicting active versions for package-check dependency "
                    f"{name}: {selected_version}, {version}"
                )
            return

        visiting.append(name)
        dependencies = entry.get("dependencies", [])
        if not isinstance(dependencies, list):
            raise PipelineError(f"uv.lock dependencies are invalid for {name}")
        for dependency in dependencies:
            active = active_edge(dependency, parent=name)
            if active is not None:
                dependency_name, dependency_version = active
                visit(dependency_name, dependency_version)
        visiting.pop()
        closure[name] = version

    for dependency in package_check:
        active = active_edge(dependency, parent="package-check")
        if active is not None:
            name, version = active
            visit(name, version)
    return tuple(f"{name}=={closure[name]}" for name in sorted(closure))


def _assert_runtime_lock(root: Path) -> None:
    actual = locked_runtime_requirements(root)
    if actual != LOCKED_RUNTIME_REQUIREMENTS:
        raise PipelineError("Package-check runtime pins differ from the recursive uv.lock closure")


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
    project_root: Path | None = None,
    runner: Runner | None = None,
) -> None:
    if package.is_symlink() or not package.is_dir() or package.name != "iikocloud_client":
        raise PipelineError("Staged package must be a regular iikocloud_client directory")
    _assert_regular_tree(package)
    requested_build = build_root or package.parents[2]
    if requested_build.is_symlink():
        raise PipelineError(f"Package-check build root must not be a symlink: {requested_build}")
    controlled_build = requested_build.resolve(strict=False)
    if project_root is not None:
        _assert_runtime_lock(project_root.resolve(strict=True))
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
    _assert_runtime_lock(resolved_root)
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
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    contract_root = resolved_root / "build/contract-check"
    if contract_root.is_symlink():
        raise PipelineError(f"Contract-check root must not be a symlink: {contract_root}")
    run_root = contract_root / "run"
    _clean_directory(run_root, controlled_root=contract_root)
    _run(
        [
            sys.executable,
            "-I",
            "-c",
            _CONTRACT_TEST_SCRIPT,
            str(package.parent.resolve(strict=True)),
            str(package.resolve(strict=True)),
            *(str((resolved_root / relative).resolve(strict=True)) for relative in selected),
        ],
        cwd=run_root,
        purpose="Generated contract tests",
        runner=runner or subprocess.run,
        env=environment,
    )
