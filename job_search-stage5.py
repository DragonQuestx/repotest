# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: JobSearch
def delete_record(record_id: int, record_type: str) -> bool:
    if not hasattr(JobSearchApp, '_db'):
        return False
    db = JobSearchApp._db.get(record_type, [])
    for i, item in enumerate(db):
        if item['id'] == record_id:
            del db[i]
            print(f"Запись {record_type} #{record_id} удалена.")
            return True
    print(f"Запись {record_type} #{record_id} не найдена.")
    return False

if __name__ == "__main__":
    JobSearchApp._db = {'jobs': [], 'applications': [], 'interviews': [], 'notes': []}
    delete_record(99, 'jobs')  # Не существует
    delete_record(1, 'jobs')   # Удаление
