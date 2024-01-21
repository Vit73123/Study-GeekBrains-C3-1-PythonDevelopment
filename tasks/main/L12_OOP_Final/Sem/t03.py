# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.
class FactorialGenerator:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
        # if self.start <= self.stop:
            res = 1
            for i in range(1, self.start + 1):
                res *= i
            self.start += self.step
            return res
        raise StopIteration


if __name__ == '__main__':
    f = FactorialGenerator(1, 10)
    for i in f:
        print(i)