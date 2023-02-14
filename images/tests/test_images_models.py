from images.models import Picture, Thumbnail


def test_image_creation(picture_handler):
    """Test creating Picture object."""

    assert isinstance(picture_handler, Picture)
    assert picture_handler.owner.username == 'testuser'
    assert picture_handler.url.url == '/static/media/pictures/test_picture.jpg'
    assert picture_handler.name == 'picture1'
    assert str(picture_handler) == 'picture1'


def test_thumbnail_creation(thumbnail_handler, picture_handler):
    """Test creating Thumbnail object."""

    assert isinstance(thumbnail_handler, Thumbnail)
    assert thumbnail_handler.picture == picture_handler
    assert thumbnail_handler.size.height == 400
    assert str(thumbnail_handler) == f"Thumbnail for picture: picture1. Height: 400px"
    assert thumbnail_handler.url.url == '/static/media/thumbnails/test_thumbnail.jpg'
