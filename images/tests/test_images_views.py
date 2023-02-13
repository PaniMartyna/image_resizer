import json
import os

from django.core.files.uploadedfile import SimpleUploadedFile

from config import settings
from images.models import Picture


def test_picture_post_image_file(client, user):
    """Test posting a valid image file"""

    post_data = {
        "name": "test_picture1",
        "owner": user,
        "url": SimpleUploadedFile('test_picture.jpg',
                                  content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read())
    }
    client.force_authenticate(user)

    response = client.post('/api/images/', post_data)

    assert response.status_code == 201
    assert post_data["name"] == response.data["name"]

    os.remove(os.path.join(settings.BASE_DIR, 'media', 'pictures', 'test_picture.jpg'))


def test_picture_post_non_image_file(client, user):
    """Test posting non-image file. Should fail at file type validation"""

    post_data = {
        "name": "test_file",
        "owner": user,
        "url": SimpleUploadedFile('test_file.txt',
                                  content=open(os.path.join('images', 'tests', 'test_file.txt'), 'rb').read())
    }
    client.force_authenticate(user)

    response = client.post('/api/images/', post_data)

    assert response.status_code == 400


def test_picture_list_get(client, user):
    """Test getting users picture list"""

    Picture.objects.create(name="1", owner=user, url="1.jpg")
    Picture.objects.create(name="2", owner=user, url="2.jpg")
    client.force_authenticate(user)

    response = client.get('/api/images/')

    assert response.status_code == 200
    assert len(response.data) == 2
