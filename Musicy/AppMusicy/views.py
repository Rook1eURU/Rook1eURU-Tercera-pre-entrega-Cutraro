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
        
    title = "Todos"
    song = Song.objects.all()

    return render(request, "AppMusicy/M_songs.html", {"song":song, "title":title})

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

            return render(request, "AppMusicy/M_songs.html")

    else:
        form = SongFormulario()

    return render(request, "AppMusicy/C_songs.html", {"form_songs":form})

def r_song(request):

    if request.GET["title"]:
        
        title = request.GET["title"]
        song = Song.objects.filter(title__icontains=title)

        return render(request, "AppMusicy/M_songs.html", {"song":song, "title":title})

    else:
        
        title = "Todos"
        song = Song.objects.all()

        return render(request, "AppMusicy/M_songs.html", {"song":song, "title":title})

def u_song(request, song_title, title):
    song = Song.objects.get(title = song_title)

    if request.method == "POST":
        form = SongFormulario(request.POST)
        print(form)

        if form.is_valid:
            info = form.cleaned_data

            song.title = info['title']
            song.album = info['album']
            song.artist = info['artist']
            song.year = info['year']
            song.genre = info['genre']

            song.save()

            song = Song.objects.filter(title__icontains=title)
            return render(request, "AppMusicy/M_songs.html", {"song":song, "title":title})
        
    else:

        form = SongFormulario(initial={'title': song.title,
                                       'album': song.album,
                                       'artist': song.artist,
                                       'year': song.year,
                                       'genre': song.genre,})

    return render(request, "AppMusicy/U_songs.html", {"form_songs":form, "title":song_title})

def d_song(request, song_title, title):
    song = Song.objects.get(title = song_title)
    song.delete()

    song = Song.objects.filter(title__icontains=title)
    return render(request, "AppMusicy/M_songs.html", {"song":song, "title":title})


# --------------------
# ----- ARTISTAS -----
# --------------------

def artists_main(request):
        
    name = "Todos"
    artist = Artist.objects.all()

    return render(request, "AppMusicy/M_artists.html", {"artist":artist, "name":name})

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

            return render(request, "AppMusicy/M_artists.html")

    else:
        form = ArtistFormulario()

    return render(request, "AppMusicy/C_artist.html", {"form_artists":form})

def r_artist(request):

    if request.GET["name"]:
        
        name = request.GET["name"]
        artist = Artist.objects.filter(name__icontains=name)

        return render(request, "AppMusicy/M_artists.html", {"artist":artist, "name":name})

    else:
        
        name = "Todos"
        artist = Artist.objects.all()

        return render(request, "AppMusicy/M_artists.html", {"artist":artist, "name":name})

def u_artist(request, artist_name, name):
    artist = Artist.objects.get(name = artist_name)

    if request.method == "POST":
        form = ArtistFormulario(request.POST)
        print(form)

        if form.is_valid:
            info = form.cleaned_data

            artist.name = info['name']
            artist.songs = info['songs']
            artist.albums = info['albums']

            artist.save()

            artist = Artist.objects.filter(name__icontains=name)
            return render(request, "AppMusicy/M_artists.html", {"artist":artist, "name":name})
        
    else:

        form = ArtistFormulario(initial={'name': artist.name,
                                         'songs': artist.songs,
                                         'albums': artist.albums,})

    return render(request, "AppMusicy/U_artists.html", {"form_artists":form, "name":artist_name})

def d_artist(request, artist_name, name):
    artist = Artist.objects.get(name = artist_name)
    artist.delete()

    artist = Artist.objects.filter(name__icontains=name)
    return render(request, "AppMusicy/M_artists.html", {"artist":artist, "name":name})


# -------------------
# ----- ALBUMES -----
# -------------------

def albums_main(request):
        
    title = "Todos"
    album = Album.objects.all()

    return render(request, "AppMusicy/M_albums.html", {"album":album, "title":title})

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

            return render(request, "AppMusicy/M_albums.html")

    else:
        form = AlbumFormulario()

    return render(request, "AppMusicy/C_album.html", {"form_albums":form})

def r_album(request):

    if request.GET["title"]:
        
        title = request.GET["title"]
        album = Album.objects.filter(title__icontains=title)

        return render(request, "AppMusicy/M_albums.html", {"album":album, "title":title})

    else:
        
        title = "Todos"
        album = Album.objects.all()

        return render(request, "AppMusicy/M_albums.html", {"album":album, "title":title})

def u_album(request, album_title, title):
    album = Album.objects.get(title = album_title)

    if request.method == "POST":
        form = AlbumFormulario(request.POST)
        print(form)

        if form.is_valid:
            info = form.cleaned_data

            album.title = info['title']
            album.artist = info['artist']
            album.year = info['year']
            album.genre = info['genre']
            album.songs = info['songs']

            album.save()

            album = Album.objects.filter(title__icontains=title)
            return render(request, "AppMusicy/M_albums.html", {"album":album, "title":title})
        
    else:

        form = AlbumFormulario(initial={'title': album.title,
                                        'artist': album.artist,
                                        'year': album.year,
                                        'genre': album.genre,
                                        'songs': album.songs,})

    return render(request, "AppMusicy/U_albums.html", {"form_albums":form, "title":album_title})

def d_album(request, album_title, title):
    album = Album.objects.get(title = album_title)
    album.delete()

    album = Album.objects.filter(title__icontains=title)
    return render(request, "AppMusicy/M_albums.html", {"album":album, "title":title})


# -------------------
# ----- GÉNEROS -----
# -------------------

def genres_main(request):
        
    name = "Todos"
    genre = Genre.objects.all()

    return render(request, "AppMusicy/M_genres.html", {"genre":genre, "name":name})

def c_genre(request):

    # Almaceno en tablas los formularios
    if request.method == "POST":
        form = GenreFormulario(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            genre = Genre(name=info["name"],
                          songs=info["songs"],)

            genre.save()

            return render(request, "AppMusicy/M_genres.html")

    else:
        form = GenreFormulario()

    return render(request, "AppMusicy/C_genre.html", {"form_genres":form})

def r_genre(request):

    if request.GET["name"]:
        
        name = request.GET["name"]
        genre = Genre.objects.filter(name__icontains=name)

        return render(request, "AppMusicy/M_genres.html", {"genre":genre, "name":name})

    else:
        
        name = "Todos"
        genre = Genre.objects.all()

        return render(request, "AppMusicy/M_genres.html", {"genre":genre, "name":name})

def u_genre(request, genre_name, name):
    genre = Genre.objects.get(name = genre_name)

    if request.method == "POST":
        form = GenreFormulario(request.POST)
        print(form)

        if form.is_valid:
            info = form.cleaned_data

            genre.name = info['name']
            genre.songs = info['songs']

            genre.save()

            genre = Genre.objects.filter(name__icontains=name)
            return render(request, "AppMusicy/M_genres.html", {"genre":genre, "name":name})
        
    else:

        form = GenreFormulario(initial={'name': genre.name,
                                        'songs': genre.songs,})

    return render(request, "AppMusicy/U_genres.html", {"form_genres":form, "name":genre_name})

def d_genre(request, genre_name, name):
    genre = Genre.objects.get(name = genre_name)
    genre.delete()

    genre = Genre.objects.filter(name__icontains=name)
    return render(request, "AppMusicy/M_genres.html", {"genre":genre, "name":name})