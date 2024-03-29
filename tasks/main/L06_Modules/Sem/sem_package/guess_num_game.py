# Задание 2
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# 📌 Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# 📌 Функция выводит подсказки “больше” и “меньше”.
# 📌 Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Задание 3
# 📌 Улучшаем задачу 2.
# 📌 Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# 📌 Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# 📌 Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv


__all__ = ['guess_num_game']


def guess_num_game(start: int, end: int, attempts: int) -> bool:
    '''
    Принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
    Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
    Выводит подсказки “больше” и “меньше”.
    Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

    :param start:
    :param end:
    :param attempts:
    :return:
    '''
    num = randint(start, end)
    for i in range(attempts):
        ask_num = int(input(f"Угадайте число от {start} до {end} : "))
        if ask_num == num:
            return True
        elif ask_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")
    else:
        print("Вы не угадали!")
    return False


if __name__ == "__main__":
    # start, end, attempts = [int(num) for num in argv[1:4]]
    _, start, end, attempts = argv
    start = int(start)
    end = int(end)
    attempts = int(attempts)
    print(guess_num_game(start, end, attempts))
