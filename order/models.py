from __future__ import unicode_literals

from django.db import models
from mongoengine import *

from shopcart.models import CartItem

# Create your models here.
class Order(Document):
    user_id = LongField(required=True)
    status = StringField(required=True)
    cart_items = ListField(EmbeddedDocumentListField(CartItem))

    @classmethod
    def create_order(cls, user):
        user_id = user.id
        order = cls(user_id=user_id, status="active", cart_items=[])
        order.save()
        return order
        
    @classmethod
    def add_cart_item(cls, order, cart_item):
    	order.cart_items.push(cart_item)
