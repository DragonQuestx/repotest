# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: JobSearch
import json, sys, os
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        raise ValueError("JSON должен содержать объект (словарь).")

    # Валидация обязательных полей
    required_keys = ["vacancies", "applications", "interviews", "notes"]
    missing = [k for k in required_keys if k not in data]
    if missing:
        raise ValueError(f"Отсутствуют обязательные поля: {', '.join(missing)}")

    # Преобразование списков в объекты (если данные пришли как простые массивы)
    def normalize_list(items, model):
        return [model(**item) for item in items] if isinstance(items, list) else []

    data["vacancies"] = normalize_list(data.get("vacancies", []), Vacancy)
    data["applications"] = normalize_list(data.get("applications", []), Application)
    data["interviews"] = normalize_list(data.get("interviews", []), Interview)
    data["notes"] = [Note(**note) for note in data.get("notes", [])]

    return data

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
        "vacancies": [{"id": 1, "title": "Python Dev", "company": "TechCorp"}],
        "applications": [],
        "interviews": [],
        "notes": []
    }'''

    initial_data = load_initial_data(sample_json)
    print(f"Загружено {len(initial_data['vacancies'])} вакансий.")
