#!/usr/bin/env python3
"""
Скрипт для добавления securitySchemes и security в OpenAPI JSON файл.

Добавляет Bearer authentication схему и применяет её глобально.
"""

import json
import sys


def add_security(json_file: str) -> None:
    """
    Добавляет securitySchemes и security в OpenAPI JSON файл.
    
    Args:
        json_file: Путь к JSON файлу
    """
    print(f"Загрузка файла {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes_made = False
    
    # Добавляем components, если его нет
    if 'components' not in data:
        data['components'] = {}
        changes_made = True
    
    # Добавляем securitySchemes, если его нет
    if 'securitySchemes' not in data['components']:
        data['components']['securitySchemes'] = {}
        changes_made = True
    
    # Добавляем Bearer схему, если её нет
    if 'Bearer' not in data['components']['securitySchemes']:
        data['components']['securitySchemes']['Bearer'] = {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Bearer token for authentication"
        }
        changes_made = True
        print("  Добавлена securitySchemes.Bearer")
    
    # Добавляем security на верхнем уровне, если его нет
    if 'security' not in data:
        data['security'] = [
            {
                "Bearer": []
            }
        ]
        changes_made = True
        print("  Добавлен глобальный security")
    
    if not changes_made:
        print("Security схемы уже присутствуют в файле.")
        return
    
    # Сохраняем исправленный файл
    print("Сохранение исправленного файла...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Готово! Security схемы добавлены.")


if __name__ == '__main__':
    json_file = 'iikocloud_openapi.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    try:
        add_security(json_file)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

