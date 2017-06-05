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
    urlfinder = re.compile(u'(?P<link> http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    match = urlfinder.sub(r'<a href="\1">\1</a>', value)
    if not match:
        return value
    return match