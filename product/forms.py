# -*- coding: utf-8 -*-
from django import forms


class ProductForm(forms.Form):
    CATEGORIES = (
        ('Book', u'书籍'),
        ('Video', u'影音'),
        ('Dress', u'服装'),
        ('Grocery', u'食品'),
        ('Computers', u'电子产品'),
    )
    title = forms.CharField(label=u'产品标题', max_length=200)
    price = forms.CharField(label=u'产品价格', max_length=20)
    score = forms.FloatField(label=u'产品评分')
    category = forms.CharField(label=u'产品分类', max_length=10, widget=forms.Select(choices=CATEGORIES))
    description = forms.CharField(label=u'产品描述', max_length=500,widget=forms.Textarea)
