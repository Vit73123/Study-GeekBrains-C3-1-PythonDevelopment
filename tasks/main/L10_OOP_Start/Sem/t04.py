# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
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


class Employee(Person):
    def __init__(self,
                 first_name: str,
                 second_name: str,
                 last_name: str,
                 age: int,
                 id: str):
        super().__init__(first_name, second_name, last_name, age)
        self.id = id if len(id) == 6 else '000000'
        # Подсчёт суммы цифр числа
        self.level = sum(map(int, self.id)) % 7

if __name__ == '__main__':
    person = Person('Vladislav', 'Ivanovich', 'Isaev', 25)
    person.birthday()
    print(person.age())
    print(person)
    person.__age = 3
    print(person.age())

    e = Employee('Vladislav', 'Ivanovich', 'Isaev', 25, '111')
    print(e.id)
    print(e.level)

    e = Employee('Vladislav', 'Ivanovich', 'Isaev', 25, '111999')
    print(e.id)
    print(e.level)
    print(e.age())