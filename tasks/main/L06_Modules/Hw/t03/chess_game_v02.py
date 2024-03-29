# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные
# случайные варианты и выведите 4 успешных расстановки.
#
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся
# на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
#
# Пример использования На входе:
#
# print(generate_boards())
#
# На выходе:
#
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
#  [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
#  [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
#


from itertools import combinations
from random import randint

MAX_QUEENS = 8
MAX_ATTEMPTS = 100_000
SIZE = 8
SUCCESS_BOARDS = 4


def is_attacking(q1: (int, int), q2: (int, int)) -> bool:
    '''
    Проверяет, бьют ли ферзи друг друга

    :param q1:
    :param q2:
    :return:
    '''
    return (q1[0] == q2[0]
            or q1[1] == q2[1]
            or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]))


def check_queens(queens: []) -> bool:
    '''
    Проверяет все возможные пары ферзей

    :param queens:
    :return:
    '''
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


def generate_boards() -> []:
    '''
    Использует генератор случайных чисел для случайной расстановки ферзей.
    Проверяет различные случайные варианты и выводит (сохраняет в общем списке комбинаций координат)
    4 успешных расстановки.

    Под "успешной расстановкой ферзей" в подразумевается такая расстановка ферзей на шахматной доске,
    в которой ни один ферзь не бьет другого,
    т.е. ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.

    :return:
    '''
    board_list = []

    for attempt in range(MAX_ATTEMPTS):
        if len(board_list) == SUCCESS_BOARDS:
            break
        queens = set()
        while len(queens) < MAX_QUEENS:
            queens.add((randint(1, SIZE), randint(1, SIZE)))
        if check_queens(queens):
            board_list.append(list(queens))
            print(queens)
            # print('----------------- SUCCESS -----------------')
    return board_list

if __name__ == '__main__':
    print(generate_boards())
