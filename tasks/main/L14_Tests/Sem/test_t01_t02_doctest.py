# 📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_letters

CORRECT_CHARS = ascii_letters + " "

def clear_text(text: str) -> str:
    """
    Удаляет лишние символы из строки с кириллицей

    >>> clear_text("hello world")
    'hello world'

    >>> clear_text("Hello World")
    'hello world'

    >>> clear_text("hello world!")
    'hello world'

    >>> clear_text("hello world Привет Мир")
    'hello world  '

    >>> clear_text("Hello World! Привет Мир 123")
    'hello world   '
    """
    return "".join([c for c in text if c in CORRECT_CHARS]).lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)