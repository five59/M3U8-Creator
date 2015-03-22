from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('core.views',
    url(r'^channels\.m3u8', 'playlist', name='playlist'),
)
