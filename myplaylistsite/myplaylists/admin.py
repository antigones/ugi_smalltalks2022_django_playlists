from django.contrib import admin

# Register your models here.
from myplaylists.models import Artist, Song

# Register your models here.
admin.site.register(Artist)
admin.site.register(Song)