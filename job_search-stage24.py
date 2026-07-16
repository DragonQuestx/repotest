# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: JobSearch
def print_job_record(job):
    print(f"Job: {job['id']}")
    print(f"  Title: {job.get('title', 'N/A')}")
    print(f"  Company: {job.get('company', 'N/A')}")
    print(f"  Location: {job.get('location', 'N/A')}")
    print(f"  Salary: {job.get('salary', 'N/A')}")
    print(f"  Status: {job['status']}")
    if job.get("responses"):
        for resp in job["responses"]:
            print(f"  Response: {resp}")
