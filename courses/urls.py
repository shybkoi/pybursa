from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^$', views.course_list, name='list'),
    url(r'^add/$', views.course_edit, name='add'),
    url(r'^edit/(?P<course_id>\d+)/$', views.course_edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.course_remove, name='remove'),
    url(r'^(?P<course_id>\d+)/$', views.course_item, name='item'),
)
