from django.contrib import admin

from plans.models import SubscriptionPlan, UserProfile

admin.site.register(SubscriptionPlan)
admin.site.register(UserProfile)
