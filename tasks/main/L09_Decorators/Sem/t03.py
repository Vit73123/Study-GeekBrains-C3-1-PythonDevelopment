# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.
from typing import Callable
from typing import Any
import json
import os

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

@save_args
def my_func(*args, **kwargs) -> int:
    return 1

if __name__ == '__main__':
    my_func(1, 2, 3, arg1=11, arg2=21)
    my_func(2, 3, 4, arg1=12, arg2=22)
    my_func(3, 4, 5, arg1=13, arg2=23)
    my_func(4, 5, 6, arg1=14, arg2=24)
    my_func(5, 6, 7, arg1=15, arg2=25)