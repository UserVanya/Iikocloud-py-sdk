from __future__ import annotations

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

    async def call_generated(
        self,
        operation_id: str,
        request_model: object,
        invoke: Callable[[], Awaitable[ApiResponse[T]]],
    ) -> T:
        await self.guard.acquire(operation_id)
        try:
            response = await invoke()
        except ApiException as error:
            self.guard.record_status(operation_id, int(error.status or 0))
            if error.status == 429:
                raise SafetyError("iiko returned 429; live circuit opened") from error
            raise

        self.guard.record_status(operation_id, response.status_code)
        if self.capture is not None:
            self.capture.write_model_pair(
                operation_id,
                request_model,
                response.data,
                metadata={"status": response.status_code},
            )
        return response.data
