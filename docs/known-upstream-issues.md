# Известные проблемы upstream OpenAPI

Этот реестр описывает только проверенные corrections текущего tracked
snapshot. Он не заменяет сами overlays: точные guard hashes и полные actions
находятся в `openapi/overlays/`. Private captures и реальные IDs здесь не
публикуются.

## Как читать реестр

`issue` — стабильный `x-iiko-sdk-guard.issue`. `Fragment` — raw upstream
JSONPath или компонент, к которому привязана correction. Любой guard проверяет
ровно ожидаемое число совпадений и SHA-256 исходного fragment; изменение
upstream останавливает pipeline до нового review.

Correction можно удалить только когда новый upstream выражает тот же контракт
без overlay, generated contract tests проходят, а `verify` подтверждает
воспроизводимость. Нельзя просто обновить digest под изменившийся fragment.

`Наблюдалось` — дата, когда текущая correction или её evidence впервые была
зафиксирована в tracked repository. В колонке evidence перечислены только
synthetic fixtures и offline tests; private captures не являются частью
реестра. Диапазоны и фигурные скобки в Issue разворачиваются в literal IDs из
соответствующего overlay, без неявных дополнительных corrections.

## Authentication и server contract

Источник: `openapi/overlays/contracts.overlay.yaml`.

| Issue | Fragment | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `iiko-root-server` | document root | Добавить canonical iiko Cloud server URL | Synthetic composition в `tests/pipeline/test_pipeline.py` | 2026-07-17 | Upstream содержит проверенный root `servers` |
| `iiko-bearer-scheme` | `$.components` | Добавить HTTP bearer scheme `BearerAuth` | `tests/pipeline/test_contracts.py`, `tests/contracts/test_bearer_auth.py` | 2026-07-17 | Upstream объявляет эквивалентную reusable scheme |
| `remove-raw-authorization-parameters` | raw `Authorization` header parameters операций | Удалить дублирующиеся ручные header parameters | `tests/pipeline/test_contracts.py`, `tests/contracts/test_bearer_auth.py` | 2026-07-17 | Upstream больше не дублирует header в операциях |
| `require-bearer-authentication` | все API operations | Добавить `security: [{BearerAuth: []}]` | `tests/pipeline/test_contracts.py`, generated bearer contract test | 2026-07-17 | Upstream корректно задаёт security для всех защищённых операций |
| `remove-bearer-from-post-/api/1/access_token`, `mark-post-/api/1/access_token-public` | `/api/1/access_token` POST | Явно оставить endpoint публичным | Synthetic public-auth assertions в `tests/pipeline/test_pipeline.py` | 2026-07-17 | Upstream public security семантически совпадает |
| `remove-bearer-from-post-/api/v2/access_token`, `mark-post-/api/v2/access_token-public` | `/api/v2/access_token` POST | Явно оставить endpoint публичным | Synthetic public-auth assertions в `tests/pipeline/test_pipeline.py` | 2026-07-17 | Upstream public security семантически совпадает |

## Mechanical типы и имена

Источник: `openapi/overlays/types.overlay.yaml`,
`openapi/model-name-overrides.yaml` и naming stage.

| Issue family | Fragment | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `normalize-pseudo-type-1…59-*` (точные `clear-*`/`apply` IDs в overlay) | schema properties с raw типами `bool`, `uuid`, `float`, `integer <int64>`, `Array of strings <uuid>` и constant-string pseudo types | Преобразовать в валидные OpenAPI `type`/`format`/`items`/`enum` | Synthetic cases в `tests/pipeline/test_normalization.py` | 2026-07-21 | Upstream использует стандартный JSON Schema/OpenAPI shape |
| `remove-malformed-scalar-required-1…9` | `TaxCategoryDto*` scalar properties | Удалить boolean `required` внутри property; required-list допустим только у object schema | Synthetic cases в `tests/pipeline/test_normalization.py` | 2026-07-21 | Upstream удаляет malformed scalar keyword |
| reviewed model mappings (registry, не overlay action) | collision-prone CLR-qualified component keys | Выдать стабильные доменные Python model names | `tests/pipeline/test_naming.py` и reviewed registry | 2026-07-21 | Upstream names больше не collide и public Python names можно сохранить совместимо |
| generator-invalid CLR generic keys (physical naming stage) | CLR `RmsItemsResponseWrapper` component keys с backtick/brackets | Физически переименовать только invalid component keys по тому же reviewed mapping и переписать точные local `$ref` | `tests/pipeline/test_naming.py` и pinned generator validation | 2026-07-21 | Upstream публикует валидные стабильные component keys; старые refs отсутствуют |

## External menu: стабильный response union

