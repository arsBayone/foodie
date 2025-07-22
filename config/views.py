from django.http import HttpResponse
from django.shortcuts import render
from random import choice

fruits=["apple","banana","mangoes"]

def index(request):
    return render(request, "config/index.html")
    # data={ "name":"Arsalan", "profession":"SDE"    }
    # data = choice(fruits)
    # return HttpResponse(f"Hello there {data}!")
