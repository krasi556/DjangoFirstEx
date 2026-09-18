import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown_to_html(text):
    if not text:
        return ''
    message = markdown.markdown(text)
    return mark_safe(message)
