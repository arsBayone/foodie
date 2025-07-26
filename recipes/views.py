

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def recipes(request):  # Renamed from 'recipes' to 'index'
    return HttpResponse("This is the recipes page.")