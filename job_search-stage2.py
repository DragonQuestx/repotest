# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: JobSearch
class JobEntry:
    def __init__(self, title, company, link, status='new', notes='', date=None):
        self.title = title
        self.company = company
        self.link = link
        self.status = status
        self.notes = notes
        self.date = date or datetime.now()

    def validate(self):
        errors = []
        if not self.title.strip():
            errors.append("Заголовок вакансии не может быть пустым.")
        if not self.company.strip():
            errors.append("Название компании не может быть пустым.")
        if not self.link or not self.link.startswith(('http://', 'https://')):
            errors.append("Ссылка должна быть валидным URL (начинаться с http:// или https://).")
        if self.status not in ('new', 'applied', 'interview', 'rejected', 'hired'):
            errors.append(f"Неверный статус. Допустимые: new, applied, interview, rejected, hired.")
        return errors

    def __str__(self):
        return f"[{self.status.upper()}] {self.title} @ {self.company}"
