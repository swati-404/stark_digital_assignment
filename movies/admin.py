from django.contrib import admin
from .models import Movie, Poster, Genre


# Register your models here.
"""
For displaying data on movie list page
"""
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'popularity', 'director', 'imdb_score')
    search_fields = ('id', 'name', 'director')

"""
For displaying data on poster list page
"""
class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_id', 'poster_url')
    search_fields = ('id', 'movie_id')


admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Poster, PosterAdmin)
