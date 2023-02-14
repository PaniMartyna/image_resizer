from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import PictureListView, PictureCreateView, PictureRetrieveView

app_name = 'images'

# router = SimpleRouter()
# router.register('images', views.PictureViewSet, basename='images')
#
# urlpatterns = router.urls

urlpatterns = [
    path('images/', PictureListView.as_view(), name="picture-list"),
    path('images/upload/', PictureCreateView.as_view(), name="picture-upload"),
    path('images/<int:pk>/', PictureRetrieveView.as_view(), name="picture-detail")
]