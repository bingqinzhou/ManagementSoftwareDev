from __future__ import unicode_literals

from django.db import models
from Agency import Agency

import uuid


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet_name = models.CharField(max_length=30, unique=True)
    if_adopted = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)