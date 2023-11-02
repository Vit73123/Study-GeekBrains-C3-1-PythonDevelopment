# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

hike = {
    "Aaz": ("спички", "спальник", "дрова", "топор"),
    "Skeeve": ("спальник", "спички", "вода", "еда"),
    "Tananda": ("вода", "спички", "косметика"),
}

temp_bag = None
# Пересечение множеств, чтобы получить все элементы, встречающиеся в разных кортежах
for things in hike.values():
    if not temp_bag:
        temp_bag = set(things)
        continue
    temp_bag = temp_bag.intersection(set(things))
print(temp_bag)

# Для примера - наполняем СПИСОК из КОРТЕЖЕЙ - append()
# Объединенить (temp_o) и вычесть (temp) множества, чтобы получить не встречающиеся элементы
result_uniq = []
for name, things in hike.items():
    temp = set(things)
    temp_o = set()
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.union(set(other))
    temp = temp.difference(temp_o)
    if temp:
        result_uniq.append((name, temp))
print(result_uniq)

# Для примера - наполняем СЛОВАРЬ - update()
res_missing = {}
for name, things in hike.items():
    temp = set(things)
    for other in hike.values():
        if things == other:
            continue
        temp_o = temp_o.intersection(set(other))
    temp = temp_o.difference((temp))
    if temp:
        res_missing.update({name: temp})
print(res_missing)