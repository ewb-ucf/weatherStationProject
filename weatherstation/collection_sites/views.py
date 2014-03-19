"""

These views render the template html files with
data received from models.py 

Next: render a template

Think about class based views....reusable templates...

"""

from django.http import HttpResponse, Http404

from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404

from django import forms
from collection_sites.models import WeatherCollectionSystem, WeatherData


location_list = []
for i in WeatherCollectionSystem.objects.all():
	if i.sitename not in location_list:
		location_list.append(str(i.sitename))

def weatherstationhome_template_display(request):
	context = {
		'request': request,
		'location_list': location_list
				}
	return render_to_response('weatherstationhome_template.html', context)

def realtime_template_display(request, siteLocation='drcongo'):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
	return render_to_response('realtime_template.html', context)

def pastdata_template_display(request, siteLocation):
	wcs = get_object_or_404(WeatherCollectionSystem, sitename=siteLocation)
	context = {
		'request': request,
		'site': wcs}
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
		'site': wcs}
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