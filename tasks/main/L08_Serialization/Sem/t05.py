# 📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pathlib
import pickle


def json_files_to_pickle(directory: pathlib.Path = pathlib.Path.cwd()):
    if isinstance(directory, str):
        directory = pathlib.Path(directory)
    for file in directory.iterdir():
        if file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as src, \
                open(file.name[:-5] + '.pickle', 'wb') as otp:
                pickle.dump(json.load(src), otp)

if __name__ == '__main__':
    json_files_to_pickle()