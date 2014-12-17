from django.conf.urls import patterns, include, url
from coaches import views


urlpatterns = patterns('',
    url(r'^$', views.coaches_list, name='list'),
    url(r'^(?P<coach_id>\d+)/$', views.coach_item, name='item'),
)
