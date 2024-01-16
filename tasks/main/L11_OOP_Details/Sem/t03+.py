# 📌 Добавьте к задачам 1 и 2 строки документации для классов.
from datetime import datetime


class MyStr(str):
    # Doc Test - '>>>' в строке документацмм
    # Создаёт исполняемый кот, который можно запустить из документации
    # для того, чтобы продемонстрировать, как можно взаимодействовать с данным классом
    '''
    Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания (time.time).
    >>> MyStr('text', 'Vladislav')
    '''
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.datetime.now()
        return instance


class Archive:
    '''
    Создайте класс Архив, который хранит пару свойств.
    Например, число и строку.
    При новом экземпляре класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
    list-архивы также являются свойствами экземпляра
    '''
    instance = None

    def __new__(cls, text, number):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_num = []
        else:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_num.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number