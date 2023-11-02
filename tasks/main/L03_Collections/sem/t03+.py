# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (1, "2", [1, 2, 3], True, 1.33, 2, "4", min, max)
result = {}

for element in data:
    # Применяется сложение списков: [] + [element]
    result[(type(element))] = result.get(type(element), []) + [element]
print(result)