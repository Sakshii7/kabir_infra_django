from django.db import models


# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    street2 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
