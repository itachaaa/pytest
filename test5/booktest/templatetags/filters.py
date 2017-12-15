from django.template import Library
register = Library()


@register.filter
def mod(value):
    return value % 2


@register.filter
def mod_num(value, num):
    return value % num
