# 2.Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

def get_punctuation_chars(text):
    # Списковое включение
    punctuation_chars = [char for char in text if char in string.punctuation]
    yield from punctuation_chars

my_string = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
punctuation_chars = get_punctuation_chars(my_string)
print(list(punctuation_chars))
