from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='address')

