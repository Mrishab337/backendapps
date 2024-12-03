from django.db import models

# Create your models here.
class Businessregister(models.Model):
    business_name=models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    workspace_name = models.CharField(max_length=255)
    def __str__(self):
        return self.business_name
    