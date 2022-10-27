from django.db import models


# Create your models here.

class Vendors(models.Model):
    vendor_code = models.CharField(max_length=20)
    trade_name = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    street2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    gstin = models.CharField(max_length=20)
    pan_no = models.CharField(max_length=20)
    vendor_type = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=20)
    credit_days = models.CharField(max_length=20)
    credit_amount = models.FloatField(max_length=20)
