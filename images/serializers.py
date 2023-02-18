from rest_framework import serializers

from images.models import Picture, Thumbnail


class ThumbnailSerializer(serializers.ModelSerializer):
    """Serializer for thumbnails"""
    size = serializers.SlugRelatedField(
        read_only=True,
        slug_field='height'
    )

    class Meta:
        model = Thumbnail
        fields = ['size', 'url']

    # def get_queryset(self):
    #     """Returns only thumbnails for a given picture."""


class PictureCreateSerializer(serializers.ModelSerializer):
    """Serializer for uploading pictures"""

    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'created_at']
        read_only_fields = ['id']


class PictureListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for listing pictures"""

    details = serializers.HyperlinkedIdentityField(view_name='images:image-detail')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Picture
        fields = ['id', 'name', 'details', 'created_at']
        read_only_fields = ['id', 'details']


class PictureRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for picture details"""

    owner = serializers.ReadOnlyField(source='owner.username')
    thumbnails = ThumbnailSerializer(many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'thumbnails', 'created_at']
        read_only_fields = ['id', 'thumbnails']


