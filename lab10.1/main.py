from datetime import datetime


def parse_time(time_str):
    # Парсимо час у форматі AM/PM
    return datetime.strptime(time_str, "%I:%M %p").time()


def min_meetings(meetings):
    # Сортуємо зустрічі за кінцевим часом
    meetings.sort(key=lambda x: x[1])

    # Ініціалізуємо змінні
    min_meetings_count = 0
    last_end_time = None

    # Проходимо по зустрічах
    for meeting in meetings:
        start, end = meeting

        # Перетворюємо рядок у часовий об'єкт
        start_time = parse_time(start)
        end_time = parse_time(end)

        # Якщо початок зустрічі після часу закінчення попередньої зустрічі,
        # то цю зустріч можна відвідати
        if last_end_time is None or start_time >= last_end_time:
            min_meetings_count += 1
            last_end_time = end_time

    return min_meetings_count


# Плановi зустрiчi
meetings = [
    ("10:00 AM", "11:00 AM"),
    ("11:30 AM", "12:30 PM"),
    ("1:00 PM", "2:00 PM"),
    ("12:00 PM", "1:00 PM"),
    ("2:30 PM", "3:30 PM")
]
print("Мінімальна кількість зустрічей:", min_meetings(meetings))
