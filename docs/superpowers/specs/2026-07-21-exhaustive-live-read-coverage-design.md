# Исчерпывающий guarded live-read контур iiko Cloud SDK

Дата: 2026-07-21
Статус: утверждённый дизайн, ожидающий реализации

## 1. Результат

Репозиторий должен явно классифицировать каждую операцию итоговой OpenAPI-схемы
и иметь исполнимую read-проверку для каждого метода, который можно безопасно
вызвать на выбранном сервере. Полный live-read запускается только вручную,
последовательно и через существующие project safety gates. Между любыми двумя
HTTP-запросами, включая авторизацию, выдерживается не менее 30 секунд; известный
более строгий лимит операции имеет приоритет.

На первом этапе live выполняются только операции без изменения состояния.
Write-операции классифицируются, но не получают автоматического разрешения.
Связывающие их lifecycle-сценарии проектируются и реализуются следующим
отдельным этапом.

## 2. Исходное состояние

Текущий репозиторий уже содержит:

- строгий allowlist `contracts/live-operations.yaml`;
- каталог лимитов `contracts/rate-limits.yaml`;
- process lock, persistent rate state и circuit breaker;
- одну авторизацию на session и запрет retry;
- generated SDK adapter;
- private HTTP captures и live receipts;
- маркеры `live_read_smoke`, `live_read_full` и `live_write`;
- один generated-SDK smoke-тест организаций;
- отдельный opt-in stop-list write-тест с mutation journal.

Итоговая схема содержит 225 операций, но существующий live allowlist покрывает
только небольшую проверенную часть. Название метода или HTTP `POST` не позволяет
надёжно определить, изменяет ли операция данные. Поэтому полный набор нельзя
безопасно получить простой генерацией pytest-функций по путям OpenAPI.

## 3. Область текущего этапа

В этап входят:

1. Исчерпывающая семантическая классификация всех операций effective OpenAPI.
2. Строгая проверка соответствия классификации текущей схеме.
3. Реестр типизированных `ReadCase`, разбитый по областям API.
4. Разрешение зависимостей между read-операциями через process-memory context.
5. Один детерминированный полный live-read runner на базе существующих pytest
   fixtures.
6. Безопасный локальный JSON-отчёт без payloads и идентификаторов.
7. Явно включаемый sanitized capture одной выбранной операции.
8. Offline-тесты каталогов, планировщика, runner и safety invariants.
9. Один полный контролируемый live-read на профиле Amato после прохождения всех
   offline gates.

В этап не входят:

- новые live-write вызовы;
- генерация или выполнение lifecycle-сценариев;
- создание тестовых заказов, клиентов или других сущностей;
- автоматический cleanup запросами;
- автоматическое определение write-связей из OpenAPI;
- retry, параллельный HTTP или переход на `IIKO_API_KEY_2`;
- commit, push или публикация результатов live-run;
- изменение существующего stop-list lifecycle-теста, кроме совместимости с
  новой классификацией.

## 4. Два разных смысла классификации

Семантический эффект операции и разрешение на её live-выполнение хранятся
раздельно.

Поле `effect` отвечает на вопрос, что делает операция:

- `auth` — получает access token;
- `read` — читает или рассчитывает данные без изменения состояния;
- `create` — создаёт сущность;
- `update` — изменяет существующее состояние;
- `delete` — удаляет или отменяет сущность;
- `action` — выполняет бизнес-команду;
- `irreversible` — имеет необратимый или неприемлемо опасный эффект;
- `unknown` — семантика ещё не рассмотрена.

Поле `live_policy` отвечает на вопрос, когда операция может выполняться:

- `automatic` — разрешена в соответствующем guarded live-run;
- `lifecycle_only` — допустима только внутри будущего явно выбранного сценария;
- `manual_only` — требует отдельного ручного процесса и подтверждения;
- `blocked` — live-вызов запрещён.

`compensating` и `cleanup` не являются семантическими эффектами. Это роли
операции в конкретном lifecycle-сценарии. Существующие значения `kind` в
`live-operations.yaml` пока сохраняются как роли исполнительного allowlist;
будущий lifecycle-дизайн нормализует их отдельно.

