#  В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # матрица

N = int(input("Введите номер строки: "))  # ввод

def calculate_row_sum(matrix, N):
    yield sum(matrix[N])

def calculate_row_product(matrix, N):  # генератор
    product = 1
    for num in matrix[N]:
        product *= num
        yield product

row_sum = None
row_product = None

for result in calculate_row_sum(matrix, N):
    row_sum = result

for result in calculate_row_product(matrix, N):
    row_product = result

print("Сумма элементов строки:", row_sum)
print("Произведение элементов строки:", row_product)
