from django.db import models
from project.models import ProjectItem
from client.models import Client
from Feedo.models import Feedo


class Task(models.Model):
    class TaskStatusType(models.TextChoices):
        TODO = 'Todo'
        COMPLETE = 'Complete'
        ON_HOLD = 'On Hold'
    
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500, null=True, blank=True)
    status=models.CharField(max_length=50, choices=TaskStatusType.choices, default=TaskStatusType.TODO)
    client_visible=models.BooleanField(default=False)
    due_date=models.DateField(null=True, blank=True)
    ticket_link=models.URLField(null=True, blank=True)
    related_project_item=models.ForeignKey(ProjectItem, null=True, blank=True, on_delete=models.SET_NULL)
    related_client=models.ForeignKey(Client, null=True, blank=True, related_name='tasks', on_delete=models.CASCADE)
    related_client_epfm=models.ForeignKey(Feedo, null=True, blank=True, related_name='task_feedo', on_delete=models.SET_NULL)

    def related_client_name(self):
        if self.related_client is not None:
            return self.related_client.name
        return None

    def related_project_item_name(self):
        if self.related_project_item is not None:
            return self.related_project_item.title
        return None

    # def related_project(self):
    #     if self.related_project_item is not None:
    #         print('here is the printout: ', self.related_project_item)
    #         return self.related_project_item.related_project
    #     return None

    def __str__(self):
        #it will return the title
        return self.title