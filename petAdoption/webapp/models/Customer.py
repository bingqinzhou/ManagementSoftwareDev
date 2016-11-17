from __future__ import unicode_literals
from django.db import models

import uuid


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=500, blank=True)

    class Meta:
        abstract = True