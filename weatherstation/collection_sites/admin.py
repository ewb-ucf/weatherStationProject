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
	timestamp = models.DateTimeField()
	value =  models.FloatField()
	dataType = models.CharField(max_length=200)
	collection_frequency = models.FloatField()

	def get_locations_list():
		"""
		Return a list of objects
		"""
		pass

class WeatherCollectionSystem(models.Model):
	location = models.FloatField()
	name = models.CharField(max_length=200)
	data = models.ForeignKey(WeatherData)
