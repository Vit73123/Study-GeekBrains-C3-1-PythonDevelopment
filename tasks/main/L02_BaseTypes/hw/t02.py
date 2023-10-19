# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
#
# Пример
#
# На входе:
#
# frac1 = "1/2"
# frac2 = "1/3"
#
# На выходе:
#
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

import fractions

frac1 = '1/2'
frac2 = '1/3'
frac1_nums = [int(item) for item in frac1.split('/')]
frac2_nums = [int(item) for item in frac2.split('/')]

print('Сумма дробей: ', end='')
print(str(frac1_nums[0] * frac2_nums[1] + frac2_nums[0] * frac1_nums[1]), end='/')
print(str(frac1_nums[1] * frac2_nums[1]))
print('Произведение дробей: ', end='')
# Произведение дробей
print(str(frac1_nums[0] * frac2_nums[0]), end='/')
print(str(frac1_nums[1] * frac2_nums[1]))

f1 = fractions.Fraction(frac1)
f2 = fractions.Fraction(frac2)
print('Сумма дробей: ', end='')
print(fractions.Fraction(f1 + f2))
print('Произведение дробей: ', end='')
print(fractions.Fraction(f1 * f2))