# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.
#
# Пример использования
#
# На входе:
#
# date_to_prove = 15.4.2023
#
# На выходе:
#
# True
#
# На входе:
#
# date_to_prove = 31.6.2022
#
# На выходе:
#
# False

__DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def is_date_valid(date: str) -> bool:
    day, month, year = [int(s) for s in date.split('.')]
    return (1 <= year <= 9999
        and 1 <= month <= 12
        and __day_valid(day, month, year))


def __day_valid(day, month, year) -> bool:
    if __is_leap_year(year) and month == 2:
        return 1 <= day <= 29
    return 1 <= day <= __DAYS_IN_MONTH[month]


def __is_leap_year(year) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if __name__ == '__main__':
    # date_to_prove = '15.4.2023'
    # date_to_prove = '31.6.2022'
    print(is_date_valid(date_to_prove))