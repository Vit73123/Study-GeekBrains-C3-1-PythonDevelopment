# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет  для работы с файлами разных форматов.

# Тест 1

# 1-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 35229672}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}]

# [
#     {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#     {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#     {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#     {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#     {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#     {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
#
#     {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684},
#     {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
#
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
#
# Ответ:
#
# [
#     {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#     {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#     {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#     {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#     {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#     {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
#
#     {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 35229672},
#     {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 0},
#
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
#     {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}]

# 2-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
#
# Ответ:
#
# [{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}]

# Тест 2

# 1-я попытка

# [{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
# [{'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}]

# 2-я попытка

# [{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
#
# Ответ:
#
# [{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171}]

# Тест 3

# 1-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 35229672}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}]

# 2-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
#
# Ответ:
#
# [{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}]

# Тест 4

# 1-я попытка

# [['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains/my_ds_projects', 'Directory', '684'], ['geekbrains/my_ds_projects/My-code', 'Directory', '342'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70']]
# [['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains', 'Directory', '35229672'], ['geekbrains/my_ds_projects', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code', 'Directory', '0'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171']]

# 2-я попытка

# [['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'],
#  ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'],
#  ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'],
#  ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains/my_ds_projects', 'Directory', '684'],
#  ['geekbrains/my_ds_projects/My-code', 'Directory', '342'],
#  ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'],
#  ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'],
#  ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70']]
#
# Ответ:
#
# [['Path', 'Type', 'Size'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'],
#  ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70'],
#  ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'],
#  ['geekbrains/my_ds_projects/My-code', 'Directory', '171'], ['geekbrains/my_ds_projects', 'Directory', '171'],
#  ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'],
#  ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'],
#  ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85']]

# Тест 5

# 1-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 35229672}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 0}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}]

# 2-я попытка

# [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]
#
# Ответ:
#
# [{'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
#  {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
#  {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
#  {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
#  {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
#  {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
#  {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}]

import json
import os
import pickle
import csv


def traverse_directory(directory: str) -> []:
    dir_info = {}
    for root, dirs, files in os.walk(directory, topdown=False):
        size = 0
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            dir_info[file_path] = {
                'Path': file_path,
                'Type': 'File',
                'Size': file_size
            }
            size += file_size
        if root != directory:
            size += sum(dir_info[os.path.join(root, d)]['Size'] for d in dirs)
            dir_info[root] = {
                'Path': root,
                'Type': 'Directory',
                'Size': size
            }
    return [{**dir} for dir in dir_info.values()]


