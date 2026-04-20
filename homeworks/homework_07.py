import sqlite3


conn = sqlite3.connect("store.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

conn.commit()


def create_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))
    conn.commit()


def read_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


def update_product(product_id, price):
    cursor.execute("""
    UPDATE products
    SET price = ?
    WHERE id = ?
    """, (price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute("""
    DELETE FROM products
    WHERE id = ?
    """, (product_id,))
    conn.commit()


def close_connection():
    conn.close()

create_product("Test", 10, 5)
print(read_products())