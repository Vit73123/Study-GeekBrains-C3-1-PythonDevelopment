# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:

# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input('Количество рядов: '))
spaces = rows
for i in range(rows):
    points = i * 2 + 1
    spaces -= 1
    print(' ' * spaces + '*' * points)
