# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='inventory',
            new_name='inventory_id',
        ),
    ]