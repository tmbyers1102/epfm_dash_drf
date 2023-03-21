from django.contrib import admin

# import the model Todo
from .models import Project, ProjectItem

# create a class for the admin-model integration
class ProjectAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("title","related_client","status")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Project,ProjectAdmin)

# create a class for the admin-model integration
class ProjectItemAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("title", "related_project","status")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(ProjectItem,ProjectItemAdmin)
