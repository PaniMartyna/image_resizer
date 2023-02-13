from images.models import Picture


def test_image_creation(picture_handler):
    """Test creating Picture object."""

    assert isinstance(picture_handler, Picture)
    assert picture_handler.owner.username == 'testuser'
    assert picture_handler.url.url == '/static/media/pictures/test_picture.jpg'
    assert picture_handler.name == 'picture1'
    assert str(picture_handler) == 'picture1'
