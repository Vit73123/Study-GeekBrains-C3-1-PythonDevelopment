# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.
import t04_user_module
import t03_06_exceptions

class Project:
    def __init__(self, filename="users.json"):
        self.source = filename
        self.users = t04_user_module.load_users(filename)
        self.admin = None

    def auth(self, name: str, id: int):
        temp_user = t04_user_module.User(name, id, None)
        if temp_user not in self.users:
            raise t03_06_exceptions.ProjectAccessException(temp_user)
        for user in self.users:
            if user == temp_user:
                self.admin = user

    def add_new_user(self, new_name, new_id, new_level):
        if not self.admin:
            raise t03_06_exceptions.NotAuthentificatedError()
        temp_user = t04_user_module.User(new_name, new_id, new_level)
        self.__vallidate_new_user(temp_user)
        self.users.add(temp_user)

    def __vallidate_new_user(self, new_user: t04_user_module.User):
        for user in self.users:
            if user.id == new_user.id:
                raise t03_06_exceptions.ExistingIdError(new_user)
        if new_user.level < self.admin.level:
            raise t03_06_exceptions.ProjectLevelException(self.admin, new_user)

    def save_session(self):
        t04_user_module.save_data(self.users, self.source)


if __name__ == "__main__":
    p1 = Project()
    print(p1.users)
    # p1.auth("vlads", 1000011)
    p1.add_new_user("gfnags", 19091481, 1)
    print(p1.users)
    p1.save_session()
