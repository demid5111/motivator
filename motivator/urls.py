from django.conf.urls import patterns, include, url

from django.contrib import admin
from aimer import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'motivator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('aimer.urls', namespace="aimer")),
    url(r'^admin/', include(admin.site.urls)),
)
