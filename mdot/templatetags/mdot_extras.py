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
    return value.replace('This field', add_whitespace(title(field)))\
        if 'This field' in value else value


# class and method below from vinta.ws
class SetVarNode(template.Node):
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value

        return u""


@register.tag(name='set')
def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError(
            "'set' tag must be of the form: {% set <var_name> = <var_value> %}"
        )

    return SetVarNode(parts[1], parts[3])
