from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from core.models import *

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def xmltv(request):
    response = HttpResponse(content_type='text/html; charset=utf-8')
    response.content = "<html><body>XMLTV Page</body></html>"
    return response

def playlist(request):
    items = u'#EXTM3U\n\n'
    active_channels = Channel.objects.all()
    for ac in active_channels:
        if ac.is_active:
            items += '#EXTINF: -1'
            if ac.xmltv_id:
                items += u''.join([' tvg-id="',ac.xmltv_id,'"'])
            if ac.xmltv_name:
                items += u''.join([' tvg-name="',ac.xmltv_name,'"'])
            if ac.logo:
                items += u''.join([' tvg-logo="',ac.logo_basename(),'"'])
            if ac.grouping:
                items += u''.join([' group-title="',ac.grouping.name,'"'])
            if ac.name:
                if ac.country:
                    items += u''.join([',',ac.country.iso2,': ',ac.name])
                else:
                    items += u''.join([',',ac.name])
            items += u''.join(['\n', ac.stream_uri, "\n\n"])

            # response = HttpResponse(content_type='application/x-mpegURL')
            # response['Content-Disposition'] = 'attachment; filename="channels.m3u8"'

    response = HttpResponse(content_type='text/html; charset=utf-8')
    response.content = items
#    response.content = "<html><body><pre>",items,"</pre></body></html>"
    return response
