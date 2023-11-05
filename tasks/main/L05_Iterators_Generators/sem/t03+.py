# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

in_line = 'a11sssddfffqqqwweeeerr'

in_chars_dic = {c: ord(c) for c in in_line}
print(in_chars_dic)

# Вывод только ключей
# Применение _ - неиспользуемой переменной как счётчика цикла
in_iter = iter(in_chars_dic)

for _ in range(5):
    print(next(in_iter))

# Вывод ключей и значений
# Применение _ - неиспользуемой переменной как счётчика цикла
in_iter = iter(in_chars_dic.items())

for _ in range(5):
    print(next(in_iter))

# Распаковка итератора - вывод всех элементов
print(*in_iter)