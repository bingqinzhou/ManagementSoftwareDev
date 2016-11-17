from __future__ import unicode_literals

from django.db import models
from Agency import Agency
from Adopter import Adopter

import uuid


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True)
    answer = models.TextField(null=True)
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

