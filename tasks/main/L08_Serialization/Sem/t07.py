# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.
import pickle
import csv


def csv_to_pickle_string(source='users_new.csv'):
    with open(source, 'r', newline='', encoding='utf-8') as src:
        data = csv.reader(src)
        output_data = []
        for i, line in enumerate(data):
            if i == 0:
                header = line
            else:
                output_data.append(
                    {
                        header[i]: cell for i, cell in enumerate(line)
                    }
                )
        return pickle.dumps(output_data)


if __name__ == '__main__':
    print(csv_to_pickle_string())
