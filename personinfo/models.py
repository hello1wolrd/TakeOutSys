# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models
from django.contrib.auth.models import User

from utils.img_function import UploadToPathAndRename
# Create your models here.


class PersonInfo(models.Model):
    LOVES = (
        ('YY', u'音乐'),
        ('YD', u'运动'),
        ('YX', u'游戏'),
    )
    SEXS = (
        ('B', u'男'),
        ('G', u'女'),
    )
    user = models.OneToOneField(User, primary_key=True)
    #send_mails = models.BooleanField(default=False)
    head_img = models.ImageField(upload_to=UploadToPathAndRename('personinfo/imgs/'), default='')
    sex = models.CharField(max_length=1, choices=SEXS)
    love = models.CharField(max_length=2, choices=LOVES)

    def __unicode__(self):
        return "%s - %s" % (self.user.username, self.sex)

    @property
    def love_honor(self):
        love_str = self.get_love_display()
        return love_str + u'之王'

