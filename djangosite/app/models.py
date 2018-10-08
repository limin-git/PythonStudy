# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# C:\My Document\Python\djangosite>python manage.py makemigrations app
class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
