from django.conf.urls import patterns, include, url
from coaches import views


urlpatterns = patterns('',
    url(r'^$', views.CoachListView.as_view(), name='list'),
    url(r'^add/$', views.CoachCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CoachUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CoachDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/$', views.CoachDetailView.as_view(), name='item'),
)
