# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: JobSearch
def edit_record(record_id, updates):
    if record_id not in records:
        raise ValueError(f"Запись с ID {record_id} не найдена")
    for key, value in updates.items():
        if key in record_fields and key != 'id':
            records[record_id][key] = value
        elif key == 'status' and record_type == 'job_application':
            valid_statuses = ['applied', 'interview_scheduled', 'offer_received', 'rejected']
            if value not in valid_statuses:
                raise ValueError(f"Недопустимый статус '{value}'. Доступные: {valid_statuses}")
