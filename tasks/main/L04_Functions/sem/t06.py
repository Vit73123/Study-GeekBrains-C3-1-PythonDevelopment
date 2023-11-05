# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_by_index(nums: list, start: int, stop: int):
    '''
    # ✔ Получает на вход список чисел и два индекса.
    # ✔ Возвращает сумму чисел между между переданными индексами.
    # ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

    :param nums:
    :param start:
    :param stop:
    :return:
    '''
    if stop < start:
        stop, start = start, start
    if start < 0:
        start = 0
    if start > len(nums) - 1:
        stop = len(nums) - 1
    return sum(nums[start:stop + 1])


if __name__ == "__main__":
    print(sum_by_index([1, 2, 3, 4, 5, 6], 0, 1000))
    print(sum_by_index([1, 2, 3, 4, 5, 6], 2, 3))
