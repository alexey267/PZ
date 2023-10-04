# Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.

a = input('Введите число a: ')
b = input('Введите число b: ')
c = input('Введите число с: ')

while type(a) != int:   # фильтр числа а
    try:
        a = int(a)
    except ValueError:
        print('Вы ввели неправильно число "а", исправьте!')
        a = input('Введите число a: ')

while type(b) != int:   # фильтр числа b
    try:
        b = int(b)
    except ValueError:
        print('Вы ввели неправильно число "b", исправьте!')
        b = input('Введите число b: ')

while type(c) != int:   # фильтр числа с
    try:
        c = int(c)
    except ValueError:
        print('Вы ввели неправильно число "b", исправьте!')
        c = input('Введите число b: ')

MIN = min(a, b, c)   # ищем минимум
MAX = max(a, b, c)   # ищем максимум

print('Минимальное число: ', MIN)
print('Минимальное число: ', MAX)
