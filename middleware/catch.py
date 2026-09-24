from middleware import process
from config import bot
from config import DEFAULT_SHAKAL_COEFFICIENT
from middleware import write
from middleware import parse

def photo(message, mode):
    if message.content_type == "photo":
        photo = message.photo[-1]
        file_id = photo.file_id
        file_unique_id = photo.file_unique_id

        photo_id = write.new_media(
            file_id, file_unique_id, message_id=message.message_id, chat_id=message.chat.id
        )

        photo = parse.media_id_to_file(photo_id)

        message = bot.send_photo(
            chat_id=message.chat.id,
            photo=file_id,
            caption="Получено фото"
        )

        process.photo(
            mode="shakal",
            photo=photo, 
            photo_id=photo_id, 
            message=message,
            coefficient=DEFAULT_SHAKAL_COEFFICIENT
        )