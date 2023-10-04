# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2

a = input('Введите число a: ')
b = input('Введите число b: ')

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

suma = a + b
if suma % 5 == 0:
    otvet = suma + 1
else:
    otvet = suma - 2

print('Ответ: ', otvet)