## 5. Исчерпывающий safety catalog

Новый `contracts/operation-safety.yaml` является human-reviewed индексом всех
operation ID итоговой схемы:

```yaml
version: 1
operations:
  get_external_menus:
    effect: read
    live_policy: automatic
    reason: non-mutating menu query

  create_delivery:
    effect: create
    live_policy: lifecycle_only
    reason: requires an owned test order and compensation

  close_delivery:
    effect: irreversible
    live_policy: manual_only
    reason: final business action is not safely reversible
```

Catalog не является разрешением на HTTP. Он не дублирует `method` и `path`:
они берутся из effective OpenAPI и сверяются с исполнительным allowlist.

Правила catalog:

- множество operation ID должно точно совпадать с effective OpenAPI;
- каждая операция встречается ровно один раз;
- неизвестные поля, дубликаты ключей и неизвестные enum запрещены;
- все token endpoints классифицируются как `auth`, включая
  `authenticate_v2`;
- единственная `auth`-операция с `automatic` на этом этапе — уже используемая
  `authenticate`; остальные auth-варианты остаются `blocked` до отдельной
  миграции session/profile contract;
- `unknown` всегда сочетается только с `blocked`;
- `create`, `update`, `delete`, `action` и `irreversible` не могут иметь
  `automatic`;
- `reason` обязателен и не должен содержать live identifiers или секреты;
- новая upstream-операция остаётся fail-closed до ручной классификации;
- удаление или перенос операции обнаруживается до генерации или live-run.

Классификация определяется семантикой, а не префиксом operation ID и не HTTP
verb. Например, `POST` с JSON-фильтром может быть `read`, а метод с `get` в
названии не получает разрешение без проверки контракта.

## 6. Четыре независимых live-разрешения

Операция может дойти до HTTP только при одновременном выполнении четырёх
условий:

```text
operation-safety: effect=read, live_policy=automatic
                         ↓
contracts/live-operations.yaml: точные method и path, kind=read
                         ↓
contracts/rate-limits.yaml: verified=true и допустимый budget
                         ↓
ReadCase registry: типизированный request и проверки ответа
                         ↓
                    HTTP разрешён
```

Ни один слой автоматически не расширяет следующий. В частности, добавление
`automatic read` в исчерпывающий catalog не добавляет операцию в allowlist и не
делает её rate limit подтверждённым.

`contracts/live-operations.yaml` остаётся минимальным исполнительным
allowlist. `contracts/rate-limits.yaml` должен содержать запись для каждой
allowlisted операции и не может разрешить отсутствующую в allowlist операцию.
Rate entry раздельно хранит обязательный verified test budget и необязательный
документированный server limit:

```yaml
get_nomenclature:
  test_budget:
    min_interval_seconds: 30
    source: user-approved-global-read-cadence-2026-07-21
    verified: true
  server_limit: null

get_external_menus:
  test_budget:
    min_interval_seconds: 30
    source: user-approved-global-read-cadence-2026-07-21
    verified: true
  server_limit:
    calls: 1
    per_seconds: 1800
    source: existing-manager-configuration
    verified: true
```

`test_budget.verified` означает reviewed разрешение на конкретную тестовую
частоту, а не утверждение о серверном лимите. `server_limit` присутствует
только при отдельном подтверждённом источнике. Effective interval равен
максимуму из global minimum, operation test budget и 20%-ного бюджета
документированного server limit.

Глобальные правила остаются следующими:

- utilization не выше 20% подтверждённого server limit, если он известен;
- глобальный минимум между любыми запросами — 30 секунд;
- test budget каждой исполнимой операции подтверждён и не меньше глобального
  минимума;
- максимум один вызов конкретной операции за run;
- более строгий operation-specific interval имеет приоритет;
- последний вызов и circuit сохраняются между процессами;
- неподтверждённый rate budget запрещает HTTP до отправки запроса.

Глобальные 30 секунд являются согласованным владельцем минимальным тестовым
интервалом, но не выдуманным server limit. `test_budget.verified: true`
фиксирует это явное решение. `server_limit.verified: true` выставляется только
после проверки отдельного авторитетного источника. Неизвестный server limit не
проверяется учащением запросов и остаётся `null`.

