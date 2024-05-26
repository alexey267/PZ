# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9
# я взял код с PZ_4_1
# ---------------------------------------------------------------------------------
# # Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
# # целые степени числа A от 1 до N
#
# A = input('Введите число A (можно не целое): ')
# N = input('Введите число N (больше нуля): ')
# B = 1
#
# while type(A) != float or type(N) != int or B <= N:  # [A != плавает], [N != целое], [1 <= N]
#     try:
#         A = float(A)
#         N = int(N)
#         if B <= N:  # если B меньше или равно N
#             print('\n', f'{A} возводим в степень {B} и получаем = {int(A ** B)}')
#         B = B + 1
#     except ValueError:
#         print('Вы ввели неправильно одно из чисел, исправьте!')
#         A = input('Введите число A (можно не целое): ')
#         N = input('Введите число (больше нуля): ')

import tkinter as tk
from tkinter import messagebox

def calculate_powers():
    try:
        A = float(entry_A.get())
        N = int(entry_N.get())
        if N <= 0:
            raise ValueError("N должно быть больше нуля.")

        results.delete("1.0", tk.END)  # Очистить предыдущие результаты
        for B in range(1, N + 1):
            result = A ** B
            results.insert(tk.END, f"{A} возведенное в степень {B} = {result}\n")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Возведение в степень")

# Ввод числа A
tk.Label(root, text="Введите число A (можно не целое):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Ввод числа N
tk.Label(root, text="Введите число N (больше нуля):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_N = tk.Entry(root)
entry_N.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Кнопка для выполнения вычисления
calculate_button = tk.Button(root, text="Вычислить", command=calculate_powers)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Окно для отображения результатов
results = tk.Text(root, height=10, width=40, wrap="word")
results.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
