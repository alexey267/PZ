# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов.

import re
import chardet

with open('experience.txt', 'rb') as f:  # подбираем формат
  rawdata = f.read()
  result = chardet.detect(rawdata)
  encoding = result['encoding']

with open('experience.txt', encoding=encoding) as f:
  lines = f.readlines()


data = [match.group() for line in lines  # поиск совпадений
        for match in [re.search(r'(\d+ \w+)(\s+\d+ \w+)?$', line)]
        if match]


print(data)  # вывод списка
print(f'Количество сегментов: {len(data)}')  # количество сегментов списка
