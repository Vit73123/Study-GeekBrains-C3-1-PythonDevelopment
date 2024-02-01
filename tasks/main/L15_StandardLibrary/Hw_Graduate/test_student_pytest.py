import pytest
from student import *

STUDENT_NAME = "Иван Иванов"
INVALID_STUDENT_NAME = "иван Иванов"
SUBJECTS_FILE = "subjects.csv"
INVALID_SUBJECTS_FILE = "invalid_subjects.csv"

SUBJECT_1 = "Математика"
SUBJECT_2 = "История"
SUBJECT_1_GRADE_1 = 3
SUBJECT_1_GRADE_2 = 2
SUBJECT_2_GRADE_1 = 4
AVERAGE_GRADE = (SUBJECT_1_GRADE_1 + SUBJECT_1_GRADE_2 + SUBJECT_2_GRADE_1) / 3
SUBJECT_1_TEST_SCORE_1 = 80
SUBJECT_1_TEST_SCORE_2 = 70
SUBJECT_1_TEST_SCORE_3 = 50
SUBJECT_2_TEST_SCORE_1 = 40
AVERAGE_TEST_SCORE = (SUBJECT_1_TEST_SCORE_1 + SUBJECT_1_TEST_SCORE_2 + SUBJECT_1_TEST_SCORE_3) / 3

INVALID_SUBJECT = "Биология"
INVALID_GRADE = 8
INVALID_TEST_SCORE = 110


@pytest.fixture
def student():
    return Student(STUDENT_NAME, SUBJECTS_FILE)


@pytest.fixture
def student_with_grades():
    student = Student(STUDENT_NAME, SUBJECTS_FILE)

    student.add_grade(SUBJECT_1, SUBJECT_1_GRADE_1)
    student.add_grade(SUBJECT_1, SUBJECT_1_GRADE_2)
    student.add_grade(SUBJECT_2, SUBJECT_2_GRADE_1)
    student.add_test_score(SUBJECT_1, SUBJECT_1_TEST_SCORE_1)
    student.add_test_score(SUBJECT_1, SUBJECT_1_TEST_SCORE_2)
    student.add_test_score(SUBJECT_1, SUBJECT_1_TEST_SCORE_3)
    student.add_test_score(SUBJECT_2, SUBJECT_1_TEST_SCORE_1)

    return student


def test_init_student_name(student):
    """
    Тест конструктора студента
    """
    assert student.name == STUDENT_NAME


def test_init_invalid_student_name():
    """
    Тест конструктора с неправильным именем студента
    """
    with pytest.raises(InvalidNameError):
        Student(INVALID_STUDENT_NAME, SUBJECTS_FILE)


def test_init_invalid_subjects_file():
    """
    Тест конструктора с неправильным файлом с предметами
    """
    with pytest.raises(FileNotFoundError):
        Student(STUDENT_NAME, INVALID_SUBJECTS_FILE)


def test_str(student_with_grades):
    """
    Тест дантер-метода __str__
    """
    assert str(student_with_grades) == f'Студент: {STUDENT_NAME}\n' \
                                       f'Предметы: {SUBJECT_1}, {SUBJECT_2}'


def test_add_grade(student):
    """
    Тест метода add_grade(): Добавление оценки по заданному предмету
    """
    student.add_grade(SUBJECT_1, SUBJECT_1_GRADE_1)
    assert student.subjects[SUBJECT_1]['grade'] == [SUBJECT_1_GRADE_1]


def test_add_invalid_grade(student):
    """
    Тест метода add_grade() с неправильной оценкой
    """
    assert student.add_grade(SUBJECT_1, INVALID_GRADE) == None


def test_add_grade_invalid_subject(student):
    """
    Тест метода add_grade() с неправильным предметом
    """
    assert student.add_grade(INVALID_SUBJECT, SUBJECT_1_GRADE_1) == None


def test_add_test_score(student):
    """
    Тест метода add_test_score(): Добавление результата теста по заданному предмету
    """
    student.add_test_score(SUBJECT_1, SUBJECT_1_TEST_SCORE_1)
    assert student.subjects[SUBJECT_1]['test_score'] == [SUBJECT_1_TEST_SCORE_1]


def test_add_invalid_test_score(student):
    """
    Тест метода add_test_score() с неправильным результатом
    """
    assert student.add_test_score(SUBJECT_1, INVALID_TEST_SCORE) == None


def test_get_average_grade(student_with_grades):
    """
    Тест метода add_average_grade(): Получение среднего бала по всем предметам
    """
    assert student_with_grades.get_average_grade() == AVERAGE_GRADE


def test_get_average_test_score(student_with_grades):
    """
    Тест метода add_average_test_score(): Получение среднего результата по тестам по заданному предмету
    """
    assert student_with_grades.get_average_test_score(SUBJECT_1) == AVERAGE_TEST_SCORE


def test_get_average_test_score_invalid_subject(student_with_grades):
    """
    Тест метода add_average_test_score() с неправильным предметом
    """
    assert student_with_grades.get_average_test_score(INVALID_SUBJECT) == None


pytest.main(['-v'])
