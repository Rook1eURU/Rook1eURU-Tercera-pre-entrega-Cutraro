from django import forms

class SongFormulario(forms.Form):

    title = forms.CharField()
    artist = forms.CharField()
    album = forms.CharField()
    year = forms.IntegerField()
    genre = forms.CharField()

class ArtistFormulario(forms.Form):

    name = forms.CharField()
    songs = forms.CharField()
    albums = forms.CharField()

class AlbumFormulario(forms.Form):

    title = forms.CharField()
    artist = forms.CharField()
    year = forms.IntegerField()
    genre = forms.CharField()
    songs = forms.CharField()

class GenreFormulario(forms.Form):

    name = forms.CharField()
    songs = forms.CharField()