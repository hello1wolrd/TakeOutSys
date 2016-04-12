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
    description = models.TextField(max_length=500, default='')
    #review = ForeignKey(Review, unique=True)
    
    @classmethod
    def get_page_items(cls, page, nitem, category):
        page = page -1
        start = page * nitem
        end = (page+1) * nitem
        return cls.objects.filter(category=category).order_by('score')[start:end]
    
    @classmethod
    def get_books(cls, page, nitem, category):
        return cls.get_page_items(page, nitem, category)

