from django import templates

register = templates.Library()

@register.replace(name='cut')
def cut(value,args):

    return value.replace(arg,'')

# register.filter('cut',cut)
