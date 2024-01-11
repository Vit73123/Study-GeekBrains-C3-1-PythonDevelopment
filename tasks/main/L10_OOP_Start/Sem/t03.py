# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы:
# birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. # на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Person:
    def __init__(self,
                 first_name,
                 second_name,
                 last_name,
                 age):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.last_name} {self.__age}'

    def age(self):
        return self.__age

if __name__ == '__main__':
    person = Person('Vladislav', 'Ivanovich', 'Isaev', 25)
    person.birthday()
    print(person.age())
    print(person)
    person.__age = 3
    print(person.age())