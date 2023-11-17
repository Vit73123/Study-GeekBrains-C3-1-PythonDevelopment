# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

def write_nums(file_name: str, lines_num: int):
    '''
    Заполняет файл (добавляет в конец) случайными парами чисел

    Первое число int, второе - float разделены вертикальной чертой
    Минимальное число - -1000, максимальное - +1000

    Имя файла передаются, количество строк
    :param file_name: str
    :param lines_num: int
    :return:
    '''
    with open(file_name, mode='a', encoding='utf-8') as f:
        for i in range(lines_num):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num}\n')

if __name__ == '__main__':
    write_nums('matrix.txt', 30)