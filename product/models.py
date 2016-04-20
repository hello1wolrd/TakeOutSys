# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import redis

from django.db import models
from django.conf import settings
from django.contrib.auth.decorators import login_required

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
    inventory_id = models.CharField(max_length=30, default='')
    #review = ForeignKey(Review, unique=True)

    class Meta:
        permissions = (
            ('read_product', 'can read product'),
        )
    
    @classmethod
    def get_page_items(cls, page, nitem, category):
        page = page -1
        start = page * nitem
        end = (page+1) * nitem
        return cls.objects.filter(category=category).order_by('score')[start:end]

    @classmethod
    def get_books(cls, page, nitem, category):
        return cls.get_page_items(page, nitem, category)
    
    @classmethod
    def update_items_zrange(cls, category, product):
        client = redis.Redis(connection_pool=settings.REDIS_POOL)
        top_key = 'top:' + category
        client.zadd(top_key, product.pk,  product.score)

    @classmethod
    def get_top_products(cls, tops):
        products = list()
        
        for (pk, score) in tops:
            product = Product.objects.get(pk=pk)
            products.append(product)

        return products

    @classmethod
    def get_items_zrange(cls, category, page, pageCount):
        client = redis.Redis(connection_pool=settings.REDIS_POOL)
        top_key = 'top:' + category
        page = page - 1
        start = page * pageCount
        end = (page+1) * pageCount
        results = client.zrevrange(top_key, start, end, withscores=True)

        return results

    @classmethod
    def get_items_by_key(cls, key, page, pageCount):
        page = int(page)
        page = page - 1
        start = page * pageCount
        end = (page+1) * pageCount
        
        return cls.objects.filter(title__contains=key)[start:end]
