import sqlite3


def new_user(user_id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))

    connection.commit()
    connection.close()


def new_media(file_id, file_unique_id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO media (file_id, file_unique_id) VALUES (?, ?)",
        (file_id, file_unique_id),
    )

    connection.commit()

    cursor.execute("SELECT id FROM media WHERE (file_id) = (?)", (file_id,))
    id = cursor.fetchone()

    connection.close()

    return id[0]
