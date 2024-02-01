# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
from collections import namedtuple
import pathlib
import sys

File = namedtuple(
    "File", (
        "filename",
        "extension",
        "is_directory",
        "parent"
    )
)


def get_dir_info(path: [str, pathlib.Path]) -> []:
    # base_dir = pathlib.Path(r"E:\Proj\Study\GeekBrains\C3_01_PythonDeep\tasks\main\L15_StandardLibrary\Sem")
    base_dir = path
    result = []
    for file in base_dir.iterdir():
        result.append(File(file.name, file.suffix, file.is_dir(), file.parent))
        # print(*result, sep="\n")
    return result


def command_run(*args):
    if len(args) == 1:
        return pathlib.Path.cwd()
    _, path, *_ = args
    return pathlib.Path(path)


if __name__ == "__main__":
    path = command_run(*sys.argv)
    # print(path)
    print(*get_dir_info(path), sep="\n")