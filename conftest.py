import os

import pytest

from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_django.fixtures import django_user_model

from config import settings
from config.settings import BASE_DIR
from images.models import Picture, Size, Thumbnail


@pytest.fixture
def user(db, django_user_model):
    """Create test user."""
    return django_user_model.objects.create_user(
        username='testuser',
        password='testPass123'
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def picture_handler(db, user):
    """Create test picture."""
    picture = Picture.objects.create(
        owner=user,
        name="picture1",
        url=SimpleUploadedFile(
            'test_picture.jpg',
            content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read())
    )

    yield picture

    os.remove(os.path.join(settings.MEDIA_ROOT, 'pictures', 'test_picture.jpg'))


@pytest.fixture
def thumbnail_handler(db, user, picture_handler):
    """Create instance of Size"""
    size1 = Size.objects.create(height=400)

    """Create test thumbnail."""
    thumbnail = Thumbnail.objects.create(
        picture=picture_handler,
        url=SimpleUploadedFile(
            'test_thumbnail.jpg',
            content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read()),
        size=size1
    )

    yield thumbnail

    os.remove(os.path.join(settings.MEDIA_ROOT, 'thumbnails', 'test_thumbnail.jpg'))



@pytest.fixture
def image():
    yield SimpleUploadedFile('test_image.jpeg',
                             content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read())
