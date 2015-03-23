from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples: 5
    # url(r'^blog/', include('blog.urls')),
    url(r'^iptv/', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('core.views.home'))),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
