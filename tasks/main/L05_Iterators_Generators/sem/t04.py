# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

odd_gen = (num for num in range(0, 101, 2) if (num // 10 + num % 10) == 8)
print([num for num in odd_gen])

odd_gen = (num for num in range(0, 101, 2) if sum(int(c) for c in str(num)) == 8)
print([num for num in odd_gen])