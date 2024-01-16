# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста и для пользователя.
from datetime import datetime


class MyStr(str):
    # Doc Test - '>>>' в строке документацмм
    # Создаёт исполняемый кот, который можно запустить из документации
    # для того, чтобы продемонстрировать, как можно взаимодействовать с данным классом
    '''
    Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания (time.time).
    # >>> MyStr('text', 'Vladislav')
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

    def __repr__(self):
        return f'Archive({self.text}, {self.number})'

    def __str__(self):
        return f'{self.text = } {self.number = }'


if __name__ == '__main__':
    a1 = Archive('fakfkaf', 12)
    print(a1.old_text, a1.old_num)
    a2 = Archive('jagnagj', 111)
    print(a2.old_text, a2.old_num)
    print(a1.old_text, a1.old_num)

    print()

    print(a1)
    print(a2)
    print(repr(a1))
    print(repr(a2))

