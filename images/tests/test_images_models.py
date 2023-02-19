import os

from config import settings
from images.models import Picture, Thumbnail, Size


def test_create_picture(picture_handler):
    """Test creating Picture object."""

    assert isinstance(picture_handler, Picture)
    assert picture_handler.owner.username == 'basic_testuser'
    assert picture_handler.url.url == f"/static/media/{picture_handler.url.name}"
    assert picture_handler.name == 'picture1'
    assert str(picture_handler) == 'picture1'

    thumbnails_to_delete = Thumbnail.objects.filter(picture=picture_handler)
    for thumbnail in thumbnails_to_delete:
        os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail.url.name))


def test_create_thumbnail(thumbnail_handler, picture_handler):
    """Test creating Thumbnail object."""

    assert isinstance(thumbnail_handler, Thumbnail)
    assert thumbnail_handler.picture == picture_handler
    assert thumbnail_handler.size.height == 400
    assert str(thumbnail_handler) == f"Thumbnail for picture: picture1. Height: 400px"
    assert thumbnail_handler.url.url == '/static/media/thumbnails/test_thumbnail.jpg'

    thumbnails_to_delete = Thumbnail.objects.all()
    for thumbnail in thumbnails_to_delete:
        print(thumbnail.url.name)
        os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail.url.name))


def test_size_creation(db):
    """Test creating new size object"""

    new_size = Size.objects.create(height=245)

    assert isinstance(new_size, Size)
    assert new_size.height == 245
    assert str(new_size) == f"Picture height: {new_size.height}"
