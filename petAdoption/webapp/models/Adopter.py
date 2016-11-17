from __future__ import unicode_literals

from django.db import models
from Customer import Customer
from Pet import Pet


class Adopter(Customer):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    favorite = models.ForeignKey(Pet, null=True, on_delete=models.SET_NULL)