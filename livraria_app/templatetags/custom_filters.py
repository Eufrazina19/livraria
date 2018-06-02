from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def filename(path):
    splited_path = path.split('/')
    file_name = splited_path[-1]
    return file_name
