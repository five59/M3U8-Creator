from django.contrib import admin
from core.models import *
#from adminsortable.admin import SortableAdmin

class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'virtual_channel', 'is_active', 'has_logo', 'has_stream',
        'chan_id', 'xmltv_id', 'xmltv_name', 'grouping', ]
    list_editable = ['xmltv_id','xmltv_name', ]
    list_filter = ['grouping', 'country', 'content_type' ] # 'is_active', 'has_logo', 'has_stream',

class GroupingAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass

class ContentTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Grouping, GroupingAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
