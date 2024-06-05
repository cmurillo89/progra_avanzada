from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def soporte(request):
    return render(request, 'paginas/soporte.html')

def index(request):
    return render(request, 'peliculas/index.html')

def agregar(request):
    return render(request, 'peliculas/agregar.html')

def editar(request):
    return render(request, 'peliculas/editar.html')