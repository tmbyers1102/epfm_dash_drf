from django.db import models
from client.models import Client


class Checkin(models.Model):
    
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)
    next_check_date=models.DateField(blank=True)
    related_client=models.ForeignKey(Client, on_delete=models.CASCADE)

    def related_client_name(self):
        if self.related_client is not None:
            return self.related_client.name
        return None

    def __str__(self):
        #it will return the title
        return self.title