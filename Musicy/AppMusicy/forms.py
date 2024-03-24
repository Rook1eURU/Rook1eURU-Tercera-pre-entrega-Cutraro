from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppMusicy.models import *

class SongFormulario(forms.Form):

    title = forms.CharField()
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    album = forms.ModelChoiceField(queryset=Album.objects.all())
    year = forms.IntegerField()
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    link = forms.CharField()
    lyrics = forms.CharField(widget=forms.Textarea)
    translation = forms.CharField(widget=forms.Textarea)

class ArtistFormulario(forms.Form):

    name = forms.CharField()

class AlbumFormulario(forms.Form):

    title = forms.CharField()
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    year = forms.IntegerField()

class GenreFormulario(forms.Form):

    name = forms.CharField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Nombre de Usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class EditFormulario(UserCreationForm):

    username = forms.CharField(label="Nombre de Usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]