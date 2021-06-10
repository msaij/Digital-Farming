from django import template

register = template.Library()

@register.filter
def remove0(value):
    print(value)
    print(list(value)[1:])
    return value[1:]