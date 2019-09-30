from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^event/delete/(?P<event_id>\d+)/$', views.delete, name='event_delete'),
    path('delete/<int:event_id>', views.delete, name='event_delete'),
]
