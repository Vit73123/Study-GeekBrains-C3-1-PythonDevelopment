# 📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.
from string import ascii_letters, punctuation

CORRECT_CHARS = ascii_letters + " "

def clear_text(text: str) -> str:
    """
    Удаляет лишние символы из строки с кириллицей
    """
    return "".join([c for c in text if c in CORRECT_CHARS]).lower()


if __name__ == "__main__":
    print(clear_text("JSDLKJ123 JD ФЫВ!!Я!, АЦSJI3 L"))