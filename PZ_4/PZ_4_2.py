# Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
# деления, найти количество и сумму его цифр.

colichestvo = 0
summa = 0
N = input('Введите число N (больше нуля): ')

while True:  # точка фильтрации
    try:
        N = int(N)
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("Вы не прошли фильтрацию, введите другое число!")
        N = input('Введите снова число N (больше нуля): ')

while N > 0:  # пока N больше 0
    A = N % 10
    colichestvo = colichestvo + 1
    summa = summa + A
    N = N // 10

    if N == 0:  # если N == 0, то ломаем цикл (так проверяет пока новый подсчет не прийдет к целому 0)
        break

print(f'Количество цифр: {colichestvo}')
print(f'Сумма цифр: {summa}')
