"""
Tests for signals.
"""

from plans.models import UserProfile


def test_automatic_user_profile_creation(basic_user, django_user_model):
    """
    Test whether user profile with basic subscription plan is automatically created
    upon new user registration.
    """

    assert UserProfile.objects.count() == 1
    assert UserProfile.objects.get(user=basic_user).subscription_plan.plan_name == "Basic"

