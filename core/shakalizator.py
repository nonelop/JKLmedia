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

    if size >= 1_000_000:
        coefficient = 15
    elif size <= 1_000_000 and size >= 500_000:
        coefficient = 10
    else:
        coefficient = 5

    image = image.resize(size=(width // coefficient, height // coefficient))

    photo.seek(0)

    image.save(photo, format="JPEG")
    image.close()

    photo.seek(0)

    return photo
