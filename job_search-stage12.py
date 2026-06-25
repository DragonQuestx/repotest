# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: JobSearch
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return {item.get('id'): item for item in data}
        return {}
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON из '{filepath}': {e}")
        return {}
