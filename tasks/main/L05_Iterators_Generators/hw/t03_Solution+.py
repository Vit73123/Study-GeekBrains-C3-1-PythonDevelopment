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

def fibonacci():
    '''
    Генератор чисел Фибоначчи

    :param num:
    :return:
    '''
    yield 0
    yield 1
    prev = 0
    next = 1
    while True:
        buf = next
        next = prev + next
        prev = buf
        yield next

f = fibonacci()
for i in range(10):
    print(next(f))