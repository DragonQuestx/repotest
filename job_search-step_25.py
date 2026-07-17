# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: JobSearch
def parse_date(date_str):
    """Парсит дату в формате 'ДД.ММ' или 'ГГГГ-ММ-ДД'. Возвращает datetime.date или None."""
    if not date_str or not isinstance(date_str, str):
        return None
    try:
        for fmt in ("%d.%m", "%Y-%m-%d"):
            d = datetime.strptime(date_str[:len(fmt)], fmt)
            return d.date()
        raise ValueError("Неизвестный формат даты")
    except (ValueError, TypeError):
        return None

def validate_date_input(date_str, field_name="Дата"):
    """Валидация ввода: возвращает отформатированную строку или сообщение об ошибке."""
    if not date_str or not isinstance(date_str, str) or len(date_str.strip()) == 0:
        return f"Ошибка: {field_name} не может быть пустой."
    parsed = parse_date(date_str.strip())
    if parsed is None:
        return f"Ошибка: '{date_str}' — неверный формат даты. Используйте ДД.ММ или ГГГГ-ММ-ДД."
    return date_str.strip()[:10]  # нормализация до DD.MM

def safe_int(value, default=None):
    """Конвертирует в int с понятным сообщением при ошибке."""
    if value is None or (isinstance(value, str) and len(value.strip()) == 0):
        return default
    try:
        return int(str(value).strip())
    except ValueError:
        return default

def safe_float(value, default=None):
    """Конвертирует в float с понятным сообщением при ошибке."""
    if value is None or (isinstance(value, str) and len(value.strip()) == 0):
        return default
    try:
        return float(str(value).strip())
    except ValueError:
        return default

def handle_errors(func):
    """Декоратор для обёртывания функций в блоки try/except с понятными сообщениями."""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, Exception):
                return f"Ошибка: {result}"
            return result
        except (ValueError, TypeError, KeyError) as e:
            return f"Ошибка ввода: {e}"
        except Exception as e:
            return f"Неизвестная ошибка: {type(e).__name__}: {str(e)[:120]}"
    wrapper.__name__ = func.__name__
    return wrapper
