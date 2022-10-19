from django.db import models


# Create your models here.

class Materials(models.Model):
    name = models.CharField(max_length=200)
    site_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    requisition_date = models.CharField(max_length=50)
