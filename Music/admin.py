# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Music.models import *

# Register your models here.



class collab_artistAdmin(admin.ModelAdmin):
    list_display = ('name', 'song_name')
    list_filter = ("name",)

class musicAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'featuring', 'studio','submission_date')
    list_filter = ("name",)

admin.site.register(collab_artist,collab_artistAdmin)
admin.site.register(music,musicAdmin)