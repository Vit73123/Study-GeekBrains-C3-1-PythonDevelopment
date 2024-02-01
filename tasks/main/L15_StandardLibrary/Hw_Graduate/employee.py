import decimal
import logging
from logger import init_logger

LOGGER_LEVEL = logging.DEBUG
LOGGER_NAME = "employee"
LOGGER_FILE_ACCESS = "a"
LOGGER_ENCODING = "windows-1251"  # Actual if Python v3.9+

init_logger(LOGGER_NAME,
            LOGGER_LEVEL,
            LOGGER_FILE_ACCESS,
            LOGGER_ENCODING)
log = logging.getLogger(LOGGER_NAME)


class InvalidTitleError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Неправильное имя: {self.name}. Имя должно быть непустой строкой"


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Неправильный возраст: {self.age}. Возраст должен быть положительным целым числом не больше 130 лет"


class InvalidSalaryError(ValueError):
    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Неправильная зарплата: {self.salary}. Зарплата должна быть положительным числом"


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        msg = f"Неправильный id: {self.id}. Id должен быть 6-значным целым числом от 100000 до 999999"
        return msg


class Title:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate(value)
        setattr(instance, self.param_name, value.title())

    def validate(self, value: str):
        if not isinstance(value, str) or value == '':
            raise InvalidTitleError(value)


class Age:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: int):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not isinstance(value, int) or value <= 0 or value > 130:
            raise InvalidAgeError(value)


class Salary:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner) -> decimal.Decimal:
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: float):
        value = decimal.Decimal(value)
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: decimal.Decimal):
        if value <= 0:
            raise InvalidSalaryError(value)


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
    """
    Обычные люди организации

    Атрибуты:
    first_name: Имя
    second_name: Отчество
    last_name: Фамилия
    age: возраст
    """
    first_name = Title()
    second_name = Title()
    last_name = Title()
    age = Age()

    def __init__(self,
                 first_name,
                 second_name,
                 last_name,
                 age):
        log.debug(f"Person | init() | "
                  f"first_name={first_name} "
                  f"second_name={second_name} "
                  f"last_name={last_name} "
                  f"age={age}")
        try:
            self.first_name = first_name
            self.second_name = second_name
            self.last_name = last_name
            self.age = age
        except ValueError as e:
            log.error(f"Person | init() | {e}")
            raise e
        log.info(f"Person | init() | "
                 f"first_name={first_name} "
                 f"second_name={second_name} "
                 f"last_name={last_name} "
                 f"age={age} done")

    def full_name(self):
        """
        Получить ФИО
        """
        log.debug(f"Person | full_name() | {self}")
        return f'{self.last_name} {self.first_name} {self.second_name}'

    def birthday(self):
        """
        Увеличить год рождения на 1
        """
        log.debug(f"Person | birthday() | {self} | age={self.age}")
        try:
            self.age += 1
        except InvalidAgeError as e:
            log.error(f"Person | birthday() | {e}")
            raise e
        log.info(f"Person | birthday() | {self} | age={self.age} done")

    def get_age(self):
        """
        Получить возраст
        """
        log.debug(f"Person | get_age() | {self} | age={self.age}")
        return self.age

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'


class Employee(Person):
    """
    Сотрудники организации

    Атрибуты:
    first_name: Имя
    second_name: Отчество
    last_name: Фамилия
    age: возраст
    position: должность
    salary: зарплата
    level: уровень доступа
    id: идентификационный номер сотрудника в организации
    """
    id = Id()
    position = Title()
    salary = Salary()

    def __init__(self,
                 first_name: str,
                 second_name: str,
                 last_name: str,
                 age: int,
                 position: str,
                 salary: float,
                 id: int):
        log.debug(f"Employee | init() | "
                  f"first_name={first_name} "
                  f"second_name={second_name} "
                  f"last_name={last_name} "
                  f"age={age} "
                  f"position={position} "
                  f"salary={salary:.2f} "
                  f"id={id}")
        super().__init__(first_name,
                         second_name,
                         last_name,
                         age)
        try:
            self.position = position
            self.salary = decimal.Decimal(salary)
            self.id = id
        except ValueError as e:
            log.error(f"Employee | init() | {e}")
            raise e
        # Подсчёт суммы цифр числа
        self.level = sum(map(int, str(self.id))) % 7
        log.info(f"Employee | init() | "
                 f"first_name={first_name} "
                 f"second_name={second_name} "
                 f"last_name={last_name} "
                 f"age={age} "
                 f"position={position} "
                 f"salary={salary:.2f} "
                 f"id={id} done")

    def get_level(self) -> int:
        """
        Получить уровень доступа
        """
        log.debug(f"Employee | get_level() | {self} | level={self.level}")
        return self.level

    def get_salary(self) -> decimal.Decimal:
        """
        Получить заработную плату
        """
        log.debug(f"Employee | get_salary() | {self} | salary={self.salary:.2f}")
        return self.salary

    def raise_salary(self, percent: float):
        """
        Увеличить заработную плату на заданный %
        """
        log.debug(f"Employee | raise_salary() | {self} | salary={self.salary:.2f} percent={percent} ")
        percent = decimal.Decimal(percent)
        self.salary *= (1 + percent / 100)
        log.info(f"Employee | raise_salary() | {self} | salary={self.salary:.2f} percent={percent} done")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name} id={self.id}"


if __name__ == '__main__':
    try:
        employee = Employee("Иван", "Иванович", "Иванов", 30, "инженер", 50_000, 123456)
        employee.raise_salary(10)
        employee.birthday()
        print(employee)

        # Неправильное имя: . Имя должно быть непустой строкой
        try:
            employee = Employee("", "Иванович", "Иванов", 30, "инженер", 50_000, 123456)
            print(employee)
        except InvalidTitleError as e:
            print(e)

        # Неправильный возраст: 131. Возраст должен быть положительным целым числом не больше 130 лет
        try:
            employee = Employee("Иван", "Иванович", "Иванов", 131, "инженер", 50_000, 123456)
        except InvalidAgeError as e:
            print(e)

        # Неправильный возраст: 131. Возраст должен быть положительным целым числом не больше 130 лет
        try:
            employee = Employee("Иван", "Иванович", "Иванов", 130, "инженер", 50_000, 123456)
            employee.birthday()
        except InvalidAgeError as e:
            print(e)

        # Неправильный id: 12345. Id должен быть 6-значным целым числом от 100000 до 999999
        try:
            employee = Employee("Иван", "Иванович", "Иванов", 30, "инженер", 50_000, 12345)
        except InvalidIdError as e:
            print(e)

    except RuntimeError as e:
        log.critical(e)
