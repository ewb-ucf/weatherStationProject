from django.conf.urls import patterns, include, url

from django.contrib import admin
from collection_sites import views, urls

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('collection_sites.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
