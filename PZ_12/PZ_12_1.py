# Вариант 32.
# 1.В последовательности на n целых чисел умножить все элементы на первый
# максимальный элемент.
# реализовать с использованием списковых включений, итераторов,
# генераторов

def multiply_sequence(numbers):
    max_element = max(numbers)

    # Списковое включение
    multiplied_seq = [n * max_element for n in numbers]
    yield from multiplied_seq


# Пример использования функции
sequence = [2, 8, 3, 1, 5]
result = multiply_sequence(sequence)
result_list = list(result)
result_list = list(dict.fromkeys(result_list))
print(f'Максимальный элемент: {max(sequence)} \n')

# Вывод результата
for num in result_list:
    print(num)


