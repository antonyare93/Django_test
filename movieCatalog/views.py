from django.shortcuts import render
from django.http import HttpResponse
from .models import Peliculas
# Create your views here.

def main(request):
    return render(request, 'index.html')

def peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {
        'peliculas': peliculas
    })

def hola(request, username):
    return HttpResponse(f'<h1>Hola {username}</h1>')
