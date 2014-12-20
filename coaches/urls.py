from django.conf.urls import patterns, include, url
from coaches import views


urlpatterns = patterns('',
    url(r'^$', views.coaches_list, name='list'),
    url(r'^add/$', views.coach_edit, name='add'),
    url(r'^edit/(?P<coach_id>\d+)/$', views.coach_edit, name='edit'),
    url(r'^remove/(?P<coach_id>\d+)/$', views.coach_remove, name='remove'),
    url(r'^(?P<coach_id>\d+)/$', views.coach_item, name='item'),
)
