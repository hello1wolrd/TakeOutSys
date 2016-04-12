# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from review.models import Review
# Create your models here.
class Product(models.Model):
    CATEGORIES = (
        ('Book', u'书籍'),
        ('Video', u'影音'),
        ('Dress', u'服装'),
        ('Grocery', u'食品'),
        ('Computers', u'电子产品'),
    )
    title = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    score = models.FloatField(default=10.0)
    category = models.CharField(max_length=10, choices=CATEGORIES )


class Attributes(models.Model):
    description = models.TextField(max_length=500)
    #review = ForeignKey(Review, unique=True)


