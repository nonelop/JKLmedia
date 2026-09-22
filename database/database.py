import sqlite3


def init_database():
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        balance INT DEFAULT 300,
        watermark INT DEFAULT 1,
        unlimited INT DEFAULT 0
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS media (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id TEXT UNIQUE,
        file_unique_id TEXT UNIQUE
    )""")

    connection.commit()
    connection.close()
