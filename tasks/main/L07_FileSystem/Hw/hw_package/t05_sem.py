# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
from string import ascii_lowercase
from random import choice, randint

__all__ = ['make_files_more_ext']


def file_name(min_len: int, max_len: int) -> str:
    letters = [choice(ascii_lowercase) if letter != 2 else choice('aeiouy') for letter in
               range(randint(min_len, max_len))]
    return ''.join(letters).capitalize()


def make_files(extension: str,
               min_len: int = 6,
               max_len: int = 30,
               min_bytes: int = 256,
               max_bytes: int = 4096,
               count_files: int = 42):
    for _ in range(count_files):
        with open('_' + file_name(min_len, max_len) + '.' + extension, 'wb') as f:
            bytes_w = bytes([randint(0, 255) for _ in range(randint(min_bytes, max_bytes + 1))])
            f.write(bytes_w)


def make_files_more_ext(*args, **kwargs):
    '''
    Генерирует файлы с разными расширениями

    Количество переданных расширений может быть любым
    Количество файлов для каждого расширения различно

    Расширения и количество файлов
    :param args:
    :param kwargs:
    :return:
    '''
    for ext in args:
        make_files(ext, **kwargs)


if __name__ == '__main__':
    make_files_more_ext('.java', '.mp4', 'jpeg', count_files=10)