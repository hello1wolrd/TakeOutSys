#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField(label=u'产品图片')
    img_description = forms.CharField(label=u'图片描述', max_length=200,widget=forms.Textarea(attrs={}))
    #publish_date = forms.DateTimeField(label=u'')
