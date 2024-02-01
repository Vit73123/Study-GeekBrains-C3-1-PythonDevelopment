# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая)
# Имя (строка, не пустая)
# Отчество (строка, не пустая)
# Возраст (целое положительное число)
#
# Сотрудники имеют также уникальный идентификационный номер (ID), который
# должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст).
#
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError,
# если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр
# в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.

# Тест 1

# person = Person("", "John", "Doe", 30)

# Ожидаемый ответ:
#
# __main__.InvalidNameError: Invalid name: . Name should be a non-empty string.
#
# Ваш ответ:
#
# __main__.InvalidNameError: Invalid name: . Text should be a non-empty string.

# Тест 2

# person = Person("Alice", "Smith", "Johnson", -5)

# Тест 3

# Ожидаемый ответ:
#
# __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.
#
# Ваш ответ:
#
# __main__.InvalidIdError: Invalid ID: 12345. ID should be a positive six-digit integer.

# Тест 4

# person = Person("Alice", "Smith", "Johnson", 25)
# print(person.get_age())

# Ожидаемый ответ:
#
# 25
#
# Ошибка:
#
# Traceback (most recent call last):
#   File "IBTFKALGM55TWG8E4DPA.py", line 134, in <module>
#     print(person.get_age())
# AttributeError: 'Person' object has no attribute 'get_age'
class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid name: {self.name}. Name should be a non-empty string."


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age}. Age should be a positive integer."


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999."


class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        if not isinstance(value, str) or value == '':
            raise InvalidNameError(value)


class Age:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: int):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError(value)


class Id:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: int):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not isinstance(value, int) or value < 100_000 or value >= 1_000_000:
            raise InvalidIdError(value)


class Person:

    first_name = Name()
    second_name = Name()
    last_name = Name()
    age = Age()

    def __init__(self,
                 first_name,
                 second_name,
                 last_name,
                 age):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.last_name} {self.age}'

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):

    id = Id()

    def __init__(self,
                 first_name: str,
                 second_name: str,
                 last_name: str,
                 age: int,
                 id: int):
        super().__init__(first_name, second_name, last_name, age)
        self.id = id
        # Подсчёт суммы цифр числа
        self.level = sum(map(int, str(self.id))) % 7

    def get_level(self) -> int:
        return self.level


if __name__ == '__main__':
    # person = Person('Vladislav', 'Ivanovich', 'Isaev', 25)
    # print(person)
    # person.birthday()
    # print(person.age)
    # print(person)
    # person.age = 3
    # print(person.age)

    # e = Employee('Vladislav', 'Ivanovich', '', -25, 111)
    # print(e.id)
    # print(e.level)
    #
    # e = Employee('Vladislav', 'Ivanovich', 'Isaev', 25, '111999')
    # print(e.id)
    # print(e.level)
    # print(e.age())

    # Тесты

    # person = Person("", "John", "Doe", 30)
    # print(person)

    # person = Person("Alice", "Smith", "Johnson", -5)

    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)

    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())
