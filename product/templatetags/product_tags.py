from django import template
from django.conf import settings

register = template.Library()


@register.filter
def img_url(image):
    return image.image.url

