from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import ProjectSerializer
from .serializers import ProjectItemSerializer

# import the Todo model from the models file
from .models import Project, ProjectItem

# create a class for the Todo model viewsets
class ProjectView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = ProjectSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Project.objects.all()

# create a class for the Todo model viewsets
class ProjectItemView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = ProjectItemSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = ProjectItem.objects.all()
