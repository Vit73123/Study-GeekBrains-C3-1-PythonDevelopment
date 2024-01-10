# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.
from typing import Callable
from typing import Any
import json
import os
from random import randint

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


def save_args(func: Callable) -> Callable[[], Any]:
    file_name = f'{func.__name__}.json'
    data = []
    if file_name in os.listdir(os.curdir):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal file_name
        result = func(*args, **kwargs)
        data.append({'args': args, **kwargs, 'result': result})
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    return wrapper


def count(num: int) -> Callable[[], Any]:
    def deco(func: Callable) -> Callable[[], Any]:
        def wrapper(*args, **kwargs) -> Any:
            result = []
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result

        return wrapper
    return deco


@count(3)
@save_args
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
    guess_num(3, 4)