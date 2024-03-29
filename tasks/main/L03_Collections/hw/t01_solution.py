# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
#
# Пример
#
# На входе:
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
# На выходе:
#
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0

items = {
    "лодка": 3.0,
    "велосипед": 4.0,
    "мангал": 2.0
}
max_weight = 2.0

# items = {
#     "спальник": 1.5,
#     "палатка": 3.2,
#     "термос": 0.6,
#     "карта": 0.1,
#     "фонарик": 0.3,
#     "котелок": 0.8,
#     "еда": 2.5,
#     "одежда": 1.7,
#     "обувь": 1.2,
#     "нож": 0.2
# }
# max_weight = 1.0

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
