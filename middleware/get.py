import sqlite3


def file_id(id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT file_id FROM media WHERE id = (?)""", (id,))

    file_id = cursor.fetchone()

    connection.close()

    return file_id[0]


def balance(user_id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT balance FROM users WHERE id = (?)""", (user_id,))

    balance = cursor.fetchone()

    connection.close()

    return balance[0]
