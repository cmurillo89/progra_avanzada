from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    id = models.AutoField(primary_key=True , verbose_name="Id")
    nombre = models.CharField(max_length=50 , verbose_name="Nombre")

    def __str__(self):
        fila = str(self.id) + " - " + self.nombre 
        return fila

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True , verbose_name="Id")
    titulo = models.CharField(max_length=100 , verbose_name="Título")
    categoria = models.ForeignKey('categoria', on_delete=models.CASCADE, verbose_name="Categoría")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)

    def __str__(self):
        fila = str(self.id) + " - " + self.titulo + " - " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete()
        super().delete()

