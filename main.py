from config import bot
from database import database
from interface import menu
from middleware import get
from middleware import write
from middleware import parse
from core import shakalizator
import io


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
                pass

            case ["user", "balance"]:
                menu.balance_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                    user_id=callback.from_user.id,
                )

            case ["process", "photo", "shakal", photo_id]:
                photo = parse.media_id_to_file(photo_id)

                menu.process_photo_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                    process_mode="Шакал"
                )

                processed_photo = shakalizator.router(
                    file=photo, file_type="photo", mode="default"
                )

                menu.done_photo_menu(
                    chat_id=callback.message.chat.id,
                    message_to_edit_id=callback.message.message_id,
                    photo=processed_photo,
                    photo_id=photo_id,
                    process_time=228,
                )


database.init_database()

print("Started")
bot.infinity_polling()
