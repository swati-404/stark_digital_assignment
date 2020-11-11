from django.contrib import admin
from .models import Movie,Poster,Genre
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'popularity', 'director', 'imdb_score')
    search_fields = ('id', 'name','director')

class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'poster_url')
    search_fields = ('id', 'movie_name')


admin.site.register(Genre)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Poster, PosterAdmin)
