# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, a: float, b: float = None):
        self.a = a
        self.b = b if b else a

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __add__(self, other: 'Rectangle'):
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a + other.a
        new_b = new_perimeter / 2 - new_a
        if new_a <= 0 or new_b <= 0:
            raise ValueError
        return Rectangle(new_a, new_b)

    def __sub__(self, other: 'Rectangle'):
        new_perimeter = self.perimeter() - other.perimeter()
        new_a = self.a - other.a
        new_b = new_perimeter / 2 - new_a
        if new_a <= 0 or new_b <= 0:
            raise ValueError
        return Rectangle(new_a, new_b)

    def __eq__(self, other: ' Rectangle'):
        return self.area() == other.area()

    def __gt__(self, other: 'Rectangle'):
        return self.area() > other.area()

    def __lt__(self, other: 'Rectangle'):
        return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'


if __name__ == '__main__':
    r1 = Rectangle(2, 2)
    r2 = Rectangle(4, 2)
    print(r1 < r2)
    print(r1 > r2)
    print(r1 == r2)
    print(r1 != r2)
    print(r1 + r2)
    print(r2 - r1)    # ValueError: new_b = 0
