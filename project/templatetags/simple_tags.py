from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def show_difficulty_in_color(difficulty):
    colors = {
        'easy': '#28a745',
        'hard': '#fd7e14',
        'extreme': '#dc3545',
        'kek': '#6f42c1',
    }

    color = colors.get(difficulty, colors['easy'])

    return mark_safe(f'<span style="color: {color};">{difficulty}</span>')