# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: JobSearch
class JobSearchState:
    def __init__(self):
        self.jobs = []
        self.responses = []
        self.interviews = []
        self.notes = {}

def add_job(job_data, state):
    job_id = len(state.jobs) + 1
    new_job = {"id": job_id, **job_data}
    state.jobs.append(new_job)
    return job_id

def submit_response(response_data, state):
    response_id = len(state.responses) + 1
    new_response = {"id": response_id, **response_data}
    state.responses.append(new_response)
    return response_id

def schedule_interview(interview_data, state):
    interview_id = len(state.interviews) + 1
    new_interview = {"id": interview_id, **interview_data}
    state.interviews.append(new_interview)
    return interview_id

def add_note(note_text, note_title, state):
    if not note_title:
        note_title = f"Note {len(state.notes)}"
    state.notes[note_title] = note_text
    return len(state.notes)
