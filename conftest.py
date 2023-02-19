import os
import tempfile

import pytest
from PIL import Image

from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

from config import settings
from images.models import Picture, Size, Thumbnail
from plans.models import UserProfile, SubscriptionPlan


@pytest.fixture
def client():
    return APIClient()


"""
Different types of users.
"""


@pytest.fixture
def basic_user(db, django_user_model):
    """Create test basic user."""
    yield django_user_model.objects.create_user(
        username='basic_testuser',
        password='testPass123'
    )


@pytest.fixture
def premium_user(db, django_user_model):
    """Create test premium user."""
    user = django_user_model.objects.create_user(
        username='premium_testuser',
        password='testPass123'
    )
    premium_subscription_plan = SubscriptionPlan.objects.get(plan_name="Premium")
    userprofile = UserProfile.objects.get(user=user)
    userprofile.subscription_plan = premium_subscription_plan
    userprofile.save()

    yield user


@pytest.fixture
def enterprise_user(db, django_user_model):
    """Create test premium user."""
    user = django_user_model.objects.create_user(
        username='enterprise_testuser',
        password='testPass123'
    )
    enterprise_subscription_plan = SubscriptionPlan.objects.get(plan_name="Enterprise")
    userprofile = UserProfile.objects.get(user=user)
    userprofile.subscription_plan = enterprise_subscription_plan
    userprofile.save()

    yield user


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

    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.name))


@pytest.fixture
def thumbnail_handler(db, picture_handler):
    """Create instance of Size"""
    size1 = Size.objects.get(height=400)

    """Create test thumbnail."""
    thumbnail = Thumbnail.objects.create(
        picture=picture_handler,
        url=SimpleUploadedFile(
            'test_thumbnail.jpg',
            content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read()),
        size=size1
    )

    yield thumbnail


@pytest.fixture
def temp_picture():
    org_pic = tempfile.NamedTemporaryFile(suffix=".jpg")
    pic = Image.new("RGB", (500, 500))
    pic.save(org_pic, format="JPEG")
    org_pic.seek(0)

    yield org_pic


@pytest.fixture
def subscription_plan(db):
    """Test subscription plan."""

    size = Size.objects.first()

    plan = SubscriptionPlan.objects.create(
        plan_name="test_plan",
        original_url=True,
    )

    plan.thumbnail_sizes.add(size)
    plan.save()

    return plan
