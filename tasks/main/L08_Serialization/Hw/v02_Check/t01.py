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
            parent = os.path.dirname(root)
            dir_info.setdefault(root, {
                'Path': root,
                'Type': 'Directory',
                'Size': 0})
            dir_info[root]['Size'] += size
            dir_info.setdefault(parent, {
                'Path': parent,
                'Type': 'Directory',
                'Size': 0})
            dir_info[parent]['Size'] += dir_info[root]['Size']
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
