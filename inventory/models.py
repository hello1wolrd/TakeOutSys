from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class InventoryCart(EmbeddedDocument):
    qty = IntField(required=True)
    card_id = ObjectIdField(required=True)
    timestamp = DateTimeField(required=True)

class Inventory(Document):
    product_id = LongField(required=True)
    qty = IntField(required=True)
    carted = ListField(EmbeddedDocumentField(InventoryCart))

    @classmethod
    def create_inventory(cls, product, inventory_qty):
        product_id = product.pk
        inventory = cls(product_id=product_id, qty=inventory_qty, carted=[])
        inventory.save()
        product.inventory_id = inventory.id
        product.save()


