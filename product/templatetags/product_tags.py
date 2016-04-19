from django import template
from django.conf import settings

register = template.Library()


@register.filter
def img_url(image):
    image_url = ''
    try:
        image_url = image.image.url
    except ValueError:
        image_url = ''
    return image_url


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
