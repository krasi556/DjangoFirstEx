import markdown
from django import template

register = template.Library()

@register.filter
def markdown_to_html(text):
    pass
