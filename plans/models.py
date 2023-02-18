from django.contrib.auth import get_user_model
from django.db import models


class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=80)
    thumbnail_sizes = models.ManyToManyField("images.Size")
    original_url = models.BooleanField(default=False)
    temporary_url = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plan_name} plan"


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey("SubscriptionPlan", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} with {self.subscription_plan}"