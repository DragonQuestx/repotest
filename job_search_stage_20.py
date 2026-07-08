# === Stage 20: Добавь восстановление записей из архива ===
# Project: JobSearch
def restore_from_archive(archive_path, db):
    """Восстанавливает записи из CSV-архива в базу данных JobSearch."""
    import csv
    if not archive_path or not os.path.exists(archive_path):
        return 0
    count = 0
    with open(archive_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record_type = row.get('type', '').strip().lower()
            if record_type == 'vacancy':
                db.vacancies.append(Vacancy(
                    id=int(row['id']), title=row['title'], company=row['company'],
                    location=row['location'], salary_min=int(row['salary_min']),
                    salary_max=int(row['salary_max']) if row['salary_max'] else None,
                    description=row.get('description', ''), status=row['status'].strip().lower(),
                ))
            elif record_type == 'application':
                db.applications.append(Application(
                    id=int(row['id']), vacancy_id=int(row['vacancy_id']),
                    position=row['position'], resume_link=row['resume_link'],
                    status=row['status'].strip().lower(), date=parse_date(row.get('date', '')),
                ))
            elif record_type == 'interview':
                db.interviews.append(Interview(
                    id=int(row['id']), application_id=int(row['application_id']),
                    company=row['company'], interviewer=row['interviewer'],
                    scheduled_at=parse_date(row.get('scheduled_at', '')),
                    notes=row.get('notes', ''), status=row['status'].strip().lower(),
                ))
            elif record_type == 'note':
                db.notes.append(Note(
                    id=int(row['id']), content=row['content'], created_at=parse_date(row.get('created_at', '')),
                ))
            count += 1
    print(f"[Archive] Restored {count} records from '{archive_path}'.")
    return count
