# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

# *************
# * Замыкание *
# *************

from typing import Callable

MIN_NUM = 1
MAX_NUM = 100
MIN_COUNT = 1
MAX_COUNT = 10

def game(num: int, count: int) -> Callable[[], bool]:
    def guess_num() -> bool:
        # nonlocal count
        # nonlocal num
        guess = None
        for i in range(count):
            guess = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))
            if guess < num:
                print("Ваше число меньше")
            elif guess > num:
                print("Ваше число больше")
            else:
                print("Вы угадали!")
                break
        return guess == num
    return guess_num

if __name__ == '__main__':
    game(53, 3)()