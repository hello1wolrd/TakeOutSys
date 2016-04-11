from django import template

from config import settings
from personinfo.models import PersonInfo

register = template.Library()

@register.simple_tag(takes_context=True)
def get_head_img(context):
    user = context['user']
    try:
        person_info = PersonInfo.objects.get(user=user)
    except PersonInfo.DoesNotExist:
        return settings.DEFAULT_HEAD_IMG
    else:
        if person_info.head_img != '':
            return setting.MEDIA_URL + person_info.head_img

        return settings.DEFAULT_HEAD_IMG

    
