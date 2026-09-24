from PIL import Image
from config import DEFAULT_SHAKAL_COEFFICIENT


def router(file, file_type, coefficient = DEFAULT_SHAKAL_COEFFICIENT, mode: str = "default"):
    match [file_type, mode]:
        case ["photo", "default"]:
            return photo_default(file, coefficient)


def photo_default(photo, power):

    try:
        image = Image.open(photo)

        width = image.width
        height = image.height

        size = width * height
        intensity = 0.03

        coefficient = intensity * (size ** power)
        coefficient = max(2, round(coefficient))

        image = image.resize(size=(width // coefficient, height // coefficient))

        photo.seek(0)

        image.save(photo, format="JPEG")
        image.close()

        photo.seek(0)

        return photo

    except Exception as e:

        return str(e)
