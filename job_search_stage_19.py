# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: JobSearch
def archive_records(records, threshold_days=365):
    """Archive records older than `threshold_days` or with status 'done'/'closed'."""
    now = datetime.datetime.now()
    archived = []
    for rec in records:
        if rec["status"] in ("done", "closed"):
            archived.append(rec)
            continue
        created = datetime.datetime.fromisoformat(rec.get("created_at", now.isoformat()))
        if (now - created).days > threshold_days:
            archived.append(rec)
    return archived
