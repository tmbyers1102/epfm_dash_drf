from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


# import the TodoSerializer from the serializer file
from .serializers import TaskSerializer, CreateTaskSerializer
from rest_framework import generics

# import the Todo model from the models file
from .models import Task
from client.models import Client
from update.models import Update
from project.models import ProjectItem




# create a class for the Todo model viewsets
class TaskView(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('due_date')
	serializer_class = TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

	def get_task_data(self, request):
		data = self.request.id
		print('here is the data')
	
	def perform_create(self, serializer):
		# this is how you attach the current user to a created record
		# serializer.save(user=self.request.user)
		# print(serializer.validated_data)
		title = serializer.validated_data.get('title')
		description = serializer.validated_data.get('description')
		# content = serializer.validated_data.get('content') or None
		# if content is None:
		# 	content = title
		serializer.save(title=title, description=description)
		

class CreateTaskView(APIView):
	serializer_class = CreateTaskSerializer

	def post(self, reqest, format=None):

		# for booleans, we need to conv the value from str to bool
		def to_boolean(raw_value: str) -> bool:
			if not isinstance(raw_value, str):
				raw_value = str(raw_value)
			raw_value = raw_value.strip()
			return {'true': True, 'false': False}.get(raw_value.lower(), False)

		data = self.request.data
		client = Client.objects.get(pk=data['related_client'])
		project_item = ProjectItem.objects.get(pk=data['related_project_item'])
		print('here is the data: ' + str(data))
		task = Task(
				title=data['title'],
				status=data['status'],
				due_date=data['due_date'],
				description=data['description'],
				related_client=client,
				related_project_item=project_item,
				# client_visible=to_boolean(data['client_visible']),
				# cant get the boolean to work on drf so cheating here
				client_visible=True,

			)
		task.save()
		return Response({'success': 'Task Created'})
		
    # "title": "test 4",
    # "status": "Todo",
    # "client_visible": false,
    # "due_date": "2023-01-12",
    # "related_client": "3",
    # "related_project_item": null

