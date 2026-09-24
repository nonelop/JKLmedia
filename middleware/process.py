from config import bot
import time
from interface import menu
from core import shakalizator
from middleware import write

def photo(mode, photo, photo_id, message, coefficient):
    match mode:
        case "shakal":
            start_time = time.time()
            
            menu.process_photo_menu(
                chat_id=message.chat.id,
                message_to_edit_id=message.message_id,
                process_mode="Шакал"
            )

            write.new_coefficient(photo_id, coefficient)

            processed_photo = shakalizator.router(
                file=photo, file_type="photo", mode="default", coefficient=coefficient
            )

            if isinstance(processed_photo, str):

                bot.edit_message_caption(
                    chat_id=message.chat.id,
                    message_id=message.message_id,
                    caption=f"Ошибка: {processed_photo}"
                )

                return

            ends_time = time.time()

            menu.done_photo_menu(
                chat_id=message.chat.id,
                message_to_edit_id=message.message_id,
                photo=processed_photo,
                photo_id=photo_id,
                process_time=ends_time - start_time,
            )

            return