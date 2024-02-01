# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
import json


class User:
    def __init__(self, name: str, id: int, level: int):
        self.name = name
        self.id = id
        self.level = level

    def __str__(self):
        return f"{self.name}-{self.id}-{self.level}"

    def __repr__(self):
        return f"User({self.name}, {self.id}, {self.level}"

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return self.id


def load_users(filename: str = "users.json") -> set:
    with open("users.json", "r", encoding="utf-8") as source:
        data = json.load(source)
    return set(map(lambda x: User(**x), data))  # **x: User(id=id, name=name, level=level)


def save_data(users: set, filename: str):
    with open(filename, "w", encoding="utf-8") as source:
        users = [{
            "name": user.name,
            "id": user.id,
            "level": user.level
        } for user in users]
        json.dump(users, source, indent=2)


if __name__ == "__main__":
    print(load_users())
