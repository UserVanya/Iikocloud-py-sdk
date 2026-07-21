from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .errors import PipelineError


@dataclass(frozen=True)
class RepoPaths:
    root: Path

    @classmethod
    def discover(cls, start: Path | None = None) -> RepoPaths:
        current = (start or Path.cwd()).resolve()
        for candidate in (current, *current.parents):
            if (candidate / "pyproject.toml").is_file():
                return cls(candidate)
        raise PipelineError("Cannot find repository root containing pyproject.toml")

    @property
    def build(self) -> Path:
        return self.root / "build"

    @property
    def candidate(self) -> Path:
        return self.build / "upstream/candidate.json"

    @property
    def effective(self) -> Path:
        return self.build / "openapi/effective.json"

    @property
    def operation_safety(self) -> Path:
        return self.root / "contracts/operation-safety.yaml"

    @property
    def upstream(self) -> Path:
        return self.root / "openapi/upstream/iikocloud.openapi.json"

    @property
    def private(self) -> Path:
        return self.root / "private"

    @property
    def state(self) -> Path:
        return self.root / ".state"