Источник: `openapi/overlays/operations.overlay.yaml` и
`openapi/overlays/polymorphism.overlay.yaml`. Evidence acceptance потребовал
три отдельно полученных sanitized response версии 2, 3 и 4. В Git сохранены
только минимальные synthetic fixtures:
`tests/fixtures/contracts/external-menu-v2.json`,
`external-menu-v3.json` и `external-menu-v4.json`.

### Response model

| Issue | Fragment | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `external-menu-response-title` | `/api/2/menu/by_id` POST, JSON response `200` schema | Добавить title `ExternalMenuResponse` | `external-menu-v2.json`, `external-menu-v3.json`, `external-menu-v4.json` и generated union test | 2026-07-20 | Upstream даёт стабильное, совместимое имя response union |

### Корневые V2, V3 и V4

| Issues | Fragment | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `external-menu-v2-format-version`, `external-menu-v2-required-remove`, `external-menu-v2-required` | `ExternalMenuV2` | Зафиксировать `formatVersion` как enum/default `2` и включить поле в object `required` | `tests/fixtures/contracts/external-menu-v2.json` | 2026-07-20 | Upstream делает V2 branch структурно взаимоисключающей |
| `external-menu-v3-format-version`, `external-menu-v3-required-remove`, `external-menu-v3-required` | `ExternalMenuV3` | Зафиксировать `formatVersion` как enum/default `3` и включить поле в `required` | `tests/fixtures/contracts/external-menu-v3.json` | 2026-07-20 | То же для V3 |
| `external-menu-v4-format-version`, `external-menu-v4-required-remove`, `external-menu-v4-required` | `ExternalMenuV4` | Зафиксировать `formatVersion` как enum/default `4` и включить поле в `required` | `tests/fixtures/contracts/external-menu-v4.json` | 2026-07-20 | То же для V4 |

Без этих actions все три upstream branches допускают недостаточно различимые
объекты, а V3/V4 ошибочно имеют default `2`. Generated test
`tests/generated/test_external_menu_response.py` требует ровно один выбранный
branch для каждой synthetic fixture.

### Неверные shapes и nullability в menu data

Все перечисленные IDs имеют префикс `external-menu-schema-`; remove-actions с
суффиксом `-remove` сначала удаляют конфликтующие `type`, `items`, `description`
или `enum`, после чего guarded update задаёт reviewed shape.

| Issue ID(s) | Upstream fragment / проблема | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `external-menu-schema-ExternalMenuPriceByDepartmentsDto-properties-organizationId` | `ExternalMenuPriceByDepartmentsDto.properties`: отсутствует встречающееся поле | Добавить UUID string `organizationId` | Versioned external-menu fixtures и `tests/pipeline/test_evidence_schema_repairs.py` | 2026-07-20 | Upstream содержит эквивалентное property |
| `external-menu-schema-ExternalMenuItem-properties-taxCategory{,-items-remove,-type-remove}` | `ExternalMenuItem.properties.taxCategory`: object ошибочно описан как array | Nullable `oneOf` со ссылкой на `TaxCategoryDto3` | Versioned external-menu fixtures и schema repair tests | 2026-07-20 | Upstream содержит корректный nullable ref |
| `external-menu-schema-ExternalMenuItemSize-properties-nutritionPerHundredGrams{,-description-remove,-items-remove,-type-remove}` | `ExternalMenuItemSize.properties.nutritionPerHundredGrams`: object ошибочно описан как array | Ссылка на `NutritionInfoDto` | Versioned external-menu fixtures и schema repair tests | 2026-07-20 | Upstream содержит корректный ref |
| `external-menu-schema-ExternalMenuModifierItem-properties-nutritionPerHundredGrams{,-items-remove,-type-remove}` | `ExternalMenuModifierItem.properties.nutritionPerHundredGrams`: object ошибочно описан как array | Nullable `oneOf` с `NutritionInfoDto5` | Versioned external-menu fixtures и schema repair tests | 2026-07-20 | Upstream содержит корректный nullable ref |
| `external-menu-schema-ExternalMenuModifierItem{,2,3}-properties-restrictions{,-items-remove,-type-remove}` | `ExternalMenuModifierItem{,2,3}.properties.restrictions`: object ошибочно описан как array | Nullable `oneOf` к соответствующему `ModifierRestrictionsDto5/6/7` | `external-menu-v2.json`, `external-menu-v3.json`, `external-menu-v4.json` | 2026-07-20 | Все соответствующие upstream branches исправлены |
| `external-menu-schema-ExternalMenuV{3,4}-properties-overrideTaxCategories{,-items-remove}` | `ExternalMenuV3/V4.properties.overrideTaxCategories`: UUID-keyed map ошибочно описан как array | Object с `additionalProperties`, значением которого является array соответствующего `OverrideTaxesDto*` | `external-menu-v3.json`, `external-menu-v4.json` | 2026-07-20 | Upstream содержит корректную map schema |
| `external-menu-schema-ExternalMenuItem{,2,3}-properties-type{,-enum-remove}` | `ExternalMenuItem{,2,3}.properties.type`: enum не содержит публичный literal `SERVICE` | Enum `DISH`, `COMBO`, `SERVICE` до V4 branch specialization | Versioned fixtures, schema-aware hints и analyzer regressions | 2026-07-20 | Upstream содержит полный enum |
| `external-menu-schema-ExternalMenuItem{,2,3}-properties-modifierSchemaId` | `ExternalMenuItem{,2,3}.properties.modifierSchemaId`: реальный `null` запрещён | Добавить `nullable: true` | `external-menu-v2.json`, `external-menu-v3.json`, `external-menu-v4.json` | 2026-07-20 | Upstream выражает nullability |
| `external-menu-schema-ExternalMenuItemSize-properties-sizeId`, `external-menu-schema-ExternalMenuItemSize{2,3}-properties-id` | Default/единственный size может иметь `null` ID | Добавить `nullable: true` | Versioned external-menu fixtures | 2026-07-20 | Upstream выражает nullability |
| `external-menu-schema-ExternalMenuPriceByDepartmentsDto{,2,3}-properties-price` | Недоступный для продажи size может иметь `null` price | Добавить `nullable: true` | Versioned external-menu fixtures | 2026-07-20 | Upstream выражает nullability |

