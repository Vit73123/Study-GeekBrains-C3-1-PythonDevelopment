# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.
MIN_LEN = 1
MAX_LEN = 10


class Side:
    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value <= 0 or value < self.min_len or value > self.max_len:
            raise ValueError


class Rectangle:
    height = Side(MIN_LEN, MAX_LEN)
    width = Side(MIN_LEN, MAX_LEN)

    def __init__(self, height: float, width: float = None):
        self._height = height
        self._width = width if width else height

    def perimeter(self):
        return 2 * (self._height + self._width)

    def area(self):
        return self._height * self._width

    # @property
    # def height(self):
    #     return self._height
    #
    # @height.setter
    # def height(self, value):
    #     if value <= 0:
    #         raise ValueError
    #     self._height = value
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     if value <= 0:
    #         raise ValueError
    #     self._width = value

    def __add__(self, other: 'Rectangle'):
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self._height + other._height
        new_b = new_perimeter / 2 - new_a
        if new_a <= 0 or new_b <= 0:
            raise ValueError
        return Rectangle(new_a, new_b)

    def __sub__(self, other: 'Rectangle'):
        new_perimeter = self.perimeter() - other.perimeter()
        new_a = self._height - other._height
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
        return f'Rectangle({self._height}, {self._width})'


if __name__ == '__main__':
    r1 = Rectangle(2, 4)
    print(r1._width)
    r1.width = 5
    print(r1._width)
    r1.width = -5
    print(r1._width)
    r1.width = 11
    print(r1._width)
