# 2. Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно вставив после каждой
# строки строку из символов «*».
import string

# Чтение содержимого файла
with open('text18-32.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

# Вывод содержимого файла
for line in content:
    print(line.strip())

# Расчет количества знаков пунктуации в первых четырех строках
punctuation_count = 0
for i in range(4):
    line = content[i]
    punctuation_count += sum(1 for char in line if char in string.punctuation)

# Вывод количества знаков пунктуации
punctuation_count -= 1
print("Количество знаков пунктуации в первых четырех строках:", punctuation_count)

# Создание нового файла с текстом в стихотворной форме
with open('output1.txt', 'w', encoding='utf-8') as output_file:
    for line in content:
        output_file.write(line.strip() + "\n")
        output_file.write("******\n")
