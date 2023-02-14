from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import ClientSerializer, ClientContactSerializer

# import the Todo model from the models file
from .models import Client, ClientContact

# create a class for the Todo model viewsets
class ClientView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = ClientSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Client.objects.all()


# create a class for the Todo model viewsets
class ClientContactView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = ClientContactSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = ClientContact.objects.all()
