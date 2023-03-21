from django.db import models
from client.models import Client
from task.models import Task
from datetime import date


class Update(models.Model):
    class UpdateType(models.TextChoices):
        TASK_UPDATE = 'Task Update'
        TASK_COMPLETED = 'Task Completed'
        TASK_DELAYED = 'Task Delayed'
        TASK_CREATED = 'Task Created'
        QUESTION_POSTED = 'Question Posted'
        QUESTION_ANSWERED = 'Question Answered'
        NEW_PROJECT_CREATED = 'New Project Created'
        PROJECT_COMPLETED = 'Project Completed'
        PROJECT_DELAYED = 'Project Delayed'
        NEW_PROMOTION = 'New Promotion'
        PROMOTION_ISSUE = 'Promotion Issue'
        PROMOTION_UPDATE = 'Promotion Update'
        DOCUMENT_POSTED = 'Document Posted'
        VIDEO_POSTED = 'Video Posted'
        OTHER = 'Other'

    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500, blank=True, null=True)
    update_type=models.CharField(max_length=50, choices=UpdateType.choices, default=UpdateType.OTHER)
    update_date=models.DateField(auto_now_add=True)
    related_client=models.ForeignKey(Client, on_delete=models.CASCADE)
    related_task=models.ForeignKey(Task, blank=True, null=True, on_delete=models.CASCADE, related_name="task_update")

    def related_client_name(self):
        if self.related_client is not None:
            return self.related_client.name
        return None

    def __str__(self):
        #it will return the title
        return self.title