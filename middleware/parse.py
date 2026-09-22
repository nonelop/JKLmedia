from config import bot
from middleware import get
from PIL import Image


def media_id_to_file(media_id):
    file_id = get.file_id(media_id)
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    return bot.download_file(str(file_path))

def photo_to_size(photo):
    image = Image.open(photo)

    width = image.width
    height = image.height

    return (width, height)