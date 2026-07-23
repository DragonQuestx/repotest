# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: JobSearch
python
def print_metrics(jobs, applications, interviews, notes):
    total = len(jobs) + len(applications) + len(interviews) + len(notes)
    applied_jobs = sum(1 for a in applications if a.get('status') == 'applied')
    interviewed = sum(1 for i in interviews if i.get('status') == 'interview')
    print(f"Jobs: {len(jobs)}")
    print(f"Applications: {len(applications)} (active: {applied_jobs})")
    print(f"Interviews: {len(interviews)} (scheduled: {interviewed})")
    print(f"Notes: {len(notes)}")
    print(f"Total items: {total}")

if __name__ == "__main__":
    from job_tracker import jobs, applications, interviews, notes
    print_metrics(jobs, applications, interviews, notes)
print("Metrics printed.")
