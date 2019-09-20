# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers

from django.shortcuts import render
from .models import *

# Create your views here.

def getMusic(request):
    numsongs = music.objects.all().count()
    songslist = serializers.serialize("json", music.objects.all())
    return render(request,"music.html",{"songs_list":songslist,"numsongs":numsongs})
