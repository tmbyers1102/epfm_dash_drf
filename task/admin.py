from django.contrib import admin

# import the model Todo
from .models import Task

# create a class for the admin-model integration
class TaskAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("title", "related_client_name", "status", "related_project_item")
	list_editable = ('status', )

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Task,TaskAdmin)
