from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from plans.models import UserProfile, SubscriptionPlan


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    """
    Create user profile with basic plan automatically when a new user registers.
    """
    if created:
        basic_subscription_plan = SubscriptionPlan.objects.get(plan_name="Basic")
        userprofile = UserProfile.objects.create(
            user=instance,
            subscription_plan=basic_subscription_plan,
        )

        userprofile.save()
