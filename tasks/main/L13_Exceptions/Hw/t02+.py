# Допишите в вашу задачу Archive обработку исключений.
#
# Добавьте в ваш код исключение InvalidTextError, которjе будет вызываться, когда текст не является
# строкой или является пустой строкой.
#
# Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
#
# И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом
# с плавающей запятой.
#
# Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'

# Тест 1

# archive_instance = Archive("Sample text", 42.5)
# print(archive_instance)

# Тест 2

# invalid_archive_instance = Archive("", -5)
# print(invalid_archive_instance)

# Тест 3

# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)
from typing import Union


class InvalidTextError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"Invalid text: {self.text}. Text should be a non-empty string."


class InvalidNumberError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Invalid number: {self.number}. Number should be a positive integer or float."


class Text:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: str):
        if not isinstance(value, str) or value == '':
            raise InvalidTextError(value)


class Number:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    # +: Задать тип данных
    # var: Union[]
    def __set__(self, instance, value: Union[int, float]):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: Union[int, float]):
        if not (isinstance(value, int) or isinstance(value, float)) or value <= 0:
            raise InvalidNumberError(value)


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    text = Text()
    number = Number()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == "__main__":
    print(Archive('', 1))