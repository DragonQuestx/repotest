# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: JobSearch
def reset_demo_data():
    """Сбрасывает все данные в состояние демо для тестирования."""
    global jobs, applications, interviews, notes, current_user, app_id_counter, note_id_counter
    
    DEMO_JOBS = [
        {"id": 1, "title": "Python Developer", "company": "TechCorp", "salary": 120000, "location": "Remote", "posted_date": "2024-01-15"},
        {"id": 2, "title": "Frontend Engineer", "company": "WebInc", "salary": 95000, "location": "New York", "posted_date": "2024-01-20"},
        {"id": 3, "title": "Data Scientist", "company": "DataFlow", "salary": 110000, "location": "Chicago", "posted_date": "2024-02-01"},
    ]
    
    DEMO_APPLICATIONS = [
        {"id": 1, "job_id": 1, "applied_date": "2024-01-16", "status": "Applied", "cover_letter": "I am excited about this opportunity..."},
        {"id": 2, "job_id": 3, "applied_date": "2024-02-02", "status": "Applied", "cover_letter": "My background in ML makes me a perfect fit..."},
    ]
    
    DEMO_INTERVIEWS = [
        {"id": 1, "job_id": 1, "date": "2024-01-25", "status": "Scheduled", "notes": "Technical round with team lead."},
    ]
    
    jobs = DEMO_JOBS
    applications = DEMO_APPLICATIONS
    interviews = DEMO_INTERVIEWS
    notes = []
    current_user = {"name": "Demo User", "email": "demo@example.com"}
    app_id_counter = 2
    note_id_counter = 1
