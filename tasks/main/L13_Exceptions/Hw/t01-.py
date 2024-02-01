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

# -: Тип исключения должен быть не Exception:
# ValueError
class NegativeValueError(Exception):
    def __init__(self, name: str, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} должна быть положительной, а не {self.value}"


class Size:
    def __init__(self, name: str):
        self.name = name

    def __set_name__(self, owner, name: str):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: [int, float]):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: [int, float]):
        if not ((isinstance(value, int) or isinstance(value, float)) and value > 0):
            raise NegativeValueError(self.name, value)


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    width = Size("Ширина")
    height = Size("Высота")

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    # r = Rectangle(-2)
    # r = Rectangle(5, -3)
    #
    # r = Rectangle(4, 4)
    # r.width = -3
    #
    r = Rectangle(4, 4)
    r.height = -3