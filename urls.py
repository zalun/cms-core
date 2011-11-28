from django.conf import settings
from django.conf.urls.defaults import url, include, patterns
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.views import static

admin.autodiscover()

# Do not use 5 char links to avoid confusion with fiddles

urlpatterns = patterns('',
    (r'^api/v1/', include('fiber.api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
)

#urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
