# Создайте класс студента.
# 📌 Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию, выведите:
#
# ФИО должно состоять только из букв и начинаться с заглавной буквы
#
# 📌 Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
#
# Предмет {Название предмета} не найден
#
# 📌 Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:
#
# Оценка должна быть целым числом от 2 до 5
#
# Результат теста должен быть целым числом от 0 до 100
#
# 📌 Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
#

# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
#
# Математика,Физика,История,Литература
#

# Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:

# Атрибуты класса:
#
# name (str): ФИО студента
# subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов
# для каждого предмета в виде словаря.

# Магические методы (Dunder-методы):
#
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
# Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
#
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
# Убеждается, что name начинается с заглавной буквы и состоит только из букв.
#
# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
#
# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История

# Методы класса:
#
# load_subjects(self, subjects_file): Загружает предметы из файла CSV.
# Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
#
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
# Убеждается, что оценка является целым числом от 2 до 5.
#
# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
# Убеждается, что результат теста является целым числом от 0 до 100.
#
# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
#
# get_average_grade(self): Возвращает средний балл по всем предметам.

# Тест 1
#
# На входе:
#
# student = Student("Иван Иванов", "subjects.csv")
#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
#
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
#
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
#
# print(student)
#
# На выходе:
#
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История
#
# Тест 2
#
# student = Student("123 Иван", "subjects.csv")
#
# Tect 3
#
# student = Student("Петров Петр", "subjects.csv")
#
# student.add_grade("Физика", 6)
#
# Тест 4
#
# student = Student("Сидоров Сидор", "subjects.csv")
#
# average_history_score = student.get_average_test_score("Биология")
#
# Ожидаемый ответ:
#
# ValueError: Предмет Биология не найден
#
# Ваш ответ:
#
# KeyError: 'Биология'
import csv

class Student:
    name = None
    subjects = {}

    def __init__(self, name: str, subjects_file: str):
        '''Принимает имя студента и файл с предметами и их результатами'''
        self.name = name
        self.load_subjects(subjects_file)

    def __getattr__(self, name: str):
        '''Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам'''
        if not name in self.subjects.keys():
            raise ValueError(f"Предмет {name} не найден")
        return self.subjects[name]

    def __setattr__(self, name: str, value: str):
        '''Проверяет установку атрибута name

         Убеждается, что name начинается с заглавной буквы и состоит только из букв'''
        if name == 'name':
            if not (isinstance(value, str) and ''.join(value.split()).isalpha() and value.istitle()):
                raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')
            return object.__setattr__(self, name, value)

    def __str__(self):
        '''Возвращает строковое представление студента, включая имя и список предметов.

        Студент: Иван Иванов
        Предметы: Математика, История'''
        subjects = ', '.join([key for key, value in self.subjects.items()
                              if value['grade'] or value['test_score']])
        return f'Студент: {self.name}\n' \
               f'Предметы: {subjects}'

    def load_subjects(self, subjects_file):
        '''Загружает предметы из файла CSV

        Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects'''
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, quoting=csv.QUOTE_MINIMAL)
            for field in reader.fieldnames:
                self.subjects[field] = \
                    {
                        'grade': [],
                        'test_score': []
                    }

    def add_grade(self, subject, grade):
        '''Добавляет оценку по заданному предмету

        Убеждается, что оценка является целым числом от 2 до 5'''
        if not 2 <= grade <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        self.subjects[subject]['grade'].append(grade)

    def add_test_score(self, subject, test_score):
        '''Добавляет результат теста по заданному предмету

        Убеждается, что результат теста является целым числом от 0 до 100'''
        if not 0 <= test_score <= 100:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        self.subjects[subject]['test_score'].append(test_score)

    def get_average_grade(self):
        '''Возвращает средний балл по всем предметам'''
        grades = [grade for value in self.subjects.values() for grade in value['grade']]
        return sum(grades) / len(grades)

    def get_average_test_score(self, subject):
        '''Возвращает средний балл по тестам для заданного предмета'''
        test_score = getattr(self, subject)['test_score']
        return sum(test_score) / len(test_score)


if __name__ == '__main__':
    # student = Student("Иван Иванов", "subjects.csv")
    #
    # student.add_grade("Математика", 4)
    # student.add_test_score("Математика", 85)
    #
    # student.add_grade("История", 5)
    # student.add_test_score("История", 92)
    #
    # average_grade = student.get_average_grade()
    # print(f"Средний балл: {average_grade}")
    #
    # average_test_score = student.get_average_test_score("Математика")
    # print(f"Средний результат по тестам по математике: {average_test_score}")
    #
    # print(student)

    student = Student("Сидоров Сидор", "subjects.csv")

    average_history_score = student.get_average_test_score("Биология")