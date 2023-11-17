# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
import pathlib


def sort_by_dir(directory: pathlib.Path):
    '''
    Генерирует файлы в указанную директорию

    Отсутствие/наличие директории не вызывает ошибок в работе функции
    Существующие файлы не удаляются/изменяются в случае совпадения имён

    Директорий, в который генерируются файлы
    :param directory:
    :return:
    '''
    os.chdir(directory)
    directories = set(file.suffix for file in directory.iterdir()
                      if file.suffix != '.py'
                      and not file.is_dir())

    for dir in directories:
        if pathlib.Path(directory / dir) not in directory.iterdir():
            os.mkdir(dir)

    for file in directory.iterdir():
        if file.suffix and file.suffix != '.py':
            file.replace(f'{file.suffix}\\{file.name}')


if __name__ == '__main__':
    sort_by_dir(pathlib.Path(os.getcwd()))
