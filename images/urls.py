from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'images'

router = SimpleRouter()
router.register('images', views.PictureViewSet, basename='image')

urlpatterns = [
    path('', include(router.urls)),
    # path('images/<int:pk>/get_temp_url/', views.TemporaryUrlView.as_view(), name='image-temp-url')
]
