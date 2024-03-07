from django.contrib import admin
from AppMusicy.models import *

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)