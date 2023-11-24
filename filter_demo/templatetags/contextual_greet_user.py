from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def contextual_greet_user(context, message):
    username = context['username']
    return "{greeting_msg}, {user}!".format(greeting_msg=message, user=username)