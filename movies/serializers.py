from rest_framework import serializers
from .models import Movie, Genre, Poster


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
