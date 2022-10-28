from django.db import models

from clients.models import Clients


# Create your models here.

class Sites(models.Model):
    site_no = models.CharField(max_length=20)
    site_desc = models.CharField(max_length=200)
    alias_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company = models.CharField(max_length=20)
