#  1. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

def has_positive_elements(matrix):
    positive_rows = [row for row in matrix if any(x > 0 for x in row)]
    return bool(positive_rows)

matrix = [[1, -2, -3], [-4, -5, -6], [-7, -8, -9]]  # матрица
print(has_positive_elements(matrix))  # вывод


