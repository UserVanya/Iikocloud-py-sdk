from __future__ import annotations

import re
import stat
import subprocess
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any, TypeVar

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 compatibility
    import tomli as tomllib  # type: ignore[import-not-found,no-redef]

from .errors import SafetyError
from .live.receipt import LiveArtifactHashes, LiveReceipt

PUBLISH_PREFIXES = (
    "openapi/",
    "contracts/",
    "generator/",
    "src/iikocloud_client/",
    "tests/fixtures/contracts/",
    "tests/generated/",
    "docs/generation.md",
    "docs/known-upstream-issues.md",
    "README.md",
    "pyproject.toml",
    "uv.lock",
)

_SEMVER = re.compile(
    r"(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*)\."
    r"(?:0|[1-9][0-9]*)"
    r"(?:-(?:(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+(?:[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?\Z"
)
_VERSION_LINE = re.compile(r'version = "([^"]+)"\Z')
_PROTECTED_BRANCHES = frozenset({"main", "master"})
_MAX_PRIVATE_CONFIG_BYTES = 64 * 1024

CommandRunner = Callable[..., subprocess.CompletedProcess[Any]]
T = TypeVar("T")


@dataclass(frozen=True)
class PublishDependencies:
    git_runner: CommandRunner
    lock_check: Callable[[Path], None]
    offline_verify: Callable[[Path], None]
    runtime_version_gate: Callable[[Path, str], None]
    receipt_gate: Callable[[Path], str]
    circuit_gate: Callable[[Path, str], None]
    mutation_gate: Callable[[Path], None]
    known_secrets_loader: Callable[[Path], Iterable[str]]
    secret_scan: Callable[[Path, Iterable[str]], None]
    wheel_smoke: Callable[[Path], None]
    emit: Callable[[str], object]
    today: Callable[[], date]


def _normalized_publish_path(value: object) -> str:
    if (
        type(value) is not str
        or not value
        or "\\" in value
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Publish path is not a canonical repository path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or any(part in {"", ".", ".."} for part in path.parts)
        or path.as_posix() != value
    ):
        raise SafetyError("Publish path is not a canonical repository path")
    return value


def assert_publishable_paths(paths: Iterable[str]) -> tuple[str, ...]:
    """Return sorted canonical paths only when every path is publish-allowlisted."""

    try:
        values = tuple(paths)
    except Exception:
        raise SafetyError("Publish paths must be an iterable of repository paths") from None
    normalized: list[str] = []
    for value in values:
        path = _normalized_publish_path(value)
        approved = any(
            path.startswith(prefix) if prefix.endswith("/") else path == prefix
            for prefix in PUBLISH_PREFIXES
        )
        if not approved:
            raise SafetyError(f"Path is outside the publish allowlist: {path}")
        normalized.append(path)
    return tuple(sorted(set(normalized)))


def _validated_semver(version: object) -> str:
    if type(version) is not str or _SEMVER.fullmatch(version) is None:
        raise SafetyError("Publish version must be strict SemVer")
    if version.split("+", 1)[0].split("-", 1)[0].count(".") != 2:
        raise SafetyError("Publish version must be strict SemVer")
    return version


def update_project_version(root: Path, version: str) -> bytes:
    """Require the release version to be prepared before generation and live tests."""

    selected_version = _validated_semver(version)
    path = root / "pyproject.toml"
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise OSError
        original = path.read_bytes()
        text = original.decode("utf-8")
    except (OSError, UnicodeError):
        raise SafetyError("Project metadata is not a readable regular UTF-8 file") from None

    lines = text.splitlines(keepends=True)
    in_project = False
    project_sections = 0
    version_indexes: list[int] = []
    current_version: str | None = None
    for index, line in enumerate(lines):
        body = line.removesuffix("\n")
        if body.endswith("\r"):
            raise SafetyError("Project version line must use exact canonical formatting")
        if body.startswith("[") and body.endswith("]"):
            in_project = body == "[project]"
            if in_project:
                project_sections += 1
            continue
        if not in_project:
            continue
        match = _VERSION_LINE.fullmatch(body)
        if match is not None:
            version_indexes.append(index)
            current_version = match.group(1)
        elif body.lstrip().startswith("version"):
            raise SafetyError("Project version line must use exact canonical formatting")

    if project_sections != 1 or len(version_indexes) != 1 or current_version is None:
        raise SafetyError("Project version line must appear exactly once in [project]")
    _validated_semver(current_version)
    if current_version != selected_version:
        raise SafetyError(
            "Publish version must be set before generation, lock, and live verification"
        )
    return original


