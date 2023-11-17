# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from string import ascii_lowercase
from random import choice, randint

MIN_LETTERS_COUNT = 4
MAX_LETTERS_COUNT = 7

def write_names(file_name: str, lines_num: int):
    '''
    Генерирует псевдоимена
    Полученные имена сохраняет в файл.

    :param file_name:
    :param lines_num:
    :return:
    '''
    with open(file_name, mode='a', encoding='utf-8') as f:
        for i in range(lines_num):
            new_name = pseudo_name()
            f.write(f'{new_name}\n')

def pseudo_name() -> str:
    '''
    Генерирует псевдоимя
    Имя начинается с заглавной буквы, состоит из 4-7 букв, среди которых обязательно должны быть гласные

    :return:
    '''
    letters_list = [choice(ascii_lowercase) if letter != 2 else choice('aeiouy') for letter in range(randint(MIN_LETTERS_COUNT, MAX_LETTERS_COUNT))]
    return ''.join(letters_list).capitalize()

if __name__ == '__main__':
    write_names('pseudo_names.txt', 10)