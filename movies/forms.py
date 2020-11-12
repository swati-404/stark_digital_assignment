from django import forms
from .models import Movie

"""
Movie Form 
"""
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
