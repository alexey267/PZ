# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
#  перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().
#  удалить файл test.txt.

import os
import shutil
import tkinter as tk
from tkinter import messagebox, scrolledtext

def perform_operations():
    results.delete(1.0, tk.END)  # Очистить предыдущие результаты

    try:
        # Перейти в каталог PZ11 и вывести список всех файлов
        os.chdir('C:\\Users\\User861\\Desktop\\PZ\\PZ_11')
        all_files = [f for f in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), f))]
        results.insert(tk.END, "Список всех файлов в каталоге PZ11:\n")
        results.insert(tk.END, f"{all_files}\n\n")

        # Перейти в корень проекта
        os.chdir('C:\\Users\\User861\\Desktop\\PZ')

        # Создать папку с именем test и вложенную папку test1
        if not os.path.exists('test'):
            os.mkdir('test')
        if not os.path.exists(os.path.join('test', 'test1')):
            os.mkdir(os.path.join('test', 'test1'))

        # Переместить два файла из ПЗ6 в папку test
        shutil.move('PZ_6/PZ_6_1.py', 'test/PZ_6_1.py')
        shutil.move('PZ_6/PZ_6_2.py', 'test/PZ_6_2.py')

        # Переместить один файл из ПЗ7 в папку test1 и переименовать его в test.txt
        shutil.move('PZ_7/PZ_7_1.py', 'test/test1/test.txt')

        # Вывести информацию о размере файлов в папке test
        results.insert(tk.END, "Информация о размере файлов в папке test:\n")
        for filename in os.listdir('test'):
            filepath = os.path.join('test', filename)
            if os.path.isfile(filepath):
                results.insert(tk.END, f"{filename}: {os.path.getsize(filepath)} bytes\n")

        # Перейти в папку с PZ11 и найти файл с самым коротким именем
        os.chdir('C:\\Users\\User861\\Desktop\\PZ\\PZ_11')
        shortest_file = min((f for f in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), f))),
                            key=lambda f: len(os.path.basename(f)))
        results.insert(tk.END, "\nФайл с самым коротким именем в PZ11:\n")
        results.insert(tk.END, f"{shortest_file}\n\n")

        # Перейти в любую папку где есть отчет в формате .pdf и «запустить» файл
        pdf_file_path = 'C:\\Users\\User861\\Desktop\\PZ\\reports\\report PZ_3.pdf'
        if os.path.exists(pdf_file_path):
            os.startfile(pdf_file_path)

        # Удаление файла test.txt из папки test1
        os.remove('C:\\Users\\User861\\Desktop\\PZ\\test\\test1\\test.txt')

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Выполнение операций")

# Кнопка для запуска выполнения операций
perform_button = tk.Button(root, text="Выполнить операции", command=perform_operations)
perform_button.pack(pady=10)

# Окно для отображения результатов
results = scrolledtext.ScrolledText(root, width=80, height=20)
results.pack(padx=10, pady=10)

root.mainloop()
