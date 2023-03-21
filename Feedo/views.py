from django.shortcuts import render
from Feedo.models import Feedo
from rest_framework import generics


from .serializers import FeedoSerializer



class FeedoListCreateView(generics.ListCreateAPIView):
	queryset = Feedo.objects.all()
	serializer_class = FeedoSerializer

	def get_feedo_data(self, request):
		data = self.request.id
		print('here is the data')
	
	def perform_create(self, serializer):
		# this is how you attach the current user to a created record
		# serializer.save(user=self.request.user)
		# print(serializer.validated_data)
		name = serializer.validated_data.get('name')
		role = serializer.validated_data.get('role')
		status = serializer.validated_data.get('status')
		# description = serializer.validated_data.get('description')
		# content = serializer.validated_data.get('content') or None
		# if content is None:
		# 	content = title
		serializer.save(name=name, role=role, status=status)