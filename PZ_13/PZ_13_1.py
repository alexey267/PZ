#  1. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random

def has_positive_elements(matrix):
    positive_rows = [row for row in matrix if any(x > 0 for x in row)]
    return bool(positive_rows)

matrix = [[random.randint(-100, 100) for _ in range(3)] for _ in range(3)]  # генератор матрицы
for row in matrix:
    print(row)

print(has_positive_elements(matrix))  # вывод


