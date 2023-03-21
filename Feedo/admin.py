from django.contrib import admin

from .models import Feedo

class FeedoAdmin(admin.ModelAdmin):

	list_display = (
		'name',
        'role',
        'status',
        'created_date',
        'direct_report',
        'profile_image_url',
    )
	list_editable = ('direct_report', )

admin.site.register(Feedo,FeedoAdmin)