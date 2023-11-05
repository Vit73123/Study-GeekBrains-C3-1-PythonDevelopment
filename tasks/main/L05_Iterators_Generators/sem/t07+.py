# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».


N = 100
START = 2


def is_prime(num: int) -> bool:
    for i in range(START, num):
        if num / i == num // i:
            return False
    return True

# Генератор
def prime_num(count: int):
    counter = 0
    num = START
    while counter < count:
        if is_prime(num):
            yield num
            counter += 1
        num += 1


# Вызов генератора
res = [num for num in prime_num(N)]
print(res)
