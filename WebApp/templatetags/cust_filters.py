from django import template
register = template.Library()

def truncaten(value, n):
    #custom Filter
    result = value[0:n]
    return result
register.filter('t_n', truncaten)