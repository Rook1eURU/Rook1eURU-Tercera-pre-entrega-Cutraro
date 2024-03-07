from django.shortcuts import render
from django.http import HttpResponse
from AppMusicy.models import *
from AppMusicy.forms import *

# Inicio
def inicio(request):

    return render(request, "AppMusicy/inicio.html")

# Canciones
def songs_main(request):

    return render(request, "AppMusicy/songs.html")

def c_song(request):

    # Almaceno en tablas los formularios
    if request.method == "POST":
        form = SongFormulario(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            song = Song(title=info["title"],
                         artist=info["artist"],
                         album=info["album"],
                         year=info["year"],
                         genre=info["genre"],)

            song.save()

            return render(request, "AppMusicy/songs.html")

    else:
        form = SongFormulario()

    return render(request, "AppMusicy/C_songs.html", {"form_songs":form})

def r_song(request):

    if request.GET["title"]:
        
        title = request.GET["title"]
        song = Song.objects.filter(title__icontains=title)

        return render(request, "AppMusicy/songs.html", {"song":song, "title":title})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

# Artistas
def artists_main(request):

    return render(request, "AppMusicy/artists.html")

# Albumes
def albums_main(request):

    return render(request, "AppMusicy/albums.html")

# Géneros
def genres_main(request):

    return render(request, "AppMusicy/genres.html")