_RUNTIME_VERSION_PATTERNS = (
    (
        "src/iikocloud_client/__init__.py",
        re.compile(r'^__version__ = "([^"\r\n]+)"$', re.MULTILINE),
    ),
    (
        "src/iikocloud_client/api_client.py",
        re.compile(r"OpenAPI-Generator/([^/'\"\s]+)/python"),
    ),
    (
        "src/iikocloud_client/configuration.py",
        re.compile(r"SDK Package Version: ([^\"\\\r\n]+)"),
    ),
)


def assert_generated_runtime_version(root: Path, version: str) -> None:
    selected_version = _validated_semver(version)
    for relative, pattern in _RUNTIME_VERSION_PATTERNS:
        path = root / relative
        try:
            metadata = path.lstat()
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                raise OSError
            body = path.read_bytes()
            if len(body) > 64 * 1024 * 1024:
                raise OSError
            text = body.decode("utf-8")
        except (OSError, UnicodeError):
            raise SafetyError("Generated runtime version file is missing or unsafe") from None
        matches = pattern.findall(text)
        if matches != [selected_version]:
            raise SafetyError(f"Generated runtime version is inconsistent in {relative}")


def _git_bytes(
    root: Path,
    arguments: Sequence[str],
    *,
    purpose: str,
    runner: CommandRunner = subprocess.run,
    input_data: bytes | None = None,
) -> bytes:
    try:
        completed = runner(
            ["git", *arguments],
            cwd=root,
            check=True,
            capture_output=True,
            shell=False,
            input=input_data,
        )
        output = completed.stdout
        if type(output) is not bytes:
            raise TypeError
        return output
    except Exception:
        raise SafetyError(f"Git {purpose} failed") from None


def _protected_branch_opt_in(root: Path, *, runner: CommandRunner) -> bool:
    relative = "private/publish.toml"
    path = root / relative
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            return False
        ignored = _git_bytes(
            root,
            ["check-ignore", "-z", "--stdin"],
            purpose="protected-branch opt-in check",
            runner=runner,
            input_data=f"{relative}\0".encode(),
        )
        if ignored != f"{relative}\0".encode():
            return False
        body = path.read_bytes()
        if len(body) > _MAX_PRIVATE_CONFIG_BYTES:
            return False
        document = tomllib.loads(body.decode("utf-8"))
        return type(document) is dict and document == {"allow_protected_branch": True}
    except Exception:
        return False


def assert_publish_branch(
    root: Path,
    *,
    runner: CommandRunner = subprocess.run,
) -> str:
    output = _git_bytes(
        root,
        ["branch", "--show-current"],
        purpose="branch inspection",
        runner=runner,
    )
    try:
        branch = output.decode("utf-8").removesuffix("\n")
    except UnicodeError:
        raise SafetyError("Git branch name is not valid UTF-8") from None
    if (
        not branch
        or "\n" in branch
        or "\r" in branch
        or any(ord(character) < 32 or ord(character) == 127 for character in branch)
    ):
        raise SafetyError("Git branch name is unsafe for publication")
    if branch in _PROTECTED_BRANCHES and not _protected_branch_opt_in(root, runner=runner):
        raise SafetyError("Publishing from a protected branch is not allowed") from None
    return branch


def _nul_paths(output: bytes) -> tuple[str, ...]:
    if not output:
        return ()
    if not output.endswith(b"\0"):
        raise SafetyError("Git returned a malformed repository path list")
    result: list[str] = []
    for raw in output[:-1].split(b"\0"):
        try:
            result.append(raw.decode("utf-8"))
        except UnicodeError:
            raise SafetyError("Git repository path is not valid UTF-8") from None
    return tuple(result)


def _dirty_paths(root: Path, *, runner: CommandRunner) -> tuple[str, ...]:
    paths: list[str] = []
    for arguments, purpose in (
        (["diff", "--no-renames", "--name-only", "-z", "--"], "unstaged path inspection"),
        (
            ["diff", "--cached", "--no-renames", "--name-only", "-z", "--"],
            "staged path inspection",
        ),
        (
            ["ls-files", "--others", "--exclude-standard", "-z", "--"],
            "untracked path inspection",
        ),
    ):
        paths.extend(
            _nul_paths(
                _git_bytes(
                    root,
                    arguments,
                    purpose=purpose,
                    runner=runner,
                )
            )
        )
    return tuple(sorted(set(paths)))


def _assert_clean_index(root: Path, *, runner: CommandRunner) -> None:
    staged = _nul_paths(
        _git_bytes(
            root,
            ["diff", "--cached", "--no-renames", "--name-only", "-z", "--"],
            purpose="release index inspection",
            runner=runner,
        )
    )
    if staged:
        raise SafetyError("Publish requires an empty Git index before it stages release paths")


