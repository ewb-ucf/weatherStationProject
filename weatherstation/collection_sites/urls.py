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

urlpatterns = patterns('',
    
    # Ex. domainName.com/weatherstation
    url(r'^weatherstation/$', 'collection_sites.views.weatherstationhome_template_display', name='home'),

    # Ex. domainName.com/weatherstation/drcongo/realtime
    # THIS NEEDS TO BE CHANGED SO IT ONLY DISPLAYS SITES IN THE GROUP
    #(?P<name>pattern), where name is the name of the group and pattern is some pattern to match
    url(r'^weatherstation/(\w+)/$', 'collection_sites.views.realtime_template_display', name='realtime'),
    url(r'^weatherstation/(\w+)/realtime/$', 'collection_sites.views.realtime_template_display', name='realtime'),

    # Ex. domainName.com/weatherstation/dominicanrepublic/pastdata
    url(r'^weatherstation/(\w+)/pastdata/$', 'collection_sites.views.pastdata_template_display', name='pastdata'),

    # Ex. domainName.com/weatherstation/thailand/solaranalysis
    url(r'^weatherstation/(\w+)/solaranalysis/$', 'collection_sites.views.solaranalysis_template_display', name='solaranalysis'),

    # Ex. domainName.com/weatherstation/usb/analysis/solar
    url(r'^weatherstation/(\w+)/windanalysis/$', 'collection_sites.views.windanalysis_template_display', name='windanalysis'),

    # Ex. domainName.com/weatherstation/usb/analysis/other
    url(r'^weatherstation/(\w+)/otheranalysis/$', 'collection_sites.views.otheranalysis_template_display', name='otheranalysis'),

    # Ex. domainName.com/weatherstation/someotherlocation/analysis/wind
    url(r'^weatherstation/(\w+)/pastdata/$', 'collection_sites.views.hydroanalysis_template_display', name='hydroananalysis'),

    # Default Admin
    url(r'^admin/', include(admin.site.urls)),
)
