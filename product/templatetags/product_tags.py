from django import template
from django.conf import settings

register = template.Library()


@register.filter
def img_url(image):
    return image.image.url


@register.filter
def img_pk(image):
    return image.pk


@register.inclusion_tag('product/key_search.html', takes_context=True)
def render_key_search(context):
    u'''
    key-search
    '''
    return {
    }
