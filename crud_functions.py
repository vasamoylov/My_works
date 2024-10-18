import sqlite3


def initiate_db():
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    connection.commit()
    connection.close()


def insert_product(id_product, title, description, price):
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    check_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (id_product,))
    if check_product is None:
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{id_product}', f'{title}', f'{description}', f'{price}'))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


initiate_db()

insert_product(1, 'Продукт 1', 'Мультивитамины', 100)
insert_product(2, 'Продукт 2', 'В-комлекс', 200)
insert_product(3, 'Продукт 3', 'Омега-3', 300)
insert_product(4, 'Продукт 4', 'Кальций, Витамин D', 400)