def save_results_to_json(dir_info: [], file_name: str = 'dir_info.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dir_info, f, indent=2)


def save_results_to_csv(dir_info: [], file_name: str = 'dir_info.csv'):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, ['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(dir_info)


def save_results_to_pickle(dir_info: [], file_name: str = 'dir_info.pickle'):
    with open(file_name, 'wb') as f:
        pickle.dump(dir_info, f)


if __name__ == '__main__':
    dir_info = traverse_directory('test')
    print(dir_info)

    save_results_to_json(dir_info)
    save_results_to_csv(dir_info)
    save_results_to_pickle(dir_info)

    with open('dir_info.pickle', 'rb') as f:
        print(pickle.load(f))

# [
#     {'Path': 'test\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\fff.txt', 'Type': 'File', 'Size': 77},
#     {'Path': 'test\\ggg.txt', 'Type': 'File', 'Size': 97},
#     {'Path': 'test', 'Type': 'Directory', 'Size': 405},
#     {'Path': 'test\\test1\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test1\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1', 'Type': 'Directory', 'Size': 231},
#     {'Path': 'test\\test1\\test1-1\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-1\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-1', 'Type': 'Directory', 'Size': 73},
#     {'Path': 'test\\test1\\test1-1\\test1-1-1\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-1\\test1-1-1\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test1\\test1-1\\test1-1-1', 'Type': 'Directory', 'Size': 109},
#     {'Path': 'test\\test1\\test1-1\\test1-1-2\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-1\\test1-1-2', 'Type': 'Directory', 'Size': 35},
#     {'Path': 'test\\test1\\test1-1\\test1-1-3\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-1\\test1-1-3\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-1\\test1-1-3\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-1\\test1-1-3', 'Type': 'Directory', 'Size': 108},
#     {'Path': 'test\\test1\\test1-2', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'test\\test1\\test1-3\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-3\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-3', 'Type': 'Directory', 'Size': 87},
#     {'Path': 'test\\test1\\test1-3\\test1-3-1', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'test\\test1\\test1-4\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4', 'Type': 'Directory', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4\\test1-4-1\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4\\test1-4-1\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-4\\test1-4-1', 'Type': 'Directory', 'Size': 87},
#     {'Path': 'test\\test1\\test1-4\\test1-4-2\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-4\\test1-4-2\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test1\\test1-4\\test1-4-2\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-4\\test1-4-2', 'Type': 'Directory', 'Size': 169},
#     {'Path': 'test\\test1\\test1-4\\test1-4-3', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'test\\test1\\test1-4\\test1-4-4\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-4\\test1-4-4\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-4\\test1-4-4', 'Type': 'Directory', 'Size': 106},
#     {'Path': 'test\\test1\\test1-4\\test1-4-5\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4\\test1-4-5\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-4\\test1-4-5', 'Type': 'Directory', 'Size': 62},
#     {'Path': 'test\\test1\\test1-4\\test1-4-6\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4\\test1-4-6\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-4\\test1-4-6', 'Type': 'Directory', 'Size': 62},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-4\\test1-4-7', 'Type': 'Directory', 'Size': 231},
#     {'Path': 'test\\test1\\test1-4\\test1-4-8\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test1\\test1-4\\test1-4-8\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test1\\test1-4\\test1-4-8', 'Type': 'Directory', 'Size': 95},
#     {'Path': 'test\\test2\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test2\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test2', 'Type': 'Directory', 'Size': 81},
#     {'Path': 'test\\test2\\test2-1', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'test\\test2\\test2-2\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test2\\test2-2\\eee.txt', 'Type': 'File', 'Size': 60},
#     {'Path': 'test\\test2\\test2-2', 'Type': 'Directory', 'Size': 87},
#     {'Path': 'test\\test2\\test2-3', 'Type': 'Directory', 'Size': 0},
#     {'Path': 'test\\test2\\test2-3\\test2-3-1\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test2\\test2-3\\test2-3-1', 'Type': 'Directory', 'Size': 63},
#     {'Path': 'test\\test3\\fff.txt', 'Type': 'File', 'Size': 77},
#     {'Path': 'test\\test3', 'Type': 'Directory', 'Size': 77},
#     {'Path': 'test\\test4\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test4\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test4\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test4', 'Type': 'Directory', 'Size': 125},
#     {'Path': 'test\\test4\\test4-1\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test4\\test4-1\\ccc.txt', 'Type': 'File', 'Size': 46},
#     {'Path': 'test\\test4\\test4-1\\fff.txt', 'Type': 'File', 'Size': 77},
#     {'Path': 'test\\test4\\test4-1', 'Type': 'Directory', 'Size': 150},
#     {'Path': 'test\\test4\\test4-1\\test4-1-1\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test4\\test4-1\\test4-1-1', 'Type': 'Directory', 'Size': 27},
#     {'Path': 'test\\test4\\test4-1\\test4-1-2\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test4\\test4-1\\test4-1-2\\ddd.txt', 'Type': 'File', 'Size': 63},
#     {'Path': 'test\\test4\\test4-1\\test4-1-2\\ggg.txt', 'Type': 'File', 'Size': 97},
#     {'Path': 'test\\test4\\test4-1\\test4-1-2', 'Type': 'Directory', 'Size': 195},
#     {'Path': 'test\\test4\\test4-1\\test4-1-3\\aaa.txt', 'Type': 'File', 'Size': 27},
#     {'Path': 'test\\test4\\test4-1\\test4-1-3\\bbb.txt', 'Type': 'File', 'Size': 35},
#     {'Path': 'test\\test4\\test4-1\\test4-1-3', 'Type': 'Directory', 'Size': 62},
#     {'Path': 'test\\test4\\test4-2', 'Type': 'Directory', 'Size': 0}]
