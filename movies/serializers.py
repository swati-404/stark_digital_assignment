from rest_framework import serializers
from .models import Movie, Genre, Poster

"""
Serializer for Genre Model
"""
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

"""
serializer for Poster model
"""
class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

"""
serializer for Movie Model
"""
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
