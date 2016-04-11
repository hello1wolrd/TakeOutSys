# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
        return os.path.join(self.sub_path, filename)

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
    user = models.OneToOneField(User, unique=True, related_name='profile')
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

