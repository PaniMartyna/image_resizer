from rest_framework.permissions import BasePermission


class CanGetTempUrl(BasePermission):
    """
    Allows access only to users whose subscription plan allows to get temporary picture urls.
    """

    def has_permission(self, request, view):
        return bool(request.user.userprofile.subscription_plan.temporary_url)
