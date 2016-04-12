from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    score = models.FloatField(default=10.0)
    anonymous = models.BooleanField(default=False)
    description = models.TextField(max_length=500)
    vote = models.IntegerField(default=0)

