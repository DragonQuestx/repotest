# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: JobSearch
def add_reminders():
    reminders = []
    
    def create_reminder(text, date=None):
        if date is None:
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        
        reminder = {
            "text": text,
            "date": date,
            "completed": False
        }
        reminders.append(reminder)
        return reminder
    
    def get_reminders():
        return reminders
    
    def complete_reminder(index):
        if 0 <= index < len(reminders):
            reminders[index]["completed"] = True
            print(f"✓ Напоминание '{reminders[index]['text']}' выполнено")
    
    def show_reminders():
        if not reminders:
            print("Нет напоминаний. Добавьте первое!")
            return
        
        print("\n📋 Ваши напоминания:")
        for i, r in enumerate(reminders):
            status = "✓" if r["completed"] else "○"
            print(f"{status} [{i}] {r['text']} (до: {r['date']})")

    print("🔔 Система напоминаний добавлена!")
    print("\nДоступные функции:")
    print(create_reminder)
    print(get_reminders)
    print(complete_reminder)
    print(show_reminders)

add_reminders()
