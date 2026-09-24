import sqlite3
from config import bot
from config import SERVICE_CHANNEL_ID


def file_id(id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT message_id FROM media WHERE id = (?)""", (id,))
    message_id = cursor.fetchone()
    cursor.execute("""SELECT chat_id FROM media WHERE id = (?)""", (id,))
    chat_id = cursor.fetchone()

    message = bot.forward_message(
        chat_id=SERVICE_CHANNEL_ID,
        from_chat_id=chat_id,
        message_id=message_id
    )

    try:
        photo = message.photo[-1] # type: ignore
        file_id = photo.file_id
    except:
        return None


    connection.close()

    return file_id


def balance(user_id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT balance FROM users WHERE id = (?)""", (user_id,))

    balance = cursor.fetchone()

    connection.close()

    return balance[0]


def coefficient(media_id):
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT coefficient FROM media WHERE id = (?)""", (media_id,))

    coefficient = cursor.fetchone()

    connection.close()

    return coefficient[0]