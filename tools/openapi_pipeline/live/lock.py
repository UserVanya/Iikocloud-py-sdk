from __future__ import annotations

import errno
import fcntl
import os
import stat
from pathlib import Path
from types import TracebackType

from ..errors import SafetyError

_DIRECTORY_MODE = 0o700
_FILE_MODE = 0o600
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)


def _mode_text(mode: int) -> str:
    return f"{stat.S_IMODE(mode):04o}"


def _same_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _validate_private_regular_metadata(current: os.stat_result, *, label: str) -> None:
    if not stat.S_ISREG(current.st_mode):
        raise SafetyError(f"{label} is not a regular file")
    if stat.S_IMODE(current.st_mode) != _FILE_MODE:
        raise SafetyError(f"{label} must have mode 0600")
    if current.st_uid != os.getuid():
        raise SafetyError(f"{label} is not owned by the current user")
    if current.st_nlink != 1:
        raise SafetyError(f"{label} must not have multiple hard links")


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
    except BaseException:
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
    """Linux/WSL non-blocking exclusive lock for a complete live run."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._fd: int | None = None
        self._owner_pid: int | None = None

    @property
    def held(self) -> bool:
        return self._fd is not None and self._owner_pid == os.getpid()

    def acquire(self) -> LiveProcessLock:
        if self._fd is not None:
            raise SafetyError("live process lock is already held by this lock object")
        ensure_private_directory(self.path.parent)

        flags = os.O_RDWR | os.O_CLOEXEC
        nofollow = getattr(os, "O_NOFOLLOW", 0)
        created = False
        try:
            fd = os.open(
                self.path,
                flags | os.O_CREAT | os.O_EXCL | nofollow,
                _FILE_MODE,
            )
            created = True
        except FileExistsError:
            expected = validate_private_regular_file(self.path, label="Live process lock")
            try:
                fd = os.open(self.path, flags | nofollow)
            except OSError as error:
                raise SafetyError(f"Cannot open live process lock safely: {self.path}") from error
            actual = os.fstat(fd)
            if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
                os.close(fd)
                raise SafetyError("Live process lock changed while it was being opened") from None
        except OSError as error:
            raise SafetyError(f"Cannot create live process lock safely: {self.path}") from error

        try:
            if created:
                os.fchmod(fd, _FILE_MODE)
            opened = os.fstat(fd)
            if not stat.S_ISREG(opened.st_mode):
                raise SafetyError(f"Live process lock is not a regular file: {self.path}")
            if stat.S_IMODE(opened.st_mode) != _FILE_MODE:
                raise SafetyError(f"Live process lock must have mode 0600: {self.path}")
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            os.close(fd)
            raise SafetyError("another live test process is active") from error
        except OSError as error:
            os.close(fd)
            if error.errno in (errno.EACCES, errno.EAGAIN):
                raise SafetyError("another live test process is active") from error
            raise SafetyError(f"Cannot acquire live process lock: {self.path}") from error
        except BaseException:
            os.close(fd)
            raise

        self._fd = fd
        self._owner_pid = os.getpid()
        return self

    def assert_current_binding(self) -> None:
        """Prove this held fd is still the private file at the current lock path."""

        if not self.held or self._fd is None:
            raise SafetyError(
                "live process lock was released or is not held by the current process"
            )
        parent_fd: int | None = None
        reopened_fd: int | None = None
        try:
            parent_fd = _open_absolute_parent_nofollow(self.path)
            name = self.path.name
            if not name or name in {".", ".."}:
                raise SafetyError("Live process lock path is not canonical")
            expected = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
            _validate_private_regular_metadata(expected, label="Live process lock")
            reopened_fd = os.open(
                name,
                os.O_RDWR | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=parent_fd,
            )
            reopened = os.fstat(reopened_fd)
            _validate_private_regular_metadata(reopened, label="Live process lock")
            current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
            held = os.fstat(self._fd)
            _validate_private_regular_metadata(held, label="Held live process lock")
            if not (
                _same_identity(expected, reopened)
                and _same_identity(reopened, current)
                and _same_identity(current, held)
            ):
                raise SafetyError("Live process lock binding changed to another inode")
        except OSError as error:
            raise SafetyError("Cannot revalidate live process lock binding safely") from error
        finally:
            if reopened_fd is not None:
                os.close(reopened_fd)
            if parent_fd is not None:
                os.close(parent_fd)

    def release(self) -> None:
        if self._fd is None:
            return
        if self._owner_pid != os.getpid():
            raise SafetyError("live process lock belongs to a different process")
        fd = self._fd
        self._fd = None
        self._owner_pid = None
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)

    def __enter__(self) -> LiveProcessLock:
        return self.acquire()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.release()
