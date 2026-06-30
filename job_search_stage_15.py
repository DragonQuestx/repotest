# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: JobSearch
def calculate_weekly_stats(jobs, interviews):
    from datetime import datetime, timedelta
    
    if not jobs:
        return {}
    
    all_dates = set()
    for job in jobs:
        date_str = job.get('date') or job.get('created_at', '')
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            all_dates.add(dt)
        except ValueError:
            pass
    
    if not interviews:
        return {}
    
    for interview in interviews:
        date_str = interview.get('date') or interview.get('created_at', '')
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            all_dates.add(dt)
        except ValueError:
            pass
    
    if not all_dates:
        return {}
    
    min_date = min(all_dates)
    max_date = max(all_dates)
    current_week_start = (min_date - timedelta(days=min_date.weekday())).date()
    week_map = {}
    
    while True:
        week_end = current_week_start + timedelta(weeks=1, days=-1)
        if not week_map.get(current_week_start):
            week_map[current_week_start] = {'jobs': 0, 'interviews': 0}
        
        for job in jobs:
            date_str = job.get('date') or job.get('created_at', '')
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d').date()
                if current_week_start <= dt <= week_end:
                    week_map[current_week_start]['jobs'] += 1
            except ValueError:
                pass
        
        for interview in interviews:
            date_str = interview.get('date') or interview.get('created_at', '')
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d').date()
                if current_week_start <= dt <= week_end:
                    week_map[current_week_start]['interviews'] += 1
            except ValueError:
                pass
        
        if week_end >= max_date:
            break
        current_week_start = week_end + timedelta(days=1)
    
    return dict(sorted(week_map.items()))
