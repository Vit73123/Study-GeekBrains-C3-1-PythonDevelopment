# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = 100000
if 1 < num <= 100_000:
    for i in range(2, num):
        if num // i == num / i:
            print(f'{num} является составным числом')
            exit()
    print(f'{num} является простым числом')
else:
    print('Число должно быть больше 1 и меньше 100000')