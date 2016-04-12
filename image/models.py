from __future__ import unicode_literals

from django.db import models

from product.models import Product

from utils.img_function import UploadToPathAndRename
# Create your models here.
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=UploadToPathAndRename('product/imgs/'))
    description = models.TextField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)

