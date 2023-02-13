from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from images.models import Picture
from images.serializers import PictureSerializer


class PictureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PictureSerializer

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)