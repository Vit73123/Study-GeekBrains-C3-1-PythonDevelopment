# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
#
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
#
# На выходе:
#
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

# a = 1
# b = 'hello'
# c = [1, 2, 3]
# d = {}

# a = 42
# b = 'hello'
# c = 3.14
# d = 'world'

# a = None
# b = ''
# c = []
# d = {}

# Ответ:
# {'None': 'a', '': 'b', '[]': 'c', '{}': 'd'}

# a = True
# b = False
# c = True
# d = False

# Ответ:
# {True: 'c', 'False': 'd'}

# name = 'Alice'
# age = 30
# scores = [85, 90, 78]
# info = {'city': 'New York', 'email': 'alice@example.com'}


def key_params(**kwargs) -> dict:
    r = {}
    for k, v in kwargs.items():
        # Применение "магического метода" __hash__ для проверки существования хэша, чтобы не применять функцию hash(),
        # т.к. hash() выбрасывает исключение, если у объекта нет такого метода
        # Это применяется для проверки того, является ли тип неизменяемым (имеет метод __hash__)
        # Если объект неизменяемый, то у него нет метода __hash__ (функция hash() выбросит исключение)
        # У None есть метод __hash__, поэтому дополнительно надо проверять объект на его существование,
        # т.е. делать проверку is not None (a != null - в Java)
        if v is not None and v.__hash__:
            r[v] = k
        else:
            r[str(v)] = k
    return r


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
params = key_params(a=None, b='', c=[], d={})
print(params)
params = key_params(a=True, b=False, c=True, d=False)
print(params)
