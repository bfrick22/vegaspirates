from django import template

register = template.Library()


@register.filter(name='obj_debug')
def obj_debug(value):
    if isinstance(value, dict):
        print(value)
    else:
        print(value.__dict__)