from django.db import models

from address.models import City, State, Country


# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    street2 = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
