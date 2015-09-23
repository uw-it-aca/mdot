from django import template

register = template.Library()


@register.filter()
def strip_protocol(url):
    if url[0:5] == 'https':
        return url[6:]
    elif url[0:4] == 'http':
        return url[5:]
    else:
        return url
