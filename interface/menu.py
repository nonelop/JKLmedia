from config import bot
from interface import inline
from middleware import get
from telebot import types


def start_menu(chat_id, message_to_edit_id=None):
    with open("assets/taksa.jpg", "rb") as photo:
        if message_to_edit_id:
            bot.edit_message_media(
                chat_id=chat_id,
                message_id=message_to_edit_id,
                media=types.InputMediaPhoto(
                    media=types.InputFile(photo),
                    caption="JKL - Инструменты обработки медиа \n\nПришлите боту файл либо выберете вариант обработки кнопкой ниже",
                ),
                reply_markup=inline.start_inline(),
            )

        else:
            bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption="JKL - Инструменты обработки медиа \n\nПришлите боту файл либо выберете вариант обработки кнопкой ниже",
                reply_markup=inline.start_inline(),
            )


def recv_photo_menu(chat_id, file_id, photo_id):

    bot.send_photo(
        chat_id=chat_id,
        photo=file_id,
        caption="Получено фото",
        reply_markup=inline.recv_photo_inline(photo_id),
    )


def process_photo_menu(chat_id, message_to_edit_id, process_mode):

    bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_to_edit_id,
        caption=f"Обработка\n\nТип обработки: {process_mode}",
    )


def done_photo_menu(chat_id, message_to_edit_id, photo, photo_id, process_time):

    bot.edit_message_media(
        chat_id=chat_id,
        message_id=message_to_edit_id,
        media=types.InputMediaPhoto(
            media=types.InputFile(photo),
            caption=f"Фото обработанно.\n\nВремя на обработку: {process_time} сек."
        ),
        reply_markup=inline.done_shakal_photo_inline(photo_id)
    )


def variants_categories_menu(chat_id, message_to_edit_id):

    bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_to_edit_id,
        caption="Выберите категорию контента и вариант его обработки кноками ниже.",
        reply_markup=inline.variants_inline(),
    )


def balance_menu(chat_id, message_to_edit_id, user_id):

    balance = get.balance(user_id)

    bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_to_edit_id,
        caption=f"Ваш баланс: {balance} Кредитов.\n\nБаланс восстанавливается в 00:00 по МСК",
        reply_markup=inline.balance_inline(),
    )
