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

    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'created_at']
        read_only_fields = ['id']


class PictureListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for uploading pictures"""
    details = serializers.HyperlinkedIdentityField(view_name='images:picture-detail')

    class Meta:
        model = Picture
        fields = ['id', 'name', 'details', 'created_at']
        read_only_fields = ['id', 'details']


class PictureRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for uploading pictures"""

    owner = serializers.ReadOnlyField(source='owner.username')
    thumbnails = ThumbnailSerializer(many=True)

    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'thumbnails', 'created_at']
        read_only_fields = ['id', 'thumbnails']


# class PictureSerializer(serializers.ModelSerializer):
#     """Serializer for uploading pictures"""
#
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Picture
#         fields = ['id', 'name', 'owner', 'created_at']
#         read_only_fields = ['id']
#         extra_kwargs = {'url': {'write_only': True}}
#
#         def create(self, validated_data):
#             picture = Picture(
#                 name=validated_data['name'],
#             )
#             picture.url = validated_data['url']
#             picture.save()
#             return picture
