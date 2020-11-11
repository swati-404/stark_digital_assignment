from django.urls import path
# from .views import
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('home/', views.index),

]
