# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: JobSearch
def filter_jobs(status=None, category=None, tags=None):
    filtered = []
    for job in jobs:
        if status and job['status'] != status: continue
        if category and job.get('category') != category: continue
        if tags:
            job_tags = set(job.get('tags', [])).intersection(tags)
            if not job_tags: continue
        filtered.append(job)
    return filtered

def filter_notes(status=None, tag=None):
    filtered = []
    for note in notes:
        if status and note['status'] != status: continue
        if tag and tag not in note.get('tags', []): continue
        filtered.append(note)
    return filtered
