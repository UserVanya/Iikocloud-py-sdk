from __future__ import annotations

import asyncio
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING, Any
from urllib.parse import unquote, urlsplit
from uuid import UUID

import httpx
import yaml

from ..errors import SafetyError
from ..paths import RepoPaths
from .profile import ResolvedDiscoveryProfile, ResolvedLiveProfile
from .receipt import AUTH_OPERATION_IDS, LiveReceipt
from .state import LiveStateStore

if TYPE_CHECKING:
    from ..capture import LiveCapture

_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_METHODS = {"GET", "POST"}
_MAX_TOKEN_BODY = 64 * 1024
_MAX_CAPTURE_BODY = 64 * 1024 * 1024


@dataclass(frozen=True)
class LiveOperation:
    kind: str
    cleanup: str | None
    method: str
    path: str


class _UniqueKeySafeLoader(yaml.SafeLoader):
    pass


def _unique_mapping(
    loader: _UniqueKeySafeLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found duplicate key",
                key_node.start_mark,
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _unique_mapping,
)


def load_operation_contract(path: Path) -> Mapping[str, LiveOperation]:
    try:
        body = path.read_bytes()
        if len(body) > 1024 * 1024:
            raise SafetyError("Live operation contract is too large")
        value = yaml.load(body.decode("utf-8"), Loader=_UniqueKeySafeLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise SafetyError(f"Cannot load strict live operation contract: {path}") from error
    if not isinstance(value, dict) or set(value) != {"version", "operations"}:
        raise SafetyError("Live operation contract root is invalid")
    if type(value["version"]) is not int or value["version"] != 1:
        raise SafetyError("Live operation contract version must be the integer 1")
    operations = value["operations"]
    if not isinstance(operations, dict):
        raise SafetyError("Live operation contract operations must be an object")
    result: dict[str, LiveOperation] = {}
    for operation_id, entry in operations.items():
        if not isinstance(operation_id, str) or _OPERATION_ID.fullmatch(operation_id) is None:
            raise SafetyError("Live operation contract contains an invalid operation ID")
        if not isinstance(entry, dict) or set(entry) != {
            "kind",
            "cleanup",
            "method",
            "path",
        }:
            raise SafetyError(f"Live operation {operation_id!r} has invalid fields")
        kind = entry["kind"]
        cleanup = entry["cleanup"]
        method = entry["method"]
        endpoint_path = entry["path"]
        if not isinstance(kind, str) or kind not in {
            "auth",
            "read",
            "compensating",
            "cleanup",
        }:
            raise SafetyError(f"Live operation {operation_id!r} has an invalid kind")
        if cleanup is not None and (
            not isinstance(cleanup, str) or _OPERATION_ID.fullmatch(cleanup) is None
        ):
            raise SafetyError(f"Live operation {operation_id!r} has an invalid cleanup")
        if not isinstance(method, str) or method not in _METHODS:
            raise SafetyError(
                f"Live operation {operation_id!r} method must be uppercase GET or POST"
            )
        try:
            safe_path = _safe_relative_path(endpoint_path)
        except SafetyError as error:
            raise SafetyError(f"Live operation {operation_id!r} has an unsafe path") from error
        result[operation_id] = LiveOperation(kind, cleanup, method, safe_path)
    auth_ids = frozenset(
        operation_id
        for operation_id, operation in result.items()
        if operation.kind == "auth"
    )
    if not auth_ids or auth_ids - AUTH_OPERATION_IDS:
        raise SafetyError(
            "Live operation contract must define only the reviewed authentication operations"
        )
    for operation_id, operation in result.items():
        if operation.cleanup is not None:
            cleanup = result.get(operation.cleanup)
            if cleanup is None or cleanup.kind != "cleanup":
                raise SafetyError(f"Live operation {operation_id!r} references an invalid cleanup")
    return MappingProxyType(result)


def _unique_json(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _safe_relative_path(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value.startswith("/")
        or value.startswith("//")
        or len(value) > 2048
        or "\\" in value
        or "{" in value
        or "}" in value
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Live request path is unsafe")
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or parsed.path != value:
        raise SafetyError("Live request path must be a query-free relative path")
    decoded = unquote(value)
    if any(character in decoded for character in ("?", "#", "\\")):
        raise SafetyError("Live request path contains encoded delimiters")
    if any(segment in {"", ".", ".."} for segment in decoded.split("/")[1:]):
        raise SafetyError("Live request path contains unsafe segments")
    return value


class SafeLiveSession:
    """One-token, no-retry client for guarded auth and read-only live calls."""

    def __init__(
        self,
        *,
        profile: ResolvedLiveProfile | ResolvedDiscoveryProfile,
        guard: Any,
        state: LiveStateStore | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        operation_contract: Mapping[str, LiveOperation] | None = None,
        receipt: LiveReceipt | None = None,
        receipt_path: Path | None = None,
        capture: LiveCapture | None = None,
    ) -> None:
        if state is not None and getattr(guard, "state", state) is not state:
            raise SafetyError("Live session state must be the guard's state store")
        if (receipt is None) != (receipt_path is None):
            raise SafetyError("Live session receipt and path must be supplied together")
        if receipt is not None and receipt.completed:
            raise SafetyError("Live session receipt must start incomplete")
        if operation_contract is None:
            root = RepoPaths.discover().root
            operation_contract = load_operation_contract(root / "contracts/live-operations.yaml")
        self.profile = profile
        self.guard = guard
        self.state = state
        if not isinstance(operation_contract, Mapping) or any(
            not isinstance(operation_id, str)
            or _OPERATION_ID.fullmatch(operation_id) is None
            or not isinstance(operation, LiveOperation)
            for operation_id, operation in operation_contract.items()
        ):
            raise SafetyError("Live session operation contract is invalid")
        self._operations = MappingProxyType(dict(operation_contract))
        self._receipt = receipt
        self._receipt_path = receipt_path
        if capture is not None:
            from ..capture import LiveCapture

            if not isinstance(capture, LiveCapture):
                raise SafetyError("Live session capture must be a LiveCapture")
            capture.add_known_secret(profile.api_login)
            if profile.client_secret is not None:
                capture.add_known_secret(profile.client_secret)
        self._capture = capture
        self._access_token: str | None = None
        self._auth_attempted = False
        self._unusable = False
        self._closed = False
        selected_transport = transport or httpx.AsyncHTTPTransport(retries=0)
        self._client = httpx.AsyncClient(
            base_url=profile.base_url,
            transport=selected_transport,
            timeout=httpx.Timeout(connect=10.0, read=30.0, write=30.0, pool=10.0),
            follow_redirects=False,
            trust_env=False,
            headers={"Accept": "application/json"},
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(profile={self.profile.name!r}, "
            f"authenticated={self._access_token is not None}, "
            f"closed={self._closed}, unusable={self._unusable})"
        )

    @property
    def access_token(self) -> str:
        if self._access_token is None:
            raise SafetyError("Live session is not authenticated")
        return self._access_token

    @property
    def is_closed(self) -> bool:
        return self._closed

    @property
    def had_429(self) -> bool:
        return self._receipt.had_429 if self._receipt is not None else self._unusable

    @property
    def receipt(self) -> LiveReceipt | None:
        return self._receipt

    def _assert_usable(self) -> None:
        if self._closed:
            raise SafetyError("Live session is closed")
        if self._unusable:
            raise SafetyError("Live session is unusable after a failed live call")

    async def _reserve(self, operation_id: str) -> None:
        await self.guard.acquire(operation_id)
        if self._receipt is not None and self._receipt_path is not None:
            self._receipt = self._receipt.with_operation(operation_id)
            self._receipt.write(self._receipt_path)

    async def _request_once(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        try:
            return await self._client.request(method, path, **kwargs)
        except asyncio.CancelledError:
            self._unusable = True
            raise
        except Exception:
            self._unusable = True
            raise SafetyError("Live HTTP request failed without a retry") from None

    def _record_response(self, operation_id: str, response: httpx.Response) -> None:
        try:
            self.guard.record_status(operation_id, response.status_code)
        except Exception:
            self._unusable = True
            raise
        if response.status_code == 429:
            self._unusable = True
            if self._receipt is not None and self._receipt_path is not None:
                self._receipt = self._receipt.with_429()
                self._receipt.write(self._receipt_path)
            raise SafetyError("Live API returned 429; circuit is open and no retry is allowed")

    async def authenticate(self) -> None:
        self._assert_usable()
        if self._auth_attempted:
            raise SafetyError("Live authentication may be attempted only once per session")
        auth_version = self.profile.auth_version
        if auth_version == "v2":
            operation_id = "authenticate_v2"
            app_id = self.profile.app_id
            client_secret = self.profile.client_secret
            if app_id is None or client_secret is None:
                raise SafetyError(
                    "Live v2 authentication requires application credentials in the profile"
                )
            payload: dict[str, str] = {
                "appId": app_id,
                "clientSecret": client_secret,
                "apiKey": self.profile.api_login,
            }
        elif auth_version == "v1":
            operation_id = "authenticate"
            payload = {"apiLogin": self.profile.api_login}
        else:
            raise SafetyError("Live profile auth version is unsupported")
        operation = self._operations.get(operation_id)
        if operation is None or operation.kind != "auth":
            raise SafetyError("Live authentication operation is not explicitly allowed")
        self._auth_attempted = True
        await self._reserve(operation_id)
        response = await self._request_once(
            operation.method,
            operation.path,
            json=payload,
        )
        self._record_response(operation_id, response)
        if response.status_code != 200:
            self._unusable = True
            raise SafetyError(f"Live authentication failed with HTTP {response.status_code}")
        if len(response.content) > _MAX_TOKEN_BODY:
            self._unusable = True
            raise SafetyError("Live authentication response is too large")
        content_type = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        if content_type != "application/json":
            self._unusable = True
            raise SafetyError("Live authentication response is not JSON")
        try:
            value = json.loads(
                response.content.decode("utf-8"),
                object_pairs_hook=_unique_json,
                parse_constant=_reject_constant,
            )
        except (UnicodeError, ValueError):
            self._unusable = True
            raise SafetyError("Live authentication response is invalid") from None
        if not isinstance(value, dict) or set(value) != {"correlationId", "token"}:
            self._unusable = True
            raise SafetyError("Live authentication response has an invalid shape")
        correlation_id = value["correlationId"]
        try:
            parsed_correlation_id = (
                UUID(correlation_id) if isinstance(correlation_id, str) else None
            )
        except ValueError:
            parsed_correlation_id = None
        if (
            parsed_correlation_id is None
            or str(parsed_correlation_id) != correlation_id.lower()
        ):
            self._unusable = True
            raise SafetyError("Live authentication response contains an invalid correlation ID")
        token = value["token"]
        if (
            not isinstance(token, str)
            or not token
            or len(token) > 4096
            or any(ord(character) < 32 or ord(character) == 127 for character in token)
        ):
            self._unusable = True
            raise SafetyError("Live authentication response contains an invalid token")
        self._access_token = token
        if self._capture is not None:
            try:
                self._capture.add_known_secret(token)
            except Exception:
                self._unusable = True
                self._access_token = None
                raise SafetyError("Live capture secret binding failed") from None

    async def request_json(
        self,
        operation_id: str,
        method: str,
        path: str,
        payload: Mapping[str, Any] | None,
    ) -> httpx.Response:
        self._assert_usable()
        if self._access_token is None:
            raise SafetyError("Live session must authenticate before API requests")
        if not isinstance(operation_id, str) or _OPERATION_ID.fullmatch(operation_id) is None:
            raise SafetyError("Live operation ID is invalid")
        operation = self._operations.get(operation_id)
        if operation is None:
            raise SafetyError(f"Unknown live operation {operation_id!r}")
        if operation.kind != "read":
            raise SafetyError(f"Safe live session refuses non-read operation {operation_id!r}")
        if not isinstance(method, str) or method not in _METHODS:
            raise SafetyError("Live request method must be uppercase GET or POST")
        safe_path = _safe_relative_path(path)
        if method != operation.method or safe_path != operation.path:
            raise SafetyError(
                f"Live operation {operation_id!r} endpoint does not match its contract"
            )
        if payload is not None:
            if not isinstance(payload, Mapping):
                raise SafetyError("Live JSON payload must be an object or explicitly omitted")
            try:
                json.dumps(payload, allow_nan=False)
            except (TypeError, ValueError):
                raise SafetyError("Live JSON payload is not strictly serializable") from None
        if self._capture is not None:
            if payload is None:
                raise SafetyError("Live capture requires a JSON object payload")
            self._capture.assert_selected(
                operation_id,
                method=method,
                path=safe_path,
            )
        await self._reserve(operation_id)
        request_options: dict[str, Any] = {
            "headers": {"Authorization": f"Bearer {self._access_token}"}
        }
        if payload is not None:
            request_options["json"] = dict(payload)
        response = await self._request_once(
            method,
            safe_path,
            **request_options,
        )
        self._record_response(operation_id, response)
        if self._capture is not None:
            assert payload is not None
            self._capture_read(operation_id, payload, response)
        return response

    def _capture_read(
        self,
        operation_id: str,
        payload: Mapping[str, Any],
        response: httpx.Response,
    ) -> None:
        assert self._capture is not None
        if not 200 <= response.status_code <= 299:
            self._unusable = True
            raise SafetyError(
                f"Live capture failed: non-success HTTP {response.status_code}; no retry"
            ) from None
        if len(response.content) > _MAX_CAPTURE_BODY:
            self._unusable = True
            raise SafetyError("Live capture failed: response too large; no retry") from None
        content_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if content_type != "application/json":
            self._unusable = True
            raise SafetyError(
                "Live capture failed: response content type is not JSON; no retry"
            ) from None
        try:
            response_json = json.loads(
                response.content.decode("utf-8"),
                object_pairs_hook=_unique_json,
                parse_constant=_reject_constant,
            )
        except (UnicodeError, ValueError, RecursionError):
            self._unusable = True
            raise SafetyError("Live capture failed: invalid JSON response; no retry") from None
        try:
            self._capture.write_model_pair(
                operation_id,
                dict(payload),
                response_json,
                metadata={
                    "status": response.status_code,
                    "headers": dict(response.headers),
                },
            )
        except Exception:
            self._unusable = True
            raise SafetyError("Live capture failed: final capture processing; no retry") from None

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._access_token = None
        await self._client.aclose()

    async def __aenter__(self) -> SafeLiveSession:
        self._assert_usable()
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.close()
