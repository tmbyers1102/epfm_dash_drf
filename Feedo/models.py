from django.db import models

class Feedo(models.Model):
    class FeedoRole(models.TextChoices):
        EPFM = 'EPFM'
        OPS = 'OPS'
        OTHER = 'OTHER'
    
    class FeedoStatus(models.TextChoices):
        ACTIVE = 'ACTIVE'
        INACTIVE = 'INACTIVE'

    name=models.CharField(max_length=150)
    role=models.CharField(max_length=50, choices=FeedoRole.choices, default=FeedoRole.EPFM)
    status=models.CharField(max_length=50, choices=FeedoStatus.choices, default=FeedoStatus.ACTIVE)
    created_date=models.DateField(auto_now_add=True)
    direct_report=models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    profile_image_url=models.URLField(blank=True, null=True)

    def __str__(self):
        #it will return the title
        return self.name