from rest_framework import serializers

from images.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    """Serializer for uploading pictures"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Picture
        fields = ['id', 'name', 'owner', 'url', 'created_at']
        read_only_fields = ['id']

