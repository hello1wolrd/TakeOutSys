from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class ItemDetail(EmbeddedDocument):
    image_url = StringField(required=True)

class CartItem(EmbeddedDocument):
    qty = IntField(required=True)
    product_id = LongField(required=True)
    item_detail = ListField(EmbeddedDocumentField(ItemDetail))

class ShopCart(Document):
    #card_id = ObjectIdField(required=True)  -> use _id
    qty = IntField(required=True)
    last_modified = DateTimeField(required=True)
    items = ListField(EmbeddedDocumentField(CartItem))