## 7. ReadCase registry

Read-логика хранится как Python registry, сгруппированный по API-доменам:

```text
tests/integration/read/cases/
  __init__.py
  organizations.py
  terminal_groups.py
  menus.py
  orders.py
  deliveries.py
  dictionaries.py
  ...
```

Один случай содержит только особенности конкретной операции:

```python
ReadCase(
    operation_id="get_external_menu_by_id",
    depends_on=("get_external_menus",),
    requires=("organization_id", "external_menu_id"),
    build_request=build_external_menu_request,
    invoke=invoke_external_menu,
    validate_response=validate_external_menu,
    extract=extract_external_menu_context,
)
```

Registry использует Python, а не исполняемые выражения из YAML, потому что
generated request models, вызовы API и безопасная проверка разных response
форм требуют типизированного кода.

Инварианты registry:

- один `ReadCase` соответствует ровно одной `automatic read` операции;
- operation ID не повторяются;
- указанный generated API method существует;
- request строится generated model, а endpoint без body использует отдельный
  неизменяемый `NoRequest` sentinel вместо произвольного словаря;
- зависимости ссылаются на существующие cases;
- граф зависимостей ацикличен;
- каждый extractor записывает только заранее объявленные context keys;
- request builder не читает `.env` напрямую;
- никакой case не выполняет retry или второй вызов той же операции.

## 8. Контекст и зависимости

Runner создаёт новый `ReadContext` только в памяти процесса. Начальные значения
берутся из уже проверенного private profile. Последующие значения извлекаются
из успешных read-ответов.

Приоритет источников:

1. Выбранная организация и уже заданные безопасные targets private profile.
2. Идентификаторы из успешных foundation reads.
3. Дополнительные read-ответы в той же session.
4. Явный `no_live_target`, если безопасного источника нет.

Контекст не сериализуется в tracked files, не переносится между запусками и не
печатает реальные значения. Request builder получает только объявленные ключи.

Планировщик выполняет topological sort. Внутри одного независимого слоя порядок
стабилен по operation ID. Если provider возвращает пустую коллекцию, зависимый
case получает `no_live_target` до rate guard и до HTTP. Если provider завершился
ошибкой проверки, его dependents получают `aborted` с безопасной причиной
`dependency_failed`, а независимые ветви могут продолжиться.

`no_live_target` разрешён только для заранее описанного типа отсутствующей
сущности. Исключение не должно содержать реальный UUID, имя клиента, содержимое
заказа или другие данные ответа.

На этом этапе runner не использует чужие существующие изменяемые объекты ради
увеличения покрытия. Методы, требующие созданную сущность, будут покрыты после
появления lifecycle-сценариев.

## 9. Что проверяет read-case

Каждый выполненный case проверяет полный путь generated SDK:

1. Generated request model принимает подготовленные значения.
2. Generated API method сериализует request.
3. Guarded adapter отправляет ровно один разрешённый запрос.
4. Сервер возвращает успешный HTTP status.
5. Generated SDK десериализует ответ в ожидаемую модель.
6. Минимальные domain assertions подтверждают связь ответа с запросом.
7. Extractor безопасно добавляет объявленные значения в `ReadContext`.

Full run выполняет один репрезентативный безопасный запрос на operation ID, а
не перебирает все допустимые payload-варианты одной операции. Например,
несколько веток полиморфного ответа одной операции закрепляются offline
fixtures и отдельными evidence-командами: общий лимит в один вызов операции за
run не ослабляется ради перебора `oneOf`.

Минимальные assertions проверяют форму и ключевые инварианты, но не делают
полный snapshot изменчивых бизнес-данных. Например, допустимо проверить наличие
выбранной организации или совпадение запрошенного ID; недопустимо коммитить
полный список заказов или меню.

Если live-ответ обнаруживает ошибку upstream-схемы, исправление проходит
существующий correction layer:

- operation ID override исправляет публичное имя;
- guarded overlay исправляет OpenAPI-контракт;
- model-name override исправляет подтверждённое имя модели;
- минимальный синтетический fixture закрепляет регрессию offline;
- приватный capture не копируется в Git.

