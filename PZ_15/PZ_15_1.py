# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.

import sqlite3

# подключение к БД
conn = sqlite3.connect('wholesale.db')
# создание курсора
c = conn.cursor()

# создание таблицы
c.execute("""CREATE TABLE IF NOT EXISTS products (
            product_code text,
            product_name text,
            shop_name text,
            shop_requests text,
            quantity_in_stock integer,
            unit_of_measure text,
            wholesale_price real
)""")
# коммит действия
conn.commit()

# После создания таблицы и перед добавлением начальных данных
c.execute("SELECT  *  FROM products")
for row in c.fetchall():
    print(row)


def add_initial_data():
    # Проверяем, есть ли уже продукты в базе. Если есть, мы не добавляем новые.
    c.execute('SELECT * FROM products')
    if c.fetchall():
        return

    # Предполагаем, что у нас есть список продуктов, которые мы хотим добавить
    products = [
        {'product_code': str(i), 'product_name': f'Товар {i}', 'shop_name': 'Пятерочка', 'shop_requests': i, 'quantity_in_stock': i, 'unit_of_measure': 'шт', 'wholesale_price': i} for i in range(1, 11)
    ]

    # Добавляем продукты в базу данных
    for product in products:
        c.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)", list(product.values()))
    conn.commit()

add_initial_data()


def insert_product():
    product_code = input("Введите код товара: ")
    product_name = input("Введите наименование товара: ")
    shop_name = input("Введите наименование магазина: ")
    shop_requests = input("Введите заявку магазина: ")
    quantity_in_stock = int(input("Введите количество товара на складе: "))
    unit_of_measure = input("Введите единицы измерения: ")
    wholesale_price = float(input("Введите оптовую цену: "))
    c.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)",
              (product_code, product_name, shop_name, shop_requests, quantity_in_stock, unit_of_measure, wholesale_price))
    conn.commit()

def find_product():
        product_code = input("Введите код товара: ")
        c.execute("SELECT * FROM products WHERE product_code = ?", (product_code,))
        product = c.fetchone()

        print(f'------------'
              f'(ID: {product[0]}) \n'
              f'Наименование: {product[1]} \n'
              f'Магазин: {product[2]} \n'
              f'Заявка: {product[3]} \n'
              f'Количество: {product[4]} \n'
              f'единицы: {product[5]} \n'
              f'Цена: {product[6]} \n'
              f'------------------')


def update_product():
    product_code = input("Введите код товара: ")
    quantity_in_stock = int(input("Введите новое количество товара на складе: "))
    c.execute("UPDATE products SET quantity_in_stock = ? WHERE product_code = ?", (quantity_in_stock, product_code))
    conn.commit()

def delete_product():
    product_code = input("Введите код товара: ")
    c.execute("DELETE from products WHERE product_code = ?", (product_code,))
    conn.commit()

def main():
    while True:
        print("""
        1.Добавить продукт
        2.Найти продукт
        3.Обновить продукт
        4.Удалить продукт
        5.Выход
        """)
        user_choice = input("Выберите действие: ")
        if user_choice == '1':
            insert_product()
        elif user_choice == '2':
            find_product()
        elif user_choice == '3':
            update_product()
        elif user_choice == '4':
            delete_product()
        elif user_choice == '5':
            break

if __name__ == '__main__':
    main()
