"""
Templatetags for form/modal helpers
"""
from django import template
from opal.templatetags.forms import extract_common_args

register = template.Library()


@register.inclusion_tag('_helpers/file_input.html')
def file_input(*args, **kwargs):
    """
    Render a text input

    Kwargs:
    - hide : Condition to hide
    - show : Condition to show
    - model: Angular model
    - label: User visible label
    - lookuplist: Name of the lookuplist
    - required: label to show when we're required!
    """
    return extract_common_args(kwargs)


@register.inclusion_tag('_helpers/file_display.html')
def file_display(*args, **kwargs):
    """
    Render a text input

    Kwargs:
    - hide : Condition to hide
    - show : Condition to show
    - model: Angular model
    - label: User visible label
    - lookuplist: Name of the lookuplist
    - required: label to show when we're required!
    """
    return {"hello": "hello"}