def _safe_git_text(output: bytes, *, label: str) -> str:
    if len(output) > 1024 * 1024:
        raise SafetyError(f"Git {label} output is too large")
    try:
        text = output.decode("utf-8")
    except UnicodeError:
        raise SafetyError(f"Git {label} output is not valid UTF-8") from None
    if any(
        ord(character) < 32 and character not in {"\n", "\t"} or ord(character) == 127
        for character in text
    ):
        raise SafetyError(f"Git {label} output contains an unsafe character")
    return text.rstrip("\n")


def select_matching_live_receipt(
    root: Path,
    artifacts: LiveArtifactHashes,
) -> LiveReceipt:
    """Strictly load every receipt residue and return the latest matching success."""

    if not isinstance(artifacts, LiveArtifactHashes):
        raise SafetyError("Publish live artifact hashes are invalid")
    runs = root / ".state/live-runs"
    try:
        metadata = runs.lstat()
        if (
            stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISDIR(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != 0o700
        ):
            raise OSError
        entries = tuple(sorted(runs.iterdir(), key=lambda path: path.name))
    except (OSError, FileNotFoundError):
        raise SafetyError("Publish live receipt directory is missing or unsafe") from None

    matching: list[LiveReceipt] = []
    for path in entries:
        if path.parent != runs or path.suffix != ".json":
            raise SafetyError("Publish live receipt residue is invalid")
        try:
            receipt = LiveReceipt.load(path)
        except Exception:
            raise SafetyError("Publish live receipt residue is invalid") from None
        if path.name != f"{receipt.run_id}.json":
            raise SafetyError("Publish live receipt filename is invalid")
        if (
            receipt.completed
            and not receipt.had_429
            and receipt.has_required_read_canary
            and receipt.effective_schema_sha256 == artifacts.effective_schema_sha256
            and receipt.generated_tree_sha256 == artifacts.generated_tree_sha256
        ):
            matching.append(receipt)
    if not matching:
        raise SafetyError("No completed matching live receipt authorizes publication")
    return max(matching, key=lambda receipt: receipt.run_id)


def _default_offline_verify(root: Path) -> None:
    from . import pipeline
    from .paths import RepoPaths

    pipeline.verify(pipeline.default_dependencies(offline=True, paths=RepoPaths(root)))


def _default_lock_check(root: Path) -> None:
    try:
        subprocess.run(
            [
                "uv",
                "lock",
                "--check",
                "--offline",
                "--no-config",
                "--project",
                str(root),
            ],
            cwd=root,
            check=True,
            capture_output=True,
            shell=False,
        )
    except Exception:
        raise SafetyError("Project lock is stale or cannot be checked offline") from None


def _default_receipt_gate(root: Path) -> str:
    from .live.receipt import verify_live_artifacts

    receipt = select_matching_live_receipt(root, verify_live_artifacts(root))
    return receipt.profile_fingerprint


def _default_circuit_gate(root: Path, profile_fingerprint: str) -> None:
    from .live.state import LiveStateStore

    LiveStateStore(root / ".state/live-rate-limits.json").assert_circuit_closed(
        profile_fingerprint
    )


def _default_mutation_gate(root: Path) -> None:
    from .live.pytest_support import mutation_journals_absent

    try:
        clean = mutation_journals_absent(root / ".state")
    except Exception:
        clean = False
    if not clean:
        raise SafetyError("Mutation journals must be absent before publication")


def _default_known_secrets_loader(root: Path) -> Iterable[str]:
    from .secrets import load_known_secrets

    return load_known_secrets(root)


def _default_secret_scan(root: Path, known_secrets: Iterable[str]) -> None:
    from .secrets import verify_no_secrets

    verify_no_secrets(root, known_secrets)


def _default_wheel_smoke(root: Path) -> None:
    from .package_checks import verify_root_wheel

    verify_root_wheel(root)


def default_publish_dependencies() -> PublishDependencies:
    return PublishDependencies(
        git_runner=subprocess.run,
        lock_check=_default_lock_check,
        offline_verify=_default_offline_verify,
        runtime_version_gate=assert_generated_runtime_version,
        receipt_gate=_default_receipt_gate,
        circuit_gate=_default_circuit_gate,
        mutation_gate=_default_mutation_gate,
        known_secrets_loader=_default_known_secrets_loader,
        secret_scan=_default_secret_scan,
        wheel_smoke=_default_wheel_smoke,
        emit=print,
        today=date.today,
    )


def _gate(label: str, operation: Callable[[], T]) -> T:
    try:
        return operation()
    except Exception:
        raise SafetyError(f"Publish {label} gate failed") from None


def _assert_tag_available(
    root: Path,
    tag: str,
    *,
    runner: CommandRunner,
) -> None:
    output = _git_bytes(
        root,
        ["tag", "--list", tag],
        purpose="tag preflight",
        runner=runner,
    )
    if _safe_git_text(output, label="tag preflight"):
        raise SafetyError("Publish tag already exists")


def _restore_precommit_state(
    root: Path,
    paths: Sequence[str],
    *,
    staging_attempted: bool,
    runner: CommandRunner,
) -> None:
    try:
        if staging_attempted and paths:
            _git_bytes(
                root,
                ["reset", "--mixed", "HEAD", "--", *paths],
                purpose="pre-commit rollback",
                runner=runner,
            )
    except Exception:
        raise SafetyError("Publish pre-commit rollback failed") from None


def publish(
    root: Path,
    *,
    version: str,
    push: bool = False,
    dependencies: PublishDependencies | None = None,
) -> None:
    """Create one allowlisted release commit and annotated tag after all gates pass."""

    if not isinstance(root, Path):
        raise SafetyError("Publish root must be a filesystem path")
    try:
        selected_root = root.resolve(strict=True)
    except OSError:
        raise SafetyError("Publish root is missing or unsafe") from None
    selected_version = _validated_semver(version)
    if type(push) is not bool:
        raise SafetyError("Publish push flag must be a boolean")
    selected = dependencies or default_publish_dependencies()
    runner = selected.git_runner
    tag = f"v{selected_version}"

    initial_paths = assert_publishable_paths(_dirty_paths(selected_root, runner=runner))
    _assert_clean_index(selected_root, runner=runner)
    assert_publish_branch(selected_root, runner=runner)
    _assert_tag_available(selected_root, tag, runner=runner)

    update_project_version(selected_root, selected_version)
    _gate("project lock", lambda: selected.lock_check(selected_root))
    _gate("offline verification", lambda: selected.offline_verify(selected_root))
    _gate(
        "generated runtime version",
        lambda: selected.runtime_version_gate(selected_root, selected_version),
    )
    profile_fingerprint = _gate(
        "live receipt",
        lambda: selected.receipt_gate(selected_root),
    )
    if (
        not isinstance(profile_fingerprint, str)
        or re.fullmatch(r"[a-f0-9]{64}", profile_fingerprint) is None
    ):
        raise SafetyError("Publish live receipt gate returned an invalid profile")
    _gate(
        "circuit",
        lambda: selected.circuit_gate(selected_root, profile_fingerprint),
    )
    _gate("mutation journal", lambda: selected.mutation_gate(selected_root))
    known_secrets = _gate(
        "known secret loading",
        lambda: tuple(selected.known_secrets_loader(selected_root)),
    )
    _gate("pre-stage secret scan", lambda: selected.secret_scan(selected_root, known_secrets))

    publish_paths: tuple[str, ...] = initial_paths
    staging_attempted = False
    committed = False
    try:
        _gate("wheel smoke", lambda: selected.wheel_smoke(selected_root))
        publish_paths = assert_publishable_paths(_dirty_paths(selected_root, runner=runner))
        if not publish_paths:
            raise SafetyError("Publish has no allowlisted changes to commit")

        stat_output = _safe_git_text(
            _git_bytes(
                selected_root,
                ["diff", "--stat", "HEAD", "--"],
                purpose="diff stat",
                runner=runner,
            ),
            label="diff stat",
        )
        path_plan = "\n".join(f"- {path}" for path in publish_paths)
        _gate(
            "plan rendering",
            lambda: selected.emit(
                "publish diff --stat:\n"
                + (stat_output or "(tracked diff is empty before staging)")
                + "\npublish paths:\n"
                + path_plan
            ),
        )

        staging_attempted = True
        _git_bytes(
            selected_root,
            ["add", "--", *publish_paths],
            purpose="allowlisted staging",
            runner=runner,
        )
        _gate("post-stage secret scan", lambda: selected.secret_scan(selected_root, known_secrets))
        release_date = _gate("release date", selected.today)
        if type(release_date) is not date:
            raise SafetyError("Publish release date gate returned an invalid date")
        message = f"chore(sdk): sync iiko OpenAPI {release_date.isoformat()}"
        _git_bytes(
            selected_root,
            ["commit", "--only", "-m", message, "--", *publish_paths],
            purpose="release commit",
            runner=runner,
        )
        committed = True
    except BaseException:
        if not committed:
            _restore_precommit_state(
                selected_root,
                publish_paths,
                staging_attempted=staging_attempted,
                runner=runner,
            )
        raise

    _git_bytes(
        selected_root,
        ["tag", "-a", tag, "-m", f"Release {tag}"],
        purpose="annotated release tag",
        runner=runner,
    )
    if push:
        _git_bytes(
            selected_root,
            ["push", "origin", "HEAD"],
            purpose="branch push",
            runner=runner,
        )
        _git_bytes(
            selected_root,
            ["push", "origin", tag],
            purpose="tag push",
            runner=runner,
        )
