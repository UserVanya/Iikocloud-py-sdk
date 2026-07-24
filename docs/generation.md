# Генерация и проверка SDK

Эта инструкция описывает текущий операторский pipeline: обновление OpenAPI
snapshot, review overlays, воспроизводимую генерацию SDK, строго ограниченные
live checks, проверку секретов и allowlisted Git-публикацию.

## Короткий сценарий: iiko изменила API

Это основной рабочий маршрут. Подробные правила и аварийные процедуры
приведены в следующих разделах.

### 1. Создать отдельную ветку и получить diff

```bash
git switch -c chore/iiko-openapi-YYYY-MM-DD
uv sync --frozen --group dev
uv run --frozen python -m tools.openapi_pipeline upstream-check
```

Откройте `build/reports/upstream-diff.md`. Команда только скачивает публичную
схему и показывает добавленные, удалённые и изменённые операции и модели. Она
не меняет tracked snapshot и generated SDK. Scheduled GitHub workflow делает
эту проверку автоматически и сигнализирует ненулевым статусом при drift.

### 2. Решить, нужна ли correction

| Изменение upstream | Действие |
|---|---|
| Добавлен корректно описанный метод или model | Дополнительная correction обычно не нужна |
| У операции плохое или нестабильное имя | Добавить reviewed mapping в `openapi/operation-ids.yaml` |
| Имя model конфликтует или не принимается генератором | Добавить mapping в `openapi/model-name-overrides.yaml` |
| Ошибочны `type`, `required`, nullable, `oneOf` или discriminator | Добавить guarded action в `openapi/overlays/` и focused contract test |
| iiko исправила дефект, который уже закрывал overlay | Удалить только ставшую ненужной correction и обновить её test |

Для подсказок по новым именам, конфликтам и mechanical types можно выполнить:

```bash
uv run --frozen python -m tools.openapi_pipeline bootstrap
```

Результаты появятся под ignored `build/bootstrap/` и требуют review. Никогда
не исправляйте `src/iikocloud_client` или raw upstream snapshot вручную. Если
guard стал stale, сначала заново проверьте upstream fragment; не заменяйте его
SHA-256 вслепую.

### 3. Подготовить версию и сгенерировать SDK

Если изменение будет новым release, задайте его версию в `pyproject.toml` до
generation и live-check, затем обновите lock:

```bash
uv lock --offline --no-config
```

После review примите свежий upstream и атомарно соберите SDK:

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen python -m tools.openapi_pipeline sync
```

`sync` применяет corrections, запускает закреплённый генератор, проверяет
contracts, imports и wheel и только после полного успеха заменяет snapshot,
manifest и generated package. При ошибке старое tracked состояние остаётся
целым.

### 4. Проверить результат офлайн

После первого `uv sync` для нового `UV_CACHE_DIR` один раз заполните resolver
metadata для точного runtime closure. Это setup-шаг с доступом только к package
index; он сверяет результат с `uv.lock`, не вызывает iiko и не входит в саму
offline-проверку:

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen --no-sync python -m tools.openapi_pipeline \
  prime-package-check-cache
```

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen --offline python -m tools.openapi_pipeline verify

PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen --offline python -m tools.openapi_pipeline verify-no-secrets
```

Полный pytest запускается через fresh-process split из
`.github/workflows/python.yml`; не заменяйте его монолитным `pytest -q`.

### 5. Выполнить один контролируемый live-read

Минимальный release checkpoint после generation:

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen --offline pytest -m live_read_smoke -n0 \
  --live-profile test-server --env-file .env \
  tests/integration/read/test_organizations.py
```

Затронутую операцию проверяйте дополнительно только через guarded entrypoint и
только если её rate limit имеет `verified: true`. Не повторяйте discovery,
если сохранённые targets всё ещё актуальны. При несовпадении реального JSON со
схемой выполните один разрешённый capture, затем создайте и отдельно
просмотрите synthetic candidate через `promote-evidence`.

Любой `429` немедленно завершает весь live-run: без retry, продолжения других
операций и переключения на `IIKO_API_KEY_2`.

### 6. Опубликовать проверенный release

Оставьте release diff unstaged: `publish` требует пустой Git index и сам
создаёт commit и tag. После отдельного явного решения на публикацию выполните:

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen --offline python -m tools.openapi_pipeline publish \
  --version X.Y.Z --push
