import os, datetime
from django.db import models
#from adminsortable.models import Sortable

def logo_filename(instance, filename):
    ext = filename.split('.')[-1]
    token = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    filename = "%s.%s.%s" % (instance.chan_id, token, ext)
    return os.path.join('logo', 'channel', filename)



class Country(models.Model):
    iso2 = models.CharField(
        max_length = 2,
        verbose_name = u'ISO2',
        unique = True,
        primary_key = True,
    )
    name = models.CharField(
        max_length = 96,
        verbose_name = u'Name',
    )
    class Meta:
        verbose_name = u'Country'
        verbose_name_plural = u'Countries'
        ordering = ['iso2',]
    def __unicode__(self):
        return ": ".join([self.iso2, self.name])


class Language(models.Model):
    iso2 = models.CharField(
        max_length = 2,
        verbose_name = u'ISO2',
        unique = True,
        primary_key = True,
    )
    name = models.CharField(
        max_length = 96,
        verbose_name = u'Name',
    )
    class Meta:
        verbose_name = u'Language'
        verbose_name_plural = u'Languages'
        ordering = ['iso2',]
    def __unicode__(self):
        return ": ".join([self.iso2, self.name])


class Grouping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length = 128,
        verbose_name = u'Name',
    )
    class Meta:
        verbose_name = u'Channel Group'
        verbose_name_plural = u'Channel Groups'
        ordering = ['name',]
    def __unicode__(self):
        return self.name


class ContentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length = 128,
        verbose_name = u'Name',
    )
    slug = models.CharField(
        max_length=3,
        verbose_name = u'Slug',
    )
    class Meta:
        verbose_name = u'Content Type'
        verbose_name_plural = u'Content Types'
    def __unicode__(self):
        return self.name


class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( # last property (display name)
        verbose_name = u'Display Name',
        help_text = u'The user-friendly name to display in the UI.',
        max_length = 128,
        default = u'',
        blank = True,
    )
    virtual_channel = models.IntegerField(
        verbose_name = u'Virtual Channel',
        help_text = u'Channel Number Assignment (Future Use. Ordering-only for now.)',
        default = 0,
    )
    chan_id = models.CharField(
        verbose_name = u'Channel ID',
        help_text = u'The internal identifier for this channel.',
        unique = True,
        max_length = 64,
    )
    xmltv_id = models.CharField( # tvg-id property
        verbose_name = u'XMLTV ID',
        help_text = u'The value of \"channel id\" in the EPG xmltv file.',
        default = u'',
        blank = True,
        max_length = 64,
    )
    xmltv_name = models.CharField( # tvg-id property
        verbose_name = u'XMLTV Name',
        help_text = u'The value in the XMLTV file for display-name.',
        default = u'',
        blank = True,
        max_length = 64,
    )
    logo = models.ImageField(
        verbose_name = u'Logo',
        help_text = u'Image in PNG format. Should be square, at least 256x256.',
        upload_to = logo_filename,
        null = True,
        blank = True,
    )
    stream_uri = models.CharField(
        verbose_name = u'Stream URI',
        help_text = u'Full URI, including protocol. Supports http(s), rtmp, mms, hdhomerun, etc. See the <a href="https://github.com/MarconiMediaGroup/M3U8-Creator/wiki" target="_blank">wiki</a> for details.',
        max_length = 256,
        default = u'',
        blank = True,
    )
    is_active = models.BooleanField(
        verbose_name = u'Active?',
        help_text = u'Should this channel be displayed?',
        default = True,
    )
    country = models.ForeignKey(Country, null=True)
    language = models.ForeignKey(Language, null=True)
    content_type = models.ForeignKey(ContentType, null=True)
    grouping = models.ForeignKey(Grouping, null=True)

    def has_stream(self):
        if self.stream_uri:
            return True
        else:
            return False
    has_stream.short_description = u'Stream?'
    has_stream.boolean = True

    def has_logo(self):
        if self.logo:
            return True
        else:
            return False
    has_logo.short_description = u'Logo?'
    has_logo.boolean = True

    def logo_basename(self):
        rval = self.logo.name.split(os.sep)[-1] #.rstrip('.png')
        return rval

    def logo_html(self, size=32):
        if self.logo:
            return u'<img src="%s" alt="%s" height="%i" width="%i" />' % (self.logo.url, self.name, size, size)
        else:
            return '-'
    logo_html.short_description = 'Logo'
    logo_html.allow_tags = True

    class Meta:
        verbose_name = u'Channel'
        verbose_name_plural = u'Channels'
        ordering = ['virtual_channel', ]
    def __unicode__(self):
        return self.name
