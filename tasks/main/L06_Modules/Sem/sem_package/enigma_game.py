# Задание 4
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Задание 5
# 📌 Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Задание 6
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
# с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

__all__ = ['enigma_game', 'show_results']


_result = {}


# Задание 4
def enigma_game(
        enigma: str,
        answers: set,
        attempts: int
) -> int:
    '''
    Получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
    Возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

    :param enigma:
    :param answers:
    :param attempts:
    :return:
    '''
    print(enigma)
    for attempt in range(attempts):
        user_answer = input("Ваш ответ: ")
        if user_answer.lower() in answers:
            result = attempt + 1
            break
    else:
        result = 0
    __save_results(enigma=enigma, attempts=result)
    return result


# Задание 5
def __demo_game():
    '''
    Хранит словарь множеств.
    Ключ словаря - загадка, значение - список с отгадками.
    Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

    :return:
    '''
    enigmas = {
        'Зимой и летом одним цветом': {'ель', 'ёлка', 'сосна'},
        'Не лает, не кусает, в дом не пускают': {'замок'},
        'Сидит дед во сто шуб одет': {'лук', 'луковица'},
    }

    for e, ans in enigmas.items():
        enigma_game(e, ans, 3)


# Задание 6
def __save_results(enigma: str, attempts: int):
    global _result
    _result[enigma] = attempts

def show_results():
    global _result
    print('---------------------- reults ----------------------')
    for k, v in _result.items():
        print(k, v)


if __name__ == "__main__":
    # print(enigma_game("Зимой и летом одним цветом", {"ель", "елка", "ёлка"}, 2))
    __demo_game()
    show_results()