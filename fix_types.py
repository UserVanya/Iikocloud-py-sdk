#!/usr/bin/env python3
"""
Скрипт для исправления недопустимых типов в OpenAPI JSON файле.

Заменяет недопустимые типы на корректные для OpenAPI 3.0:
- "float" -> "number" с "format": "float"
- "uuid" -> "string" с "format": "uuid"
- "enum" -> "string" (enum должен быть определен через массив "enum", а не как тип)
"""

import json
import sys


def fix_types(json_file: str) -> None:
    """
    Исправляет типы в OpenAPI JSON файле.
    
    Args:
        json_file: Путь к JSON файлу
    """
    print(f"Загрузка файла {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes_count = 0
    
    def fix_types_recursive(obj):
        """Рекурсивно исправляет типы в объекте."""
        nonlocal changes_count
        if isinstance(obj, dict):
            # Проверяем, есть ли поле "type" со значением "float"
            if 'type' in obj and obj['type'] == 'float':
                obj['type'] = 'number'
                obj['format'] = 'float'
                changes_count += 1
            elif 'type' in obj and obj['type'] == 'int':
                obj['type'] = 'integer'
                obj['format'] = 'int32'
                changes_count += 1
            # Проверяем, есть ли поле "type" со значением "uuid"
            elif 'type' in obj and obj['type'] == 'uuid':
                obj['type'] = 'string'
                obj['format'] = 'uuid'
                changes_count += 1
            elif 'type' in obj and obj['type'] == 'bool':
                obj['type'] = 'boolean'
                changes_count += 1
            # Проверяем, есть ли поле "type" со значением "enum"
            elif 'type' in obj and obj['type'] == 'enum':
                obj['type'] = 'string'
                obj['format'] = 'enum'
                # Если присутствует example, попробовать получить значения enum из example
                example_val = obj.get('example')
                # Обрабатываем пример вида "{\"BY_COMPONENT\", \"FIXED\", \"CALCULATE\"}"
                enum_values = []
                if example_val and isinstance(example_val, str) and example_val.startswith('{') and example_val.endswith('}'):
                    # Вырезаем фигурные скобки и кавычки
                    enum_str = example_val.strip('{} \n"')
                    # Разбиваем по запятой
                    for part in enum_str.split(','):
                        # Удаляем кавычки и пробелы
                        val = part.strip(' "')
                        if val:
                            enum_values.append(val)
                if enum_values:
                    obj['enum'] = enum_values
                else:
                    obj['enum'] = []
                changes_count += 1
            # Рекурсивно обрабатываем все значения словаря
            for key, value in obj.items():
                fix_types_recursive(value)
        elif isinstance(obj, list):
            # Рекурсивно обрабатываем все элементы списка
            for item in obj:
                fix_types_recursive(item)
    
    print("Применение исправлений...")
    fix_types_recursive(data)
    
    if changes_count == 0:
        print("Проблемных типов не найдено.")
        return
    
    # Сохраняем исправленный файл
    print(f"Сохранение исправленного файла... (исправлено {changes_count} типов)")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Готово! Исправлено {changes_count} типов.")


if __name__ == '__main__':
    json_file = 'iikocloud_openapi.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    try:
        fix_types(json_file)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