Ветки `oneOf` не удаляются ради прохождения теста. Live failure используется как
доказательство для минимальной схемной коррекции, после которой SDK полностью
регенерируется.

## 10. Полный live-read runner

Полный прогон реализуется одним orchestration test
`tests/integration/read/test_all_reads.py` с маркером `live_read_full`. Cases
остаются отдельными объектами registry, но один coordinator обеспечивает
детерминированный порядок, единственную session и глобальное прекращение при
опасной ошибке.

Команда:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_full -n0 \
  --live-profile amato --env-file .env \
  tests/integration/read/test_all_reads.py
```

Значения команды:

- `PYTHONDONTWRITEBYTECODE=1` запрещает изменения generated tree через `.pyc`;
- `uv run --frozen --offline` использует lock без загрузки пакетов;
- `--offline` относится к dependency resolution `uv`, а не запрещает iiko HTTP;
- `-m live_read_full` выбирает только полный read-run;
- `-n0` явно запрещает параллельный pytest;
- `--live-profile` выбирает private profile без помещения его значений в Git;
- `--env-file .env` явно разрешает только корневой `.env`;
- точный test path исключает случайный выбор write-тестов.

Имя `amato` в команде является именем локального private profile, а не
организацией из tracked-конфигурации. Если существующий профиль называется
иначе, команда использует его фактическое безопасное имя; acceptance target при
этом остаётся сервером и организацией Amato.

Перед чтением `.env` и авторизацией runner проверяет:

- generated package загружен строго из текущего `src/`;
- catalogs синтаксически корректны и согласованы;
- все `automatic read` имеют allowlist, verified rate и `ReadCase`;
- граф зависимостей валиден;
- live marker, точный путь и `-n0` заданы явно;
- private directory, profile и `.env` имеют безопасные owner/mode;
- persistent circuit закрыт;
- другой live process не держит lock.

После preflight runner печатает только число потенциальных запросов,
минимальную оценку длительности и безопасные operation IDs. Затем:

1. Выполняет одну guarded авторизацию через `IIKO_API_KEY`.
2. Перед каждым следующим HTTP использует общий persistent rate guard.
3. Строит request только после разрешения dependencies.
4. Выполняет каждую operation максимум один раз.
5. Обновляет только process-memory context и private receipt/report.
6. Закрывает generated client и auth session даже при ошибке.

`IIKO_API_KEY_2` никогда не используется автоматически.

## 11. Ошибки и завершение

Статусы отдельных cases:

- `passed` — request, HTTP, deserialization и assertions успешны;
- `no_live_target` — case существует, но безопасного объекта нет; HTTP не было;
- `failed` — операция выявила несовместимость generated-контракта, assertion
  или extractor;
- `aborted` — case не выполнялся из-за failed dependency или общего останова.

Политика продолжения:

- assertion/extractor failure после уже успешно десериализованного `2xx`
  помечает case как `failed`; независимые read-ветви могут продолжиться;
- ошибка десериализации помечает текущий case как `failed`, делает generated
  adapter непригодным и переводит все следующие cases в `aborted`;
- неожиданный HTTP status, transport error, timeout, ошибка rate/state/receipt
  или нарушение safety invariant прекращает все следующие HTTP;
- `429` открывает persistent circuit и немедленно прекращает весь run;
- после `429` нет retry, cleanup, продолжения и смены API login;
- Ctrl-C и отмена coroutine делают session непригодной для продолжения;
- неполный или неуспешный run не создаёт completed receipt.

Full run успешен только если:

- был хотя бы один live-read;
- каждый доступный case имеет `passed`;
- каждый невыполнимый case имеет заранее допустимый `no_live_target`;
- нет `failed` и `aborted`;
- circuit закрыт;
- оба HTTP client закрыты;
- mutation journals отсутствуют;
- receipt успешно финализирована.

## 12. Отчёты и captures

Каждый full run создаёт закрытый JSON-отчёт под ignored private root, например:

```text
private/reports/live-read/<run-id>.json
```

Отчёт содержит:

- run ID и fingerprint профиля;
- hashes effective schema и generated artifacts;
- operation ID и один из безопасных статусов;
- нормализованный код причины `no_live_target`, `failed` или `aborted`;
- timestamps и итоговые counts.

Raw exception text в отчёт не переносится. Отчёт не содержит API login, access
token, request/response body, UUID targets, имена клиентов, состав заказов или
другие live-значения. Каталоги создаются с mode `0700`, файлы — `0600`; symlink
и неожиданный существующий файл отклоняются.

Полные request/response JSON по умолчанию не сохраняются. Явный режим требует
одновременно:

```bash
--capture-http --capture-operation <operation_id>
```

Один запуск захватывает только выбранную allowlisted read-операцию. Capture
проходит существующую sanitizer-защиту и сохраняется только в ignored
`private/captures/`. Auth body не записывается. Попытка включить capture без
точного operation ID, для write-операции или сразу для всего full run
отклоняется до HTTP.

## 13. Offline-проверки

Реализация следует test-driven подходу. До любого full live-run должны пройти:

1. Strict parsing safety catalog: размеры, UTF-8, duplicate keys, exact fields,
   enum и policy matrix.
2. Exact parity между effective OpenAPI и operation safety catalog.
3. Exact parity между `automatic read`, executable allowlist, verified rate
   entries и `ReadCase` registry.
4. Проверка generated API methods и request/response model imports.
5. Проверка DAG: стабильный порядок, отсутствующие dependencies и cycles.
6. Проверка, что `no_live_target` возникает до rate acquisition и HTTP.
7. Fake-clock тест глобального интервала между auth и любыми operations.
8. Fake-clock тест более строгого operation-specific persistent interval.
9. Проверка one-call-per-operation и запрета retry.
10. Fake-transport сценарии success, assertion failure, HTTP error, timeout и
    `429` circuit break.
11. Проверка отчётов и captures на redaction, permissions, path traversal,
    symlink и atomic writes.
12. Проверка, что обычный `pytest` и CI не выбирают live markers.
13. Collect-only проверка, что full runner не включает `live_write` tests.

Длинный тестовый набор разрешается разбивать на несколько свежих pytest
процессов согласно зафиксированному workaround в `docs/troubleshooting.md`.
Live-run при этом всегда остаётся одним процессом и не дробится на параллельные
команды.

## 14. Критерии готовности

Этап завершён, когда одновременно выполнены условия:

1. Все операции текущей effective OpenAPI классифицированы.
2. Все `automatic read` имеют reviewed `ReadCase`, allowlist entry и verified
   rate budget.
3. Все новые offline-тесты и существующий `verify` проходят.
4. Generated tree воспроизводим и не содержит ручных исправлений.
5. Один guarded `live_read_full` выполнен на профиле Amato без `429`.
6. Все доступные read-cases имеют `passed`, остальные — обоснованный
   `no_live_target`.
7. Никакая write-операция не была выполнена в рамках этапа.
8. Ни один секрет, private profile, live payload или identifier не попал в
   tracked diff.
9. Инструкция запуска и интерпретации отчёта добавлена в `docs/generation.md`.

Если для операции нельзя подтвердить rate limit, построить корректный request
или получить безопасный target, это не обходится предположением. Операция
остаётся fail-closed с точной причиной, а критерий полного live-покрытия явно
показывает незавершённый участок.

## 15. Следующие этапы

После завершения этого дизайна отдельно проектируются:

1. Lifecycle registry, связывающий `prepare -> create -> check/update ->
   finally cleanup`.
2. Ownership markers, LIFO compensation stack и persistent mutation journal
   для создаваемых тестом объектов.
3. Политика ручного восстановления после crash или `429`, при котором
   автоматический cleanup запрещён текущими safety rules.
4. Repository-local Codex skill, который проверяет обновление upstream,
   классифицирует изменения, вносит обоснованные offline-коррекции, запускает
   `sync/verify` и оставляет unstaged diff без live, commit, push или publish.

OpenAPI не содержит достаточной бизнес-семантики, чтобы безопасно вывести
lifecycle-связи автоматически. Генератор сможет создать только fail-closed
заготовку новой write-операции; сам сценарий и компенсация проходят отдельный
review.
