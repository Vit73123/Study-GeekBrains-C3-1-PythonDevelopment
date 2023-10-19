a: int = 42
b: float = float(input('Введи число: '))
a = a / b

# PEP-8! Код до и после функции отделяется двумя пустыми строками.

def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res

print(my_func([2, 5.5, 15, 8.0, 13.74]))

# | - не поддерживается в Python до v10

a: int | float = 42
b: float = float(input('Введи число: '))
a = a / b