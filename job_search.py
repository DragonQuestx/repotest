# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: JobSearch
def init_demo_data():
    vacancies = [
        {"id": 1, "title": "Python Developer", "company": "TechCorp", "salary": "150k-200k", "posted": "2023-10-01"},
        {"id": 2, "title": "Backend Engineer", "company": "DataSystems", "salary": "180k-250k", "posted": "2023-10-05"}
    ]
    applications = [
        {"id": 1, "vacancy_id": 1, "status": "applied", "date": "2023-10-02", "notes": "Отправил резюме через сайт."}
    ]
    interviews = []
    notes = ["Нужно обновить LinkedIn профиль.", "Подготовиться к собеседованию по алгоритмам."]
    
    return {
        "vacancies": vacancies,
        "applications": applications,
        "interviews": interviews,
        "notes": notes
    }

if __name__ == "__main__":
    demo_data = init_demo_data()
    print("Демо-данные инициализированы:", len(demo_data["vacancies"]), "вакансий.")
