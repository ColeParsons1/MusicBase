from django.contrib import admin
from django.db import models
from .models import Artist
from .models import Album
from .models import Genre


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)


class ModelAdmin(admin.ModelAdmin):
  admin.site.site_header = 'MusicBase'
  admin.site.site_title = 'MusicBase'
  list_display = ('id', 'genre_history')
  class Media:
           
        css = {
             'all': ('music/styles.css',)
        }