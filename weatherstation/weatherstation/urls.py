from django.conf.urls import patterns, include, url

from django.contrib import admin
from collection_sites import views, urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('collection_sites.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
