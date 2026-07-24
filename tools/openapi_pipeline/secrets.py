from __future__ import annotations

import json
import os
import re
import stat
import subprocess
import tempfile
from collections.abc import Callable, Iterable, Mapping, Sequence
from contextlib import suppress
from io import StringIO
from pathlib import Path, PurePosixPath
from typing import Any

from dotenv import dotenv_values

from .errors import SafetyError
from .io import canonical_json_bytes

_BASELINE_NAME = ".secrets.baseline"
_KNOWN_SECRET_NAMES = (
    "IIKO_API_KEY",
    "IIKO_API_KEY_2",
    "IIKO_WRITE_API_KEY",
    "IIKO_CLIENT_SECRET",
)
_ALLOWED_PRIVATE_PATHS = frozenset({"private/.gitignore", "private/README.md"})
_FORBIDDEN_ROOTS = frozenset({".state", "build", "dist"})
_MAX_ENV_BYTES = 1024 * 1024
_MAX_BASELINE_BYTES = 16 * 1024 * 1024
_MAX_INDEX_BLOB_BYTES = 256 * 1024 * 1024
_INDEX_ENTRY = re.compile(rb"(100644|100755|120000|160000) ([a-f0-9]{40}|[a-f0-9]{64}) ([0-3])\t")

CommandRunner = Callable[..., subprocess.CompletedProcess[Any]]


def _canonical_relative_path(value: object) -> str:
    if (
        type(value) is not str
        or not value
        or "\\" in value
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Secret scan path policy rejected a noncanonical path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or any(part in {"", ".", ".."} for part in path.parts)
        or path.as_posix() != value
    ):
        raise SafetyError("Secret scan path policy rejected a noncanonical path")
    return value


def assert_secret_path_policy(paths: Iterable[str]) -> tuple[str, ...]:
    """Return canonical paths after rejecting all private/runtime material."""

    try:
        values = tuple(paths)
    except Exception:
        raise SafetyError("Secret scan path policy requires repository paths") from None
    accepted: list[str] = []
    for raw_path in values:
        path = _canonical_relative_path(raw_path)
        parts = PurePosixPath(path).parts
        forbidden = (
            parts[0] in _FORBIDDEN_ROOTS
            or parts[-1] in {".env", ".env.local"}
            or (parts[0] == "private" and path not in _ALLOWED_PRIVATE_PATHS)
        )
        if forbidden:
            raise SafetyError(f"Secret scan path policy rejected: {path}")
        accepted.append(path)
    return tuple(sorted(set(accepted)))


def _parse_nul_paths(body: object, *, label: str) -> tuple[str, ...]:
    if type(body) is not bytes:
        raise SafetyError(f"Git {label} did not return bytes")
    if not body:
        return ()
    if not body.endswith(b"\0"):
        raise SafetyError(f"Git {label} did not return NUL-terminated paths")
    raw_paths = body[:-1].split(b"\0")
    if any(not value for value in raw_paths):
        raise SafetyError(f"Git {label} returned an empty NUL-delimited path")
    try:
        return tuple(value.decode("utf-8") for value in raw_paths)
    except UnicodeError:
        raise SafetyError(f"Git {label} returned a non-UTF-8 path") from None


def _checked_git_paths(
    root: Path,
    arguments: Sequence[str],
    *,
    label: str,
    runner: CommandRunner,
) -> tuple[str, ...]:
    try:
        completed = runner(
            ["git", *arguments],
            cwd=root,
            capture_output=True,
            check=True,
        )
    except Exception:
        raise SafetyError(f"Cannot enumerate Git {label} safely") from None
    return _parse_nul_paths(completed.stdout, label=label)


def collect_tracked_and_staged_paths(
    root: Path,
    *,
    runner: CommandRunner = subprocess.run,
) -> tuple[str, ...]:
    """Collect exact tracked and index-dirty paths using NUL-delimited Git output."""

    repository = root.resolve(strict=True)
    tracked, staged = _collect_tracked_and_staged_paths(repository, runner=runner)
    return assert_secret_path_policy((*tracked, *staged))


