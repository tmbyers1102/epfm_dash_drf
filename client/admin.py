from django.contrib import admin

# import the model Todo
from .models import Client, ClientContact

# create a class for the admin-model integration
class ClientAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("name","cfu_link","active")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Client,ClientAdmin)

class ClientContactAdmin(admin.ModelAdmin):
	list_display = ("name","email","related_client","main_poc")

admin.site.register(ClientContact,ClientContactAdmin)
