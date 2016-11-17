from __future__ import unicode_literals

from django.db import models
from Customer import Customer


class Agency(Customer):
    company_name = models.CharField(max_length=100)