from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    phone_code = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class City(models.Model):
    name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
