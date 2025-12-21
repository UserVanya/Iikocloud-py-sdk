#!/usr/bin/env python3
"""
Скрипт для исправления недопустимых имён схем в OpenAPI JSON файле.

Заменяет имена схем с недопустимыми символами (обратные кавычки, квадратные скобки и т.д.)
на валидные имена, соответствующие регулярному выражению ^[a-zA-Z0-9\.\-_]+$
"""

import json
import re
import sys
from typing import Dict


def normalize_schema_name(name: str) -> str:
    """
    Нормализует имя схемы, заменяя недопустимые символы на валидные.
    
    Args:
        name: Исходное имя схемы
        
    Returns:
        Нормализованное имя схемы
    """
    # Извлекаем тип из generic-параметра
    # Паттерн: RmsItemsResponseWrapper`1[[iikoTransport.PublicApi.Contracts.Address.City, ...]]
    match = re.search(r'RmsItemsResponseWrapper`1\[\[([^,]+)', name)
    if match:
        type_name = match.group(1).strip()
        # Извлекаем последнюю часть имени типа (например, City из Address.City)
        parts = type_name.split('.')
        if len(parts) > 0:
            # Берем последние 2-3 части для более понятного имени
            if len(parts) >= 2:
                # Например: Address.City -> Address_City
                type_part = '_'.join(parts[-2:])
            else:
                type_part = parts[-1]
            return f"RmsItemsResponseWrapper_{type_part}"
    
    # Если паттерн не совпал, просто заменяем недопустимые символы
    # Заменяем обратные кавычки, квадратные скобки, запятые, пробелы на подчеркивания
    normalized = re.sub(r'[`\[\],\s]', '_', name)
    # Удаляем множественные подчеркивания
    normalized = re.sub(r'_+', '_', normalized)
    # Удаляем подчеркивания в начале и конце
    normalized = normalized.strip('_')
    return normalized


def fix_schema_names(json_file: str) -> None:
    """
    Исправляет имена схем в OpenAPI JSON файле.
    
    Args:
        json_file: Путь к JSON файлу
    """
    print(f"Загрузка файла {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Собираем все проблемные имена схем
    schema_mapping: Dict[str, str] = {}
    
    if 'components' in data and 'schemas' in data['components']:
        schemas = data['components']['schemas']
        for old_name in list(schemas.keys()):
            # Проверяем, содержит ли имя недопустимые символы
            if not re.match(r'^[a-zA-Z0-9.\-_]+$', old_name):
                new_name = normalize_schema_name(old_name)
                # Убеждаемся, что новое имя уникально
                counter = 1
                original_new_name = new_name
                while new_name in schema_mapping.values() or new_name in schemas:
                    new_name = f"{original_new_name}_{counter}"
                    counter += 1
                schema_mapping[old_name] = new_name
                print(f"  {old_name[:80]}... -> {new_name}")
    
    if not schema_mapping:
        print("Проблемных имён схем не найдено.")
        return
    
    print(f"\nНайдено {len(schema_mapping)} проблемных имён схем.")
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
    
    print(f"Готово! Исправлено {len(schema_mapping)} имён схем.")


if __name__ == '__main__':
    json_file = 'iikocloud_openapi.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    try:
        fix_schema_names(json_file)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

