"""
The models descirbed here are used in the views file
to render data to an html page through a template.

This creates two tables in MySQL with all the parameters
as described here

"""

from django.db import models

class Sensor(models.Model):
    """
    Creates a sensor object with all the
    specifications of the sensor for data collection
    """
    dataType = models.CharField(max_length=200)
    modelnumber = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    input_pin = models.IntegerField(null=True)
    data_rate = models.FloatField(null=True)
    collection_freq = models.FloatField(null=True)
    read_time = models.FloatField(null=True)
    write_file = models.CharField(max_length=200, null=True)
    last_collection_time = models.CharField(max_length=200, default='0')

class WeatherData(models.Model):
    """
    Creates weather data object
    """
    sitename = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    value =  models.FloatField()
    dataType = models.CharField(max_length=200)
    sensor = models.ForeignKey(Sensor, null=True)

class WeatherCollectionSystem(models.Model):
    """
    Creates weather station site object
    """
    longitude = models.FloatField(null=True) 
    latitude = models.FloatField(null=True)
    altitude = models.FloatField(null=True)
    sitename = models.CharField(max_length=200)
    data = models.ForeignKey(WeatherData, null=True)
    about = models.CharField(max_length=500, null=True, blank=True)
