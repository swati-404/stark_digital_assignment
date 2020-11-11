from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, default=None )

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    name = models.CharField(max_length=250, default=None)
    popularity = models.FloatField()
    director = models.CharField(max_length=220, default=None)
    imdb_score = models.FloatField()
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

class Poster(models.Model):
    movie_name = models.ForeignKey(Movie, related_name='movie_name', on_delete=models.CASCADE)
    poster_url = models.CharField(max_length=250, default=None)

    class Meta:
        verbose_name = "Poster"
        verbose_name_plural = "Posters"


