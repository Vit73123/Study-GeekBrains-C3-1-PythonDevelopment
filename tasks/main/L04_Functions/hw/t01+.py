# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
#
# Пример использования На входе:
#
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
#
# На выходе:
#
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# zip() для транспонирования матрицы
def transpose(matrix) -> list:
    return [list(row) for row in zip(*matrix)]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)
