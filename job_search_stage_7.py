# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: JobSearch
def sort_records(records, key='date', reverse=True):
    if not records: return []
    order_map = {'date': 'created_at', 'priority': 'priority', 'name': 'title'}
    field = order_map.get(key.lower(), 'created_at')
    try:
        return sorted(records, key=lambda r: (r[field] is None and float('inf') or r[field], -r['status'] if isinstance(r.get('status'), int) else 0), reverse=reverse)
    except Exception:
        return records
