#!/usr/bin/env python3
"""
Скрипт для удаления лишних префиксов из имён схем в OpenAPI JSON файле.

Удаляет префиксы:
- iikoTransport.PublicApi.Contracts.
- iikoNet.Service.Contracts.Api.iikoTransport.

Заменяет:
- RmsItemsResponseWrapper_ на Wrapper_
"""

import json
import re
import sys
from typing import Dict


def normalize_schema_name(name: str) -> str:
    """
    Нормализует имя схемы, удаляя лишние префиксы и заменяя длинные имена.
    
    Args:
        name: Исходное имя схемы
        
    Returns:
        Нормализованное имя схемы
    """
    new_name = name
    
    # Удаляем префикс iikoTransport.PublicApi.Contracts.
    new_name = re.sub(r'^iikoTransport\.PublicApi\.Contracts\.', '', new_name)
    
    # Удаляем префикс iikoNet.Service.Contracts.Api.iikoTransport.
    new_name = re.sub(r'^iikoNet\.Service\.Contracts\.Api\.iikoTransport\.', '', new_name)
    
    # Заменяем RmsItemsResponseWrapper_ на Wrapper_
    new_name = re.sub(r'^RmsItemsResponseWrapper_', 'Wrapper_', new_name)
    
    return new_name


def fix_schema_prefixes(json_file: str) -> None:
    """
    Исправляет префиксы в именах схем OpenAPI JSON файла.
    
    Args:
        json_file: Путь к JSON файлу
    """
    print(f"Загрузка файла {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Собираем все имена схем, которые нужно переименовать
    schema_mapping: Dict[str, str] = {}
    
    if 'components' in data and 'schemas' in data['components']:
        schemas = data['components']['schemas']
        for old_name in list(schemas.keys()):
            new_name = normalize_schema_name(old_name)
            if new_name != old_name:
                # Убеждаемся, что новое имя уникально
                counter = 1
                original_new_name = new_name
                while new_name in schema_mapping.values() or (new_name in schemas and new_name != old_name):
                    new_name = f"{original_new_name}_{counter}"
                    counter += 1
                schema_mapping[old_name] = new_name
                print(f"  {old_name[:80]}... -> {new_name}")
    
    if not schema_mapping:
        print("Имён схем для переименования не найдено.")
        return
    
    print(f"\nНайдено {len(schema_mapping)} имён схем для переименования.")
    print("Применение исправлений...")
    
    # Заменяем имена в определениях схем
    if 'components' in data and 'schemas' in data['components']:
        schemas = data['components']['schemas']
        for old_name, new_name in schema_mapping.items():
            if old_name in schemas:
                schemas[new_name] = schemas.pop(old_name)
    
    # Заменяем ссылки на схемы во всём файле
    def replace_refs(obj):
        """Рекурсивно заменяет ссылки на схемы в объекте."""
        if isinstance(obj, dict):
            if '$ref' in obj and isinstance(obj['$ref'], str):
                # Заменяем ссылку, если она указывает на переименованную схему
                for old_name, new_name in schema_mapping.items():
                    ref_path = f"#/components/schemas/{old_name}"
                    if obj['$ref'] == ref_path:
                        obj['$ref'] = f"#/components/schemas/{new_name}"
                        break
            else:
                # Рекурсивно обрабатываем все значения словаря
                for key, value in obj.items():
                    replace_refs(value)
        elif isinstance(obj, list):
            # Рекурсивно обрабатываем все элементы списка
            for item in obj:
                replace_refs(item)
    
    replace_refs(data)
    
    # Сохраняем исправленный файл
    print("Сохранение исправленного файла...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Готово! Переименовано {len(schema_mapping)} схем.")


if __name__ == '__main__':
    json_file = 'iikocloud_openapi.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    try:
        fix_schema_prefixes(json_file)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

