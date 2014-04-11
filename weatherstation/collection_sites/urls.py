from django.conf.urls import patterns, include, url
from django.template import RequestContext

from django.contrib import admin
from collection_sites import views
admin.autodiscover()

from collection_sites.models import WeatherCollectionSystem, WeatherData

location_list = []
for i in WeatherCollectionSystem.objects.all():
    if i.sitename not in location_list:
        location_list.append(str(i.sitename))

#This regex captures any of the locations listed in location_list
sites_re = '(?:' + '|'.join(location_list) + ')'

urlpatterns = patterns('',
   
    # Ex. domainName.com/weatherstation
    url(r'^weatherstation/$', 'collection_sites.views.weatherstationhome_template_display', name='home'),

    # Ex. domainName.com/weatherstation/<site location>/realtime, where site location is a location in location_list
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/$', 'collection_sites.views.realtime_template_display', name='realtime'),
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/realtime/$', 'collection_sites.views.realtime_template_display', name='realtime'),

    # Ex. domainName.com/weatherstation/dominicanrepublic/pastdata
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/pastdata/$', 'collection_sites.views.pastdata_template_display', name='pastdata'),

    # Ex. domainName.com/weatherstation/thailand/solaranalysis
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/poweranalysis/$', 'collection_sites.views.poweranalysis_template_display', name='poweranalysis'),

    # Ex. domainName.com/weatherstation/usb/analysis/solar
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/sanitationanalysis/$', 'collection_sites.views.sanitationanalysis_template_display', name='sanitationanalysis'),

    # Ex. domainName.com/weatherstation/usb/analysis/solar
    url(r'^weatherstation/' + '(?P<siteLocation>' + sites_re + ')/agricultureanalysis/$', 'collection_sites.views.agricultureanalysis_template_display', name='agricultureanalysis'),


    # Default Admin
    url(r'^admin/', include(admin.site.urls)),
)
