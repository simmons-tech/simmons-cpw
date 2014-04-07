from django.conf.urls import patterns, url

from tours import views

urlpatterns = patterns('',
                       url(r'^$', views.info, name='index'),                       
                       url(r'^info$', views.info, name='index'),
                       url(r'^request$', views.request_tour, name='request'),
                       url(r'^claim$', views.claim_tour, name='claim'),
                       url(r'^start$', views.start_tour, name='start'),
)
                       
