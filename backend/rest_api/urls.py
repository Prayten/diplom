from django.conf.urls import url, include
from . import views

room_patterns = ([
    url(r'^$', views.RoomList.as_view(), name='list'),
    url(r'^new/$', views.RoomNew.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', views.RoomEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.RoomDelete.as_view(), name='delete'),
], 'room')

subject_patterns = ([
    url(r'^$', views.SubjectList.as_view(), name='list'),
    url(r'^new/$', views.SubjectNew.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', views.SubjectEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.SubjectDelete.as_view(), name='delete'),
], 'subject')

event_patterns = ([
    url(r'^$', views.EventList.as_view(), name='list'),
    url(r'^new/$', views.EventNew.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', views.EventEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.EventDelete.as_view(), name='delete'),
], 'event')

urlpatterns = [
    url(r'^room/', include(room_patterns, namespace='room')),
    url(r'^subject/', include(subject_patterns, namespace='subject')),
    url(r'^event/', include(event_patterns, namespace='event')),
    url(r'^$', views.index, name='index'),
    url(r'^w/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', views.week, name='week'),
    url(r'^w/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/(?P<group_id>\d+)/$', views.week, name='week_g'),
    url(r'^w/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/(?P<group_id>\d+)/$', views.week, name='week_gr'),
    url(r'^w/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/(?P<group_id>\d+)/$', views.week, name='week_r'),
]
