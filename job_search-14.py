# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: JobSearch
def generate_summary():
    if not jobs and not applications:
        print("Нет данных для сводки.")
        return
    
    total_jobs = len(jobs)
    applied_count = sum(1 for j in jobs if j.get('status') == 'applied')
    
    status_breakdown = {
        'new': sum(1 for j in jobs if j.get('status') == 'new'),
        'applied': sum(1 for j in jobs if j.get('status') == 'applied'),
        'interview': sum(1 for j in jobs if j.get('status') == 'interview'),
        'offer': sum(1 for j in jobs if j.get('status') == 'offer'),
    }
    
    print(f"=== Сводка поиска работы ===")
    print(f"Вакансий всего: {total_jobs}")
    print(f"Отправлено откликов: {applied_count}")
    print("Статусы:")
    for status, count in status_breakdown.items():
        if count > 0:
            print(f"  - {status.capitalize()}: {count}")

if __name__ == "__main__":
    generate_summary()
