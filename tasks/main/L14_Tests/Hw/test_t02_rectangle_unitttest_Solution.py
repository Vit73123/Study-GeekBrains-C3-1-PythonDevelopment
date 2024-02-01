# Возьмите код из прошлой задачи "Класс Rectangle".
#
# Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)
#
# Тесты:
#
# test_width: Тестирование инициализации ширины.
# Создайте прямоугольник с шириной 5 и убедитесь, что атрибут width корректно установлен на 5.
#
# test_height: Тестирование инициализации ширины и высоты.
# Создайте прямоугольник с шириной 3 и высотой 4 и убедитесь, что атрибут height корректно установлен на 4.
#
# test_perimeter: Тестирование вычисления периметра.
# Создайте прямоугольник с шириной 5 и вычислите его периметр. Убедитесь, что результат равен 20.
#
# test_area: Тестирование вычисления площади.
# Создайте прямоугольник с шириной 3 и высотой 4 и вычислите его площадь. Убедитесь, что результат равен 12.
#
# test_addition: Тестирование операции сложения.
# Создайте два прямоугольника: один с шириной 5, другой с шириной 3 и высотой 4.
# Выполните операцию сложения r1 + r2 и убедитесь, что полученный прямоугольник
# имеет правильные значения ширины и высоты (8 и 6.0 соответственно).
#
# Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.
#
# Запускать тесты не надо, автотест это сделает сам:
#
# unittest.main()
#
# На выходе после автоматической обрезки информации в тестах вы должны получить:
#
# FAILED (failures=1)

# Тест на сложение должен проверять ошибочный результат!
import unittest


class NegativeValueError(ValueError):
    pass


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

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self.width = width
        if height is None:
            self.height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
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


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.width, 5)

    def test_height(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.height, 4)

    def test_perimeter(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.perimeter(), 20)

    def test_area(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_addition(self):
        r1 = Rectangle(5)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 6.0)


if __name__ == "__main__":
    import unittest

    unittest.main(verbosity=4)
