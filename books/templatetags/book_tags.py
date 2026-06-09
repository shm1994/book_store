from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def highlight_word(text, word):
    highlighted = text.replace(
        word,
        f'<span style="color:red;">{word}</span>'
    )
    return mark_safe(highlighted)
