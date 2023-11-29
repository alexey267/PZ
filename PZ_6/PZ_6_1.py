# Вариант 32
# 1. Дан список размера N. Поменять местами его минимальный и максимальный
# элементы.
import random  # импорт библиотеки

a = input('введите минимальный диапазон: ')
b = input('введите максимальный диапазон: ')
n = input('введите количество чисел в списке: ')

while True:  # фильтр ошибок
    try:
        a = int(a)
        b = int(b)
        n = int(n)
        if a >= b:
            print('\n Минимальное значение слишком большое')
            raise ValueError  # принудительный вызов ошибки
        break

    except ValueError:  # сама инфа об ошибке
        print('Вы допустили ошибку! \n')
        a = input('введите минимальный диапазон: ')
        b = input('введите максимальный диапазон: ')
        n = input('введите количество чисел в списке: ')

c = []

for i in range(n):  # цикл в диапазоне N (после остановка)
    numbers = random.randint(a, b)
    c.append(numbers)

print('Исходный список:', c)

mini = min(c)
maxi = max(c)

min_index = c.index(mini)
max_index = c.index(maxi)

c[min_index] = maxi
c[max_index] = mini

print('Конечный список:', c)
