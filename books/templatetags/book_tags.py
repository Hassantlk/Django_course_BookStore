from django import template

register = template.Library()

@register.filter(name="name_to_use_in_html")
def to_lowercase(value):
    return value.lower()