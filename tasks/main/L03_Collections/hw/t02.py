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

# text = 'Hello world. Hello Python. Hello again.'
# text = 'This is a sample text without repeating words.'
# text = "Python 3.9 is the latest version of Python. It's awesome!"
# [('python', 2), ('is', 1), ('the', 1), ('latest', 1), ('version', 1), ('of', 1), ('it', 1), ('s', 1), ('awesome', 1)]
# text = 'Python is python, is, IS, and PYTHON.'
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
# [('and', 3), ('python', 2), ('language', 2), ('code', 2), ('its', 2), ('is', 1), ('an', 1), ('interpreted', 1), ('high', 1), ('level', 1)]
# text = "Hello    don't5  123 1didn't Hello"

signs = "!()-[]{};?@#$%:'\"\\,./^&;*_'0123456789"

new_text = text
for sign in signs:
    new_text = new_text.replace(sign, ' ')
new_text = new_text.lower()

words = {word: None for word in new_text.split()}

has_first = False
has_last = False
for word in words:
    count = new_text.count(' ' + word + ' ')
    if not has_first and new_text.startswith(word + ' '):
        count += 1
    if not has_last and new_text.endswith(' ' + word):
        count += 1
    words[word] = count

print(sorted(words.items(), key=lambda x: x[1], reverse=True)[:10])

# print()
# print(text)
# print(new_text)
# print(new_text.split())
# print(set(new_text.split()))
# print(words, end='\n\n')
