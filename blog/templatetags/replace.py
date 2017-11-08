from django import template

register = template.Library()

@register.filter
def replace(value):
    a=value.replace('[', '')
    b=a.replace(']', '')
    c=b.replace("'", "")
    return c