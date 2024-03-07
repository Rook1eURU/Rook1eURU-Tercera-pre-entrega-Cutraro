from django.urls import path

# Mis vistas
from AppMusicy.views import *

urlpatterns = [
    # Main
    path('', inicio, name="Inicio"),

    # Canciones
    path('songs/', songs_main, name="Canciones"),
    path('songCreate/', c_song, name="C_Canciones"),
    path('songRead/', r_song, name="R_Canciones"),
    
    # Artistas
    path('artists/', artists_main, name="Artistas"),
    
    # Albumes
    path('albums/', albums_main, name="Albumes"),
    
    # Géneros
    path('genres/', genres_main, name="Géneros")
]