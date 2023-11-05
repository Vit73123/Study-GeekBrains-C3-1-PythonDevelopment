# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

in_line = 'a11sssddfffqqqwweeeerr'

res_chars_dic = {c: ord(c) for c in in_line}
print(res_chars_dic)

# Нет решения:
# res_dic_line = ''
# res_dic_line.join({k: v for k, v in res_chars_dic.items()})
# print(res_dic_line)

