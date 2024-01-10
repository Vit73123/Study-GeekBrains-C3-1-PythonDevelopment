# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

# *************
# * Декоратор *
# *************

from random import randint
from typing import Callable

MIN_NUM = 1
MAX_NUM = 100
MIN_ATTEMPTS = 1
MAX_ATTEMPTS = 10


def game(func: Callable) -> Callable[[int, int], bool]:
    def wrapper(num: int, attempts: int) -> bool:
        print(f'Исходные данные   : Загаданное число {num:>3} Число попыток {attempts:>3}', end='')
        if not (MIN_NUM <= num <= MAX_NUM and MIN_ATTEMPTS <= attempts <= MAX_ATTEMPTS):
            num = randint(MIN_NUM, MAX_NUM)
            attempts = randint(MIN_ATTEMPTS, MAX_ATTEMPTS)
            print(': Некорректные данные')
            print(f'Фактические данные: Загаданное число {num:>3} Число попыток {attempts:>3}')
        print()
        return func(num, attempts)

    return wrapper


@game
def guess_num(num: int, attempts: int) -> bool:
    guess = None
    for i in range(attempts):
        guess = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
        if guess < num:
            print("Ваше число меньше")
        elif guess > num:
            print("Ваше число больше")
        else:
            print("Вы угадали!")
            break
    return guess == num


if __name__ == '__main__':
    guess_num(105, 11)
    # guess_num(53, 3)
