from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^$', views.CourseListView.as_view(), name='list'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='item'),
)
