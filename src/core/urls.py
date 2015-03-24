from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('core.views',
    url(r'^channels\.m3u8', 'playlist', name='playlist'),
    url(r'^logo/', RedirectView.as_view(url=reverse_lazy('core.views.home'))),
    url(r'^xmltv\.xml', 'xmltv', name='xmltv'),
    url(r'^$', 'home', name='home'),
)

# Logos are found here, served statically: /media/logo/channel/x.png
