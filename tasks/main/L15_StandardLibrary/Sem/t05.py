# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.
import sys
from datetime import datetime

WEEKDAYS = {
    "понедельник": 1,
    "вторник": 2,
    "среда": 3,
    "четверг": 4,
    "пятница": 5,
    "суббота": 6,
    "воскресенье": 7
}

MONTHS = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12
}

def correct_date(text: str) -> datetime:
    week_count, weekday, month = text.split()
    week_count = int(week_count[0])
    weekday = int(WEEKDAYS[weekday])
    month = int(MONTHS[month])
    # print(week_count, weekday, month)

    weeks_passed = 0
    for day in range(1, 31):
        temp_date = datetime (
            datetime.now().year,
            month,
            day
        )
        if temp_date.weekday() + 1 == weekday:
            weeks_passed += 1
            if weeks_passed == week_count:
                return temp_date
    raise ValueError(f"Такой даты не существует: '{text}'")



if __name__ == "__main__":
    # print(correct_date("1-й четверг ноября"))
    # print(correct_date("3-я среда мая"))
    # print(correct_date("5-й четверг января"))

    path, date, *_ = sys.argv
    print(correct_date(date))