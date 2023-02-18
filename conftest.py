import os
import tempfile

import pytest
from PIL import Image
from django.urls import reverse

from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_django.fixtures import django_user_model

from config import settings
from config.settings import BASE_DIR
from images.models import Picture, Size, Thumbnail
from plans.models import UserProfile, SubscriptionPlan


@pytest.fixture
def basic_user(db, django_user_model):
    """Create test user."""
    return django_user_model.objects.create_user(
        username='testuser',
        password='testPass123'
    )


@pytest.fixture
def premium_user(db, django_user_model):
    """Create test premium user."""
    user = django_user_model.objects.create_user(
        username='testuser',
        password='testPass123'
    )
    premium_subscription_plan = SubscriptionPlan.objects.get(plan_name="Premium")
    userprofile = UserProfile.objects.get(user=user)
    userprofile.subscription_plan = premium_subscription_plan
    userprofile.save()

    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def picture_handler(db, basic_user):
    """Create test picture."""
    picture = Picture.objects.create(
        owner=basic_user,
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



# @pytest.fixture
# def image():
#     yield SimpleUploadedFile('test_image.jpeg',
#                              content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read())


@pytest.fixture
def temp_picture():
    org_pic = tempfile.NamedTemporaryFile(suffix=".jpg")
    pic = Image.new("RGB", (500, 500))
    pic.save(org_pic, format="JPEG")
    org_pic.seek(0)

    yield org_pic


# @pytest.fixture
# def picture_handler(db, basic_user, temp_picture):
#     """Create test picture."""
#     picture = Picture.objects.create(
#         owner=basic_user,
#         name="picture1",
#         url=temp_picture
#     )
#
#     yield picture
#
#     os.remove(os.path.join(settings.MEDIA_ROOT, 'pictures', picture.ur.path))


