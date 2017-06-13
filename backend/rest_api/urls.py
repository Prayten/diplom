from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^room/(?P<room_id>\d+)/$', views.room_calendar, name='room_calendar'),
    url(r'^room/(?P<room_id>\d+)/(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})/$', views.room, name='room'),
    url(r'^teacher/(?P<teacher_id>\d+)/(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})/$', views.teacher, name='teacher'),
    url(r'^group/(?P<group_id>\d+)/(?P<y>\d{4})-(?P<m>\d{1,2})-(?P<d>\d{1,2})/$', views.group, name='group'),
]
