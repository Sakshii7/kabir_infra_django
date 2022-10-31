from django.db import models


# Create your models here.

class MaterialReq(models.Model):
    name = models.CharField(max_length=200)
    site_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    requisition_date = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
