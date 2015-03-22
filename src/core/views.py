from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

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


#    response = HttpResponse(content_type='application/x-mpegURL')
#    response['Content-Disposition'] = 'attachment; filename="channels.m3u8"'
    response = HttpResponse(content_type='text/html; charset=utf-8')
    response.content = "<html><body><pre>",items,"</pre></body></html>"
    return response


    #EXTINF:-1 tvg-id="id1" tvg-name="Channel_1" tvg-logo="logo1" group-title="Group 1",Channel 1

    # chan_id = models.CharField( # tvg-id property
    # slug = models.CharField( # tvg-name property
    # logo_name = models.CharField( # tvg-logo property
    # grouping = models.ForeignKey(Grouping, null=True)
    # stream_uri = models.CharField(
    #
    # country = models.ForeignKey(Country, null=True)
    # name = models.CharField( # last property (display name)
    #
    #
    # id = models.AutoField(primary_key=True)
    # chan_order = models.IntegerField(
