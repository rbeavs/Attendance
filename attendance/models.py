from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin


class Event(models.Model):
    events = models.CharField(max_length=50)

    def __str__(self):
        return self.events


class Snippet(models.Model):
    name = models.CharField(max_length=200)
    FR = models.BooleanField(default=False)
    SO = models.BooleanField(default=False)
    JR = models.BooleanField(default=False)
    SR = models.BooleanField(default=False)
    email = models.EmailField(default='')
    points = models.IntegerField(default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    @admin.display(
        ordering='created_at',
        description='Submitted',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=6) <= self.created_at <= now
