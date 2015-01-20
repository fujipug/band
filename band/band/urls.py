from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'band.views.home', name='home'),
    url(r'^contacts', 'band.views.contacts', name='contacts'),
    url(r'^bio', 'band.views.bio', name='bio'),
    url(r'^tourdates', 'band.views.tourdates', name='tourdates'),
    url(r'^home', 'band.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
