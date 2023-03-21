from django.shortcuts import render
from django.utils.timezone import now
from django.shortcuts import get_list_or_404, get_object_or_404
from task.models import Task

# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework import generics

# import the TodoSerializer from the serializer file
from .serializers import UpdateSerializer

# import the Todo model from the models file
from .models import Update

# create a class for the Todo model viewsets
class UpdateView(viewsets.ModelViewSet):
	serializer_class = UpdateSerializer
	queryset = Update.objects.all().order_by('-update_date')


class UpdateListCreateView(generics.ListCreateAPIView):
	queryset = Update.objects.all()
	serializer_class = UpdateSerializer
	print('UpdateListCreateView')

	def get_update_data(self, request):
		data = self.request.id
		print('here is the data')
	
	def perform_create(self, serializer):
		print('perform_create activated')
		title = serializer.validated_data.get('title')
		description = serializer.validated_data.get('description')
		update_date = serializer.validated_data.get('update_date')
		update_type = serializer.validated_data.get('update_type')
		related_task = serializer.validated_data.get('related_task')
		related_client = serializer.validated_data.get('related_client')
		serializer.save(
			title=title,
			description=description,
			update_type=update_type,
			update_date=update_date,
			related_task=related_task,
			related_client=related_client,
			)
