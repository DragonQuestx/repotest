# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: JobSearch
def calculate_monthly_stats(jobs, interviews):
    from collections import defaultdict
    stats = defaultdict(lambda: {'jobs': 0, 'interviews': 0})
    for job in jobs:
        if hasattr(job, 'date_posted'):
            key = f"{job.date_posted.year}-{job.date_posted.month}"
            stats[key]['jobs'] += 1
    for interview in interviews:
        if hasattr(interview, 'date_scheduled'):
            key = f"{interview.date_scheduled.year}-{interview.date_scheduled.month}"
            stats[key]['interviews'] += 1
    return dict(sorted(stats.items()))
