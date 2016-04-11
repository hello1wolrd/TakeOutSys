# -*- coding: utf-8 -*-
from django import forms

class PersonInfoForm(forms.Form):
    head_img = forms.ImageField(label=u'用户头像')
    sex = forms.CharField(max_length=1)
    love = forms.CharField(max_length=2)


