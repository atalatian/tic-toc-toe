

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models
import json
from django import forms

from django.utils import timezone


class GameHistory(models.Model):
    turn1 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn2 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn3 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn4 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn5 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn6 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn7 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn8 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    turn9 = ArrayField(models.IntegerField(null=True, blank=True, default=None), null=True, blank=True)

    user = models.CharField(max_length=10, null=True, blank=True, default=None)
    computer = models.CharField(max_length=10, null=True, blank=True, default=None)
    row = models.BooleanField(default=False)
    starter = models.CharField(max_length=10, null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return "(" + "User: " + str(self.user) + " | " + "Computer: " + str(self.computer) + " | " \
               + "Row: " + str(self.row) + ")"



class mainObject(models.Model):
    mainObject = JSONField(null=True, encoder=json.JSONEncoder, default=dict)