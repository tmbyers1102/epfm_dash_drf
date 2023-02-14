from django.db import models


class Client(models.Model):
    name=models.CharField(max_length=150)
    cfu_link=models.URLField()
    active=models.BooleanField(default=False)

    def __str__(self):
        #it will return the name
        return self.name


class ClientContact(models.Model):
    name=models.CharField(max_length=150)
    role=models.CharField(max_length=150, null=True, blank=True)
    location=models.CharField(max_length=150, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    is_agency=models.BooleanField(default=False)
    related_client=models.ForeignKey(Client, null=True, blank=True, related_name='client_contacts', on_delete=models.CASCADE)
    main_poc=models.BooleanField(default=False)

    def __str__(self):
        #it will return the name
        return f"{self.name}' | '{self.related_client}"
    
    # creates client in ZOHO(?) ==> create client in BS