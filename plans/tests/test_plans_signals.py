from plans.models import UserProfile


def test_automatic_user_profile_creation(user, django_user_model):
    """
    Test whether user profile with basic subscription plan is automatically created
    upon new user registration.
    """

    assert UserProfile.objects.count() == 1
    assert UserProfile.objects.get(user=user).subscription_plan.plan_name == "Basic"

