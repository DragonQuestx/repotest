# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: JobSearch
def export_to_json():
    import json
    from datetime import datetime
    
    def serialize(obj):
        if isinstance(obj, (datetime,)):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    data = {
        "vacancies": [
            {"id": v["id"], "title": v["title"], "company": v.get("company", ""), "url": v.get("url", "")} 
            for v in _data.get("vacancies", [])
        ],
        "applications": [
            {
                "id": a["id"],
                "vacancy_id": a["vacancy_id"],
                "status": a["status"],
                "date_applied": serialize(a.get("date_applied")),
                "notes": a.get("notes", ""),
                "interviews": [
                    {"date": serialize(i.get("date")), "role": i.get("role"), "feedback": i.get("feedback")} 
                    for i in a.get("interviews", [])
                ]
            } 
            for a in _data.get("applications", [])
        ],
        "notes": [
            {"id": n["id"], "title": n["title"], "content": n["content"]} 
            for n in _data.get("notes", [])
        ],
        "exported_at": serialize(datetime.now())
    }
    
    return json.dumps(data, ensure_ascii=False, indent=2)
