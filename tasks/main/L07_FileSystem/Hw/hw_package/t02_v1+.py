# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__test.py и запишите в него функцию rename_files

with open('__init__.py', 'w', encoding='utf-8') as file:
    file.write(
        '''\
from pathlib import Path

__all__ = ['rename_files', 't01_sem', 't02_sem', 't03_sem', 't05_sem', 't07_sem']

DIRECTORY = Path('test_folder')


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str, source_from=0, source_to=0):
    idx = 0
    for file in DIRECTORY.iterdir():
        if file.suffix == '.' + source_ext:
            idx += 1
            f = Path(file.stem[source_from:source_to] + desired_name + format(idx, f'0>{num_digits}') + '.' + target_ext)
            file.replace(DIRECTORY / f)
        '''
    )