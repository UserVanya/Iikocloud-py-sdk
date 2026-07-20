# iikocloud-client

Асинхронный Python SDK для iiko Cloud API. Клиент генерируется из
зафиксированного OpenAPI snapshot, а ошибки upstream исправляются отдельно —
через проверяемые overlays, реестры имён и синтетические contract fixtures.
Generated-код в `src/iikocloud_client` вручную не редактируется.

Требуется Python 3.10 или новее.

## Установка из Git tag

После публикации проверенного tag закрепляйте именно tag (или commit), а не
ветку. Например, для `v0.1.0`:

```bash
python -m pip install "iikocloud-client @ git+ssh://git@github.com/UserVanya/Iikocloud-py-sdk.git@v0.1.0"
```

До появления такого tag используйте локальный wheel; эта документация не
создаёт и не публикует tag автоматически.

## Быстрый старт

Ниже показан совместимый flow с одним iiko API login. Upstream уже помечает
`/api/1/access_token` deprecated; для новой трёхкомпонентной авторизации SDK
также генерирует `GetAccessTokenV2Request` и
`AuthorizationApi.authenticate_v2`.

```python
import asyncio
import os
from uuid import UUID

from iikocloud_client import (
    ApiClient,
    AuthorizationApi,
    Configuration,
    GetAccessTokenRequest,
    GetOrganizationsRequest,
    OrganizationsApi,
)

BASE_URL = "https://api-ru.iiko.services"


async def list_organizations() -> list[tuple[str, str | None]]:
    auth_configuration = Configuration(host=BASE_URL)
    async with ApiClient(auth_configuration) as auth_client:
        token_response = await AuthorizationApi(auth_client).authenticate(
            get_access_token_request=GetAccessTokenRequest(
                api_login=os.environ["IIKO_API_KEY"],
            ),
            _request_timeout=(10.0, 30.0),
        )

    configuration = Configuration(
        host=BASE_URL,
        access_token=token_response.token,
    )
    async with ApiClient(configuration) as api_client:
        response = await OrganizationsApi(api_client).get_organizations(
            get_organizations_request=GetOrganizationsRequest(
                organization_ids=[UUID(os.environ["IIKO_ORGANIZATION_ID"])],
                return_additional_info=False,
                include_disabled=False,
            ),
            _request_timeout=(10.0, 30.0),
        )

    return [(str(organization.id), organization.name) for organization in response.organizations]


print(asyncio.run(list_organizations()))
```

Прямые вызовы SDK не добавляют проектный rate guard и не делают безопасный
retry. Соблюдение лимитов API остаётся обязанностью приложения. Guarded live
проверки этого репозитория запускаются только по инструкции ниже.

## Конвейер генерации

Четыре реализованные основные команды:

```bash
# Сетевое сравнение свежего upstream с tracked snapshot; tracked files не меняются.
uv run --frozen python -m tools.openapi_pipeline upstream-check

# Сетевая подготовка bootstrap-кандидатов под build/; tracked files не меняются.
uv run --frozen python -m tools.openapi_pipeline bootstrap

# Атомарная регенерация из уже зафиксированного snapshot, без сети.
uv run --frozen --offline python -m tools.openapi_pipeline sync --offline

# Полная offline-проверка воспроизводимости generated tree и wheel.
uv run --frozen --offline python -m tools.openapi_pipeline verify
```

Перед обновлением upstream, live-read или сбором evidence прочитайте
[инструкцию по генерации](docs/generation.md). Текущие исправления upstream и
условия их удаления перечислены в
[реестре известных проблем](docs/known-upstream-issues.md). Проверенные обходы
ошибок находятся в [troubleshooting ledger](docs/troubleshooting.md).

## Граница live и секретов

Обычные tests, `sync --offline` и `verify` не выполняют live HTTP-запросов.
Профили, `.env`, captures, receipts и state являются локальными данными и не
должны попадать в Git. Любой `429` прекращает весь live-run без retry и без
переключения на второй API login.

