from django.conf import settings
from django.conf.urls.defaults import url, include, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import static

from base.views import fake

admin.autodiscover()

# Do not use 5 char links to avoid confusion with fiddles

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', static.serve,
        {'document_root': settings.MEDIA_ROOT}, name='media'),
    #url(r'^$', fake, name='fake'),

    (r'^lib/', include('library.urls')),
    (r'^account/', include('registration.urls')),

    (r'^adm/doc/', include('django.contrib.admindocs.urls')),
    (r'^adm/', include(admin.site.urls)),

    url(r'', include('fiddle.urls'))
)

urlpatterns += staticfiles_urlpatterns()
