# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi

class Circle:
    _pi = pi

    def __init__(self, r: float):
        self.r = r

    def length(self):
        return 2 * Circle._pi * self.r

    def square(self):
        return Circle._pi * self.r ** 2

if __name__ == '__main__':
    r = 1
    print(f'{Circle(r).length():>7.3f}{Circle(r).square():>7.3f}')
    r = 2
    print(f'{Circle(r).length():>7.3f}{Circle(r).square():>7.3f}')
    r = 3
    print(f'{Circle(r).length():>7.3f}{Circle(r).square():>7.3f}')
