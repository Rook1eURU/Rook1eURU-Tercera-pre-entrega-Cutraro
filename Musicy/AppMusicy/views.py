from django.shortcuts import render
from django.http import HttpResponse
from AppMusicy.models import *
from AppMusicy.forms import *

# Inicio
def inicio(request):

    return render(request, "AppMusicy/inicio.html")

# ---------------------
# ----- CANCIONES -----
# ---------------------

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

def d_song(request, song_title, title):
    song = Song.objects.get(title = song_title)
    song.delete()

    song = Song.objects.filter(title__icontains=title)
    return render(request, "AppMusicy/songs.html", {"song":song, "title":title})


# --------------------
# ----- ARTISTAS -----
# --------------------

def artists_main(request):

    return render(request, "AppMusicy/artists.html")

def c_artist(request):

    # Almaceno en tablas los formularios
    if request.method == "POST":
        form = ArtistFormulario(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            artist = Artist(name=info["name"],
                          songs=info["songs"],
                          albums=info["albums"],)

            artist.save()

            return render(request, "AppMusicy/artists.html")

    else:
        form = ArtistFormulario()

    return render(request, "AppMusicy/C_artist.html", {"form_artists":form})

def r_artist(request):

    if request.GET["name"]:
        
        name = request.GET["name"]
        artist = Artist.objects.filter(name__icontains=name)

        return render(request, "AppMusicy/artists.html", {"artist":artist, "name":name})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

def d_artist(request, artist_name, name):
    artist = Artist.objects.get(name = artist_name)
    artist.delete()

    artist = Artist.objects.filter(name__icontains=name)
    return render(request, "AppMusicy/artists.html", {"artist":artist, "name":name})


# -------------------
# ----- ALBUMES -----
# -------------------

def albums_main(request):

    return render(request, "AppMusicy/albums.html")

def c_album(request):

    # Almaceno en tablas los formularios
    if request.method == "POST":
        form = AlbumFormulario(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            album = Album(title=info["title"],
                          artist=info["artist"],
                          year=info["year"],
                          genre=info["genre"],
                          songs=info["songs"],)

            album.save()

            return render(request, "AppMusicy/albums.html")

    else:
        form = AlbumFormulario()

    return render(request, "AppMusicy/C_album.html", {"form_albums":form})

def r_album(request):

    if request.GET["title"]:
        
        title = request.GET["title"]
        album = Album.objects.filter(title__icontains=title)

        return render(request, "AppMusicy/albums.html", {"album":album, "title":title})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

def d_album(request, album_title, title):
    album = Album.objects.get(title = album_title)
    album.delete()

    album = Album.objects.filter(title__icontains=title)
    return render(request, "AppMusicy/albums.html", {"album":album, "title":title})


# -------------------
# ----- GÉNEROS -----
# -------------------

def genres_main(request):

    return render(request, "AppMusicy/genres.html")

def c_genre(request):

    # Almaceno en tablas los formularios
    if request.method == "POST":
        form = GenreFormulario(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            genre = Genre(name=info["name"],
                          songs=info["songs"],)

            genre.save()

            return render(request, "AppMusicy/genres.html")

    else:
        form = GenreFormulario()

    return render(request, "AppMusicy/C_genre.html", {"form_genres":form})

def r_genre(request):

    if request.GET["name"]:
        
        name = request.GET["name"]
        genre = Genre.objects.filter(name__icontains=name)

        return render(request, "AppMusicy/genres.html", {"genre":genre, "name":name})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

def d_genre(request, genre_name, name):
    genre = Genre.objects.get(name = genre_name)
    genre.delete()

    genre = Genre.objects.filter(name__icontains=name)
    return render(request, "AppMusicy/genres.html", {"genre":genre, "name":name})