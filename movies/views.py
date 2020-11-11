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
        print("$$$$$$$$$$$")
        queryset = Movie.objects.all()
        print("@@@@@")
        name = request.query_params.get('name', None)
        print(name)
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
    print("update")
    print(form.data)
    if form.is_valid():
        print("form valid")
        form.save()
        return redirect("http://127.0.0.1:8000/home/")
        print("ok")
    return render(request, 'edit.html', {'mov': mov})

# def update(request, id):
#     res = Movie.objects.get(pk=id)
#     res.response = Movie.POST.get('Response')
#     res.save()
#     return render(request, 'update_add.html', {'rform': res})


# def update(request, id):
#     mov = Movie.objects.get(id=id)
#     form = MovieForm(request.POST, instance = mov)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request, 'update.html', {'mov': mov})

def delete(request,id):
    mov = Movie.objects.filter(pk=id)
    mov.delete()
    return redirect('http://127.0.0.1:8000/home')


def New_Movie(request):
    print("Create")
    if request.method == "POST":
        print(" in if")
        form = MovieForm(request.POST)
        if form.is_valid():
            print("form valid")
            try:
                form.save()
                return redirect('home/')
            except:
                pass
        print("end if")
    else:
        form = MovieForm()

    return render(request, 'create_movie.html',
                  {'form': form}
                  )
