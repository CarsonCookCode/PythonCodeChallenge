import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    Entries = models.Manager()

    def __str__(self):
        return self.title

