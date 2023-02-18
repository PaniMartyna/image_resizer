import os

from rest_framework.reverse import reverse

from config import settings
from images.models import Picture, Thumbnail


def test_picture_post_basic_user(client, basic_user, temp_picture):
    """
    Test posting a valid image file as user with a basic subscription plan.
    Along with posting a picture, one thumbnail should be created.
    """

    with temp_picture as org_pic:
        post_data = {
            "name": "test_picture1",
            "owner": basic_user,
            "url": org_pic,
        }

        client.force_authenticate(basic_user)
        url = reverse("images:image-list")
        response = client.post(url, post_data)

    thumbnails = Thumbnail.objects.filter(picture__owner=basic_user, picture__name="test_picture1")

    assert response.status_code == 201
    assert post_data["name"] == response.data["name"]
    assert thumbnails.count() == 1
    assert thumbnails[0].size.height == 200

    picture = Picture.objects.get(name=post_data["name"])
    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.path))
    os.remove(os.path.join(settings.MEDIA_ROOT, thumbnails.url.path))


def test_picture_post_premium_user(client, premium_user, temp_picture):
    """
    Test posting a valid image file as user with a premium subscription plan.
    Along with posting a picture, two thumbnails should be created.
    """

    with temp_picture as org_pic:
        post_data = {
            "name": "test_picture1",
            "owner": premium_user,
            "url": org_pic,
        }

        client.force_authenticate(premium_user)
        url = reverse("images:image-list")
        response = client.post(url, post_data)

    thumbnails = Thumbnail.objects.filter(picture__owner=premium_user, picture__name="test_picture1")
    thumbnail_sizes = [thumbnail.size.height for thumbnail in thumbnails]

    assert response.status_code == 201
    assert post_data["name"] == response.data["name"]
    assert thumbnails.count() == 2
    assert 200 in thumbnail_sizes
    assert 400 in thumbnail_sizes

    picture = Picture.objects.get(name=post_data["name"])
    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.path))
    for thumbnail in thumbnails:
        os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail.url.path))


def test_picture_list_get(client, basic_user, temp_picture):
    """Test getting users picture list"""

    with temp_picture as org_pic:
        post_data = {
            "name": "test_picture1",
            "owner": basic_user,
            "url": org_pic,
        }

        client.force_authenticate(basic_user)
        url = reverse("images:image-list")
        client.post(url, post_data)
        response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1

    picture = Picture.objects.get(name=post_data["name"])
    os.remove(os.path.join(settings.MEDIA_ROOT, picture.url.path))
    thumbnail_to_remove = Thumbnail.objects.get(picture__owner=basic_user, picture__name="test_picture1")
    os.remove(os.path.join(settings.MEDIA_ROOT, thumbnail_to_remove.url.path))
