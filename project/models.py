from django.db import models
from client.models import Client

class Project(models.Model):
    class ProjectStatusType(models.TextChoices):
        TODO = 'Todo'
        COMPLETE = 'Complete'
        ON_HOLD = 'On Hold'

    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    status=models.CharField(max_length=50, choices=ProjectStatusType.choices, default=ProjectStatusType.TODO)
    client_visible=models.BooleanField(default=False)
    due_date=models.DateField(blank=True)
    start_date=models.DateField(blank=True)
    end_date=models.DateField(blank=True)
    related_client=models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        #it will return the title
        return self.title


class ProjectItem(models.Model):
    class ProjectItemStatusType(models.TextChoices):
        TODO = 'Todo'
        COMPLETE = 'Complete'
        ON_HOLD = 'On Hold'

    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    status=models.CharField(max_length=50, choices=ProjectItemStatusType.choices, default=ProjectItemStatusType.TODO)
    client_visible=models.BooleanField(default=False)
    due_date=models.DateField(blank=True)
    start_date=models.DateField(blank=True)
    end_date=models.DateField(blank=True)
    related_project=models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        #it will return the title
        return self.title