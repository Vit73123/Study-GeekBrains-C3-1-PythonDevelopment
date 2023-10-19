# Для проверки типа можно вызывать функцию type() и сравнить значение с результатом.
# Но документация к языку не рекомендует так делать.
# Для получения информации о типе объекта правильно использовать функцию
# isinstance().

# isinstance(object, classinfo)

data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

# Функция принимает 2 аргумента.
# Второй аргумент — кортеж, внутри которого через запятую перечислены 3 класса.

data = 3.14
print(isinstance(data, (int, float, complex)))