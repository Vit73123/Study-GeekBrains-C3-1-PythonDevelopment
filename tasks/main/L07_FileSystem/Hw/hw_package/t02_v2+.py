# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__test.py и запишите в него функцию rename_files

with open('__init__.py', 'w', encoding='utf-8') as file:
    file.write(
        '''\
__all__ = ['t01', 't01_sem', 't02_sem', 't03_sem', 't05_sem', 't07_sem']
        '''
    )