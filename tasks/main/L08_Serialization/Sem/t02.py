# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import os


def input_user_json(json_data : str='users.json') -> bool:
    if json_data in os.listdir():
        with open(json_data, 'r', encoding='utf-8') as f:
            inp_dict = json.load(f)
    else:
        with open(json_data, 'w') as f:
            inp_dict = {str(i): [] for i in range(1, 8)}
            json.dump(inp_dict, f, indent=2, ensure_ascii=False)
    inp = input("Имя, id, уровень доступа от 1 до 7 (Выйти - Ввод): ")
    if inp == '':
        return False
    name, id, sec_id = inp.split()
    if 1 <= int(sec_id) <= 7:
        inp_dict[str(sec_id)].append({
            "name": name,
            "id": int(id),
            })
        with open(json_data, 'w', encoding='utf-8') as f:
            json.dump(inp_dict, f, indent=2, ensure_ascii=False)
    else:
        print("Неправильный уровень доступа")
    return True

if __name__ == '__main__':
    while True:
        inp : bool = input_user_json()
        if not inp:
            break