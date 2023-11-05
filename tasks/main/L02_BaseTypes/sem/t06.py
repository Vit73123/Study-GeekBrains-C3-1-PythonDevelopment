# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0
BALANCE_TAX_LIMIT = 5_000_000

counter = 1
while True:
    mode = input("Введите операцию 1-пополнение, 2-снятие, 3-выход: ")
    if balance >= BALANCE_TAX_LIMIT:
        balance *= 0.9
    if mode == '1':
        withdraw = int(input('Сумма пополнения: '))
        if withdraw % 50 != 0:
            continue
        balance += withdraw
        counter += 1
    elif mode == '2':
        outdraw = int(input('Сумма снятия: '))
        if outdraw % 50 != 0:
            continue
        comission = outdraw * 0.015
        if comission < 30:
            comission = 30
        elif comission > 600:
            comission = 600
        if outdraw + comission < balance:
            balance -= (outdraw + comission)
        counter += 1
    elif mode == '3':
        break
    if counter % 3 == 0:
        balance *= 1.03

    print(balance)
