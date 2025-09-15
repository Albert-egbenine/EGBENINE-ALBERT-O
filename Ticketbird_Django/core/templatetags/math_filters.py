from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiply value and arg in templates"""
    try:
        return float(value) * float(arg)
    except:
        return 0