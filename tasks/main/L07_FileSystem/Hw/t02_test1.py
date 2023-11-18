from hw_package import rename_files  # v1
# from hw_package.t01 import rename_files  # v2
from pathlib import Path
import os
import shutil

DIRECTORY = Path('test_folder')

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
