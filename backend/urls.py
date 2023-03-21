from django.contrib import admin
from . import views

# add include to the path
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

# import views from todo
from todo import views as todoviews
# must add the 'as _______' to differentiate
from client import views as clientviews
from task import views as taskviews
from project import views as projectviews
from checkin import views as checkinviews
from update import views as updateviews
from Feedo import views as feedoviews

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers

# create a router object
router = routers.DefaultRouter()

# register the router
router.register(r'todos',todoviews.TodoView, 'task')
router.register(r'clients',clientviews.ClientView, 'client')
# router.register(r'updates',updateviews.UpdateView, 'update')
router.register(r'client_contacts',clientviews.ClientContactView, 'client_contact')
# router.register(r'tasks',taskviews.TaskView, 'task')
router.register(r'checkins',checkinviews.CheckinView, 'checkin')
router.register(r'projects',projectviews.ProjectView, 'project')
router.register(r'project_items',projectviews.ProjectItemView, 'project_item')

urlpatterns = [
	path('admin/', admin.site.urls),
	re_path(
		r"^.*$",
        TemplateView.as_view(template_name="src/index.html"),
	),

	# add another path to the url patterns
	# when you visit the localhost:8000/api
	# you should be routed to the django Rest framework
	path('api/', include(router.urls)),
	path('api/tasks/', taskviews.TaskListCreateView.as_view(), name='create_task'),
	path('api/updates/', updateviews.UpdateListCreateView.as_view(), name='create_update'),
	path('api/feedos/', feedoviews.FeedoListCreateView.as_view(), name='create_feedo'),
]
