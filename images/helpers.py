import os

from PIL import Image

from config import settings
from images.models import Picture


def picture_resizer(picture, thumbnail_height):
    """Resize picture to a thumbnail of a given height and proportional width."""

    with Image.open(picture.url.path) as org_picture:
        width, height = org_picture.size
        thumbnail_width = int(width / (height / thumbnail_height))

        thumbnail = org_picture.resize((thumbnail_width, thumbnail_height), Image.LANCZOS)

        path = os.path.join(settings.MEDIA_ROOT, "thumbnails")
        os.makedirs(path, exist_ok=True)

        org_picture_filename = os.path.split(picture.url.url)[1]
        splitext = os.path.splitext(org_picture_filename)
        thumbnail_filename = splitext[0] + "_" + str(thumbnail_height) + "px" + splitext[1]

        thumbnail_path = os.path.join(path, thumbnail_filename)

        thumbnail.save(thumbnail_path)

    return thumbnail_filename

