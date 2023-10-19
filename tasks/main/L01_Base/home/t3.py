# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

MAX_ATTEMPTS = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
GUESS_NUM = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, MAX_ATTEMPTS + 1):
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    if num < GUESS_NUM:
        print(f'Число {num} меньше')
    elif num > GUESS_NUM:
        print(f'Число {num} больше')
    else:
        print('Вы угадали!', end=' ')
        break
print(f'Было загадано число {GUESS_NUM}')