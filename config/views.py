from django.http import HttpResponse
from django.shortcuts import render
from random import choice

fruits={"name":"Arsalan", "profession":"SDE"}

def index(request):
    context={"foods": fruits}
    return render(request, "config/index.html",context  )
    # data={ "name":"Arsalan", "profession":"SDE"    }
    # data = choice(fruits)
    # return HttpResponse(f"Hello there {data}!")
