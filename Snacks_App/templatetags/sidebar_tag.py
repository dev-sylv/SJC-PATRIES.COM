from django import template
from Snacks_App.models import *

register = template.Library()

@register.inclusion_tag('public/frontend/admin-sidebar.html')
def sidebar_list():
    cake = Cakes.objects.all()
    food =  Food.objects.all()
    drink = Drinks.objects.all()
    chocolate = Chocolate.objects.all()
    return{'cake':cake,'food':food, 'drink':drink, 'chocolate':chocolate}