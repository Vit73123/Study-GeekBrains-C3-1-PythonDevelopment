# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
from decimal import Decimal, getcontext
from math import pi

PREC = 42

diam = Decimal(input('Введите диаметр: '))
getcontext().prec = PREC
pi_ = Decimal(pi)
print("Площадь круга:", pi_ * diam ** 2 / 4)
print("Длина окружности:", pi_ * diam)
