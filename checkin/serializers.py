# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Checkin

# create a serializer class
class CheckinSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Checkin
		fields = (
            'title',
            'description',
            'completed',
            'next_check_date',
            'related_client',
            'related_client_name',
        )
