import re
import time

from django import template
from django.utils.dateparse import parse_datetime

register = template.Library()


@register.filter(name='obj_debug')
def obj_debug(value):
    if isinstance(value, dict):
        print(value)
    else:
        print(value.__dict__)


@register.filter(name='string_to_date')
def string_to_date(value):
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(str(value), '%a %b %d %H:%M:%S +0000 %Y'))
    date_obj = parse_datetime(ts)
    if date_obj:
        return date_obj
    return value


@register.filter(name='linkify')
def linkify(value):
    urlfinder = re.compile(u'(?P<link> http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    match = urlfinder.sub(r'<a href="\1">\1</a>', value)
    if not match:
        return value
    return match