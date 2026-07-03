# === Stage 17: Добавь группировку записей по категориям ===
# Project: JobSearch
from collections import defaultdict

def group_by_category(records, key_field):
    groups = defaultdict(list)
    for record in records:
        category = record.get(key_field, 'Uncategorized')
        groups[category].append(record)
    return dict(sorted(groups.items()))
