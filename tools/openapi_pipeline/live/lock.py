from __future__ import annotations

import errno
import fcntl
import os
import stat
from contextlib import suppress
from dataclasses import dataclass, field
from pathlib import Path
from threading import RLock
from types import TracebackType

from ..errors import SafetyError

_DIRECTORY_MODE = 0o700
_FILE_MODE = 0o600
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)


def _mode_text(mode: int) -> str:
    return f"{stat.S_IMODE(mode):04o}"


def _same_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _validate_private_directory_metadata(current: os.stat_result, *, label: str) -> None:
    if not stat.S_ISDIR(current.st_mode):
        raise SafetyError(f"{label} is not a directory")
    if stat.S_IMODE(current.st_mode) != _DIRECTORY_MODE:
        raise SafetyError(f"{label} must have mode 0700")
    if current.st_uid != os.getuid():
        raise SafetyError(f"{label} is not owned by the current user")


def _validate_private_regular_metadata(current: os.stat_result, *, label: str) -> None:
    if not stat.S_ISREG(current.st_mode):
        raise SafetyError(f"{label} is not a regular file")
    if stat.S_IMODE(current.st_mode) != _FILE_MODE:
        raise SafetyError(f"{label} must have mode 0600")
    if current.st_uid != os.getuid():
        raise SafetyError(f"{label} is not owned by the current user")
    if current.st_nlink != 1:
        raise SafetyError(f"{label} must not have multiple hard links")


def _stable_file_metadata(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_uid,
        value.st_gid,
        value.st_nlink,
        value.st_size,
    )


def _stable_parent_metadata(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_uid,
        value.st_gid,
        value.st_nlink,
    )


@dataclass(frozen=True, slots=True)
class _LiveProcessLockBindingToken:
    _issuer: object = field(repr=False)
    _generation: int = field(repr=False)
    _owner_pid: int = field(repr=False)
    _owner_uid: int = field(repr=False)
    _held_metadata: tuple[int, ...] = field(repr=False)
    _parent_metadata: tuple[int, ...] = field(repr=False)


def _absolute_lock_path(path: Path) -> Path:
    return Path(os.path.abspath(path))


def _acquire_exclusive_flock(fd: int) -> None:
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as error:
        raise SafetyError("another live test process is active") from error
    except OSError as error:
        if error.errno in (errno.EACCES, errno.EAGAIN):
            raise SafetyError("another live test process is active") from error
        raise SafetyError("Cannot acquire live process lock safely") from error


def _best_effort_unlock_close(fd: int | None) -> None:
    if fd is None:
        return
    with suppress(OSError):
        fcntl.flock(fd, fcntl.LOCK_UN)
    with suppress(OSError):
        os.close(fd)


def _open_absolute_parent_nofollow(path: Path) -> int:
    if getattr(os, "O_NOFOLLOW", 0) == 0 or not path.is_absolute():
        raise SafetyError("Secure live process lock revalidation is unavailable")
    components = path.parent.parts[1:]
    if not components or any(component in {"", ".", ".."} for component in components):
        raise SafetyError("Live process lock parent path is not canonical")
    try:
        current_fd = os.open("/", _DIRECTORY_FLAGS)
    except OSError as error:
        raise SafetyError("Cannot open live process lock ancestry safely") from error
    try:
        for index, component in enumerate(components):
            expected = os.stat(component, dir_fd=current_fd, follow_symlinks=False)
            if not stat.S_ISDIR(expected.st_mode) or stat.S_ISLNK(expected.st_mode):
                raise SafetyError("Live process lock ancestry contains an unsafe component")
            next_fd = os.open(component, _DIRECTORY_FLAGS, dir_fd=current_fd)
            try:
                actual = os.fstat(next_fd)
                if not _same_identity(expected, actual):
                    raise SafetyError("Live process lock ancestry changed during revalidation")
                if index == len(components) - 1:
                    if stat.S_IMODE(actual.st_mode) != _DIRECTORY_MODE:
                        raise SafetyError("Live process lock parent must have mode 0700")
                    if actual.st_uid != os.getuid():
                        raise SafetyError(
                            "Live process lock parent is not owned by the current user"
                        )
            except BaseException:
                os.close(next_fd)
                raise
            os.close(current_fd)
            current_fd = next_fd
        return current_fd
    except OSError as error:
        with suppress(OSError):
            os.close(current_fd)
        raise SafetyError("Cannot open live process lock ancestry safely") from error
    except BaseException:
        with suppress(OSError):
            os.close(current_fd)
        raise


def ensure_private_directory(path: Path) -> None:
    """Create or validate one private state directory without following it."""
    try:
        current = path.lstat()
    except FileNotFoundError:
        try:
            path.mkdir(mode=_DIRECTORY_MODE, parents=True)
        except FileExistsError:
            current = path.lstat()
        else:
            os.chmod(path, _DIRECTORY_MODE, follow_symlinks=False)
            current = path.lstat()

    if stat.S_ISLNK(current.st_mode):
        raise SafetyError(f"Private state directory is a symlink: {path}")
    if not stat.S_ISDIR(current.st_mode):
        raise SafetyError(f"Private state path is not a directory: {path}")
    if stat.S_IMODE(current.st_mode) != _DIRECTORY_MODE:
        raise SafetyError(
            "Private state directory must have mode 0700, "
            f"got {_mode_text(current.st_mode)}: {path}"
        )
    if current.st_uid != os.getuid():
        raise SafetyError(f"Private state directory is not owned by the current user: {path}")


