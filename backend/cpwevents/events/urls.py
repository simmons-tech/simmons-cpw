from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from events import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpwtours.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),                       

    url(r'^$', views.info, name='info'),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^admin/', include(admin.site.urls)),
)
