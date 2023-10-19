# Если планируется писать код для банковской системы или любой другой, где важна точность расчётов,
# используется модуль decimal вместо класса float.

import decimal

# Точность по умолчанию - до 28 знаков после запятой
pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

# Задать точность
decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)