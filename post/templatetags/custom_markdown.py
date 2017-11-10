from django import template
import markdown

register = template.Library()


# markdown filter to parse the markdown document
@register.filter
def mark(value):
    return markdown.markdown(value)

