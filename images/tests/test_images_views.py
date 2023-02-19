"""
Tests for views.
"""

import os

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

from config import settings
from images.models import Picture, Thumbnail

from images.serializers import PictureRetrieveSerializer, PictureListSerializer


@pytest.mark.parametrize(
    "user_param, expected_thumb_count",
    [("basic_user", 1), ("premium_user", 2), ("enterprise_user", 2)])
def test_picture_upload(client, user_param, expected_thumb_count, request, temp_picture):
    """
    Test posting a valid image file as users with built-in subscription plans.
    """

    user = request.getfixturevalue(user_param)

    with temp_picture as org_pic:
        post_data = {
            "name": f"test_picture1 from {user.username}",
            "owner": user,
            "url": org_pic,
        }

        client.force_authenticate(user)
        url = reverse("images:image-list")
        response = client.post(url, post_data)

    thumbnails = Thumbnail.objects.filter(picture__owner=user)

    assert response.status_code == 201
    assert post_data["name"] == response.data["name"]
    assert thumbnails.count() == expected_thumb_count

    picture = Picture.objects.get(name=post_data["name"])
    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.path))
    for thumbnail in thumbnails:
        os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail.url.path))


def test_get_picture_list(client, basic_user, picture_handler):
    """Test getting users picture list"""

    url = reverse('images:image-list')
    client.force_authenticate(basic_user)
    response = client.get(url)

    factory = APIRequestFactory()
    request = factory.get(url)
    request.user = basic_user

    serializer = PictureListSerializer(picture_handler, context={"request": request})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0] == serializer.data

    thumbnail_to_remove = Thumbnail.objects.get(picture__owner=basic_user)
    os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail_to_remove.url.path))


@pytest.mark.parametrize("user_param", ["basic_user", "premium_user", "enterprise_user"])
def test_get_picture_details(client, user_param, request):
    """Test get picture details as users with different built-in subscription plans."""

    user = request.getfixturevalue(user_param)

    picture = Picture.objects.create(
        owner=user,
        name=f"picture1 from {user.username}",
        url=SimpleUploadedFile(
            'test_picture.jpg',
            content=open(os.path.join('images', 'tests', 'test_picture.jpg'), 'rb').read())
    )

    url = reverse('images:image-detail', args=[picture.id])
    client.force_authenticate(user)
    response = client.get(url)

    factory = APIRequestFactory()
    req = factory.get(url)
    req.user = user

    serializer = PictureRetrieveSerializer(picture, context={"request": req})

    assert response.status_code == 200
    assert response.data == serializer.data

    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.name))
    thumbnails = Thumbnail.objects.filter(picture__owner=user)
    for thumbnail in thumbnails:
        os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail.url.path))
