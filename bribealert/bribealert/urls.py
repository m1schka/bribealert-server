from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bribe.models import Bribe

admin.autodiscover()

urlpatterns = patterns('',
	(r'^upload/$',   'bribe.views.upload'),
    (r'^national-chapter/$', 'bribe.views.get_national_chapter'),
	(r'^$',          direct_to_template, {'template': 'home.html', 'extra_context': { 
	    'bribes': Bribe.objects.published(), 
    }}),    
    (r'^admin/',     include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
