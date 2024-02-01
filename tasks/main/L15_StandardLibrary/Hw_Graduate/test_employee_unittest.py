import unittest

from employee import *


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp = Employee("Иван", "Иванович", "Иванов", 30, "начальник отдела", 50_000, 123456)

    def test_employee_full_name(self):
        """
        Тестирование метода full_name()
        """
        self.assertEquals(self.emp.full_name(), "Иванов Иван Иванович")

    def test_employee_birthday(self):
        """
        Тестирование метода birthday()
        """
        self.emp.birthday()
        self.assertEquals(self.emp.get_age(), 31)

    def test_employee_invalid_birthday(self):
        """
        Тестирование метода birthday() с превышением допустимого возраста
        """
        emp = Employee("Иван", "Иванович", "Иванов", 130, "начальник отдела", 50_000, 123456)
        with self.assertRaises(InvalidAgeError):
            emp.birthday()
        self.assertEquals(emp.get_age(), 130)

    def test_employee_raise_salary(self):
        """
        Тестирование метода raise_salary()
        """
        self.emp.raise_salary(10)
        self.assertEquals(self.emp.salary, 55000)

    def test_employee_str(self):
        """
        Тестирование метода __str__()
        """
        self.assertEquals(str(self.emp), "Иванов Иван Иванович id=123456")

    def test_employee_invalid_last_name_title(self):
        """
        Тестирование атрибута last_name
        """
        self.assertNotEquals(self.emp.last_name, "Иван")

    def test_init_employee_invalid_id(self):
        """
        Тестирование конструктора сотрудника с неправильным id
        """
        with self.assertRaises(InvalidIdError):
            Employee("Иван", "Иванович", "Иванов", 30, "начальник отдела", 50_000, 12345)

    def test_init_employee_invalid_position(self):
        """
        Тестирование конструктора сотрудника с неправильным наименованием должности: не строка
        """
        with self.assertRaises(InvalidTitleError):
            Employee("Иван", "Иванович", "Иванов", 30, 111, 50_000, 123456)

    def test_get_level(self):
        """
        Тестирование метода get_level(): Получить уровень доступа по идентификационному номеру сотрудника
        """
        self.assertEquals(self.emp.get_level(), 0)

    def test_get_salary(self):
        """
        Тестирование метода get_salary()
        """
        self.assertEquals(self.emp.get_salary(), 50_000)

    def test_get_age(self):
        """
        Тестирование метода get_age()
        """
        self.assertEquals(self.emp.get_age(), 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)
