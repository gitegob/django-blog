from django.db import models
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    user = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
