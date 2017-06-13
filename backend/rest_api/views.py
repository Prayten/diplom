from django.contrib.auth.models import Group
import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from . import models


def index(request):
    today = datetime.datetime.now()
    year = request.session.get('year', today.year)
    month = request.session.get('month', today.month)
    day = request.session.get('day', today.day)
    return redirect('week', year, month, day)


def week(request, year, month, day, group_id=None):
    year, month, day = int(year), int(month), int(day)
    request.session['year'] = year
    request.session['month'] = month
    request.session['day'] = day
    start = datetime.datetime(year, month, day)
    start -= datetime.timedelta(days=start.weekday())
    end = start + datetime.timedelta(days=7)
    if group_id is None:
        events = models.Event.objects.filter(begin__gte=start, end__lt=end)
    else:
        events = models.Event.objects.filter(begin__gte=start, end__lt=end, participants=group_id)
    return render(request, 'rest_api/week.html', {
        'start': start,
        'prev_week': start - datetime.timedelta(days=7),
        'next_week': start + datetime.timedelta(days=7),
        'events': events,
        'group': None if group_id is None else Group.objects.get(pk=group_id),
        'groups': Group.objects.all(),
    })


###################################################################################################


class EventList(ListView):
    model = models.Event


class EventNew(CreateView):
    model = models.Event
    fields = ['name', 'begin', 'end', 'room', 'subject', 'leader', 'participants']
    success_url = reverse_lazy('index')


class EventEdit(UpdateView):
    model = models.Event
    fields = ['name', 'begin', 'end', 'room', 'subject', 'leader', 'participants']
    success_url = reverse_lazy('index')


class EventDelete(DeleteView):
    model = models.Event
    success_url = reverse_lazy('index')


###################################################################################################


class RoomList(ListView):
    model = models.Room


class RoomNew(CreateView):
    model = models.Room
    fields = ['name', 'type']
    success_url = reverse_lazy('room:list')


class RoomEdit(UpdateView):
    model = models.Room
    fields = ['name', 'type']
    success_url = reverse_lazy('room:list')


class RoomDelete(DeleteView):
    model = models.Room
    success_url = reverse_lazy('room:list')


###################################################################################################


class SubjectList(ListView):
    model = models.Subject


class SubjectNew(CreateView):
    model = models.Subject
    fields = ['name', 'description']
    success_url = reverse_lazy('subject:list')


class SubjectEdit(UpdateView):
    model = models.Subject
    fields = ['name', 'description']
    success_url = reverse_lazy('subject:list')


class SubjectDelete(DeleteView):
    model = models.Subject
    success_url = reverse_lazy('subject:list')
