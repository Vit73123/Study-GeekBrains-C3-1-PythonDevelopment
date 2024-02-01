# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
# которое выбрасывается при некорректных значениях ширины и высоты, как при создании объекта,
# так и при установке их через сеттеры.
#
# Тест 1
#
# Вход:
#
# r = Rectangle(-2)
#
# Ожидаемый ответ:
#
# __main__.NegativeValueError: Ширина должна быть положительной, а не -2
#
# Ваш ответ:
#
# __main__.NegativeValueError

# Тест 2

# Вход:

# r = Rectangle(5, -3)

# Ожидаемый ответ:
#
# __main__.NegativeValueError: Высота должна быть положительной, а не -3
#
# Ваш ответ:
#
# __main__.NegativeValueError

# Тест 3

# Вход:

# r = Rectangle(4, 4)
# r.width = -3

# Ожидаемый ответ:
#
# __main__.NegativeValueError: Ширина должна быть положительной, а не -3
#
# Ваш ответ:
#
# __main__.NegativeValueError

# Тест 4

# Вход:

# r = Rectangle(4, 4)
# r.height = -3

# Ожидаемый ответ:
#
# __main__.NegativeValueError: Высота должна быть положительной, а не -3
#
# Ваш ответ:
#
# __main__.NegativeValueError

# +: Тип исключений для неправильных атрибутов (не Exception)
# ValueError
class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    # +: @property
    @property
    def width(self):
        return self._width

    # +: @width.setter
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


if __name__ == "__main__":
    # r = Rectangle(-2)
    # r = Rectangle(5, -3)
    #
    # r = Rectangle(4, 4)
    # r.width = -3
    #
    r = Rectangle(4, 4)
    r.height = -3