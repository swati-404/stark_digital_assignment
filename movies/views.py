from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request,'movies/login_page.html')


def index(request):
    return render(request,'movies/homepage.html')