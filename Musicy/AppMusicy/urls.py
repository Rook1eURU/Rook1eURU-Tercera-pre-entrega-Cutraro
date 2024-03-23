from django.urls import path
from django.contrib.auth.views import LogoutView

# Mis vistas
from AppMusicy.views import *

urlpatterns = [
    # Main
    path('', inicio, name="Inicio"),
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    path('edit/', edit_user, name="Edit"),
    path('logout/', logout_request, name="Logout"),
    path('avatar/', add_avatar, name="Avatar"),

    # Canciones
    path('songs/', songs_main, name="Canciones"),
    path('songCreate/', c_song, name="C_Canciones"),
    path('songRead/', r_song, name="R_Canciones"),
    path('songUpdate/<song_title>/<title>/', u_song, name="U_Canciones"),
    path('songDelete/<song_title>/<title>/', d_song, name="D_Canciones"),
    
    # Artistas
    path('artists/', artists_main, name="Artistas"),
    path('artistCreate/', c_artist, name="C_Canciones"),
    path('artistRead/', r_artist, name="R_Artistas"),
    path('artistUpdate/<artist_name>/<name>/', u_artist, name="U_Artistas"),
    path('artistDelete/<artist_name>/<name>/', d_artist, name="D_Artistas"),
    
    # Albumes
    path('albums/', albums_main, name="Albumes"),
    path('albumCreate/', c_album, name="C_Albumes"),
    path('albumRead/', r_album, name="R_Albumes"),
    path('albumUpdate/<album_title>/<title>/', u_album, name="U_Albumes"),
    path('albumDelete/<album_title>/<title>/', d_album, name="D_Albumes"),
    
    # Géneros
    path('genres/', genres_main, name="Géneros"),
    path('genreCreate/', c_genre, name="C_Géneros"),
    path('genreRead/', r_genre, name="R_Géneros"),
    path('genreUpdate/<genre_name>/<name>/', u_genre, name="U_Géneros"),
    path('genreDelete/<genre_name>/<name>/', d_genre, name="D_Géneros"),
]