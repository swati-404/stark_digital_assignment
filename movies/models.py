from django.db import models


# Create your models here.
"""
Genre Model
"""
class Genre(models.Model):
    name = models.CharField(max_length=200, default="Family")

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

"""
Movie Model
"""
class Movie(models.Model):
    name = models.CharField(max_length=250, default=None)
    popularity = models.FloatField()
    director = models.CharField(max_length=220, default=None)
    imdb_score = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

"""
Poster Model
"""
class Poster(models.Model):
    movie_id = models.ForeignKey(Movie, related_name='movie_id', on_delete=models.CASCADE)
    poster_url = models.CharField(max_length=250, default=None)

    def __str__(self):
        return str(self.movie_id)

    class Meta:
        verbose_name = "Poster"
        verbose_name_plural = "Posters"
