# 📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
class Factorial:

    def __init__(self, k):
        self.k = k
        self.results = []

    def __call__(self, num):
        f = 1
        for i in range(2, num + 1):
            f *= i
        self.log(f)
        return f

    def log(self, res):
        if len(self.results) == self.k:
            self.results.pop(0)
        self.results.append(res)


if __name__ == '__main__':
    f = Factorial(3)
    for i in range(10):
        res = f(i)
    print(f.results)
