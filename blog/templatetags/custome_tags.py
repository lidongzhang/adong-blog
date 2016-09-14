from markdown import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def markdown_convert(value):
    #return markdown(value)
    return mark_safe(markdown(value,
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False
                              ))


register.filter('markdown_convert', markdown_convert)