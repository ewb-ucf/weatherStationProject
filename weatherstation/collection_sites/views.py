"""

These views render the template html files with
data received from models.py 

Next: render a template

Think about class based views....reusable templates...

"""
import flot
import math
import datetime
from django.views.generic import TemplateView

from django.http import HttpResponse, Http404

from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404

from django import forms
from collection_sites.models import *


location_list = []
for i in WeatherCollectionSystem.objects.all():
	if i.sitename not in location_list:
		location_list.append(str(i.sitename))

def weatherstationhome_template_display(request):
	#Context tells us what vars we want to be able to access in the template
	#on the left hand side.
	context = {
		'request': request,
		'location_list': location_list
				}
	return render_to_response('weatherstationhome_template.html', context)

def realtime_template_display(request, siteLocation):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
	return render_to_response('realtime_template.html', context)

def pastdata_template_display(request, siteLocation):
    wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
    data = WeatherData.objects.filter(sitename=siteLocation)
    sensor = get_object_or_404(Sensor, dataType=data[0].dataType)

    x_time_points = []
    d = WeatherData.objects.values('timestamp')
    for item in d:
        x_time_points.append(item.get('timestamp'))
    y_points = data.values_list('value')

    t_series = flot.Series(x=flot.TimeXVariable(points=x_time_points),
                        y=flot.YVariable(points=y_points),
                        options=flot.SeriesOptions(points={'show': True},
                                                    lines={'show': True},
                                                    label='Temperature in Celcius',
                                                    hoverable=True,
                                                    color='blue'))

    graph_option = flot.GraphOptions(xaxis={'format': '%d/%m/%Y'})

    context = {
        'request': request,
        'site': wcs,
        'data': data,
        'sensor':sensor,
        'graph1': flot.Graph(series1=t_series, options=graph_option),
        }
    return render_to_response('pastdata_template.html', context)


def solaranalysis_template_display(request, siteLocation):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
	return render_to_response('solaranalysis_template.html', context)

def windanalysis_template_display(request, siteLocation):
    wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
    context = {
        'request': request,
        'site': wcs,
        }
    return render_to_response('windanalysis_template.html', context)

def otheranalysis_template_display(request, siteLocation):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
	return render_to_response('windanalysis_template.html', context)

def hydroanalysis_template_display(request, siteLocation):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
	return render_to_response('hydroanalysis_template.html', context)
