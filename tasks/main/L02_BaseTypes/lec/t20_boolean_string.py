# Неявное преобразование boolean -> string
# Функция bool() (явное преобразование) не используется

name = input('Как вас зовут? ')

# Если name - пустая строка, то это False
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, приветствую')