def _collect_tracked_and_staged_paths(
    root: Path,
    *,
    runner: CommandRunner,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    tracked = assert_secret_path_policy(
        _checked_git_paths(
            root,
            ["ls-files", "-z", "--"],
            label="tracked files",
            runner=runner,
        )
    )
    staged = assert_secret_path_policy(
        _checked_git_paths(
            root,
            ["diff", "--cached", "--name-only", "-z", "--"],
            label="staged files",
            runner=runner,
        )
    )
    return tracked, staged


def _regular_scan_files(
    root: Path,
    paths: Iterable[str],
) -> tuple[tuple[str, ...], tuple[Path, ...]]:
    relatives: list[str] = []
    absolute: list[Path] = []
    for relative in paths:
        path = root / relative
        try:
            metadata = path.lstat()
        except FileNotFoundError:
            # A staged deletion has no worktree bytes to inspect.
            continue
        except OSError:
            raise SafetyError(f"Cannot inspect tracked/staged file safely: {relative}") from None
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise SafetyError(f"Tracked/staged scan target is not a regular file: {relative}")
        absolute.append(path)
        if relative != _BASELINE_NAME:
            relatives.append(relative)
    return tuple(relatives), tuple(absolute)


def _strict_json(body: bytes, *, label: str) -> Any:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    def reject_constant(_value: str) -> None:
        raise ValueError("non-finite JSON number")

    try:
        return json.loads(
            body.decode("utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except (UnicodeError, ValueError):
        raise SafetyError(f"{label} is not valid strict JSON") from None


def _validate_baseline_document(value: Any) -> dict[str, Any]:
    required = {"version", "plugins_used", "filters_used", "results", "generated_at"}
    if type(value) is not dict or set(value) != required:
        raise SafetyError("Secret baseline JSON has an invalid root shape")
    if (
        type(value["version"]) is not str
        or type(value["generated_at"]) is not str
        or type(value["plugins_used"]) is not list
        or type(value["filters_used"]) is not list
        or type(value["results"]) is not dict
    ):
        raise SafetyError("Secret baseline JSON has invalid field types")
    for raw_path, findings in value["results"].items():
        _canonical_relative_path(raw_path)
        if type(findings) is not list or any(type(item) is not dict for item in findings):
            raise SafetyError("Secret baseline JSON has invalid findings")
    return value


def _load_baseline(root: Path) -> bytes:
    path = root / _BASELINE_NAME
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise OSError
        body = path.read_bytes()
    except OSError:
        raise SafetyError("Secret baseline is missing or unsafe") from None
    if len(body) > _MAX_BASELINE_BYTES:
        raise SafetyError("Secret baseline is too large")
    _validate_baseline_document(_strict_json(body, label="Secret baseline"))
    return body


def _run_detector(
    scan_root: Path,
    relative_files: Sequence[str],
    baseline_body: bytes,
    *,
    runner: CommandRunner,
) -> None:
    if not relative_files:
        return
    with tempfile.TemporaryDirectory(prefix="iikocloud-secret-baseline-") as directory:
        temporary_baseline = Path(directory) / _BASELINE_NAME
        temporary_baseline.write_bytes(baseline_body)
        arguments = [
            "detect-secrets-hook",
            "--no-verify",
            "--baseline",
            str(temporary_baseline),
            "--",
            *relative_files,
        ]
        try:
            completed = runner(
                arguments,
                cwd=scan_root,
                capture_output=True,
                check=False,
            )
        except Exception:
            raise SafetyError("Secret detector could not be executed") from None
        if type(completed.returncode) is not int or completed.returncode != 0:
            raise SafetyError("Secret detector found a candidate or failed")


def _git_bytes(
    root: Path,
    arguments: Sequence[str],
    *,
    label: str,
    runner: CommandRunner,
) -> bytes:
    try:
        completed = runner(
            ["git", *arguments],
            cwd=root,
            capture_output=True,
            check=True,
        )
    except Exception:
        raise SafetyError(f"Cannot read Git {label} safely") from None
    if type(completed.stdout) is not bytes:
        raise SafetyError(f"Git {label} did not return bytes")
    return completed.stdout


def _index_blob(
    root: Path,
    relative: str,
    *,
    runner: CommandRunner,
) -> tuple[int, bytes] | None:
    entry = _git_bytes(
        root,
        ["ls-files", "--stage", "-z", "--", relative],
        label="index entry",
        runner=runner,
    )
    if not entry:
        return None
    if not entry.endswith(b"\0") or entry[:-1].count(b"\0") != 0:
        raise SafetyError("Git index entry is malformed")
    value = entry[:-1]
    match = _INDEX_ENTRY.match(value)
    if match is None:
        raise SafetyError("Git index entry is malformed")
    raw_path = value[match.end() :]
    try:
        index_path = raw_path.decode("utf-8")
    except UnicodeError:
        raise SafetyError("Git index entry path is not UTF-8") from None
    mode, object_id, stage = match.groups()
    if index_path != relative or stage != b"0":
        raise SafetyError("Git index entry does not match the staged path")
    if mode not in {b"100644", b"100755"}:
        raise SafetyError("Git staged scan target must be a regular file")
    blob = _git_bytes(
        root,
        ["cat-file", "blob", object_id.decode("ascii")],
        label="index blob",
        runner=runner,
    )
    if len(blob) > _MAX_INDEX_BLOB_BYTES:
        raise SafetyError("Git index blob is too large to scan safely")
    return (0o755 if mode == b"100755" else 0o644), blob


def _materialize_staged_snapshot(
    root: Path,
    snapshot_root: Path,
    staged_paths: Sequence[str],
    baseline_body: bytes,
    *,
    runner: CommandRunner,
) -> tuple[tuple[str, ...], tuple[Path, ...]]:
    detector_paths: list[str] = []
    exact_paths: list[Path] = []
    for relative in staged_paths:
        indexed = _index_blob(root, relative, runner=runner)
        if indexed is None:  # A staged deletion has no secret-bearing blob.
            continue
        mode, body = indexed
        if relative == _BASELINE_NAME:
            if body != baseline_body:
                raise SafetyError("Staged secret baseline differs from the audited worktree copy")
            continue
        destination = snapshot_root / relative
        destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        destination.write_bytes(body)
        destination.chmod(mode)
        detector_paths.append(relative)
        exact_paths.append(destination)
    return tuple(detector_paths), tuple(exact_paths)


def assert_known_secrets_absent(files: Iterable[Path], known_secrets: Iterable[str]) -> None:
    """Find exact active secret values without ever including a value in diagnostics."""

    try:
        values = tuple(known_secrets)
    except Exception:
        raise SafetyError("Known secrets must be an iterable of strings") from None
    if any(type(value) is not str for value in values):
        raise SafetyError("Known secrets must be strings")
    encoded = tuple(dict.fromkeys(value.encode("utf-8") for value in values if value))
    if not encoded:
        return
    for path in files:
        try:
            metadata = path.lstat()
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
                raise OSError
            body = path.read_bytes()
        except OSError:
            raise SafetyError(f"Cannot scan tracked/staged file safely: {path}") from None
        if any(value in body for value in encoded):
            raise SafetyError(f"Known active secret found in tracked/staged file: {path}")


def verify_no_secrets(
    root: Path,
    known_secrets: Iterable[str] = (),
    *,
    runner: CommandRunner = subprocess.run,
) -> None:
    """Run path policy, audited detector, and exact active-secret checks."""

    repository = root.resolve(strict=True)
    tracked, staged = _collect_tracked_and_staged_paths(repository, runner=runner)
    paths = assert_secret_path_policy((*tracked, *staged))
    baseline_body = _load_baseline(repository)
    relative_files, absolute_files = _regular_scan_files(repository, paths)
    _run_detector(repository, relative_files, baseline_body, runner=runner)
    assert_known_secrets_absent(absolute_files, known_secrets)
    if staged:
        with tempfile.TemporaryDirectory(prefix="iikocloud-index-scan-") as directory:
            snapshot_root = Path(directory)
            _git_bytes(
                snapshot_root,
                ["init", "-q"],
                label="temporary scan repository initialization",
                runner=runner,
            )
            staged_files, staged_absolute = _materialize_staged_snapshot(
                repository,
                snapshot_root,
                staged,
                baseline_body,
                runner=runner,
            )
            _run_detector(snapshot_root, staged_files, baseline_body, runner=runner)
            assert_known_secrets_absent(staged_absolute, known_secrets)


def _read_root_env(root: Path, env_file: Path | None) -> Mapping[str, str | None]:
    expected = Path(os.path.abspath(root / ".env"))
    selected = expected if env_file is None else Path(os.path.abspath(env_file))
    if selected != expected:
        raise SafetyError("Known-secret loader accepts only the repository root .env")
    try:
        metadata = selected.lstat()
    except FileNotFoundError:
        return {}
    except OSError:
        raise SafetyError("Cannot inspect repository root .env safely") from None
    if (
        stat.S_ISLNK(metadata.st_mode)
        or not stat.S_ISREG(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != 0o600
        or metadata.st_uid != os.getuid()
        or metadata.st_nlink != 1
    ):
        raise SafetyError("Repository root .env must be an owned 0600 regular file")
    try:
        body = selected.read_bytes()
    except OSError:
        raise SafetyError("Cannot read repository root .env safely") from None
    if len(body) > _MAX_ENV_BYTES:
        raise SafetyError("Repository root .env is too large")
    try:
        text = body.decode("utf-8")
    except UnicodeError:
        raise SafetyError("Repository root .env must be UTF-8") from None

    seen: set[str] = set()
    for line in text.splitlines():
        candidate = line.lstrip()
        if candidate.startswith("export "):
            candidate = candidate[7:].lstrip()
        name, separator, _remainder = candidate.partition("=")
        name = name.rstrip()
        if separator and name in _KNOWN_SECRET_NAMES:
            if name in seen:
                raise SafetyError("Repository root .env repeats a known-secret name")
            seen.add(name)
    try:
        return dotenv_values(stream=StringIO(text), interpolate=False)
    except Exception:
        raise SafetyError("Repository root .env cannot be parsed safely") from None


def load_known_secrets(
    root: Path,
    *,
    environ: Mapping[str, str] | None = None,
    env_file: Path | None = None,
) -> tuple[str, ...]:
    """Load only the two approved active login values, with process precedence."""

    repository = root.resolve(strict=True)
    environment = os.environ if environ is None else environ
    file_values = _read_root_env(repository, env_file)
    result: list[str] = []
    for name in _KNOWN_SECRET_NAMES:
        raw: object = environment[name] if name in environment else file_values.get(name)
        if raw is None or raw == "":
            continue
        if type(raw) is not str:
            raise SafetyError("Known-secret source contains a non-string value")
        if raw not in result:
            result.append(raw)
    return tuple(result)


def _write_new_baseline(path: Path, body: bytes) -> None:
    descriptor: int | None = None
    temporary: Path | None = None
    try:
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.",
            dir=path.parent,
        )
        temporary = Path(temporary_name)
        os.fchmod(descriptor, 0o644)
        view = memoryview(body)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError
            view = view[written:]
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = None
        try:
            os.link(temporary, path, follow_symlinks=False)
        except FileExistsError:
            raise SafetyError("Secret baseline already exists") from None
        temporary.unlink()
        temporary = None
        directory_flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_DIRECTORY", 0)
        directory_descriptor = os.open(path.parent, directory_flags)
        try:
            os.fsync(directory_descriptor)
        finally:
            os.close(directory_descriptor)
    except SafetyError:
        raise
    except OSError:
        raise SafetyError("Cannot publish secret baseline safely") from None
    finally:
        if descriptor is not None:
            os.close(descriptor)
        if temporary is not None:
            with suppress(FileNotFoundError):
                temporary.unlink()


def create_secrets_baseline(
    root: Path,
    *,
    runner: CommandRunner = subprocess.run,
) -> Path:
    """Create, but never replace, a strict detector baseline from tracked files."""

    repository = root.resolve(strict=True)
    target = repository / _BASELINE_NAME
    try:
        target.lstat()
    except FileNotFoundError:
        pass
    except OSError:
        raise SafetyError("Cannot inspect secret baseline destination") from None
    else:
        raise SafetyError("Secret baseline already exists")

    tracked = _checked_git_paths(
        repository,
        ["ls-files", "-z", "--"],
        label="tracked files",
        runner=runner,
    )
    approved = assert_secret_path_policy(tracked)
    relative_files, _absolute_files = _regular_scan_files(repository, approved)
    arguments = ["detect-secrets", "scan", "--no-verify", "--", *relative_files]
    try:
        completed = runner(
            arguments,
            cwd=repository,
            capture_output=True,
            check=False,
        )
    except Exception:
        raise SafetyError("Secret baseline scan could not be executed") from None
    if type(completed.returncode) is not int or completed.returncode != 0:
        raise SafetyError("Secret baseline scan failed")
    if type(completed.stdout) is not bytes or len(completed.stdout) > _MAX_BASELINE_BYTES:
        raise SafetyError("Secret baseline scan returned invalid output")
    document = _validate_baseline_document(
        _strict_json(completed.stdout, label="Secret baseline scan output")
    )
    _write_new_baseline(target, canonical_json_bytes(document))
    return target
