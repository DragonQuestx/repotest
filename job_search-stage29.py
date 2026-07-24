# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: JobSearch
APP_CONFIG = {
    "app_name": "JobSearch",
    "version": "0.1.29",
    "max_jobs_display": 5,
    "default_sort_by": "date_added",
    "allowed_statuses": ["open", "applied", "interview", "rejected", "hired"],
    "data_file": "jobs.json",
}


def load_config():
    return APP_CONFIG.copy()


def validate_job_status(job, status):
    if status not in APP_CONFIG["allowed_statuses"]:
        raise ValueError(f"Invalid status '{status}'. Allowed: {APP_CONFIG['allowed_statuses']}")
    job[status] = True
