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

    size = width * height
    intensity = 0.03
    power = 0.38

    coefficient = intensity * (size ** power)
    coefficient = max(2, round(coefficient))

    image = image.resize(size=(width // coefficient, height // coefficient))

    photo.seek(0)

    image.save(photo, format="JPEG")
    image.close()

    photo.seek(0)

    return photo
