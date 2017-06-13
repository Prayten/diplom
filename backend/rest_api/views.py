import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models


def index(request):
    today = datetime.datetime.now()
    return render(request, 'rest_api/index.html', {
        'today': today,
        'groups': models.Group.objects.all(),
        'rooms': models.Room.objects.all(),
        'teachers': models.Teacher.objects.all(),
    })


def room(request, room_id, y, m, d):
    y, m, d = int(y), int(m), int(d)
    start = datetime.datetime(y, m, d)
    start -= datetime.timedelta(days=start.weekday())
    end = start + datetime.timedelta(days=7)
    events = models.Event.objects.filter(begin__gte=start, end__lt=end, room=room_id)
    return render(request, 'rest_api/week.html', {
        'start': start,
        'room': get_object_or_404(models.Room, pk=room_id),
        'prev': start - datetime.timedelta(days=7),
        'next': start + datetime.timedelta(days=7),
        'events': events,
    })


def teacher(request, teacher_id, y, m, d):
    y, m, d = int(y), int(m), int(d)
    start = datetime.datetime(y, m, d)
    start -= datetime.timedelta(days=start.weekday())
    end = start + datetime.timedelta(days=7)
    events = models.Event.objects.filter(begin__gte=start, end__lt=end, teacher=teacher_id)
    return render(request, 'rest_api/week.html', {
        'start': start,
        'teacher': get_object_or_404(models.Teacher, pk=teacher_id),
        'prev': start - datetime.timedelta(days=7),
        'next': start + datetime.timedelta(days=7),
        'events': events,
    })


def group(request, group_id, y, m, d):
    y, m, d = int(y), int(m), int(d)
    start = datetime.datetime(y, m, d)
    start -= datetime.timedelta(days=start.weekday())
    end = start + datetime.timedelta(days=7)
    events = models.Event.objects.filter(begin__gte=start, end__lt=end, participants=group_id)
    return render(request, 'rest_api/week.html', {
        'start': start,
        'group': get_object_or_404(models.Group, pk=group_id),
        'prev': start - datetime.timedelta(days=7),
        'next': start + datetime.timedelta(days=7),
        'events': events,
    })


def room_calendar(request, room_id):
    events = models.Event.objects.all()
    response = render(request, 'rest_api/calendar.ics', {
        'events': events,
    }, 'text/calendar')
    response.content = response.content.replace(b'\n', b'\r\n')
    return response
