#!/usr/bin/env python3
"""
Скрипт для исправления путей и добавления servers в OpenAPI JSON файле.

1. Убирает префиксы /api/1 и /api/2 из путей
2. Добавляет servers к каждому методу с соответствующим URL
3. Добавляет глобальный servers
"""

import json
import re
import sys
from typing import Dict, List


def fix_paths_and_servers(json_file: str) -> None:
    """
    Исправляет пути и добавляет servers в OpenAPI JSON файл.
    
    Args:
        json_file: Путь к JSON файлу
    """
    print(f"Загрузка файла {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Добавляем глобальный servers, если его нет
    if 'servers' not in data:
        data['servers'] = [
            {
                "url": "https://api-ru.iiko.services/api/1",
                "description": "Production"
            }
        ]
        print("  Добавлен глобальный servers")
    
    if 'paths' not in data:
        print("Ошибка: В файле нет секции 'paths'")
        return
    
    paths = data['paths']
    paths_to_rename: Dict[str, str] = {}
    operations_updated = 0
    
    # Собираем информацию о путях, которые нужно переименовать
    for path in list(paths.keys()):
        new_path = path
        server_url = None
        
        # Убираем префикс /api/1/
        if path.startswith('/api/1/'):
            new_path = path.replace('/api/1/', '/')
            server_url = 'https://api-ru.iiko.services/api/1'
        # Убираем префикс /api/2/
        elif path.startswith('/api/2/'):
            new_path = path.replace('/api/2/', '/')
            server_url = 'https://api-ru.iiko.services/api/2'
        # Если путь начинается с /api/1 (без слеша после)
        elif path.startswith('/api/1'):
            new_path = path.replace('/api/1', '')
            if not new_path or new_path == '/':
                new_path = '/'
            elif not new_path.startswith('/'):
                new_path = '/' + new_path
            server_url = 'https://api-ru.iiko.services/api/1'
        # Если путь начинается с /api/2 (без слеша после)
        elif path.startswith('/api/2'):
            new_path = path.replace('/api/2', '')
            if not new_path or new_path == '/':
                new_path = '/'
            elif not new_path.startswith('/'):
                new_path = '/' + new_path
            server_url = 'https://api-ru.iiko.services/api/2'
        
        # Если путь был изменен, добавляем в список для переименования
        if server_url:
            paths_to_rename[path] = {'new_path': new_path, 'server_url': server_url}
    
    print(f"\nНайдено {len(paths_to_rename)} путей для переименования.")
    print("Применение исправлений...")
    
    # Переименовываем пути и добавляем servers к операциям
    for old_path, info in paths_to_rename.items():
        new_path = info['new_path']
        server_url = info['server_url']
        
        if old_path in paths:
            path_data = paths[old_path]
            
            # Добавляем servers к каждой операции (get, post, put, delete, patch и т.д.)
            http_methods = ['get', 'post', 'put', 'delete', 'patch', 'head', 'options', 'trace']
            for method in http_methods:
                if method in path_data:
                    operation = path_data[method]
                    # Добавляем servers только если их еще нет
                    if 'servers' not in operation or not operation['servers']:
                        operation['servers'] = [
                            {
                                "url": server_url,
                                "description": "Production"
                            }
                        ]
                        operations_updated += 1
                    # Если servers уже есть, но URL не совпадает, обновляем
                    elif operation['servers'] and operation['servers'][0].get('url') != server_url:
                        operation['servers'][0]['url'] = server_url
                        operations_updated += 1
            
            # Переименовываем путь
            if new_path != old_path:
                paths[new_path] = paths.pop(old_path)
                print(f"  {old_path} -> {new_path}")
    
    # Сохраняем исправленный файл
    print(f"\nОбновлено операций: {operations_updated}")
    print("Сохранение исправленного файла...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Готово! Переименовано {len(paths_to_rename)} путей, обновлено {operations_updated} операций.")


if __name__ == '__main__':
    json_file = 'iikocloud_openapi.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    try:
        fix_paths_and_servers(json_file)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

