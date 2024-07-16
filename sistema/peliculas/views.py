from django.shortcuts import render, redirect
from .models import Pelicula, categoria
from .forms import PeliculaForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def soporte(request):
    return render(request, 'paginas/soporte.html')

@login_required
def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

@login_required
def index_cat(request):
    categorias = categoria.objects.all()
    return render(request, 'categorias/index_cat.html', {'categorias': categorias})

def add_cat(request):
    formulario = CategoriaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index_cat')
    return render(request, 'categorias/add_cat.html', {'formulario': formulario})

def edit_cat(request, id):
    cat = categoria.objects.get(id=id)
    formulario = CategoriaForm(request.POST or None, instance=cat)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index_cat')
    return render(request, 'categorias/edit_cat.html', {'formulario': formulario})

def del_cat(request, id):
    cat = categoria.objects.get(id=id)
    cat.delete()
    return redirect('index_cat')

def agregar(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'peliculas/agregar.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'peliculas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('index')

def exit(request):
    logout(request)
    return redirect('inicio')