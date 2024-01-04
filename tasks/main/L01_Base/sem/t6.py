# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = int(input('Введите год: '))
MAIN_CONDITION = 4
ADDIOTIONAL_CONDITION = 100
EXTENSION_CONDITION = 400

if year % MAIN_CONDITION != 0\
        or year % ADDIOTIONAL_CONDITION == 0\
        and year % EXTENSION_CONDITION != 0:
    print(f"{year} Обычный", end="")
else:
    print(f"{year} Високосный")
print("год")