# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.
import json


def csv_to_json(source: str = 'users.csv', output: str = 'users_new.json'):
    with open(source, 'r', newline='', encoding='utf-8') as src:
        header = src.readline()[:-1].split(',')
        data = [dict(zip(['level', 'id', 'name'], row[:-1].split(',')))
                for row in src]
        with open(output, 'w') as otp:
            json.dump(manage_data(data), otp, indent=2)


def manage_data(data: []) -> []:
    for user in data:
        user['id'] = f'{user["id"]:>010}'
        user['hash'] = hash(user['name'] + user['id'])
        user['name'] = user['name'].capitalize()
    return data


if __name__ == '__main__':
    csv_to_json()
