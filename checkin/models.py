from django.db import models
from client.models import Client
from Feedo.models import Feedo


class Checkin(models.Model):
    class waitingOnType(models.TextChoices):
        ME = 'Me'
        CLIENT = 'Client'
        SUPPORT = 'Support'
    
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500, blank=True, null=True)
    waiting_on=models.CharField(max_length=50, choices=waitingOnType.choices, blank=True, null=True)
    completed=models.BooleanField(default=False)
    next_check_date=models.DateField(blank=True)
    ticket_link=models.URLField(null=True, blank=True)
    related_client=models.ForeignKey(Client, on_delete=models.CASCADE)
    related_client_epfm=models.ForeignKey(Feedo, null=True, blank=True, related_name='checkin_feedo', on_delete=models.SET_NULL)

    def related_client_name(self):
        if self.related_client is not None:
            return self.related_client.name
        return None

    def __str__(self):
        #it will return the title
        return self.title