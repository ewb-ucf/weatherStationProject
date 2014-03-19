#!/usr/bin/env python

"""
Description: 
This file holds all custom filters for collection_sites app

"""

__author__          ="McKinnley Workman"
__creationDate__    = 06-03-2014
__lastModified__    = ''

__license__         ="GPL"
__version__         ="1.0"
__status__          ="Development"

from django import template
from datetime import date, timedelta
import re

register = template.Library()

@register.filter(name='url_tail')
def url_tail(value):
    p = re.split('\.com', value)
    return p[-1]
