from django.shortcuts import render, redirect
from .models import Movie, Poster, Genre
from django.http import HttpResponse
from rest_framework import status
from .forms import MovieForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer

from math import ceil
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
    return render(request,'movies/login_page.html')


def index(request):
    movies = Movie.objects.all()
    print(movies)
    param = {'movie': movies}


    return render(request,'home.html',param)



def update(request, id):
    mov = Movie.objects.get(id=id)
    form = MovieForm(request.POST, instance=mov)
    if form.is_valid():
        form.save()
        # return redirect("/")
    return render(request, 'edit.html', {'mov': mov})

# def update(request, id):
#     mov = Movie.objects.get(id=id)
#     form = MovieForm(request.POST, instance = mov)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request, 'update.html', {'mov': mov})

def delete(request,id):
    print(id)
    mov = Movie.objects.filter(pk=id)
    mov.delete()
    return HttpResponse('Movie deleted!!')


def create(request):
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
