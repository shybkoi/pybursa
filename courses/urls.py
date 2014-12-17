from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^$', views.course_list, name='list'),
    url(r'^(?P<course_id>\d+)/$', views.course_item, name='item'),
)
