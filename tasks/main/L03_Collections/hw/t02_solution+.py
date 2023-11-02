# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами, апостроф не считается за пробел. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Отсортируйте по убыванию значения количества повторяющихся слов.
#
# Пример
#
# На входе:
#
# text = 'Hello world. Hello Python. Hello again.'
#
# На выходе:
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

import re
from collections import Counter

# text = 'Hello world. Hello Python. Hello again.'
# text = 'This is a sample text without repeating words.'
# text = "Python 3.9 is the latest version of Python. It's awesome!"
# [('python', 2), ('is', 1), ('the', 1), ('latest', 1), ('version', 1), ('of', 1), ('it', 1), ('s', 1), ('awesome', 1)]
# text = 'Python is python, is, IS, and PYTHON.'
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# [('and', 3), ('python', 2), ('language', 2), ('code', 2), ('its', 2), ('is', 1), ('an', 1), ('interpreted', 1), ('high', 1), ('level', 1)]
# text = "Hello    don't5  123 1didn't Hello"

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)
