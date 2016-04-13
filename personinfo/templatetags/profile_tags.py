from django import template

from config import settings
from utils.user_functions import get_user_head, get_user_profile
from personinfo.models import PersonInfo

register = template.Library()

@register.simple_tag(takes_context=True)
def get_head_img(context):
    user = context['user']
    person_info = get_user_profile(user)
    return get_user_head(person_info)


@register.inclusion_tag('personinfo/base_user.html', takes_context=True)
def render_base_skeleton(context):
    u'''
    user--outline
    '''
    user = context['user']
    user_profile = get_user_profile(user)
    head_img = get_user_head(user_profile)
    return {
        'user': user,
        'head_img': head_img,
        'username': user.username,
    }

@register.inclusion_tag('personinfo/love_skeleton.html', takes_context=True)
def render_loves_skeleton(context, category):
    u'''
    category --> dress, computers...
    '''
    user = context['user']
    user_profile = get_user_profile(user)
    head_img = get_user_head(user_profile)
    nick_name = get_user_nickname(user, user_profile)
    return {
        'head_img': head_img,
        'nick_name': nick_name,
    }
