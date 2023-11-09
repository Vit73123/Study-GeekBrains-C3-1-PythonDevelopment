# Создайте функцию генератор чисел Фибоначчи fibonacci.
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
#
# Пример использования.
# На входе:
#
# f = fibonacci()
# for i in range(10):
#     print(next(f))
#
# На выходе:
#
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# Распаковка для генерации чисел Фибоначчи
def fibonacci():
    '''
    Генератор чисел Фибоначчи

    :param num:
    :return:
    '''
    # Распаковка.
    a, b = 0, 1
    while True:
        yield a
        # Последовательность присваивания при распаковке:
        # - сначал получаются все значения, которые помещаются в элементы коллекции
        # b -> помещается в 1-й элемент коллекции (в элементе сохраняется старое значение переменной b)
        # a + b -> помещайется во 2-й элемент коллекции
        # - затем полученные элементы коллекции распаковываются в переменные на стороне распаковки
        # a = b (b - старое значение b, т.к. это не значение распакованной переменной b, а 1-й элемент полученной коллекции!)
        # b = a + b
        a, b = b, a + b

f = fibonacci()
for i in range(10):
    print(next(f))