import sqlite3

connection = sqlite3.connect('product.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()


def insert_product(id_product, title, description, price):
    check_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (id_product,))
    if check_product.fetchone() is None:
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (f'{id_product}', f'{title}', f'{description}', f'{price}'))
        connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000'))
    connection.commit()


def is_included(username):
    check_username = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    connection.commit()
    if check_username.fetchone() is None:
        return False
    else:
        return True


def get_all_products():
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


initiate_db()

insert_product(1, 'Продукт 1', 'Мультивитамины', 100)
insert_product(2, 'Продукт 2', 'В-комлекс', 200)
insert_product(3, 'Продукт 3', 'Омега-3', 300)
insert_product(4, 'Продукт 4', 'Кальций, Витамин D', 400)

cursor.execute('DELETE FROM Users WHERE id = ?', (1,))
connection.commit()
