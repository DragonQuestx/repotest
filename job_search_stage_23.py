# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: JobSearch
def print_table(headers, rows):
    """Простая отформатированная таблица для консоли."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = max(widths[i], len(str(val)))
            widths[i] = w
    lines = ['| ' + ' | '.join(f'{h:<{w}}' for h, w in zip(headers, widths)) + ' |']
    sep = '| ' + ' | '.join('-' * w for w in widths) + ' |'
    for row in rows:
        lines.append('| ' + ' | '.join(str(v)[:w] for v, w in zip(row, widths)) + ' |')
    print(sep)
    print('\n'.join(lines))
