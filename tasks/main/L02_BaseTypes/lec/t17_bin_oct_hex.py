# PEP-8! В качестве имени переменной мы использовали латинскую строчную "o".
# Это допустимое имя. Но никогда не используйте символы 'l' (строчная буква "л"), 'O'
# (заглавная буква "О") или 'I' (заглавная буква "Ай") в качестве имен переменных,
# состоящих из одного символа. В некоторых шрифтах эти символы неотличимы от цифр
# один и ноль.

# 0b — двоичное
# 0o — восьмеричное
# 0x — шестнадцатеричное представление

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)