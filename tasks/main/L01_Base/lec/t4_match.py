color = input('Твой любимый цвет: ')

# match, case не поддерживается в Python до v10

match color == 'красный':
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')