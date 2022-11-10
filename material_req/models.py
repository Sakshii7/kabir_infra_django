from django.db import models

from sites.models import Sites
from users.models import Supervisior, Users


# Create your models here.

class MaterialReq(models.Model):
    name = models.CharField(max_length=200)
    site = models.ForeignKey(Sites, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    requisition_date = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
