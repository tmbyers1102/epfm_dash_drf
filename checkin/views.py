from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import CheckinSerializer

# import the Todo model from the models file
from .models import Checkin

# create a class for the Todo model viewsets
class CheckinView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = CheckinSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Checkin.objects.all()
