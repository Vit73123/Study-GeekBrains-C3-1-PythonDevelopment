# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы -
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

# Задание №6
# 📌 Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода проекта.
from L13_Sem_t04_user_module import User


class ProjectException(Exception):
    pass


class ProjectLevelException(ProjectException):
    def __init__(self, admin: User, new_user: User) -> None:
        self.admin = admin
        self.new_user = new_user

    def __str__(self):
        return f"Нельзя добавить пользователя" + \
            f" с уровнем {self.new_user.level}" + \
            f" Ваш уровент {self.admin.level}"


class ProjectAccessException(ProjectException):
    def __init__(self, user: User) -> None:
        self.user = user

    def __str__(self):
        return f"Пользователь {self.user} не найден в базе."


class ExistingIdError(ProjectException):
    def __init__(self, user: User):
        self.user = user

    def __str__(self):
        return f"Пользователь с id: {self.user.id} уже существует"


class NotAuthentificatedError(ProjectException):
    def __str__(self):
        return "Пользователь не аутентифицирован"