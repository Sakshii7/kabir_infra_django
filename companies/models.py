from django.db import models

from address.models import Country, State, City


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gstin = models.CharField(max_length=200)
    pan_no = models.CharField(max_length=200)
    cin_no = models.CharField(max_length=200)
    company_registry = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
