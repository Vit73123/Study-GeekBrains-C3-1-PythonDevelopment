import logging
from logger import init_logger

LOGGER_LEVEL = logging.DEBUG
LOGGER_NAME = "student"
LOGGER_FILE_ACCESS = "w+"
LOGGER_ENCODING = "windows-1251"  # Actual if Python v3.9+

init_logger(LOGGER_NAME,
            LOGGER_LEVEL,
            LOGGER_FILE_ACCESS,
            LOGGER_ENCODING)
log = logging.getLogger(LOGGER_NAME)

import csv


class InvalidNameError(ValueError):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Неправильные ФИО '{self.name}': ФИО должно состоять только из букв и начинаться с заглавной буквы"


class InvalidSubjectError(ValueError):
    def __init__(self, subject: str):
        self.subject = subject

    def __str__(self):
        return f"Неправильный предмет '{self.subject}': Предмет не найден"


class InvalidNumberError(ValueError):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        self.validate(value)
        setattr(instance, self.param_name, value.title())

    def validate(self, value: str):
        if not (isinstance(value, str) and ''.join(value.split()).isalpha() and value.istitle()):
            raise InvalidNameError(value)


class Subject:
    def __init__(self, subjects: {}):
        self.subjects = subjects

    def __set_name__(self, owner, name: str):
        self.param_name = '_' + name

    def __get__(self, instance, owner, subject: str):
        self.validate(subject)
        return self.subjects[subject]

    def __set__(self, instance, subject: str):
        self.validate(subject)
        return self.subjects[subject]

    def validate(self, subject: str):
        if not subject in self.subjects.keys():
            raise InvalidSubjectError(subject)


class Range:
    def __init__(self, min_value: int = None, max_value: int = None, param_title: str = None):
        self.min_value = min_value
        self.max_value = max_value
        self.param_title = param_title

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
        if self.param_title == None:
            self.param_title = name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: int):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not (isinstance(value, int) and value >= self.min_value and value <= self.max_value):
            raise InvalidNumberError(
                f"Неправильный(ая/ое) {self.param_title}: Должно быть целое число от {self.min_value} до {self.max_value}")


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:

    name (str): ФИО студента
    subjects (dict): Информацию об оценках и результатах тестов для каждого предмета в виде словаря.
    subject: Шаблон предмета: Должен быть из списка предметов данного студента
    grade: Шаблон оценки: Должна быть целым числом от 2 до 5
    test_score: Шаблон результата теста: Должен быть целым числом от 0 до 100
    """
    name = Name()
    subjects = {}
    subject = Subject(subjects)
    grade = Range(2, 5, "оценка")
    test_score = Range(0, 100, "результат теста")

    def __init__(self, name: str, subjects_file: str):
        '''
        Принимает имя студента и файл с предметами и их результатами
        '''
        log.debug(f"init() | "
                  f"name={name} "
                  f"subjects_file={subjects_file}")

        try:
            self.name = name
            self.load_subjects(subjects_file)
        except InvalidNameError as e:
            log.error(e)
            raise e
        except FileNotFoundError:
            message = "Файл с предметами не найден. Студент не создан"
            log.critical(message)
            raise FileNotFoundError(message)

        log.info(f"init() | "
                 f"name={name} "
                 f"subjects_file={subjects_file} done")

    def __str__(self):
        '''
        Возвращает строковое представление студента, включая имя и список предметов.

        Студент: Иван Иванов
        Предметы: Математика, История
        '''
        subjects = ', '.join([key for key, value in self.subjects.items()
                              if value['grade'] or value['test_score']])
        return f'Студент: {self.name}\n' \
               f'Предметы: {subjects}'

    def load_subjects(self, subjects_file):
        '''
        Загружает предметы из файла CSV
        '''
        log.debug(f"load_subjects() | "
                  f"{self.name} | "
                  f"subject_file={subjects_file}")
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, quoting=csv.QUOTE_MINIMAL)
            for field in reader.fieldnames:
                self.subjects[field] = \
                    {
                        'grade': [],
                        'test_score': []
                    }
        log.info(f"load_subjects() | "
                 f"{self.name} | "
                 f"subject_file={subjects_file} done")

    def add_grade(self, subject: str, value: int):
        '''
        Добавляет оценку по заданному предмету
        '''
        log.debug(f"add_grade() | "
                  f"{self.name} | "
                  f"subject={subject} "
                  f"grade={value}")
        try:
            self.grade = value
            self.subject = subject
        except InvalidNumberError as e:
            log.error(f"add_grade() | {e}")
            return
        except InvalidSubjectError as e:
            log.error(f"add_grade() | {e}")
            return
        self.subjects[subject]['grade'].append(value)
        log.info(f"add_grade() | "
                 f"{self.name} | "
                 f"subject={subject} "
                 f"grade={value} done")

    def add_test_score(self, subject, value: int):
        '''
        Добавляет результат теста по заданному предмету
        '''
        log.debug(f"add_test_score() | "
                  f"{self.name} | "
                  f"subject={subject} "
                  f"score={value}")
        try:
            self.test_score = value
            self.subject = subject
        except InvalidNumberError as e:
            log.error(f"add_test_score() | {e}")
            return
        except InvalidSubjectError as e:
            log.error(f"add_test_score() | {e}")
            return
        self.subjects[subject]['test_score'].append(value)
        log.info(f"add_test_score() | "
                 f"{self.name} | "
                 f"subject={subject} "
                 f"score={value} done")

    def get_average_grade(self):
        '''
        Возвращает средний балл по всем предметам
        '''
        log.debug(f"get_average_grade() | "
                  f"{self.name}")
        grades = [grade for value in self.subjects.values() for grade in value['grade']]
        if len(grades) == 0:
            log.info(f"get_average_grade() | Оценок нет. Средний бал не посчитан")
            return
        average_grade = sum(grades) / len(grades)
        log.info(f"get_average_grade() | "
                 f"{self.name} | average_grade={average_grade} done")
        return average_grade

    def get_average_test_score(self, subject):
        '''
        Возвращает средний балл по тестам для заданного предмета
        '''
        log.debug(f"get_average_test_score() | "
                  f"{self.name}")

        try:
            self.subject = subject
        except InvalidSubjectError as e:
            log.error(f"add_test_score() | {e}")
            return
        test_scores = self.subjects[subject]['test_score']
        if len(test_scores) == 0:
            log.info(f"get_average_test_score() | Результатов тестов нет. Средний бал не посчитан")
            return None
        average_score = sum(test_scores) / len(test_scores)
        log.info(f"get_average_test_score() | "
                 f"{self.name} | average_test_score={average_score} done")
        return average_score


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")
    print(student)
    print()

    average_grade = student.get_average_grade()
    average_grade = average_grade if average_grade != None else "Нет оценок"
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    average_test_score = average_test_score if average_test_score != None else "Нет результатов теста"
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print()

    student.add_grade("Математика", 7)
    student.add_test_score("Математика", 110)
    student.add_grade("Биология", 3)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    average_grade = average_grade if average_grade != None else "Нет оценок"
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    average_test_score = average_test_score if average_test_score != None else "Нет результатов теста"
    print(f"Средний результат по тестам по математике: {average_test_score}")

    average_test_score = student.get_average_test_score("Биология")
    average_test_score = average_test_score if average_test_score != None else "Нет результатов теста"
    print(f"Средний результат по тестам по биологии: {average_test_score}")

    print()

    print(student)