# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from personinfo.models import PersonInfo

def get_user_profile(user):
    try:
        user_profile = user.personinfo
    except ObjectDoesNotExist:
        return None
    else:
        return user_profile


def get_user_head(user_profile):
    if user_profile is None:
        return settings.DEFAULT_HEAD_IMG
    else:
        if user_profile.head_img != '':
            return settings.MEDIA_URL + user_profile.head_img

        return settings.DEFAULT_HEAD_IMG

def get_user_nickname(user, user_profile):
    if None in (user, user_profile):
        return u'无名， 无称号'
    return user_profile.get_love_display() + u'之王'

