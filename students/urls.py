from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'^$', views.students_list, name='list'),
    url(r'^(?P<student_id>\d+)/$', views.students_item, name='item'),
)
