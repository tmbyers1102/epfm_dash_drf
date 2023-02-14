from django.contrib import admin

# import the model Todo
from .models import Update

# create a class for the admin-model integration
class UpdateAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = (
        "title",
        "update_type",
        "description",
        "update_date",
        "related_client",
        # "related_task",
    )

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Update,UpdateAdmin)