```

Замените `X.Y.Z` на версию, заранее записанную в `pyproject.toml`.

Команда повторно проверит version, generated artifacts, live receipt, circuit,
mutation journals, secrets и wheel; затем создаст один allowlisted commit, tag
`vX.Y.Z` и выполнит non-force push. Без явного `--push` внешний Git не
изменяется.

Если обновление потребовало менять сам pipeline, CI или неразрешённые publish
пути, оформите эти изменения отдельным обычным reviewed commit до release.

## Что является источником истины

- `openapi/upstream/iikocloud.openapi.json` — точная tracked-копия upstream;
  её не исправляют вручную.
- `openapi/operation-ids.yaml` и `openapi/model-name-overrides.yaml` —
  hand-reviewed публичные имена операций и моделей.
- `openapi/overlays/*.overlay.yaml` — механические и семантические исправления
  raw snapshot. Каждое действие привязано к числу совпадений и SHA-256
  исходного фрагмента.
- `tests/fixtures/contracts/` — только минимальные синтетические contract
  fixtures. Это не копии live payloads.
- `generator/toolchain.lock` — точный Docker image и digest OpenAPI Generator.
- `generator/generated-manifest.json` — хэши generated tree до добавления
  разрешённых manual files.
- `src/iikocloud_client/_contracts/` — hand-owned файлы, которые generation
  обязана сохранить.

Generated package под `src/iikocloud_client` не является местом для ручных
fixes. Исправление должно появиться в snapshot-composition слое, registry,
generator config или тестируемом pipeline-коде.

## Предварительные условия

Публикуемая библиотека поддерживает Python 3.10+, но для выполнения этого
операторского pipeline нужен Python 3.12. Также нужны `uv`, Git и запущенный
Docker Engine с локально доступным image из `generator/toolchain.lock`.
Генератор запускается по digest, с отключённой сетью контейнера.

```bash
uv sync --frozen --group dev
```

Перед любой работой с pipeline или live сначала прочитайте
[troubleshooting ledger](troubleshooting.md). Повторяющийся workaround можно
добавлять туда только после воспроизведения причины и проверки решения; вывод
с секретами или private payloads в ledger не переносится.

## Основные команды

### Проверить свежий upstream

```bash
uv run --frozen python -m tools.openapi_pipeline upstream-check
```

Команда делает сетевое получение публичного OpenAPI, сохраняет кандидата и
отчёт под ignored `build/`, но не меняет tracked snapshot или generated SDK.
Проверьте как минимум `build/reports/upstream-diff.md` и raw candidate перед
любой попыткой принять обновление.

Показанная ручная команда работает в report-only режиме: даже при drift она
сначала записывает оба `build/reports/upstream-diff.*` отчёта и завершается с
кодом 0. Scheduled workflow запускает только эту же команду с отдельным
`--fail-on-drift`: при drift отчёты уже записаны, после чего job получает
ненулевой сигнал; при неизменном inventory код остаётся 0. Artifact upload в
workflow выполняется с `if: always()`, поэтому отчёты сохраняются в обоих
случаях. Флаг `--fail-on-drift` существует только у `upstream-check`.

`upstream-check` не принимает snapshot и не перегенерирует SDK. `sync`,
напротив, собирает и продвигает reviewed tracked состояние; сетевую форму
`sync` нельзя использовать вместо review отчёта `upstream-check`.

### Подготовить bootstrap-кандидаты

```bash
uv run --frozen python -m tools.openapi_pipeline bootstrap
```

Команда получает upstream и создаёт reviewable candidates в
`build/bootstrap/`: mechanical types overlay, operation IDs и model collision
report. Tracked files не продвигаются.

`bootstrap --accept-current-upstream` предназначен только для первоначального
baseline с пустыми registry. В уже инициализированном репозитории новые
reviewed записи переносятся в tracked registries/overlays, после чего
используется `sync`; флаг initial acceptance не является обычной командой
обновления.

### Регенерировать атомарно

Без сети, из текущего tracked snapshot:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline sync --offline
```

После review нового публичного кандидата `sync` без `--offline` может получить
upstream заново:

```bash
uv run --frozen python -m tools.openapi_pipeline sync
```

Обе формы сначала собирают effective schema, выполняют strict lint и pinned
generator validation, генерируют во staging, проверяют imports, contracts и
wheel. Snapshot, manifest и generated package продвигаются одной транзакцией
только после успешных проверок.

### Проверить воспроизводимость

Для совершенно нового uv cache сначала выполните описанный выше
`prime-package-check-cache` после `uv sync`.

```bash
uv run --frozen --offline python -m tools.openapi_pipeline verify
```

`verify` заново строит effective schema и package, сверяет manifest, manual
contracts и wheel из корня проекта. Команда offline и не выполняет live API
calls. Для ad-hoc импортов generated package используйте
`PYTHONDONTWRITEBYTECODE=1`, иначе `__pycache__` внутри manifest-controlled
дерева будет корректно считаться незаявленным изменением; восстановить чистое
дерево можно повторным атомарным `sync --offline`.

Известный длинный прогон recursive evidence/schema tests может исчерпать native
stack CPython и завершиться с code 139. Не считайте повторный монолитный
`pytest -q` достаточной проверкой: используйте fresh-process split из строки
troubleshooting ledger от 2026-07-20 про native stack exhaustion. Каждый
указанный там test group запускается отдельным процессом; это offline
workaround и он не разрешает live markers. Точный executable partition также
зафиксирован в `.github/workflows/python.yml`.

## Как исправлять дефекты upstream

1. Не меняйте raw snapshot и generated Python.
2. Зафиксируйте точный ошибочный JSON fragment и ожидаемый контракт тестом.
3. Для operation name добавьте стабильное доменное имя в
   `openapi/operation-ids.yaml`. Для model collision или generator-invalid CLR
   generic key добавьте явное имя в `openapi/model-name-overrides.yaml`.
   Numeric suffix допустим только если число действительно относится к домену.
4. Псевдотипы вроде `bool`, `uuid` и `integer <int64>` нормализуются
   mechanical types overlay. Семантическая ошибка описывается Overlay 1.1
   action с точным JSONPath, `expected-matches` и digest исходного значения.
5. Не обновляйте guard hash вслепую. Его drift означает, что upstream fragment
   изменился и исправление нужно заново проверить. Digest должен вычисляться
   тем же canonical JSON helper, который использует pipeline.
6. Для наблюдаемого response-контракта добавьте минимальную синтетическую
   fixture и generated contract test. Live payload не копируется в tracked
   файл.
7. Запустите `sync --offline`, затем `verify` и просмотрите Git diff.

Применение overlays и physical normalization имён fail closed: отсутствующий
target, изменившийся fragment, collision, небезопасная ссылка или оставшийся
invalid schema key останавливает generation.

Текущие semantic actions и условия их удаления описаны в
[known-upstream-issues.md](known-upstream-issues.md).

## Guarded read-only live checks

Live-запуск разрешён только через project commands/pytest fixtures и только
для operation, у которой `verified: true` в `contracts/rate-limits.yaml`.
Обычный pytest и CI исключают live markers.

Создайте закрытый профиль из публичного шаблона:

```bash
install -d -m 0700 private/profiles
cp config/live-profile.example.toml private/profiles/test-server.toml
chmod 0600 private/profiles/test-server.toml .env
test "$(stat -c '%a:%u' .env)" = "600:$(id -u)"
test "$(stat -c '%a:%u' private/profiles/test-server.toml)" = "600:$(id -u)"
```

В profile остаются только имена environment variables и разрешённые target
settings. Значения API login и IDs находятся в process environment или в
явно переданном `.env`; их нельзя печатать, копировать в docs или коммитить.
Полные правила находятся в `private/README.md`.

`.env` структурирован по окружениям (шаблон — `.env.example`): SHARED
(приложение портала разработчика `IIKO_APP_ID`/`IIKO_CLIENT_SECRET`), READ
(`IIKO_API_KEY` + `IIKO_TEST_*` для профиля amato) и WRITE (`IIKO_WRITE_*`
для профиля write-server). Переменные без provisioned значений держатся
закомментированными заглушками с пояснением — profile loader fail-closed
требует непустое значение только когда оно реально нужно выбранному режиму
(`allow_write`).

### Версия live-авторизации (v1 → v2)

iiko переводит Cloud API на новую схему авторизации: старый
`POST /api/1/access_token` (тело `{apiLogin}`) отключается, замена —
`POST /api/v2/access_token` (тело `{appId, clientSecret, apiKey}`, ответ в той
же форме `{correlationId, token}`). По официальному FAQ меняется только способ
получения токена; остальные endpoints не затронуты.

Профиль выбирает контракт явно через `auth_version` (default `"v1"`). Для
перехода на v2:

1. Зарегистрируйте приложение на https://public-api.iikoweb.ru/portal и
   получите `appId` и одноразовый `clientSecret` (новый API key в iikoWeb
   получать не нужно — используется текущий `IIKO_API_KEY` как `apiKey`).
2. Добавьте значения в `.env` (например, `IIKO_APP_ID` и
   `IIKO_CLIENT_SECRET`) и поля `auth_version = "v2"`, `app_id_env`,
   `client_secret_env` в private profile (см.
   `config/live-profile.example.toml`).
3. Выполните один guarded live-прогон для проверки нового auth-контракта.

`SafeLiveSession` выбирает auth-операцию по `auth_version` профиля; обе
операции (`authenticate`, `authenticate_v2`) имеют reviewed automatic policy и
verified 30-секундный бюджет. Guarded capture/evidence/discovery/cleanup
flows пока остаются привязанными к v1-контракту и требуют отдельного review
перед миграцией.

Проверено live 2026-07-23 (профиль amato, guarded smoke и selected runs):
v2-токен принимается всеми проверенными read-endpoints, а ранее падавшие с
HTTP 403 операции `PublicApiInvoiceProcessing` под v2-токеном зарегистрированного
приложения возвращают 200 (исключение — `get_inventory_counteragents`, у
которого backend отвечает `EXTERNAL_SYSTEM_TIMEOUT`; case остаётся
`no_live_target/endpoint_unavailable`). Поэтому
`disabled_read_capabilities = ["public_api_invoice_processing"]` для этого
окружения больше не нужен под v2.

Read и write окружения разведены по отдельным API keys одного зарегистрированного
приложения: read использует `IIKO_API_KEY`, выделенный write-стенд —
`IIKO_WRITE_API_KEY` (см. `REVIEWED_API_LOGIN_ENVS`). Целевые IDs write-стенда
(organization, terminal group, write product, external menu) получают через
`discover-read-targets` с write-профилем (`allow_write = false` на время
discovery) и затем фиксируют в его private profile с `allow_write = true`.

Если для конкретного environment подтверждено отсутствие entitlement
`PublicApiInvoiceProcessing`, добавьте в его private profile:

```toml
disabled_read_capabilities = ["public_api_invoice_processing"]
```

Тогда все 6 finance и 22 inventory cases остаются в полном плане со своими
настоящими builders и bindings, но получают
`no_live_target/invoice_processing_unavailable` до создания context view,
request model, получения rate budget и HTTP-вызова. Без поля (или с пустым
массивом) эти cases выполняются как обычно. Это декларация entitlement именно
выбранного environment, а не перехват любого HTTP 403, retry-механизм или
разрешение переключить API login.

Live entrypoints принимают только точный корневой `--env-file .env` и не
подхватывают файл неявно. Process environment имеет приоритет над этим файлом.
`api_login_env` профиля обязан входить в reviewed-набор
`REVIEWED_API_LOGIN_ENVS` (`IIKO_API_KEY` — read-контур, `IIKO_WRITE_API_KEY` —
выделенное write-окружение); `IIKO_API_KEY_2` в набор не входит, наличие
альтернативного ключа не включает fallback. Перед каждым запуском заново
проверьте, что `.env` и private profile принадлежат текущему пользователю и
имеют mode `0600`.

Получить guarded список доступных организаций, terminal groups и external
menus с именами:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline discover-read-targets \
  --live-profile test-server --env-file .env
```

Проверить один target organization через generated SDK:

```bash
uv run --frozen --offline pytest -m live_read_smoke -n0 \
  --live-profile test-server --env-file .env \
  tests/integration/read/test_organizations.py
```

Эти entrypoints создают process lock, используют persistent rate state,
аутентифицируются один раз и не делают retry HTTP-вызова. Один live process
может выполнить не больше одного вызова конкретной operation за run.

### Полный guarded live-read

Полную проверку всех reviewed read cases запускайте только этой командой из
корня repository:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_full -n0 \
  --live-profile amato --env-file .env \
  tests/integration/read/test_all_reads.py
```

Каждая часть команды является частью safety contract:

- `PYTHONDONTWRITEBYTECODE=1` запрещает создавать `__pycache__` в
  manifest-controlled generated tree;
- `uv run` использует project environment, `--frozen` запрещает менять
  `uv.lock`, а `--offline` запрещает `uv` обращаться к package indexes;
- `uv --offline` **не отключает HTTP к iiko**: выбранный pytest entrypoint
  остаётся live-командой и выполняет guarded iiko requests;
- `pytest` запускает live harness, `-m live_read_full` выбирает только точный
  full marker, а `-n0` запрещает параллельных pytest workers;
- `--live-profile amato` выбирает закрытый профиль `amato`, а
  `--env-file .env` разрешает только явно указанный корневой `.env`;
- `tests/integration/read/test_all_reads.py` ограничивает collection точным
  full-runner файлом.

План содержит 91 read case и одну authentication, то есть до 92 HTTP requests.
Если каждый case доходит до HTTP, 91 межзапросный интервал по 30 секунд задаёт
минимум 45 минут 30 секунд только на cadence. Текущий tracked rate contract
задаёт ровно 30 секунд для каждой guarded operation: authentication, всех reads
и обеих write operations; operation-specific server-limit multiplier сейчас
отсутствует. Persistent rate state переживает процессы и сохраняет оставшуюся
часть того же 30-секундного интервала. Никогда не удаляйте и не обходите state,
не заменяйте guard ручным `sleep` и не меняйте API login. Если обязательного
target нет, case получает `no_live_target` до получения rate budget и до HTTP,
поэтому реальный run может быть короче.

### Выборочный read с capture

Для одного явно выбранного capture используйте точную selected-команду:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_selected -n0 \
  --live-profile amato --env-file .env \
  --capture-http --capture-operation get_nomenclature \
  tests/integration/read/test_selected_read.py
```

`PYTHONDONTWRITEBYTECODE`, `uv run --frozen --offline`, `pytest`, `-n0`,
`--live-profile` и `--env-file` имеют те же значения и ограничения, что в
полной команде. `-m live_read_selected` выбирает только selected marker;
`--capture-http` включает sanitized capture, а
`--capture-operation get_nomenclature` одновременно задаёт единственную
capture operation. Последний аргумент ограничивает collection точным
`test_selected_read.py`.

Selected runner выполняет canary и dependency closure выбранной operation, но
capture записывает только `get_nomenclature`. Authentication никогда не
попадает в capture. Sanitized файлы сохраняются с закрытыми permissions только
под ignored `private/captures/`, остаются private и не добавляются в Git.
Capture options нельзя передавать full runner; full и selected режимы нельзя
объединять в одном запуске.

### Как читать результат full/selected run

- `passed` — operation вернула успешный HTTP response, а validation,
  extraction и обновление безопасного context завершились успешно;
- `no_live_target` — разрешённый target или context отсутствует; rate budget
  не расходуется, HTTP не отправляется, и runner продолжает план;
- `failed` — полученный response не прошёл assertion или extraction; итоговый
  run неуспешен, зависимые cases получают `aborted`, но независимые cases
  продолжаются;
- `aborted` — case остановлен из-за failed dependency или safety/transport/
  HTTP/rate/cancellation/report failure. Ошибка, создающая глобальный abort,
  прекращает новые HTTP-вызовы, а все оставшиеся cases записываются как
  `aborted`.

Успешный итог требует хотя бы одного `passed` и отсутствия `failed` и
`aborted`; одни только `no_live_target` успехом не считаются.

Для подтверждённого upstream schema defect не сохраняйте private response или
capture в Git. Добавьте минимальную публичную synthetic fixture, внесите
исправление в соответствующий слой: `openapi/overlays/` для schema contract,
`openapi/operation-ids.yaml` для operation name или
`openapi/model-name-overrides.yaml` для model name. Затем перегенерируйте SDK,
повторите все offline gates и только после их успеха планируйте новый guarded
live call. Подробный fail-closed порядок приведён в разделе
[«Как исправлять дефекты upstream»](#как-исправлять-дефекты-upstream).

**429 rule:** stop the entire run; no retry; no second key; investigate and
manually reset later. Второй ключ включает `IIKO_API_KEY_2`: не продолжайте
следующую operation, не удаляйте state и не пытайтесь обойти circuit. Сначала
расследуйте причину; более поздний ручной reset требует отдельного решения, а
зарезервированное CLI-имя `reset-circuit` сейчас не реализовано.

### Как подтвердить rate limit

Сейчас у всех production entries `server_limit: null`, а единый подтверждённый
test budget задаёт ровно 30 секунд. Реализация сохраняет поддержку будущего
явного server limit. Не подтверждайте такой limit экспериментом с учащением
запросов: сначала проверьте его по авторитетному источнику или отдельно
согласованному наблюдению, сохраните безопасное описание в поле `source` и
оставьте test budget не выше 20% server limit при глобальном минимуме 30 секунд.
Затем:

1. добавьте или обновите offline tests каталога и убедитесь, что неизвестная
   operation и неподтверждённый budget продолжают fail closed;
2. выделите эксклюзивное окно для одного API login и получите отдельное явное
   разрешение на один контролируемый live checkpoint;
3. выполните только один guarded serial run без параллелизма и retry;
4. меняйте `verified` на `true` только после проверки источника, budget и
   результата без `429`, в отдельном reviewable diff.

Локальный state не координирует тот же login на другой машине или в другом
приложении. Пока эксклюзивность и реальный limit не подтверждены, operation
остаётся `verified: false` и live command должна остановиться до HTTP.

## JSON evidence для external menu

Каждая версия запрашивается отдельной командой. Не объединяйте команды в loop
и не запускайте их параллельно:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 2

uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 3

uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 4
```

Текущий tracked rate catalog задаёт этой operation тот же точный интервал 30
секунд, что и всем остальным guarded operations. Guard хранит время последнего
вызова между процессами; оператор не должен заменять его ручным `sleep` или
повторным API login. Если в будущем появится явный `server_limit`, guard по-
прежнему сможет применить его математику поверх глобального минимума.

Capture writer сохраняет sanitized request/response JSON только под ignored
`private/captures/` с закрытыми permissions. Даже sanitized capture остаётся
private и не переносится в Git.

Построить detached review candidate без изменения tracked files:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline promote-evidence \
  --operation get_external_menu_by_id
```

Проверьте `build/evidence-candidates/candidate-manifest.json`, две overlay
кандидатуры и три минимальные fixtures. После отдельного human review принять
ровно этот заново проверенный candidate:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline promote-evidence \
  --operation get_external_menu_by_id --accept
```

Acceptance повторно проверяет provenance, schema fragments, V2/V3/V4,
discriminator consistency, наличие combo evidence и отсутствие известных
secret/PII patterns. В tracked tree попадают только две overlays и три
synthetic fixtures.

## Что делать при 429

`429` немедленно открывает persistent circuit и прекращает весь live-run.
Запрещено:

- повторять запрос;
- продолжать следующую operation;
- автоматически или вручную переключаться на `IIKO_API_KEY_2`;
- удалять state ради обхода circuit.

Сначала расследуйте причину и сохраните circuit закрытым для новых запусков до
явного ручного решения. CLI-имя `reset-circuit` пока зарезервировано, но его
реализация не завершена; эта инструкция намеренно не предлагает фиктивную
команду сброса.

## Write-сценарии (жизненные циклы записи)

Записи выполняются только внутри проверенных сценариев из реестра
`contracts/write-lifecycles.yaml`. Сценарий — это цепочка «подготовка
(чтение) → создание → проверка (чтение) → откат», привязанная к метке
владения: адаптер (`execute_write`) отклоняет любой запрос вне границ
write-профиля (организация из allowlist, разрешённые таргеты) и с чужим
значением метки, поэтому тест физически не может изменить чужие данные.
Журнал отката регистрирует компенсацию до мутации; незавершённый журнал
блокирует «успех» до разбора (`cleanup-orphans`).

Каждый live-write тест помечен `@pytest.mark.write_scenario("<id>")`; на
collection гейт проверяет, что сценарий существует и включён, а поля профиля
из `requires_profile_fields` заполнены. Состояние сценариев:

| Сценарий | Состояние | Проверка |
|---|---|---|
| `stop_list_product` | enabled | live round-trip 2026-07-24 (write-server): add→remove стоп-листа, receipt completed, журнал чист |
| `customer` | disabled | Бэкенд лояльности не provisioned для write-стенда: `get_customer_info` → `Common_OrganizationNotFound` (проба 2026-07-24) |
| `delivery_draft` | disabled | На стенде нет внешнего меню, а `DeliveryOrderDraft` требует `menuId` |

Безопасно проверить только collection-контракт:

```bash
uv run --frozen --offline pytest -m live_write -n0 \
  tests/integration/write --collect-only -q
```

Реальный запуск требует одновременно: включённый сценарий в реестре,
`--allow-live-write`, `--allow-audit-residue` (если тест помечен
`audit_residue`), точный `--target-organization`, write-enabled private
profile с allowlist, поля из `requires_profile_fields`, `-n0` и отдельную
явную авторизацию именно этого запуска. Rate budgets всех операций сценария
проверяются до authentication; это подтверждает только cadence и не
разрешает live write само по себе.

### Как добавить новый write-сценарий

1. Добавить сценарий в `contracts/write-lifecycles.yaml` (`enabled: false` +
   причина, пока не проверен live).
2. Добавить операции в `contracts/live-operations.yaml` (create-шаги —
   `kind: compensating` со ссылкой `cleanup`, шаги отката — `kind: cleanup`)
   и в `contracts/rate-limits.yaml` (30 секунд; скопировать в
   `src/iikocloud_client/_contracts/rate-limits.yaml`).
3. Добавить executor в `_WRITE_EXECUTORS` (`live/generated.py`): модель
   запроса, сгенерированный метод, валидатор границ профиля и метки владения.
4. Написать offline-тесты (загрузчик, валидаторы, адаптер, гейты), затем
   тест сценария в `tests/integration/write/` с маркерами `live_write`,
   `write_scenario` и при необходимости `audit_residue`.
5. После отдельной авторизации выполнить один live-прогон; только после
   успешного — перевести сценарий в `enabled: true`.

Запрещённый шаблон: любой запуск без перечисленных write gates останавливается
до HTTP; «временно» убрать гейты или изменить чужой таргет нельзя.

### Точная команда write-прогона

Исполнять только после отдельной явной авторизации именно этого запуска и при
включённом сценарии; это не команда для проверки документации.

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -m live_write -n0 \
  tests/integration/write/test_stop_list.py::test_stop_list_add_is_accepted_and_removed \
  --live-profile write-server \
  --env-file .env \
  --target-organization "${IIKO_WRITE_ORGANIZATION_ID:?required}" \
  --allow-live-write \
  --allow-audit-residue
```

До `add` test атомарно сохраняет cleanup payload в ignored
`.state/mutations/<run-id>.json` с mode `0600`. Cleanup выполняется LIFO в
`finally`; незавершённый журнал сохраняется и блокирует успешный live receipt.
Для ручного восстановления существует только интерактивная команда:

```bash
uv run --frozen python -m tools.openapi_pipeline cleanup-orphans \
  --live-profile test-server --env-file .env
```

Она до authentication проверяет каждый journal, каждый cleanup budget,
generated-схему payload и точное совпадение organization, terminal group и
единственного dedicated product с выбранным write-профилем. Команда не
показывает payload/UUID, выводит только fingerprints и operation IDs, затем
требует точное подтверждение `cleanup N actions [y/N]`. Не повторяйте команду
после `429`, не переключайте API login и не удаляйте journal вручную. При
текущих unverified stop-list limits команда также корректно завершится до HTTP.

## Проверка секретов

Перед review, commit или публикацией запустите обычный read-only режим:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets
```

Команда сама получает NUL-delimited списки tracked и staged файлов, проверяет
worktree и точные stage-0 blobs через audited `.secrets.baseline`, а затем ищет
точные непустые значения активных `IIKO_API_KEY` и `IIKO_API_KEY_2`. Detector
получает временную копию baseline, поэтому обычная проверка не может изменить
аудированный файл. Два значения загружаются только из process environment и,
если ключ отсутствует там, из корневого `.env` без вывода значения в
диагностику. Отсутствующий ключ просто пропускается.

Нормальная проверка никогда не изменяет baseline. Для его первоначального
создания используйте отдельный bootstrap-режим, затем вручную проаудируйте
каждую находку и снова запустите обычную проверку:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets --create-baseline
uv run --frozen --offline detect-secrets audit .secrets.baseline
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets
```

Bootstrap получает tracked filenames самостоятельно, запускает
`detect-secrets scan --no-verify` без shell и атомарно создаёт новый baseline
только после успешной команды и разбора JSON. Он не предназначен для
перезаписи существующего baseline. В audit помечайте false positive только
после проверки; настоящую учётную запись нужно удалить из Git и ротировать, а
не добавлять в исключения. Не копируйте audit output в issue, логи или docs.

Если scanner нашёл настоящий API login, остановите commit/publish и не
печатайте совпадение. Отзовите и замените login в iiko, удалите его из
worktree и index (а если он уже опубликован — отдельно согласуйте очистку Git
history), затем обновите локальный `.env` с mode `0600`. После ротации заново
запустите обычный `verify-no-secrets` и убедитесь, что audited baseline не
изменился. Настоящий secret никогда не помечается false positive и не
добавляется в baseline.

`.env`, `.env.local`, captures, receipts, rate state, mutation journals и
прочие runtime-файлы под `private/`, `.state/` и `build/` никогда не должны
быть tracked или staged. Из `private/` допустимы только hand-owned
`private/.gitignore` и `private/README.md`; secret scan fail closed на остальных
private paths.

## Allowlisted публикация

`publish` — mutating operator command, а не способ проверить реализацию. Не
запускайте её в текущем checkout как часть тестов: publish-тесты используют
только временный Git repository. Release version должна быть подготовлена до
generation и live receipt, потому что она встроена в generated runtime и его
hash. Последовательность для новой версии:

1. Измените точную строку `[project] version = "..."` в `pyproject.toml`.
2. Выполните `uv lock --offline --no-config`, затем `sync --offline`.
3. Проведите guarded live-read для получившегося generated tree.
4. Оставьте release diff unstaged: `publish` требует пустой Git index.
5. Передайте ту же уже подготовленную версию в `publish`.

Без `--push` команда создаёт commit и annotated tag, но не меняет release
version после live receipt:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline publish --version 0.1.0
```

`--version` обязателен и должен совпадать с `pyproject.toml`, generated
`__version__`, User-Agent/debug report и `uv.lock`. Для отдельной, явно
подтверждённой публикации commit и tag в `origin` добавьте `--push`:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline publish --version 0.1.0 --push
```

На `main` и `master` команда по умолчанию запрещена. Единственный локальный
opt-in — ignored файл `private/publish.toml` с точным
`allow_protected_branch = true`; CLI-флага для обхода этого gate нет.

До изменения Git publish требует одновременно:

- только dirty paths из `openapi/`, `contracts/`, `generator/`,
  `src/iikocloud_client/`, `tests/fixtures/contracts/`, `tests/generated/` или
  точные файлы `docs/generation.md`, `docs/known-upstream-issues.md`,
  `README.md`, `pyproject.toml`, `uv.lock`, при полностью пустом Git index;
- совпадение requested, project и generated runtime version, актуальный
  `uv.lock`, успешный полный `verify` и completed live receipt, совпадающий с
  текущими artifact hashes;
- закрытый persistent circuit для profile fingerprint из receipt и полное
  отсутствие mutation journals;
- успешный secret scan до staging.

После gates команда повторяет wheel smoke, показывает sanitized dirty-path
list и `git diff --stat`, выполняет `git add --` только для разрешённых путей и
повторяет secret scan уже по точным staged blobs. Затем создаются ровно один commit
`chore(sdk): sync iiko OpenAPI YYYY-MM-DD` и annotated tag `v{version}`. С
`--push` выполняются только non-force push текущего `HEAD`, затем отдельный
non-force push тега.

Publish gates не разрешают live write. Записи stop-list операций `get`, `add`
и `remove` в `contracts/rate-limits.yaml` имеют подтверждённый 30-секундный
budget, но write-тесты можно только собирать: live-запуск по-прежнему требует
отдельной явной авторизации и всех write gates. CLI-имя `reset-circuit` также
остаётся зарезервированным и не должно использоваться как фиктивный способ
обойти открытый circuit.

## Проверка Git tag в downstream без изменения manager

Этот pipeline не изменяет `/home/ivan/programming/Iikocloud-manager`. После
того как tag действительно опубликован, его можно проверить из каталога
manager в изолированном окружении без изменения `pyproject.toml`, `uv.lock` и
рабочего дерева:

```bash
cd /home/ivan/programming/Iikocloud-manager
uv run --isolated --no-project \
  --with "iikocloud-client @ git+ssh://git@github.com/UserVanya/Iikocloud-py-sdk.git@v0.1.0" \
  python -c "from iikocloud_client import ApiClient, Configuration; print(ApiClient.__name__, Configuration.__name__)"
```

Замените `v0.1.0` на созданный release tag. Постоянное закрепление зависимости
в manager выполняется отдельным migration change после этой проверки; не
подменяйте tag веткой.

## Как пополнять troubleshooting ledger

Запись добавляется только когда один и тот же детерминированный failure pattern
повторился, root cause установлена, а workaround проверен. В той же change set
добавьте одну строку в `docs/troubleshooting.md`: дата, sanitized context,
симптом, причина, безопасный workaround, профилактика и способ проверки. Не
записывайте предположения, `.env` values, login/token, private payload,
capture, receipt или mutation journal. Если причина или решение ещё не
подтверждены, ledger не меняется.
