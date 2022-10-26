from django.db import models


# Create your models here.

class Materials(models.Model):
    material_code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    alias_name = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20, default=1.00)
    conversion_quantity = models.CharField(max_length=20, default=0.00)
    gst_rate = models.CharField(max_length=20, default=0.00)
    allowable_tolerance = models.CharField(max_length=20, default=0.00)
