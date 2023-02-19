"""
Test for models.
"""

from plans.models import SubscriptionPlan, UserProfile


def test_create_subscription_plan(subscription_plan):
    """Test creating new subscription plan."""

    assert isinstance(subscription_plan, SubscriptionPlan)
    assert subscription_plan.plan_name == "test_plan"
    assert subscription_plan.original_url
    assert not subscription_plan.temporary_url
    assert str(subscription_plan) == "test_plan plan"
    assert subscription_plan.thumbnail_sizes.count() == 1


def test_update_user_profile(basic_user, subscription_plan):
    """
    Test updating user profile, which is automatically created upon new user registration.
    Default subscription plan assigned to a new user is "Basic"
    """

    user_profile = UserProfile.objects.get(user=basic_user)

    assert user_profile.subscription_plan.plan_name == "Basic"

    user_profile.subscription_plan = subscription_plan

    assert str(user_profile) == f"{basic_user} with {subscription_plan}"
    assert user_profile.subscription_plan.plan_name == "test_plan"
    assert user_profile.user.username == "basic_testuser"
