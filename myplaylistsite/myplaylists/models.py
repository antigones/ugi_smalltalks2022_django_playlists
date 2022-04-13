from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name