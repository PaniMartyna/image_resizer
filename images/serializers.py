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


class PictureCreateSerializer(serializers.ModelSerializer):
    """Serializer for uploading pictures"""

    owner = serializers.ReadOnlyField(source='owner.username')

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
        read_only_fields = ['id', 'details', 'created_at']


class PictureRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for picture details"""

    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.SerializerMethodField()
    thumbnails = ThumbnailSerializer(many=True)
    temporary_url = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_url(self, obj):
        if self.context['request'].user.userprofile.subscription_plan.original_url:
            return self.context['request'].build_absolute_uri(obj.url)

    def get_temporary_url(self, obj):
        if self.context['request'].user.userprofile.subscription_plan.temporary_url:
            return "placeholder for temporary link"

    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'thumbnails', 'temporary_url', 'created_at']
        read_only_fields = ['id', 'thumbnails', 'created_at']



