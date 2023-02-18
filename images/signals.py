from django.db.models.signals import post_save
from django.dispatch import receiver

from images.helpers import picture_resizer
from images.models import Picture, Thumbnail, Size
from plans.models import UserProfile


@receiver(post_save, sender=Picture)
def create_thumbnails(sender, instance, created, **kwargs):
    """
    Create thumbnails upon saving a new picture to the database.
    Thumbnail sizes should be determined basing on user subscription plan.
    """
    if created:
        sizes = UserProfile.objects.get(user=instance.owner).subscription_plan.thumbnail_sizes.all()

        for size in sizes:
            thumbnail_filename = picture_resizer(instance, size.height)
            thumbnail = Thumbnail.objects.create(
                picture=instance,
                size=size
            )
            thumbnail.url = f"thumbnails/{thumbnail_filename}"
            thumbnail.save()
