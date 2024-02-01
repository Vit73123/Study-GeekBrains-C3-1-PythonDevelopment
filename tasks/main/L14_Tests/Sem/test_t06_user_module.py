# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.
from L13_Sem_t05_project import Project
from L13_Sem_t04_user_module import User
from L13_Sem_t03_t06_exceptions import (ProjectAccessException,
                                        ProjectLevelException)
import pytest


@pytest.fixture
def setUp_add_users():
    p1 = Project()
    p1.auth("vlads", 1000011)
    return p1


@pytest.fixture
def setUp_auth():
    p1 = Project()
    return p1


def test_auth_valid_data(setUp_auth):
    setUp_auth.auth("vlads", 1000011)
    assert setUp_auth.admin == User("vlads", 1000011, None)


def test_auth_invalid_data(setUp_auth):
    with pytest.raises(ProjectAccessException):
        setUp_auth.auth("vlaaafads", 1033100011)


def test_add_valid_user(setUp_add_users):
    setUp_add_users.add_new_user("fajnfgjhan", 181481481, 5)
    assert User("fajnfgjhan", 181481481, 5) in setUp_add_users.users


def test_add_invalid_user(setUp_add_users):
    with pytest.raises(ProjectLevelException):
        setUp_add_users.add_new_user("fajnfgjhan", 181481481, 1)


if __name__ == "__main__":
    pytest.main(verbosity=4)
