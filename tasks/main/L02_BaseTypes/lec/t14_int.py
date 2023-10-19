# PEP-8! При указании значений для ключевых аргументов функции
# пробелы вокруг знака равенства не ставятся.

# ✔ bin(x) — преобразует целое число в двоичную строку с префиксом «0b».
# ✔ oct(x) — преобразует целое число в восьмеричную строку с префиксом «0o».
# ✔ hex(x) — преобразует целое число в строчную шестнадцатеричную строку с префиксом «0x».

x = int("42")
y = int(3.1415)
z = int("hello", base=30)
print(x, y, z, sep='\n')