from django.shortcuts import render, redirect
from .models import Movie, Poster, Genre
from django.http import HttpResponse
from rest_framework import status
from .forms import MovieForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer, PosterSerializer, GenreSerializer


# Create your views here.
"""
APIs to search Movie
"""
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
"""
Api to create Movie
"""
class CreateMovieAPIView(APIView):
    def post(self,request,format=None):
        poster_url = request.data["poster_url"]
        serializer = MovieSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print(
                "valid"
            )
            name = serializer.validated_data.get("name")
            popularity = serializer.validated_data.get("popularity")
            director = serializer.validated_data.get("director")
            imdb_score = serializer.validated_data.get("imdb_score")
            genre = serializer.validated_data.get("genre")
            id = serializer.save()
            poster_obj = {
                "movie_id": id,
                "poster_url":poster_url,
            }
            Poster.objects.create(**poster_obj)
            print(serializer.data['id'])
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


"""Api to get movies"""
class Movies_list(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        movie_serializers = MovieSerializer(all_movies,many=True)
        for movie in movie_serializers.data:
            poster_id = Poster.objects.get(movie_id=movie['id']).id
            poster_url = Poster.objects.get(movie_id=movie['id']).poster_url
            movie['poster_id'] = poster_id
            movie['poster_url'] = poster_url
            genres = movie['genre']
            genres_list = []
            for genre in genres:
                genre_name = Genre.objects.get(pk=genre).name
                genres_list.append(genre_name)
            movie['genre'] = genres_list
        return Response({'Movies': movie_serializers.data})


"""
To User Login
"""
def user_login(request):
    return render(request, 'movies/login_page.html')

"""
To home page
"""
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

"""
To update movie
param : movie id
returns :redirects to home page
"""
def update(request, id):
    mov = Movie.objects.get(id=id)
    form = MovieForm(request.POST, instance=mov)
    param = {'mov': mov, 'form': form}
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/home/")
    return render(request, 'edit.html', param)

"""
To delete movie
param : movie id
returns : redirects to home page
"""
def delete(request, id):
    mov = Movie.objects.filter(pk=id)
    mov.delete()
    return redirect('http://127.0.0.1:8000/home')

"""
To create new movie
returns : redirects to home page
"""
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
    return render(request, 'create_movie.html',{'form': form})
