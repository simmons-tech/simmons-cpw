from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tours import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpwtours.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),                       

    url(r'^$', views.info, name='info'),
    url(r'^tours/', include('tours.urls', namespace='tours')),
    url(r'^admin/', include(admin.site.urls)),
)
