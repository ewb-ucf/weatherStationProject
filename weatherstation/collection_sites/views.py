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

from gmapi import maps
from gmapi.forms.widgets import GoogleMap

location_list = []
for i in WeatherCollectionSystem.objects.all():
	if i.sitename not in location_list:
		location_list.append(str(i.sitename))

from highcharts.views import HighChartsBarView

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))

def weatherstationhome_template_display(request):
    	#Context tells us what vars we want to be able to access in the template
    	#on the left hand side.
        wcs_list = WeatherCollectionSystem.objects.all()
       
        gmap = maps.Map(opts = {
            'center': maps.LatLng(38, -97),
            'mapTypeId': maps.MapTypeId.TERRAIN,
            'zoom': 8,
            'mapTypeControlOptions': {
                 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
            },
        })
    	context = {
    		'request': request,
            'wcs_list': wcs_list,
    		'location_list': location_list,
            'form': MapForm(initial={'map': gmap})
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

    context = {
        'request': request,
        'site': wcs,
        'data': data,
        }
    return render_to_response('pastdata_template.html', context)


def poweranalysis_template_display(request, siteLocation):
    wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
    data = WeatherData.objects.filter(sitename=siteLocation)
    sensor = get_object_or_404(Sensor, dataType=data[0].dataType)

    context = {
        'request': request,
        'site': wcs,
        'data': data,
        }
    return render_to_response('poweranalysis_template.html', context)

def sanitationanalysis_template_display(request, siteLocation):
    wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
    data = WeatherData.objects.filter(sitename=siteLocation)
    sensor = get_object_or_404(Sensor, dataType=data[0].dataType)

    context = {
        'request': request,
        'site': wcs,
        'data': data,
        }
    return render_to_response('sanitationanalysis_template.html', context)

def agricultureanalysis_template_display(request, siteLocation):
    wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
    data = WeatherData.objects.filter(sitename=siteLocation)
    sensor = get_object_or_404(Sensor, dataType=data[0].dataType)

    context = {
        'request': request,
        'site': wcs,
        'data': data,
        }
    return render_to_response('agriculatureanalysis_template.html', context)
