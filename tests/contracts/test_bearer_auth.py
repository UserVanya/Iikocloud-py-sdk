from iikocloud_client.api_client import ApiClient
from iikocloud_client.configuration import Configuration
from iikocloud_client.models.tag_dto import TagDto

_SYNTHETIC_TOKEN = "generated-contract-token-7f3b9d1a"


def test_bearer_token_is_applied_once_without_leaking_into_models_or_repr() -> None:
    configuration = Configuration(access_token=_SYNTHETIC_TOKEN)
    client = ApiClient(configuration)
    model = TagDto(name="public-contract-fixture")
    model_dump = model.model_dump(mode="json", by_alias=True)

    auth_settings = configuration.auth_settings()
    assert tuple(auth_settings) == ("BearerAuth",)

    headers: dict[str, str] = {}
    queries: list[tuple[str, str]] = []
    client.update_params_for_auth(
        headers,
        queries,
        ["BearerAuth"],
        "/api/2/menu/by_id",
        "POST",
        model_dump,
    )

    authorization_headers = [
        (name, value) for name, value in headers.items() if name.casefold() == "authorization"
    ]
    assert authorization_headers == [("Authorization", f"Bearer {_SYNTHETIC_TOKEN}")]
    assert queries == []

    for rendered in (
        repr(model_dump),
        repr(model),
        repr(configuration),
        repr(client),
    ):
        assert _SYNTHETIC_TOKEN not in rendered
