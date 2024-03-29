# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


# Использование справочной информации о функции
def words_list(in_str: str):
    '''
Выводит каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

:param in_str: str
:return: None
    '''
    # Цепочка вызова методов для преобразования строки, разеделния на слова и их сортировки
    words = sorted(''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in in_str).split())
    max_len = len(max(words, key=len)) + 1
    for i, word in enumerate(words, 1):
        print(f'{i:>2}{word:>{max_len}}')


words_list(
    '''# ✔ Напишите функцию, которая принимает строку текста.
    Вывести функцией каждое слово с новой строки.
    ✔ Строки нумеруются начиная с единицы.
    ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.''')

# Вывод справочной информации о функции с помощью дандер-переменной __doc__
print(words_list.__doc__)