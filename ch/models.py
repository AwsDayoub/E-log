from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now())


class Message(models.Model):
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=100000)