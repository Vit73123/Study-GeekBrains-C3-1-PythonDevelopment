# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json


def convert_json(source_file : str='data.txt') -> None:
    with open(source_file, 'r', encoding='utf-8') as src, \
        open('json_data', 'w') as res:
        res_dict = {}
        for line in src:
            name, value = line.split()
            res_dict[name] = value
        json.dump(res_dict, res, indent=2)

if __name__ == '__main__':
    convert_json()
