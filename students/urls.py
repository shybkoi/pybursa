from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'^$', views.students_list, name='list'),
    url(r'^add/$', views.students_edit, name='add'),
    url(r'^edit/(?P<student_id>\d+)/$', views.students_edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.students_remove, name='remove'),
    url(r'^(?P<student_id>\d+)/$', views.students_item, name='item'),
)
