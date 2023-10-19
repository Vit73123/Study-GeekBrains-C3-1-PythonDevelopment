# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

input_num = int(input("Введите целое число: "))
SCALE = 16
num = input_num
res = ''
while num > 0:
    digit = num % SCALE
    if digit == 10:
        digit = 'A'
    elif digit == 11:
        digit = 'B'
    elif digit == 12:
        digit = 'C'
    elif digit == 13:
        digit = 'D'
    elif digit == 14:
        digit = 'E'
    elif digit == 15:
        digit = 'F'
    else:
        digit = str(digit)
    res = digit + res
    num //= SCALE
print('0x' + res)
print(hex(input_num))