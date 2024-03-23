from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppMusicy.models import Avatar

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