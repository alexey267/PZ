#  Вариант 32.
# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы последней трети:
# Индекс максимального элемента последней трети:

#  создание файлов
with open('file1.txt', 'w') as file1:
    file1.write('1 2 3 4 5')

with open('file2.txt', 'w') as file2:
    file2.write('-1 -2 -3 -4')

#  чтение файлов
with open('file1.txt', 'r') as file1:
    content1 = file1.read().split()

with open('file2.txt', 'r') as file2:
    content2 = file2.read().split()

# Объединение содержимого файлов
combined_content = content1 + content2

# Запись объединенного содержимого в новый файл
with open('output.txt', 'w') as output_file:
    # Запись элементов первого и второго файла
    output_file.write("Элементы первого файла: {}\n".format(content1))
    output_file.write("Элементы второго файла: {}\n".format(content2))

    # Запись количества элементов в первом и втором файле
    output_file.write("Количество элементов первого файла: {}\n".format(len(content1)))
    output_file.write("Количество элементов второго файла: {}\n".format(len(content2)))

    # Выборка последней трети элементов
    last_third = combined_content[-(len(combined_content)//3):]

    # Запись элементов последней трети
    output_file.write("Элементы последней трети: {}\n".format(last_third))

    # Поиск индекса максимального элемента в последней трети
    max_index = last_third.index(max(last_third))

    # Запись индекса максимального элемента
    output_file.write("Индекс максимального элемента последней трети: {}\n".format(max_index))
