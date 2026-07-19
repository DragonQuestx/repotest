# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: JobSearch
def demo_commands():
    print("=== JobSearch Demo ===")

    # 1. Показ текущих состояний
    print(f"Вакансии: {len(jobs)}")
    print(f"Отклики: {len(applications)}")
    print(f"Интервью: {len(interviews)}")
    print(f"Заметки: {len(notes)}")

    # 2. Создаём тестовую вакансию
    if not jobs:
        demo_job = Job("Senior Python Developer", "Remote", "Full-time", "Python, Django, PostgreSQL")
        add_job(demo_job)
        print(f"Создана вакансия: {demo_job.title}")

    # 3. Откликаемся на вакансию
    if jobs and not applications:
        demo_app = Application("John Doe", "john@example.com", "5 years Python experience")
        add_application(demo_app)
        print(f"Отклик от: {demo_app.name}")

    # 4. Записываем интервью
    if applications and not interviews:
        demo_interview = Interview("2026-07-25", "Technical + Behavioral")
        add_interview(demo_interview)
        print(f"Интервью назначено на: {demo_interview.date}")

    # 5. Добавляем заметку
    if not notes:
        demo_note = Note("Позвонить кандидату через неделю", "2026-07-30")
        add_note(demo_note)
        print(f"Заметка добавлена: {demo_note.text}")

    # 6. Выводим итоговое состояние
    print("\n=== Итог ===")
    for j in jobs:
        print(f"- {j.title} ({j.location})")
    if applications:
        print(f"Кандидаты рассмотрены: {len(applications)}")
    if interviews:
        print(f"Интервью пройдено: {len(interviews)}")
    if notes:
        print(f"Заметок: {len(notes)}")

    print("Demo завершён.")
