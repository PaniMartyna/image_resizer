from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from images.models import Picture
from images.serializers import PictureCreateSerializer, PictureRetrieveSerializer, \
    PictureListSerializer


# class PictureViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PictureSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Picture.objects.filter(owner=user)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


class PictureCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PictureCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PictureListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PictureListSerializer

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)


class PictureRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PictureRetrieveSerializer
    queryset = Picture.objects.all()

