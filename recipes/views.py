
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipie  

# Create your views here.

def recipes(request):  # Renamed from 'recipes' to 'index'
    recipes = Recipie.objects.all()  # Assuming Recipe is a model in recipes/models.py
    print("recipes", recipes)
    return HttpResponse("This is the recipes page.")