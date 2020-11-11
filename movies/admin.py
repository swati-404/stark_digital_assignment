from django.contrib import admin
from .models import Movie,Poster,Genre
# Register your models here.
admin.site.register(Movie)
admin.site.register(Poster)
admin.site.register(Genre)