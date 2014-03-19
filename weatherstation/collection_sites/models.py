"""
The models descirbed here are used in the views file
to render data to an html page through a template.

This creates two tables in MySQL with all the parameters
as described here

"""

from django.db import models

class WeatherData(models.Model):
	"""
	Creates weather data object
	"""
	sitename = models.CharField(max_length=200)
	timestamp = models.DateTimeField()
	value =  models.FloatField()
	dataType = models.CharField(max_length=200)

class WeatherCollectionSystem(models.Model):
	"""
	Creates weather station site object
	"""
	location = models.FloatField(null=True)
	sitename = models.CharField(max_length=200)
	data = models.ForeignKey(WeatherData, null=True)