Validator также имеет узкое reviewed исключение для undeclared barcode property,
но только когда её значение строго `null` и component/property-name hashes
совпадают. Любое ненулевое или новое неизвестное поле продолжает fail closed;
это исключение удаляется, когда upstream явно опишет поле.

### V4 item discriminator и `ExternalMenuComboItem`

| Issue | Fragment | Correction | Evidence / fixture | Наблюдалось | Условие удаления |
|---|---|---|---|---|---|
| `external-menu-v4-discriminator` | `ExternalMenuCategory3.properties.items.items` | Discriminator `type`: `DISH` и `SERVICE` → `ExternalMenuItem3`, `COMBO` → `ExternalMenuComboItem` | `tests/fixtures/contracts/external-menu-v4.json`; analyzer проверяет literal-to-branch consistency | 2026-07-20 | Upstream содержит эквивалентный discriminator и branches остаются disjoint |
| `external-menu-item3-type-enum-remove`, `external-menu-item3-type` | `ExternalMenuItem3.properties.type` | Ограничить dish branch literals до `DISH`/`SERVICE`, default `DISH` | V4 fixture, analyzer и generated union regressions | 2026-07-20 | Upstream item branch имеет тот же enum |
| `external-menu-item3-required-remove`, `external-menu-item3-required` | `ExternalMenuItem3.required` | Добавить `type` к реально обязательным dish fields | V4 fixture и structural matching tests | 2026-07-20 | Upstream required-list эквивалентен |
| `external-menu-combo-item-type` | `ExternalMenuComboItem.properties.type` | Ограничить поле единственным literal `COMBO`, default `COMBO` | V4 fixture принят только после matching combo evidence | 2026-07-20 | Upstream combo type имеет `enum: [COMBO]` |
| `external-menu-combo-required-remove`, `external-menu-combo-required` | `ExternalMenuComboItem.required` | Заменить список на `sizes`, `type`, `id` | V4 fixture, reviewed fragment hash и combo contract tests | 2026-07-20 | Upstream удаляет undefined required names и live/synthetic contract tests подтверждают новый список |

`ExternalMenuComboItem` особенно опасен для автоматической генерации: исходный
`required` ссылается на dish-only поля `itemSizes`, `modifierSchemaId`,
`orderItemType`, `allergenGroupIds` и `splittable`, отсутствующие в combo
`properties`. Одновременно его `type` является произвольной строкой. Поэтому
обычный `oneOf` не может надёжно выбрать branch. Текущая correction делает
branches disjoint и проверяется до promotion; private payload при этом не
становится частью репозитория.

## Процедура удаления correction

1. Запустите `upstream-check` и сохраните публичный diff под `build/`.
2. Убедитесь, что upstream fragment теперь выражает тот же контракт. Старый
   guard должен стать stale — это ожидаемый сигнал review, а не повод заменить
   hash.
3. Удалите только ставшую ненужной action или mapping и обновите focused test.
4. Для menu defect заново проверьте все затронутые версии; live recapture
   выполняется только если публичных synthetic fixtures недостаточно доказать
   контракт и только по guarded процедуре из `generation.md`.
5. Выполните offline `sync`, `verify`, wheel checks и просмотрите generated API
   diff до commit.
