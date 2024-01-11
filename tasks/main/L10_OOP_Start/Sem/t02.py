# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, *args: float):
        if len(args) == 1:
            self.a = self.b = 1
        else:
            self.a, self.b = args

    def length(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

if __name__ == '__main__':
    a = 1
    print(f'{Rectangle(a).length():>7.2f}{Rectangle(a).square():>7.2f}')
    a = 2
    print(f'{Rectangle(a).length():>7.2f}{Rectangle(a).square():>7.2f}')
    a = 1
    b = 2
    print(f'{Rectangle(a, b).length():>7.2f}{Rectangle(a, b).square():>7.2f}')
    a = 2
    b = 3
    print(f'{Rectangle(a, b).length():>7.2f}{Rectangle(a, b).square():>7.2f}')
