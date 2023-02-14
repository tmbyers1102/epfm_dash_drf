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
	queryset = Update.objects.filter(related_task="2").order_by('-update_date')
	serializer_class = UpdateSerializer

	# def get_task_updates(self, request):
	# 	task = self.request.id
	# 	print(task)
	# 	updates = Update.objects.all()
	# 	return JSONResponse({updates: updates})
	
	def perform_create(self, serializer):
		# task = get_object_or_404(Task, pk=pk)
		# task = self.request.data
		# print('here is task ====>',task)
		the_data = serializer.validated_data.get('title')
		print('here is the title ====>',the_data)
		today = now().date()
		title = serializer.validated_data.get('title')
		description = serializer.validated_data.get('description')
		# update_type = serializer.validated_data.get('update_type')
		# update_date = serializer.validated_data.get('update_date') or None
		# if update_date is None:
		# 	update_date = today
		# related_task = Task.objects.get(id=2)
		# related_client = related_task.related_client
		serializer.save(
			title=title,
			description=description,
			# update_type=update_type,
			# update_date=update_date,
			# related_task=related_task,
			# related_client=related_client,
			)
