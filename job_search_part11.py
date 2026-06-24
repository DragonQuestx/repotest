# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: JobSearch
import json, os

DATA_FILE = "jobsearch_data.json"

def save_to_json(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {"jobs": [], "applications": [], "interviews": [], "notes": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"jobs": [], "applications": [], "interviews": [], "notes": []}

def persist_data(jobs=None, applications=None, interviews=None, notes=None):
    data = load_from_json()
    if jobs is not None: data["jobs"] = jobs
    if applications is not None: data["applications"] = applications
    if interviews is not None: data["interviews"] = interviews
    if notes is not None: data["notes"] = notes
    save_to_json(data)
