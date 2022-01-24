from django import template
from django.template.defaultfilters import stringfilter
from django.urls import resolve
import random
from random import randint
from uuid import uuid4
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta

register = template.Library()

@register.filter
@stringfilter
def comma_to_br(value):
    return value.replace(",","<br>")

@register.filter
@stringfilter
def pipe_to_br(value):
    return value.replace("|","<br>")

@register.filter
@stringfilter
def space_to_plus(value):
    value.replace("  "," ")
    return value.replace(" ","+")

@register.filter
def dol_no_dec(value):
    val = 0 if value == None else value
    return '{:,.0f}'.format(val)

@register.filter()
def to_int(value):
    return int(value)

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

@register.simple_tag
def random_decimal(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a*100, b*100)/100

@register.simple_tag
def random_uuid():
    return str( uuid4() )

@register.simple_tag
def random_buy_sell():
    side = random.choice(["BUY", "SELL"])
    if side == "BUY":
        return mark_safe('<td class="bb align-middle text-nowrap text-end text-success fw-bold time">'+str(side)+'</td>')
    else:
        return mark_safe('<td class="bb align-middle text-nowrap text-end text-danger fw-bold time">'+str(side)+'</td>')

@register.simple_tag
def random_datetime():
    random_point_in_time = datetime.now() + timedelta(seconds=randint(0, 86400))
    return random_point_in_time.strftime("%m/%d/%Y, %H:%M:%S")

@register.simple_tag
def random_status():
    status = random.choice(["Open", "Close", "Cancel"])
    return str(status)

