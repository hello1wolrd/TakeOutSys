from __future__ import unicode_literals
from datetime import *

from django.db import models
from mongoengine import *


# Create your models here.
class ItemDetail(EmbeddedDocument):
    title = StringField(required=True)
    price = DecimalField(required=True)
    image_url = StringField(required=True)

class CartItem(EmbeddedDocument):
    qty = IntField(required=True)
    product_id = LongField(required=True)
    item_detail = DictField()

class ShopCart(Document):
    #card_id = ObjectIdField(required=True)  -> use _id
    userid = LongField(required=True, unique=True)
    status = StringField(required=True)
    last_modified = DateTimeField(required=True)
    items = ListField(EmbeddedDocumentListField(CartItem))

    @classmethod
    def create_cart(cls, userid):
        return cls(userid=userid, status="active", last_modified=datetime.now(), items=[])

    @classmethod
    def get_cart(cls, user):
        cart_obj = None
        try:
            cart_obj = cls.objects.get(userid=user.id)
        except cls.DoesNotExist:
            cart_obj = cls.create_cart(user.id)

        return cart_obj

    @classmethod
    def add_item_to_cart(cls, cart_obj, product_id, qty, detail):
        cart_item = CartItem(qty=qty, product_id=product_id, item_detail=detail)
        cart_obj.items.push(cart_item)
        


