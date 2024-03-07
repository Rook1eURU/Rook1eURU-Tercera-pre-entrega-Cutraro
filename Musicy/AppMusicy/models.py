from django.db import models

# Modelo Canción

class Song(models.Model):

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.year})"
    
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    album = models.CharField(max_length=60)
    year = models.IntegerField()
    genre = models.CharField(max_length=60)

class Artist(models.Model):

    def __str__(self):
        return f"{self.name}"
    
    name = models.CharField(max_length=60)
    albums = models.CharField(max_length=60)

class Album(models.Model):

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"
    
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    year = models.IntegerField()
    genre = models.CharField(max_length=60)
    songs = models.CharField(max_length=60)

class Genre(models.Model):

    def __str__(self):
        return f"{self.name}"
    
    name = models.CharField(max_length=60)
    songs = models.CharField(max_length=60)