#  В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры)
import random

matrix = [[random.randint(-100, 100) for _ in range(3)] for _ in range(3)]  # генератор матрицы
for row in matrix:
    print(row)  # матрица

N = int(input("Введите номер строки: "))  # ввод

row = matrix[N]
row_sum = sum([x for x in row])
row_product = sum([x * y for x, y in zip(row, row)])

# Print the results
print(f"Сумма: {row_sum}")
print(f"Произведение: {row_product}")
