# На вход программе подаётся два списка, каждый из которых содержит 10 различных целых чисел
# Первый список ваш лотерейный билет
# Второой список содержит список чисел, которые выпали в лотерею
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

count = 0
for item in list1:
    if item in list2:
        count += 1
print(f'Количество совпадающих чисел: {count}')

print(sorted(list1))
print(sorted(list2))