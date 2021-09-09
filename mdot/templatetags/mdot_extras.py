from django import template
from django.template.defaultfilters import stringfilter, title

register = template.Library()


@register.filter
@stringfilter
def add_whitespace(value):
    return value.replace('_', ' ')


@register.filter
@stringfilter
def replace_this_field(value, field):
    return value.replace('This field', add_whitespace(title(field))) if 'This field' in value else value
