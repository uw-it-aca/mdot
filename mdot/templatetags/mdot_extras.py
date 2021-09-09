from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def add_whitespace(value):
    return value.replace('_', ' ')


@register.filter
@stringfilter
def remove_this_field(value):
    return value.replace('This field ', '')
