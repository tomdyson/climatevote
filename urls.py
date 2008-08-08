from django.conf.urls.defaults import *
from settings import MEDIA_ROOT

urlpatterns = patterns('',
     # static and direct-to-template URLs
     (r'^static/(.+)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
     (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
     (r'^about$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}),
     # doing and viewing pledges
     (r'^pledge$', 'views.pledge'),
     (r'^pledges$', 'views.pledges'),
     (r'^message/(?P<pledger>.+)$', 'views.messages'),
)