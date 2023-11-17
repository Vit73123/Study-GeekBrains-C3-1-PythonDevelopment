# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
#  * расширение
#  * минимальная длина случайно сгенерированного имени, по умолчанию 6
#  * максимальная длина случайно сгенерированного имени, по умолчанию 30
#  * минимальное число случайных байт, записанных в файл, по умолчанию 256
#  * максимальное число случайных байт, записанных в файл, по умолчанию 4096
#  * количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from string import ascii_lowercase
from random import choice, randint


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


if __name__ == '__main__':
    make_files('txt', count_files=10)
