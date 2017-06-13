from django.contrib import admin

from . import models

admin.site.register(models.Event)
admin.site.register(models.Room)
admin.site.register(models.Subject)
admin.site.register(models.Teacher)
