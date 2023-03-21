from rest_framework import serializers

from .models import Feedo

class FeedoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedo
        fields = (
            'id',
            'name',
            'role',
            'status',
            'created_date',
            'direct_report',
            'profile_image_url',
        )
