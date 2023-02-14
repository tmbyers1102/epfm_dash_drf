# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Project, ProjectItem

# create a serializer class
class ProjectSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Project
		fields = (
			'id',
			'title',
			'description',
			'status',
			'client_visible',
			'due_date',
			'start_date',
			'end_date',
			'related_client',
		)

# create a serializer class
class ProjectItemSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = ProjectItem
		fields = (
			'id',
			'title',
			'description',
			'status',
			'client_visible',
			'due_date',
			'start_date',
			'end_date',
			'related_project'
		)

