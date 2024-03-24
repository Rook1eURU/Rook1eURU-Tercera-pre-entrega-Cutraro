from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True, default="Musicy\media\avatares\BigO.png")

class Song(models.Model):

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.year})"
    
    title = models.CharField(max_length=60)
    artist = models.ForeignKey('Artist', null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL)
    year = models.IntegerField()
    genre = models.ForeignKey('Genre', null=True, on_delete=models.SET_NULL)
    link = models.CharField(max_length=60, default="HPVJTT_h3nc")
    lyrics = models.TextField(default="")
    translation = models.TextField(default="")

class Artist(models.Model):

    def __str__(self):
        return f"{self.name}"
    
    name = models.CharField(max_length=60)

class Album(models.Model):

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"
    
    title = models.CharField(max_length=60)
    artist = models.ForeignKey('Artist', null=True, on_delete=models.SET_NULL)
    year = models.IntegerField()

class Genre(models.Model):

    def __str__(self):
        return f"{self.name}"
    
    name = models.CharField(max_length=60)