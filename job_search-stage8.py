# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: JobSearch
def main():
    storage = JobSearch()
    while True:
        print("\n=== Меню ===")
        print("1. Добавить вакансию")
        print("2. Просмотреть вакансии")
        print("3. Откликнуться на вакансию")
        print("4. Записать интервью")
        print("5. Заметки")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Название вакансии: ")
            company = input("Компания: ")
            storage.add_vacancy(title, company)
        elif choice == "2":
            for v in storage.vacancies.values():
                print(f"{v.id}: {v.title} ({v.company})")
        elif choice == "3":
            vid = input("ID вакансии для отклика: ")
            if storage.apply_to_vacancy(vid):
                print("Отклик отправлен!")
            else:
                print("Вакансия не найдена или уже обработана.")
        elif choice == "4":
            vid = input("ID вакансии, где было интервью: ")
            notes = input("Заметки по интервью: ")
            storage.record_interview(vid, notes)
        elif choice == "5":
            print(storage.notes if storage.notes else "Нет заметок.")
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
