# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: JobSearch
def check_reminders():
    now = datetime.now()
    for job in jobs:
        if job.reminder_date and job.reminder_date < now:
            print(f"Напоминание просрочено для позиции {job.title}")
    return
