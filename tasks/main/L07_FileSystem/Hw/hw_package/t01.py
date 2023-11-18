# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
#    Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
#
# Пример использования.
#
# На входе:
#
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
#
# На выходе:
#
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
from pathlib import Path
import os
import shutil

__all__ = ['rename_files']

DIRECTORY = Path('test_folder')


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str, source_from=0, source_to=0):
    idx = 0
    for file in DIRECTORY.iterdir():
        if file.suffix == '.' + source_ext:
            idx += 1
            f = Path(file.stem[source_from:source_to] + desired_name + format(idx, f'0>{num_digits}') + '.' + target_ext)
            file.replace(DIRECTORY / f)


if __name__ == '__main__':
    # Создать тестовую папку
    folder_name = DIRECTORY
    folder_path = os.path.join(os.getcwd(), folder_name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

    # Заполнить тестовую папку
    file_name = "test1.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

    rename_files(desired_name="file_",
                 num_digits=4,
                 source_ext="txt",
                 target_ext="txt")

    folder_content = ""
    files = os.listdir(folder_path)
    separator = ", "
    files_as_string = separator.join(files)
    print(files_as_string)

    shutil.rmtree(folder_path)

# Ожидаемый ответ:
# file_0001.txt