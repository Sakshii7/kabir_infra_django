from django.db import models

from address.models import City, State, Country
from clients.models import Clients


# Create your models here.

class Sites(models.Model):
    site_no = models.CharField(max_length=20)
    site_desc = models.CharField(max_length=200)
    alias_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company = models.CharField(max_length=20)

    def __str__(self):
        return self.site_no
