from PIL import Image
import io


def router(file, file_type, mode: str = "default"):
    match [file_type, mode]:
        case ["photo", "default"]:
            return photo_default(file)


def photo_default(photo):
    image = Image.open(photo)

    width = image.width
    height = image.height

    image = image.resize(size=(round(width * 0.2), round(height * 0.2)))

    photo.seek(0)

    image.save(photo, format="JPEG")
    image.close()

    photo.seek(0)

    return photo
