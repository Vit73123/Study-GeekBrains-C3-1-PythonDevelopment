# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

def inplace_buble_sort(nums: list) -> None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                # Поменять местами элементы
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 10, 22, 6]
    inplace_buble_sort(nums)
    print(nums)
