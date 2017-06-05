import re
from django import template

register = template.Library()


@register.filter(name='obj_debug')
def obj_debug(value):
    if isinstance(value, dict):
        print(value)
    else:
        print(value.__dict__)


@register.filter(name='linkify')
def linkify(value):
    value = str(value)
    reg = u'(?P<link> http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
    output = re.sub(reg, "<a href=''></a>", value)
    print output
    return value