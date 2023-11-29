# 2. Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен сумме элементов списка A с номерами от K
# до N.
import random  # импорт библиотеки

c = input('введите минимальный диапазон: ')
d = input('введите максимальный диапазон: ')
n = input('введите количество чисел в списке: ')

while True:  # фильтр ошибок
    try:
        c = int(c)
        d = int(d)
        n = int(n)
        if c >= d:
            print('\n Минимальное значение слишком большое')
            raise ValueError  # принудительный вызов ошибки
        break

    except ValueError:  # сама инфа об ошибке
        print('Вы допустили ошибку! \n')
        c = input('введите минимальный диапазон: ')
        d = input('введите максимальный диапазон: ')
        n = input('введите количество чисел в списке: ')

a = []
b = []

for i in range(n):  # цикл в диапазоне N (после остановка)
    numbers = random.randint(c, d)
    a.append(numbers)
print(f'Список А: {a}')

for k in range(n):
    suma = 0
    for j in range(k, n):
        suma = suma + a[j]
        b.append(suma)
b = b[:n]  # ограничение списка B
print(f'Список B: {b}')