def validate_private_regular_file(path: Path, *, label: str) -> os.stat_result:
    """Validate an existing private file with lstat; never follow a symlink."""
    try:
        current = path.lstat()
    except FileNotFoundError:
        raise
    if stat.S_ISLNK(current.st_mode):
        raise SafetyError(f"{label} is a symlink: {path}")
    try:
        _validate_private_regular_metadata(current, label=label)
    except SafetyError as error:
        raise SafetyError(f"{error}: {path}") from None
    return current


class LiveProcessLock:
    """Linux/WSL cooperative exclusive lock for one complete live run.

    Every conforming lock name in the same private parent directory shares the
    parent flock and therefore one complete-live-run scope. Advisory locking
    does not prevent same-user code that ignores this class from mutating paths,
    and it does not claim to protect a replaced repository ancestor.
    """

    def __init__(self, path: Path) -> None:
        self.path = path
        self._parent_fd: int | None = None
        self._fd: int | None = None
        self._owner_pid: int | None = None
        self._token_issuer = object()
        self._acquisition_generation = 0
        self._binding_token: _LiveProcessLockBindingToken | None = None
        self._mutex = RLock()
        self._mutex_pid = os.getpid()

    def _current_mutex(self) -> RLock:
        current_pid = os.getpid()
        if self._mutex_pid != current_pid:
            self._mutex = RLock()
            self._mutex_pid = current_pid
        return self._mutex

    def _held_unlocked(self) -> bool:
        return (
            self._parent_fd is not None and self._fd is not None and self._owner_pid == os.getpid()
        )

    @property
    def held(self) -> bool:
        with self._current_mutex():
            return self._held_unlocked()

    def acquire(self) -> LiveProcessLock:
        with self._current_mutex():
            if self._parent_fd is not None or self._fd is not None:
                raise SafetyError("live process lock is already held by this lock object")

            absolute_path = _absolute_lock_path(self.path)
            ensure_private_directory(absolute_path.parent)
            parent_fd: int | None = None
            fd: int | None = None
            try:
                parent_fd = _open_absolute_parent_nofollow(absolute_path)
                _acquire_exclusive_flock(parent_fd)

                name = absolute_path.name
                if not name or name in {".", ".."}:
                    raise SafetyError("Live process lock path is not canonical")
                flags = os.O_RDWR | os.O_CLOEXEC
                nofollow = getattr(os, "O_NOFOLLOW", 0)
                created = False
                try:
                    fd = os.open(
                        name,
                        flags | os.O_CREAT | os.O_EXCL | nofollow,
                        _FILE_MODE,
                        dir_fd=parent_fd,
                    )
                    created = True
                except FileExistsError:
                    try:
                        expected = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
                        if stat.S_ISLNK(expected.st_mode):
                            raise SafetyError("Live process lock is a symlink")
                        _validate_private_regular_metadata(expected, label="Live process lock")
                        fd = os.open(name, flags | nofollow, dir_fd=parent_fd)
                        actual = os.fstat(fd)
                        if not _same_identity(expected, actual):
                            raise SafetyError(
                                "Live process lock changed while it was being opened"
                            )
                    except SafetyError:
                        raise
                    except OSError as error:
                        raise SafetyError("Cannot open live process lock safely") from error
                except OSError as error:
                    raise SafetyError("Cannot create or open live process lock safely") from error

                if created:
                    os.fchmod(fd, _FILE_MODE)
                opened = os.fstat(fd)
                _validate_private_regular_metadata(opened, label="Live process lock")
                _acquire_exclusive_flock(fd)
            except BaseException:
                _best_effort_unlock_close(fd)
                _best_effort_unlock_close(parent_fd)
                raise

            self._parent_fd = parent_fd
            self._fd = fd
            self._owner_pid = os.getpid()
            self._acquisition_generation += 1
            self._binding_token = None
            return self

    def _current_binding_metadata(self) -> tuple[tuple[int, ...], tuple[int, ...]]:
        if not self._held_unlocked() or self._parent_fd is None or self._fd is None:
            raise SafetyError(
                "live process lock was released or is not held by the current process"
            )
        reopened_parent_fd: int | None = None
        reopened_fd: int | None = None
        try:
            held_parent = os.fstat(self._parent_fd)
            _validate_private_directory_metadata(
                held_parent,
                label="Held live process lock parent",
            )
            absolute_path = _absolute_lock_path(self.path)
            reopened_parent_fd = _open_absolute_parent_nofollow(absolute_path)
            current_parent = os.fstat(reopened_parent_fd)
            if not _same_identity(held_parent, current_parent):
                raise SafetyError("Live process lock parent binding changed to another inode")

            name = absolute_path.name
            if not name or name in {".", ".."}:
                raise SafetyError("Live process lock path is not canonical")
            expected = os.stat(name, dir_fd=reopened_parent_fd, follow_symlinks=False)
            _validate_private_regular_metadata(expected, label="Live process lock")
            reopened_fd = os.open(
                name,
                os.O_RDWR | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=reopened_parent_fd,
            )
            reopened = os.fstat(reopened_fd)
            _validate_private_regular_metadata(reopened, label="Live process lock")
            current = os.stat(name, dir_fd=reopened_parent_fd, follow_symlinks=False)
            held = os.fstat(self._fd)
            _validate_private_regular_metadata(held, label="Held live process lock")
            if not (
                _same_identity(expected, reopened)
                and _same_identity(reopened, current)
                and _same_identity(current, held)
            ):
                raise SafetyError("Live process lock binding changed to another inode")
            return _stable_file_metadata(held), _stable_parent_metadata(held_parent)
        except OSError as error:
            raise SafetyError("Cannot revalidate live process lock binding safely") from error
        finally:
            if reopened_fd is not None:
                os.close(reopened_fd)
            if reopened_parent_fd is not None:
                os.close(reopened_parent_fd)

    def assert_current_binding(self) -> None:
        """Prove this held fd is still the private file at the current lock path."""

        with self._current_mutex():
            before = self._binding_state_unlocked()
            self._current_binding_metadata()
            if not self._same_binding_state(before) or not self._held_unlocked():
                raise SafetyError("Live process lock acquisition changed during revalidation")

    def _binding_state_unlocked(
        self,
    ) -> tuple[int | None, int | None, int | None, int, object | None]:
        return (
            self._parent_fd,
            self._fd,
            self._owner_pid,
            self._acquisition_generation,
            self._binding_token,
        )

    def _same_binding_state(
        self,
        expected: tuple[int | None, int | None, int | None, int, object | None],
    ) -> bool:
        current = self._binding_state_unlocked()
        return current[:4] == expected[:4] and current[4] is expected[4]

    def _token_is_current_unlocked(self, token: object) -> bool:
        return (
            type(token) is _LiveProcessLockBindingToken
            and token is self._binding_token
            and token._issuer is self._token_issuer
            and token._generation == self._acquisition_generation
            and token._owner_pid == self._owner_pid
            and token._owner_uid == os.getuid()
            and self._held_unlocked()
        )

    def capture_binding_token(self) -> _LiveProcessLockBindingToken:
        """Return the opaque immutable token for this exact acquisition."""

        with self._current_mutex():
            token = self._binding_token
            if token is None:
                before = self._binding_state_unlocked()
                generation = self._acquisition_generation
                owner_pid = self._owner_pid
                held_metadata, parent_metadata = self._current_binding_metadata()
                if (
                    owner_pid is None
                    or not self._held_unlocked()
                    or not self._same_binding_state(before)
                ):
                    raise SafetyError("Live process lock acquisition changed while binding")
                token = _LiveProcessLockBindingToken(
                    self._token_issuer,
                    generation,
                    owner_pid,
                    os.getuid(),
                    held_metadata,
                    parent_metadata,
                )
                self._binding_token = token
            else:
                self._assert_binding_token_unlocked(token)
            return token

    def assert_binding_token(self, token: object) -> None:
        """Prove a token still represents this exact uninterrupted acquisition."""

        with self._current_mutex():
            self._assert_binding_token_unlocked(token)

    def _assert_binding_token_unlocked(self, token: object) -> None:
        if not self._token_is_current_unlocked(token):
            raise SafetyError(
                "Live process lock was released or its acquisition binding token is invalid"
            )
        before = self._binding_state_unlocked()
        held_metadata, parent_metadata = self._current_binding_metadata()
        if not self._token_is_current_unlocked(token) or not self._same_binding_state(before):
            raise SafetyError("Live process lock acquisition changed during revalidation")
        assert type(token) is _LiveProcessLockBindingToken
        if token._held_metadata != held_metadata or token._parent_metadata != parent_metadata:
            raise SafetyError("Live process lock acquisition binding changed")

    def release(self) -> None:
        with self._current_mutex():
            if self._parent_fd is None and self._fd is None:
                return
            if self._owner_pid != os.getpid():
                raise SafetyError("live process lock belongs to a different process")
            parent_fd = self._parent_fd
            fd = self._fd
            self._parent_fd = None
            self._fd = None
            self._owner_pid = None
            self._binding_token = None
            try:
                if fd is not None:
                    try:
                        fcntl.flock(fd, fcntl.LOCK_UN)
                    finally:
                        os.close(fd)
            finally:
                if parent_fd is not None:
                    try:
                        fcntl.flock(parent_fd, fcntl.LOCK_UN)
                    finally:
                        os.close(parent_fd)

    def __enter__(self) -> LiveProcessLock:
        return self.acquire()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.release()
