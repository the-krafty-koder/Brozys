# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class collab_artist(models.Model):
    name = models.CharField(max_length=25)
    song_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class music(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=25, default="Brozy")
    description = models.TextField(default="Listen and get me the feedback")
    featuring = models.ForeignKey(collab_artist,on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now=True)
    studio = models.CharField(max_length = 25)
    cover_image = models.ImageField(upload_to="media/songCoverFolder")
    song_file = models.FileField(upload_to="media/songFileFolder",null=True)

    def __str__(self):
        return self.name
