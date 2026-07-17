from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

from iikocloud_client.api_client import ApiClient
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.exceptions import ApiException

from ..capture import LiveCapture
from ..errors import SafetyError
from .profile import ResolvedLiveProfile
from .rates import LiveRateGuard
from .state import LiveStateStore

T = TypeVar("T")


class GeneratedLiveSdk:
    """Apply live safety controls around one generated SDK invocation."""

    def __init__(
        self,
        api_client: ApiClient,
        profile: ResolvedLiveProfile,
        guard: LiveRateGuard,
        state: LiveStateStore,
        capture: LiveCapture | None = None,
    ) -> None:
        if getattr(guard, "state", state) is not state:
            raise SafetyError("Generated live guard must use the same live state")
        self.api_client = api_client
        self.profile = profile
        self.guard = guard
        self.state = state
        self.capture = capture
        self._unusable = False

    def _assert_usable(self) -> None:
        if self._unusable:
            raise SafetyError("Generated live SDK is unusable after a failed live call")

    def _record_status(self, operation_id: str, status: int) -> None:
        try:
            self.guard.record_status(operation_id, status)
        except Exception:
            self._unusable = True
            raise SafetyError("Generated SDK status recording failed without a retry") from None

    def _normalize_api_exception_status(self, status: object) -> int:
        if status is None:
            return 0
        if type(status) is int and 0 <= status <= 599:
            return status
        if (
            type(status) is str
            and len(status) == 3
            and status.isascii()
            and status.isdecimal()
        ):
            normalized = int(status)
            if 100 <= normalized <= 599:
                return normalized
        self._unusable = True
        raise SafetyError("Generated SDK exception has an invalid HTTP status") from None

    async def call_generated(
        self,
        operation_id: str,
        request_model: object,
        invoke: Callable[[], Awaitable[ApiResponse[T]]],
    ) -> T:
        self._assert_usable()
        if self.capture is not None:
            self.capture.assert_selected(operation_id)
        await self.guard.acquire(operation_id)
        try:
            response = await invoke()
        except asyncio.CancelledError:
            self._unusable = True
            raise
        except ApiException as error:
            status = self._normalize_api_exception_status(error.status)
            self._record_status(operation_id, status)
            if status == 429:
                self._unusable = True
                raise SafetyError("iiko returned 429; live circuit opened") from None
            raise
        except Exception:
            self._unusable = True
            raise SafetyError("Generated SDK invocation failed without a retry") from None

        self._record_status(operation_id, response.status_code)
        if response.status_code == 429:
            self._unusable = True
            raise SafetyError("iiko returned 429; live circuit opened") from None
        if self.capture is not None:
            try:
                self.capture.write_model_pair(
                    operation_id,
                    request_model,
                    response.data,
                    metadata={"status": response.status_code},
                )
            except Exception:
                self._unusable = True
                raise SafetyError(
                    "Generated SDK capture failed after response without a retry"
                ) from None
        return response.data
