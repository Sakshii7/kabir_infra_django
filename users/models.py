from django.db import models


# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=20, null=True)
    is_supervisior = models.BooleanField(default=False)
    is_accounts = models.BooleanField(default=False)
    is_purchase = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    is_add_sites_and_vendors = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Supervisior(models.Model):
    name = models.CharField(max_length=200, null=True)
    employee_code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
