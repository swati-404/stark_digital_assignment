from django.shortcuts import render, redirect
from .models import Movie, Poster, Genre
from django.http import HttpResponse
from .forms import MovieForm

from math import ceil
# Create your views here.
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


