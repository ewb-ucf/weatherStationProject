"""
The models descirbed here are used in the views file
to render data to an html page through a template.

This creates two tables in MySQL with all the parameters
as described here

"""

from django.contrib import admin
from models import *

admin.site.register(WeatherData)
admin.site.register(WeatherCollectionSystem)
admin.site.register(Sensor)
