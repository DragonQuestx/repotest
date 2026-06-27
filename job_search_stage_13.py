# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: JobSearch
def search_jobs(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['title', 'company', 'description']
    results = [job for job in jobs]
    for field in fields:
        filtered = []
        for job in results:
            text = getattr(job, field, '').lower()
            if q in text: filtered.append(job)
        results = filtered
    return results
