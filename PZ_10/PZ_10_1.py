#  Вариант 32.
# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}

# Полный список всех товаров
full_list = magnit.union(pyaterochka, perekrestok)
print("Полный список товаров: ", full_list)

# Магазины, где можно приобрести молоко и сыр
milk_and_cheese_stores = []

if 'молоко' in magnit and 'сыр' in magnit:
    milk_and_cheese_stores.append('Магнит')
if 'молоко' in pyaterochka and 'сыр' in pyaterochka:
    milk_and_cheese_stores.append('Пятерочка')
if 'молоко' in perekrestok and 'сыр' in perekrestok:
    milk_and_cheese_stores.append('Перекресток')

print("Магазины, где можно приобрести молоко и сыр: ", milk_and_cheese_stores)

# Магазины, где можно приобрести сахар
stores_with_sugar = []

if 'сахар' in magnit:
    stores_with_sugar.append('Магнит')
if 'сахар' in pyaterochka:
    stores_with_sugar.append('Пятерочка')
if 'сахар' in perekrestok:
    stores_with_sugar.append('Перекресток')

print("Магазины, где можно приобрести сахар: ", stores_with_sugar)
