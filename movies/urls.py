from django.urls import path
# from .views import
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('home/', views.index),
    path('update/<int:id>/', views.update, name="movie_update"),
    path('delete/<int:id>/', views.delete, name="movie_delete"),
    path('new', views.New_Movie),
    path('search_movie/', views.IndexView.as_view()),
    path('create_movie/', views.CreateMovieAPIView.as_view()),
    path('movie_list/', views.Movies_list.as_view()),

]
