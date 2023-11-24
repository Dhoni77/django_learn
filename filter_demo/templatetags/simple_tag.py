from django import template

register = template.Library()

@register.simple_tag
def greet_user(message, username):
    return "{greeting_msg}, {user}!".format(greeting_msg=message, user=username)