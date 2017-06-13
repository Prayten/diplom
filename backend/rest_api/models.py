from django.db import models
from django.urls import reverse
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Room(models.Model):
    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        ordering = ['name']

    COMPUTER_LAB = 'CMP'
    REGULAR_ROOM = 'STD'
    LARGE_ROOM = 'BIG'

    TYPES = [
        (COMPUTER_LAB, 'Компьютерный класс'),
        (REGULAR_ROOM, 'Лекционная аудитория'),
        (LARGE_ROOM, 'Большая лекционная аудитория'),
    ]

    name = models.CharField('Наименование', max_length=25)
    type = models.CharField('Тип', max_length=3, choices=TYPES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room_edit', args=[str(self.id)])


class Subject(models.Model):
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        ordering = ['name']

    name = models.CharField('Наименование', max_length=25)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['begin', 'name']

    name = models.CharField('Наименование', max_length=30)
    begin = models.DateTimeField('Начало')
    end = models.DateTimeField('Завершение')
    room = models.ForeignKey('Room')
    parent = models.ForeignKey('Event', verbose_name='Родительское событие', null=True, blank=True)
    period = models.IntegerField('Период повторения', blank=True, default=0)
    count = models.IntegerField('Количество повторений', blank=True, default=0)
    subject = models.ForeignKey('Subject', verbose_name='Дисциплина', null=True, blank=True)
    leader = models.ForeignKey('auth.User', verbose_name='Ведущий', null=True, blank=True)
    participants = models.ForeignKey('auth.Group', verbose_name='Участники', null=True, blank=True)

    def __str__(self):
        return '{:%Y-%m-%d %H:%M} {}'.format(self.begin, self.name)
