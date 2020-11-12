from django.shortcuts import render, redirect
from .models import Movie, Poster, Genre
from django.http import HttpResponse
from rest_framework import status
from .forms import MovieForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer, PosterSerializer, GenreSerializer


# Create your views here.
class IndexView(APIView):
    allowed_methods = ['GET']
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def user_login(request):
    return render(request, 'movies/login_page.html')


def index(request):
    movies = Movie.objects.all()
    movie_serializer = MovieSerializer(movies, many=True)
    for movie in movie_serializer.data:
        poster_url = Poster.objects.get(movie_id=movie['id']).poster_url
        movie['poster_url'] = poster_url
        genres = movie['genre']
        genres_text = ''
        for genre in genres:
            genre_name = Genre.objects.get(pk=genre).name
            genres_text = genres_text + (genre_name if genres_text == '' else ', ' + genre_name)
        movie['genre'] = genres_text
    param = {'movies': movie_serializer.data}
    return render(request, 'home.html', param)


def update(request, id):
    mov = Movie.objects.get(id=id)
    form = MovieForm(request.POST, instance=mov)
    param = {'mov': mov, 'form': form}
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/home/")
    return render(request, 'edit.html', param)


def delete(request, id):
    mov = Movie.objects.filter(pk=id)
    mov.delete()
    return redirect('http://127.0.0.1:8000/home')


def New_Movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home/')
            except:
                pass
    else:
        form = MovieForm()

    return render(request, 'create_movie.html',
                  {'form': form}
                  )
