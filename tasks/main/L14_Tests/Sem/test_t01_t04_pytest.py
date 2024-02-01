# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import pytest
from t01 import clear_text


def test_no_changes():
    assert clear_text("hello world") == 'hello world'

def test_register_change():
    base_text = "hello world"
    test_strings = {base_text.replace(c, c.upper()) for c in base_text}
    for test_str in test_strings:
        assert clear_text(test_str) == 'hello world'

def test_punctuation_delete():
    assert clear_text("hello world!") == 'hello world'

def test_nonlatin_alphabets():
    assert clear_text("hello world Привет Мир") == 'hello world  '

def test_all_conditions():
    assert clear_text("Hello World! Привет Мир 123") == 'hello world   '


if __name__ == "__main__":
    pytest.main(verbosity=4)