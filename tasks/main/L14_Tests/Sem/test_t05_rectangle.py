# 📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.
import unittest
from L13_Hw_t01_Solution_rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(3)
        self.r2 = Rectangle(3)


    def test_create_one_side(self):
        self.assertIsNotNone(self.r1.width,
                             f"Проверьте инициализацию ширины, если передана только высота")
        self.assertEquals(self.r1.width, 3)

    def test_create_negative_side(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -3)

    def test_sum(self):
        self.assertIsInstance(self.r1 + self.r2, Rectangle,
                              f"Проверьте, что результат сложения Rectangle")

if __name__ == "__main__":
    unittest.main(verbosity=4)
