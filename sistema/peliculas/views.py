from django.shortcuts import render
from .models import Pelicula

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def soporte(request):
    return render(request, 'paginas/soporte.html')

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def agregar(request):
    return render(request, 'peliculas/agregar.html')

def editar(request):
    return render(request, 'peliculas/editar.html')