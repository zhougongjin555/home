'''自定义过滤器'''


from django import template

register = template.Library()


@register.filter
def multi_filter(x, y):
    return x*y


@register.simple_tag
def multi_tags(x, y):
    return x*y