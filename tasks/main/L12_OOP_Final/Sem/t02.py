# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
import os
from datetime import datetime

FILE = 'results.json'

class Factorial:

    def __init__(self, k, file):
        self.k = k
        self.results = []
        self.prev_results = {}
        self.file = file

    def __call__(self, num):
        f = 1
        for i in range(2, num + 1):
            f *= i
        self.log(f)
        return f

    def __enter__(self):
        if self.file in os.listdir():
            with open(self.file, 'r') as f:
                self.prev_results = json.load(f)
        else:
            with open(self.file, 'w') as f:
                self.prev_results = {}
                json.dump({}, f, indent=2)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = {str(datetime.now()): self.results}
        self.prev_results.update(data)
        with open(self.file, 'w') as f:
            json.dump(self.prev_results, f, indent=2)

    def log(self, res):
        if len(self.results) == self.k:
            self.results.pop(0)
        self.results.append(res)


if __name__ == '__main__':
    with Factorial(3, FILE) as f:
        for i in range(10):
            res = f(i)
        print(f.results)