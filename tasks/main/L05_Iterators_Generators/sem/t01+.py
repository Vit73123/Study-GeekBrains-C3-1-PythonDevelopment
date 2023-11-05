# ✔ Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔ второе и третье число являются ключами.
# ✔ первое число является значением для первого ключа.
# ✔ четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.

in_line = "1/2/3/4/5/6/7/8"

# Распаковывание
a, b, c, *d = in_line.split('/')

# Создание кортежа из распакованного списка
in_dic = {b: a, c: (*d,)}
# in_dic = {b: a, c: tuple(*d)}
print(in_dic)