from config import bot
from database import database
from interface import menu
from middleware import get
from middleware import write
from middleware import parse
from middleware import process
from middleware import catch
from core import shakalizator
import io
import time
from telebot import types


@bot.message_handler(commands=["start"])
def start(message):

    write.new_user(message.from_user.id)
    menu.start_menu(chat_id=message.chat.id)


@bot.message_handler(content_types=["photo"])
def photo(message):

    photo = message.photo[-1]
    file_id = photo.file_id
    file_unique_id = photo.file_unique_id

    photo_id = write.new_media(
        file_id, file_unique_id, message_id=message.message_id, chat_id=message.chat.id
    )

    menu.recv_photo_menu(chat_id=message.chat.id, file_id=file_id, photo_id=photo_id)


@bot.callback_query_handler()
def callback(callback):
    bot.answer_callback_query(callback_query_id=callback.id)

    if isinstance(callback.data, str):
        match callback.data.split(":"):
            case ["menu", "start"]:
                bot.clear_step_handler_by_chat_id(
                    callback.message.chat.id
                )
                menu.start_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                )
            case ["menu", "variants"]:
                menu.variants_categories_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                )
            case ["menu", "variants", "photo"]:
                menu.variants_photos_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id
                )

            case ["user", "balance"]:
                menu.balance_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                    user_id=callback.from_user.id,
                )

            case ["process", "photo", "shakal"]:
                message = menu.shakal_photo_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id
                )
                if isinstance(message, types.Message):
                    bot.register_next_step_handler(
                        message=message,
                        callback=catch.photo,
                        mode="shakal"
                    )
            case ["process", "photo", "shakal", photo_id, coefficient]:
                photo = parse.media_id_to_file(photo_id)

                process.photo(
                    mode="shakal",
                    photo=photo,
                    photo_id=photo_id,
                    coefficient=float(coefficient),
                    message=callback.message,
                )


database.init_database()

print("Started")
bot.infinity_polling()
