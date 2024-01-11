# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

# Тест

# with open("__init__.py", "r") as init_file:
#     code = init_file.read()
#
# function_names = [
#     "def save_to_json",
#     "def find_roots",
#     "def generate_csv_file"
# ]
#
# for func_name in function_names:
#     if func_name not in code:
#         print(f"Функция {func_name} не найдена в файле __init__.py")
#     else:
#         print(f"Функция {func_name} найдена в файле __init__.py")

with open('__init__.py', 'w', encoding='utf-8') as file:
    file.write(
        '''\
__all__ = ['t06_sem']

from typing import Callable
import csv
import json
from random import randint

INPUT_DATA_CSV = 'input_data.csv'
RESULTS_JSON = 'results.json'
DATA_ROWS = 101
MIN_DATA_ROWS = 100
MAX_DATA_ROWS = 1000
MIN_NUM = 1
MAX_NUM = 10

def save_to_json(func: Callable) -> Callable[[], None]:
    def wrapper(a: str) -> None:
        with open(a, 'r', newline='') as f:
            reader = csv.reader(f)
            results = []
            for parameters in reader:
                parameters = [int(num) for num in parameters]
                results.append({'parameters': parameters, 'result': func(*parameters)})
        with open(RESULTS_JSON, 'w') as f:
            json.dump(results, f, indent=2)

    return wrapper

def generate_csv_file(file_name: str, rows: int) -> None:
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            line =\
                [
                    randint(MIN_NUM, MAX_NUM),
                    randint(MIN_NUM, MAX_NUM),
                    randint(MIN_NUM, MAX_NUM),
                ]
            writer.writerow(line)

@save_to_json
def find_roots(a: [int, str], *args: int):
    if not isinstance(a, int):
        return
    b, c = args
    d = b ** 2 - 4 * a * c
    if d > 0:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))
    elif d == 0:
        return (-b) / (2 * a)
    else:
        return None


if __name__ == '__main__':
    generate_csv_file(INPUT_DATA_CSV, DATA_ROWS)
    find_roots(INPUT_DATA_CSV)

    with open(RESULTS_JSON, 'r') as f:
        data = json.load(f)

    if MIN_DATA_ROWS <= len(data) <= MAX_DATA_ROWS:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == DATA_ROWS)
    '''
    )