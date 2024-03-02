# Вариант 32.
# 1.В последовательности на n целых чисел умножить все элементы на первый
# максимальный элемент.
import random

def multiply_sequence(numbers):
    max_element = max(numbers)

    # Списковое включение
    multiplied_seq = [n * max_element for n in numbers]
    yield from multiplied_seq


# Пример использования функции
sequence = [random.randint(-10, 50) for _ in range(5)]
print(sequence)
result = multiply_sequence(sequence)
result_list = list(result)
print(f'Максимальный элемент: {max(sequence)} \n')

# Вывод результата
for num in result_list:
    print(num)


