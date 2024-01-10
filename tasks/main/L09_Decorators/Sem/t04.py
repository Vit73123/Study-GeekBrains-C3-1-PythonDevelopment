# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.
from typing import Any
from typing import Callable
from random import randint

def count(num: int) -> Callable[[], Any]:
    def deco(func: Callable) -> Callable[[], Any]:
        def wrapper(*args, **kwargs) -> Any:
            result = []
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result

        return wrapper
    return deco


@count(5)
def any_func(*args, **kwargs):
    return randint(1, 100)

if __name__ == '__main__':
    print(any_func(1))