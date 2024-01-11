# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа
# в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет
# следующие действия:
#
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c
# и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
#
# Пример
#
# На входе:
#
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==101)
#
# На выходе:
#
# True
# True
#
# Формат JSON файла определён следующим образом:
#
# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
# ]

# Тест 1
#
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==101)

# Тест 2

# generate_csv_file("input_data.csv", 999)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==999)

# Тест 3

# generate_csv_file("input_data.csv", 1500)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==1500)

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