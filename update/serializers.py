# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Update

# create a serializer class
class UpdateSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Update
		fields = (
            'id',
            'title',
            'update_type',
            'description',
            'update_date',
            'related_client',
            'related_task',
        )
