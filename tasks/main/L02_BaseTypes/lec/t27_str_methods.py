s = input("Введите текст: ")
if (s.isdecimal()):
    print(bin(int(s)))
    print(oct(int(s)))
    print(hex(int(s)))
elif (s.isascii):
    print("Строка в ASCII")